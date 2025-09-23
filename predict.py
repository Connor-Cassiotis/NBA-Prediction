import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv('nba_games.csv', index_col=0)
df = df.sort_values(by='date')
df = df.reset_index(drop=True)

# Data cleaning
del df["mp.1"]
del df["mp_opp.1"]
del df["index_opp"]

def add_target(team):
    team = team.copy()
    team["target"] = team["won"].shift(-1)
    return team

# Reset index to avoid groupby warnings
df_grouped = []
for team_name, team_data in df.groupby("team"):
    df_grouped.append(add_target(team_data))
df = pd.concat(df_grouped, ignore_index=True)
df[df["team"] == "WAS"]
df.loc[pd.isnull(df["target"]), "target"] = 2
df["target"] = df["target"].astype(int, errors='ignore')
nulls = df.isnull().sum()
nulls = nulls[nulls > 0]
valid_columns = df.columns[~df.columns.isin(nulls.index)]
df = df[valid_columns].copy()


# Machine learning with fast feature selection
rr = RidgeClassifier(alpha=0.1)
split = TimeSeriesSplit(n_splits=3)

# Use much faster univariate feature selection instead of sequential
selector = SelectKBest(score_func=f_classif, k=35)
removed_columns = ["season", "date", "team", "target", "won", "team_opp"]
selected_columns = df.columns[~df.columns.isin(removed_columns)]
scaler = MinMaxScaler()
df[selected_columns] = scaler.fit_transform(df[selected_columns])


def backtest(data, model, predictors, start=2, step=1):
    all_predictions = []

    seasons = sorted(data["season"].unique())
    for i in range(start, len(seasons), step):
       season = seasons[i]
       train = data[data["season"] < season]
       test = data[data["season"] == season]

       model.fit(train[predictors], train["target"])

       preds = model.predict(test[predictors])
       preds = pd.Series(preds, index=test.index)

       combined = pd.concat([test["target"], preds], axis=1)
       combined.columns = ["actual", "prediction"]
       all_predictions.append(combined)
    return pd.concat(all_predictions)

# Define predictors before using them
predictors = selected_columns
predictions = backtest(df, rr, predictors)
predictions = predictions[predictions["actual"] != 2]
accuracy = accuracy_score(predictions["actual"], predictions["prediction"])

df_rolling = df[list(selected_columns) + ["team", "season", "won"]].copy()

def find_team_averages(team):
    # Only calculate rolling mean for numeric columns
    numeric_cols = team.select_dtypes(include=[float, int]).columns
    
    # Use just 5 and 10 game rolling windows for speed
    rolling_5 = team[numeric_cols].rolling(5).mean()
    rolling_10 = team[numeric_cols].rolling(10).mean()
    
    # Add suffixes to differentiate the rolling windows
    rolling_5.columns = [f"{col}_5" for col in rolling_5.columns]
    rolling_10.columns = [f"{col}_10" for col in rolling_10.columns]
    
    # Combine rolling averages
    combined_rolling = pd.concat([rolling_5, rolling_10], axis=1)
    return combined_rolling

# Process rolling averages without groupby warnings
rolling_results = []
for (team_name, season), team_data in df_rolling.groupby(["team", "season"]):
    rolling_results.append(find_team_averages(team_data))
df_rolling = pd.concat(rolling_results, ignore_index=True)

rolling_cols = list(df_rolling.columns)
df = pd.concat([df, df_rolling], axis=1)
df = df.dropna()

def shift_col(team, col_name):
    next_col = team[col_name].shift(-1)
    return next_col

def add_col(df, col_name):
    results = []
    for team_name, team_data in df.groupby("team"):
        results.append(shift_col(team_data, col_name))
    return pd.concat(results, ignore_index=True)

df["home_next"] = add_col(df, "home")
df["team_opp_next"] = add_col(df, "team_opp")
df["date_next"] = add_col(df, "date")

# Simplified rest days - just add a basic version
df['rest_days'] = 2  # Most NBA teams play every 2-3 days on average

df = df.copy()

full = df.merge(df[rolling_cols + ["team_opp_next", "team", "date_next"]], left_on=["team", "date_next"], right_on=["team_opp_next","date_next"])

# For now, let's focus on the multiple rolling windows and improved parameters
# We'll skip the complex opponent merging to avoid errors

removed_columns = list(full.columns[full.dtypes == "object"]) + removed_columns
new_selected_columns = full.columns[~full.columns.isin(removed_columns)]
selector.fit(full[new_selected_columns], full["target"])
predictors = list(new_selected_columns[selector.get_support()])

# Optimize Ridge parameters for final model
final_rr = RidgeClassifier(alpha=0.05)  # Even lower alpha for final model

# Run backtest with improved features
predictions = backtest(full, final_rr, predictors)
predictions = predictions[predictions["actual"] != 2]
final_accuracy = accuracy_score(predictions["actual"], predictions["prediction"])
print(f"Improved model accuracy: {final_accuracy}")
print(f"Number of features used: {len(predictors)}")
print(f"Total games predicted: {len(predictions)}")
"""
NBA Game Prediction System - Final Version
Best performing model with hot streaks and momentum features
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import RidgeClassifier
from sklearn.feature_selection import RFE, SelectKBest, f_classif
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

def load_data():
    df = pd.read_csv('nba_games_2018_2024.csv')
    return df

def create_prediction_features(df):
    """Create all features for prediction"""
    
    # Ensure proper data types
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['team', 'date']).reset_index(drop=True)
    
    # Calculate rolling statistics for each team
    feature_columns = ['pts', 'fg%', '3p%', 'ft%', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf']
    
    for team in df['team'].unique():
        team_mask = df['team'] == team
        team_data = df[team_mask].copy()
        
        for col in feature_columns:
            if col in team_data.columns:
                # Rolling averages
                df.loc[team_mask, f'{col}_avg_3'] = team_data[col].rolling(3, min_periods=1).mean()
                df.loc[team_mask, f'{col}_avg_5'] = team_data[col].rolling(5, min_periods=1).mean()
                df.loc[team_mask, f'{col}_avg_10'] = team_data[col].rolling(10, min_periods=1).mean()
    
    # Hot streak features
    for team in df['team'].unique():
        team_mask = df['team'] == team
        team_data = df[team_mask].copy()
        
        # Win streak calculation
        wins = team_data['won'].values
        win_streaks = []
        loss_streaks = []
        recent_form_5 = []
        recent_form_10 = []
        momentum_scores = []
        
        for i in range(len(wins)):
            if i == 0:
                win_streaks.append(0)
                loss_streaks.append(0)
                recent_form_5.append(0.5)
                recent_form_10.append(0.5)
                momentum_scores.append(0.5)
            else:
                # Win/loss streaks
                current_streak = 0
                for j in range(i-1, -1, -1):
                    if wins[j] == wins[i-1]:
                        current_streak += 1
                    else:
                        break
                
                if wins[i-1] == 1:
                    win_streaks.append(current_streak)
                    loss_streaks.append(0)
                else:
                    win_streaks.append(0)
                    loss_streaks.append(current_streak)
                
                # Recent form
                start_5 = max(0, i-5)
                start_10 = max(0, i-10)
                recent_form_5.append(wins[start_5:i].mean() if i > 0 else 0.5)
                recent_form_10.append(wins[start_10:i].mean() if i > 0 else 0.5)
                
                # Momentum (weighted recent games)
                if i >= 3:
                    weights = [0.5, 0.3, 0.2]
                    momentum = sum(wins[i-3:i] * weights) / sum(weights)
                else:
                    momentum = wins[:i].mean() if i > 0 else 0.5
                momentum_scores.append(momentum)
        
        df.loc[team_mask, 'win_streak'] = win_streaks
        df.loc[team_mask, 'loss_streak'] = loss_streaks
        df.loc[team_mask, 'recent_form_5'] = recent_form_5
        df.loc[team_mask, 'recent_form_10'] = recent_form_10
        df.loc[team_mask, 'momentum_score'] = momentum_scores
    
    # Advanced features
    df['rest_days'] = df.groupby('team')['date'].diff().dt.days.fillna(2)
    df['back_to_back'] = (df['rest_days'] <= 1).astype(int)
    df['season_progress'] = df.groupby(['team', 'season']).cumcount() / 82
    
    # Opponent features (simplified)
    df['opp_pts_avg'] = df.groupby('team_opp')['pts_opp'].transform('mean')
    df['opp_fg_pct_avg'] = df.groupby('team_opp')['fg%_opp'].transform('mean')
    
    return df

def prepare_model_data(df):

    
    # Get feature columns
    rolling_cols = [col for col in df.columns if '_avg_' in col]
    streak_cols = ['win_streak', 'loss_streak', 'recent_form_5', 'recent_form_10', 'momentum_score']
    advanced_cols = ['rest_days', 'back_to_back', 'season_progress', 'opp_pts_avg', 'opp_fg_pct_avg']
    
    feature_cols = rolling_cols + streak_cols + advanced_cols
    feature_cols = [col for col in feature_cols if col in df.columns]
    
    
    # Create model dataset
    model_data = df[['won'] + feature_cols].dropna()
    
    return model_data[feature_cols], model_data['won'], feature_cols

def train_final_model(X, y, feature_names):

    
    # Feature selection

    selector = SelectKBest(score_func=f_classif, k=40)
    X_selected = selector.fit_transform(X, y)
    selected_features = [feature_names[i] for i in selector.get_support(indices=True)]
    

    
    # Scale features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X_selected)
    
    # Train model
    model = RidgeClassifier(alpha=1.0, random_state=42)
    model.fit(X_scaled, y)
    
    return model, scaler, selector, selected_features

def backtest_model(X, y):

    
    # Feature selection
    selector = SelectKBest(score_func=f_classif, k=40)
    X_selected = selector.fit_transform(X, y)
    
    # Scale features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X_selected)
    
    # Time series cross-validation
    tscv = TimeSeriesSplit(n_splits=5)
    accuracies = []
    all_predictions = []
    all_actuals = []
    
    for fold, (train_idx, test_idx) in enumerate(tscv.split(X_scaled)):
        X_train, X_test = X_scaled[train_idx], X_scaled[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        
        # Train model
        model = RidgeClassifier(alpha=1.0, random_state=42)
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)
        
        all_predictions.extend(y_pred)
        all_actuals.extend(y_test)

    
    mean_accuracy = np.mean(accuracies)

    
    return mean_accuracy, accuracies, all_predictions, all_actuals

def predict_games(model, scaler, selector, feature_names, df, num_recent=10):

    
    # Prepare features for recent games
    X, y, _ = prepare_model_data(df)
    
    # Get recent games
    recent_games = df.tail(num_recent).copy()
    recent_X = X.tail(num_recent)
    recent_y = y.tail(num_recent)
    
    # Transform features
    recent_X_selected = selector.transform(recent_X)
    recent_X_scaled = scaler.transform(recent_X_selected)
    
    # Make predictions
    predictions = model.predict(recent_X_scaled)
    probabilities = model.decision_function(recent_X_scaled)
    
    # Create results
    results = []
    for i, (_, game) in enumerate(recent_games.iterrows()):
        result = {
            'Date': game['date'],
            'Team': game['team'],
            'Opponent': game['team_opp'],
            'Actual': ' Win' if recent_y.iloc[i] == 1 else '❌ Loss',
            'Predicted': ' Win' if predictions[i] == 1 else '❌ Loss',
            'Confidence': abs(probabilities[i]),
            'Correct': '' if predictions[i] == recent_y.iloc[i] else '❌'
        }
        results.append(result)
    
    # Show results
    correct = sum(1 for r in results if r['Correct'] == '✅')
    accuracy = correct / len(results)
    
    return results, accuracy

def main():
    """Main execution"""
    # Load and prepare data
    df = load_data()
    df = create_prediction_features(df)
    X, y, feature_names = prepare_model_data(df)
    # Backtest performance
    mean_accuracy, _, _, _ = backtest_model(X, y)
    # Print only the accuracy
    print(f"accuracy {mean_accuracy*100:.2f}")

if __name__ == "__main__":
    main()
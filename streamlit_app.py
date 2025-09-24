"""
NBA Game Prediction App - Streamlit Version
Replicating the React frontend functionality in Streamlit
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date
import random
import time

# NBA Teams data (converted from JavaScript)
NBA_TEAMS = [
    {"value": "ATL", "label": "Atlanta Hawks", "city": "Atlanta"},
    {"value": "BOS", "label": "Boston Celtics", "city": "Boston"},
    {"value": "BRK", "label": "Brooklyn Nets", "city": "Brooklyn"},
    {"value": "CHA", "label": "Charlotte Hornets", "city": "Charlotte"},
    {"value": "CHI", "label": "Chicago Bulls", "city": "Chicago"},
    {"value": "CLE", "label": "Cleveland Cavaliers", "city": "Cleveland"},
    {"value": "DAL", "label": "Dallas Mavericks", "city": "Dallas"},
    {"value": "DEN", "label": "Denver Nuggets", "city": "Denver"},
    {"value": "DET", "label": "Detroit Pistons", "city": "Detroit"},
    {"value": "GSW", "label": "Golden State Warriors", "city": "Golden State"},
    {"value": "HOU", "label": "Houston Rockets", "city": "Houston"},
    {"value": "IND", "label": "Indiana Pacers", "city": "Indiana"},
    {"value": "LAC", "label": "LA Clippers", "city": "LA"},
    {"value": "LAL", "label": "Los Angeles Lakers", "city": "Los Angeles"},
    {"value": "MEM", "label": "Memphis Grizzlies", "city": "Memphis"},
    {"value": "MIA", "label": "Miami Heat", "city": "Miami"},
    {"value": "MIL", "label": "Milwaukee Bucks", "city": "Milwaukee"},
    {"value": "MIN", "label": "Minnesota Timberwolves", "city": "Minnesota"},
    {"value": "NOP", "label": "New Orleans Pelicans", "city": "New Orleans"},
    {"value": "NYK", "label": "New York Knicks", "city": "New York"},
    {"value": "OKC", "label": "Oklahoma City Thunder", "city": "Oklahoma City"},
    {"value": "ORL", "label": "Orlando Magic", "city": "Orlando"},
    {"value": "PHI", "label": "Philadelphia 76ers", "city": "Philadelphia"},
    {"value": "PHX", "label": "Phoenix Suns", "city": "Phoenix"},
    {"value": "POR", "label": "Portland Trail Blazers", "city": "Portland"},
    {"value": "SAC", "label": "Sacramento Kings", "city": "Sacramento"},
    {"value": "SAS", "label": "San Antonio Spurs", "city": "San Antonio"},
    {"value": "TOR", "label": "Toronto Raptors", "city": "Toronto"},
    {"value": "UTA", "label": "Utah Jazz", "city": "Utah"},
    {"value": "WAS", "label": "Washington Wizards", "city": "Washington"}
]

def get_team_by_value(value):
    """Helper function to get team by value"""
    return next((team for team in NBA_TEAMS if team["value"] == value), None)

def predict_game(home_team, away_team, game_date):
    """
    Mock prediction function (replicating the Flask server logic)
    In a real scenario, this would use the actual ML model
    """
    # Simulate processing time
    time.sleep(1)
    
    # Mock prediction with consistent results for same teams
    random.seed(hash(home_team + away_team))
    
    win_probability = random.uniform(45, 80)  # Random between 45-80%
    predicted_winner = home_team if win_probability > 50 else away_team
    confidence = random.uniform(70, 90)
    
    return {
        'predictedWinner': predicted_winner,
        'winProbability': round(win_probability, 1),
        'confidence': round(confidence, 1),
        'homeTeam': home_team,
        'awayTeam': away_team,
        'gameDate': game_date.strftime("%Y-%m-%d")
    }

def main():
    # Page configuration
    st.set_page_config(
        page_title="NBA Game Predictor",
        page_icon="🏀",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state
    if 'prediction_result' not in st.session_state:
        st.session_state.prediction_result = None
    if 'form_data' not in st.session_state:
        st.session_state.form_data = None
    if 'show_form' not in st.session_state:
        st.session_state.show_form = True
    
    # Main container
    with st.container():
        # Header section
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h1 style='
                font-size: 2.5rem; 
                font-weight: bold; 
                background: linear-gradient(135deg, #7f1d1d, #991b1b);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.5rem;
            '>NBA Game Predictor</h1>
            <p style='color: #9ca3af; font-size: 0.9rem;'>Predict NBA game outcomes with AI</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show form or results based on state
        if st.session_state.show_form and st.session_state.prediction_result is None:
            show_prediction_form()
        elif st.session_state.prediction_result is not None:
            show_results()

def show_prediction_form():
    """Display the prediction form"""
    
    # Form container with custom styling
    with st.form("prediction_form", clear_on_submit=False):
        st.markdown("### Game Details")
        
        # Date input
        game_date = st.date_input(
            "Game Date",
            value=date.today(),
            help="Select the date of the NBA game"
        )
        
        # Team selection
        col1, col2 = st.columns(2)
        
        with col1:
            home_team_labels = ["Select home team"] + [team["label"] for team in NBA_TEAMS]
            home_team_selection = st.selectbox(
                "Home Team",
                home_team_labels,
                index=0
            )
            
        with col2:
            away_team_labels = ["Select away team"] + [team["label"] for team in NBA_TEAMS]
            away_team_selection = st.selectbox(
                "Away Team", 
                away_team_labels,
                index=0
            )
        
        # Submit button
        submit_button = st.form_submit_button(
            "🏀 Predict Game Outcome",
            use_container_width=True,
            type="primary"
        )
        
        # Form validation and submission
        if submit_button:
            # Validate selections
            if home_team_selection == "Select home team":
                st.error("Please select a home team")
                return
            if away_team_selection == "Select away team":
                st.error("Please select an away team")
                return
            if home_team_selection == away_team_selection:
                st.error("Home team and away team cannot be the same")
                return
            
            # Get team values
            home_team = next(team["value"] for team in NBA_TEAMS if team["label"] == home_team_selection)
            away_team = next(team["value"] for team in NBA_TEAMS if team["label"] == away_team_selection)
            
            # Store form data
            st.session_state.form_data = {
                'date': game_date,
                'home_team': home_team,
                'away_team': away_team,
                'home_team_label': home_team_selection,
                'away_team_label': away_team_selection
            }
            
            # Show loading state
            with st.spinner("Making prediction..."):
                try:
                    # Make prediction
                    result = predict_game(home_team, away_team, game_date)
                    st.session_state.prediction_result = result
                    st.session_state.show_form = False
                    st.rerun()
                except Exception as e:
                    st.error(f"Prediction failed: {str(e)}")

def show_results():
    """Display the prediction results"""
    result = st.session_state.prediction_result
    form_data = st.session_state.form_data
    
    if not result or not form_data:
        return
    
    # Results header
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <div style='
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 4rem;
            height: 4rem;
            background: linear-gradient(135deg, #7f1d1d, #991b1b);
            border-radius: 50%;
            margin-bottom: 1rem;
        '>
            <span style='color: white; font-size: 1.5rem;'>✓</span>
        </div>
        <h2 style='
            font-size: 1.5rem;
            font-weight: bold;
            background: linear-gradient(135deg, #7f1d1d, #991b1b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        '>Prediction Results</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Game matchup
    st.markdown("### Game Matchup")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown(f"""
        <div style='text-align: center; padding: 1rem; background-color: #374151; border-radius: 0.5rem;'>
            <p style='color: #9ca3af; font-size: 0.7rem; text-transform: uppercase; margin-bottom: 0.5rem;'>Away</p>
            <p style='color: white; font-weight: bold; margin: 0;'>{form_data['away_team_label']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <p style='color: #7f1d1d; font-weight: bold; font-size: 1.2rem; margin: 0;'>@</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='text-align: center; padding: 1rem; background-color: #374151; border-radius: 0.5rem;'>
            <p style='color: #9ca3af; font-size: 0.7rem; text-transform: uppercase; margin-bottom: 0.5rem;'>Home</p>
            <p style='color: white; font-weight: bold; margin: 0;'>{form_data['home_team_label']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Prediction results
    st.markdown("### Prediction")
    
    # Determine winner
    predicted_winner = result['predictedWinner']
    is_home_winner = predicted_winner == form_data['home_team']
    winner_label = form_data['home_team_label'] if is_home_winner else form_data['away_team_label']
    
    # Winner display
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 1.5rem;'>
        <p style='color: #9ca3af; font-size: 0.9rem; margin-bottom: 0.5rem;'>Predicted Winner</p>
        <p style='color: white; font-size: 1.5rem; font-weight: bold; margin: 0;'>{winner_label}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            label="Win Probability",
            value=f"{result['winProbability']}%",
            help="Probability of the predicted winner winning"
        )
    
    with col2:
        st.metric(
            label="Confidence",
            value=f"{result['confidence']}%",
            help="Model confidence in the prediction"
        )
    
    # Game date
    st.info(f"**Game Date:** {form_data['date'].strftime('%B %d, %Y')}")
    
    # New prediction button
    st.markdown("---")
    if st.button("🔄 Make Another Prediction", use_container_width=True, type="secondary"):
        st.session_state.prediction_result = None
        st.session_state.form_data = None
        st.session_state.show_form = True
        st.rerun()

if __name__ == "__main__":
    main()
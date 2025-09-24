"""
Enhanced NBA Game Prediction App - Streamlit Version
With custom CSS styling to match the original React frontend
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
    time.sleep(1.5)
    
    # Include date in the seed to make predictions vary by date
    date_string = game_date.strftime("%Y-%m-%d")
    seed_string = f"{home_team}_{away_team}_{date_string}"
    random.seed(hash(seed_string))
    
    win_probability = random.uniform(45, 80)  # Random between 45-80%
    predicted_winner = home_team if win_probability > 50 else away_team
    
    # Reset seed for confidence to add more variation
    random.seed(hash(seed_string + "_confidence"))
    confidence = random.uniform(70, 90)
    
    return {
        'predictedWinner': predicted_winner,
        'winProbability': round(win_probability, 1),
        'confidence': round(confidence, 1),
        'homeTeam': home_team,
        'awayTeam': away_team,
        'gameDate': date_string
    }

def apply_custom_css():
    """Apply enhanced custom CSS styling for better UI"""
    st.markdown("""
    <style>
    /* Import modern fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    /* Global styles with enhanced background */
    .stApp {
        background: 
            radial-gradient(circle at 20% 80%, rgba(239, 68, 68, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(185, 28, 28, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(127, 29, 29, 0.06) 0%, transparent 50%),
            linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 25%, #2d1b1b 50%, #1a1a1a 75%, #0a0a0a 100%);
        background-attachment: fixed;
        font-family: 'Poppins', 'Inter', sans-serif !important;
        color: white !important;
        min-height: 100vh;
    }
    
    /* Hide Streamlit branding completely */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}
    a[href^="https://streamlit.io"] {display: none !important;}
    
    /* Enhanced container styling */
    .main .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 32rem !important;
        margin: 0 auto !important;
    }
    
    /* Enhanced form styling with glass morphism */
    .stForm {
        background: rgba(20, 20, 20, 0.7) !important;
        border: 1px solid rgba(239, 68, 68, 0.2) !important;
        border-radius: 1.5rem !important;
        padding: 2.5rem !important;
        backdrop-filter: blur(20px) !important;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.4),
            0 2px 16px rgba(239, 68, 68, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        position: relative;
        overflow: hidden;
    }
    
    /* Add subtle glow animation to form */
    .stForm::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, 
            transparent 30%, 
            rgba(239, 68, 68, 0.3) 50%, 
            transparent 70%);
        border-radius: 1.5rem;
        z-index: -1;
        animation: borderGlow 3s ease-in-out infinite alternate;
    }
    
    @keyframes borderGlow {
        0% { opacity: 0.3; }
        100% { opacity: 0.7; }
    }
    
    /* Enhanced input styling */
    .stDateInput > div > div > input,
    .stSelectbox > div > div > select {
        background: linear-gradient(135deg, rgba(55, 65, 81, 0.8), rgba(75, 85, 99, 0.6)) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        border-radius: 1rem !important;
        color: white !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        padding: 1rem 1.25rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stDateInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: rgba(239, 68, 68, 0.8) !important;
        box-shadow: 
            0 0 0 3px rgba(239, 68, 68, 0.2),
            0 8px 16px rgba(0, 0, 0, 0.2) !important;
        outline: none !important;
        transform: translateY(-2px) !important;
    }
    
    .stDateInput > div > div > input:hover,
    .stSelectbox > div > div > select:hover {
        border-color: rgba(239, 68, 68, 0.5) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15) !important;
    }
    
    /* Enhanced label styling */
    .stDateInput > label,
    .stSelectbox > label {
        color: #f3f4f6 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 0.75rem !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    }
    
    /* Spectacular button styling */
    .stButton > button {
        background: linear-gradient(135deg, 
            #dc2626 0%, 
            #b91c1c 25%, 
            #991b1b 50%, 
            #7f1d1d 75%, 
            #dc2626 100%) !important;
        background-size: 200% 200% !important;
        border: none !important;
        border-radius: 1.25rem !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 1.25rem 2rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
        height: 4rem !important;
        box-shadow: 
            0 10px 20px rgba(220, 38, 38, 0.3),
            0 6px 6px rgba(0, 0, 0, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        position: relative;
        overflow: hidden;
        cursor: pointer !important;
        animation: gradientShift 3s ease-in-out infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.3), 
            transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, 
            #ef4444 0%, 
            #dc2626 25%, 
            #b91c1c 50%, 
            #991b1b 75%, 
            #ef4444 100%) !important;
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 
            0 15px 30px rgba(220, 38, 38, 0.4),
            0 10px 10px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98) !important;
        box-shadow: 
            0 5px 10px rgba(220, 38, 38, 0.5),
            0 3px 6px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Enhanced secondary button styling */
    .stButton > button[kind="secondary"] {
        background: rgba(55, 65, 81, 0.8) !important;
        border: 1px solid rgba(239, 68, 68, 0.4) !important;
        box-shadow: 
            0 6px 12px rgba(0, 0, 0, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stButton > button[kind="secondary"]:hover {
        background: rgba(75, 85, 99, 0.9) !important;
        border-color: rgba(239, 68, 68, 0.6) !important;
        transform: translateY(-2px) !important;
        box-shadow: 
            0 8px 16px rgba(0, 0, 0, 0.3),
            0 0 0 2px rgba(239, 68, 68, 0.3) !important;
    }
    
    /* Enhanced metric containers */
    .metric-container {
        background: linear-gradient(135deg, 
            rgba(31, 41, 55, 0.9), 
            rgba(55, 65, 81, 0.7)) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        border-radius: 1.25rem !important;
        padding: 2rem !important;
        text-align: center !important;
        margin: 0.75rem 0 !important;
        backdrop-filter: blur(15px) !important;
        box-shadow: 
            0 8px 20px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
    }
    
    .metric-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(239, 68, 68, 0.1), 
            transparent);
        transition: left 0.8s;
    }
    
    .metric-container:hover::before {
        left: 100%;
    }
    
    .metric-container:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(239, 68, 68, 0.5) !important;
        box-shadow: 
            0 12px 25px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Enhanced alert styling */
    .stAlert > div {
        border-radius: 1rem !important;
        border: none !important;
        backdrop-filter: blur(15px) !important;
        font-weight: 500 !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2) !important;
    }
    
    .stAlert[data-baseweb-kind="error"] > div {
        background: linear-gradient(135deg, 
            rgba(239, 68, 68, 0.2), 
            rgba(220, 38, 38, 0.15)) !important;
        border: 1px solid rgba(239, 68, 68, 0.4) !important;
        color: #fca5a5 !important;
    }
    
    .stAlert[data-baseweb-kind="info"] > div {
        background: linear-gradient(135deg, 
            rgba(31, 41, 55, 0.7), 
            rgba(55, 65, 81, 0.5)) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        color: #f3f4f6 !important;
    }
    
    /* Enhanced spinner */
    .stSpinner > div {
        border-top-color: #ef4444 !important;
        border-right-color: #ef4444 !important;
        border-width: 3px !important;
        width: 2.5rem !important;
        height: 2.5rem !important;
    }
    
    /* Premium gradient text */
    .gradient-text {
        background: linear-gradient(135deg, 
            #ef4444 0%, 
            #dc2626 25%, 
            #b91c1c 50%, 
            #991b1b 75%, 
            #ef4444 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        animation: gradientText 4s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(239, 68, 68, 0.3);
    }
    
    @keyframes gradientText {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Enhanced prediction card */
    .prediction-card {
        background: linear-gradient(135deg, 
            rgba(20, 20, 20, 0.9), 
            rgba(31, 41, 55, 0.8)) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        border-radius: 1.5rem !important;
        padding: 2.5rem !important;
        backdrop-filter: blur(20px) !important;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.4),
            0 8px 16px rgba(239, 68, 68, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        margin: 1.5rem 0 !important;
        position: relative;
        overflow: hidden;
    }
    
    .prediction-card::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, 
            transparent 30%, 
            rgba(239, 68, 68, 0.2) 50%, 
            transparent 70%);
        border-radius: 1.5rem;
        z-index: -1;
        animation: cardGlow 4s ease-in-out infinite alternate;
    }
    
    @keyframes cardGlow {
        0% { opacity: 0.5; }
        100% { opacity: 0.8; }
    }
    
    /* Premium team card styling */
    .team-card {
        background: linear-gradient(135deg, 
            rgba(55, 65, 81, 0.9), 
            rgba(75, 85, 99, 0.7)) !important;
        border-radius: 1.25rem !important;
        padding: 1.5rem !important;
        text-align: center !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        backdrop-filter: blur(15px) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 6px 12px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    }
    
    .team-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(239, 68, 68, 0.15), 
            transparent);
        transition: left 0.6s;
    }
    
    .team-card:hover::before {
        left: 100%;
    }
    
    .team-card:hover {
        transform: translateY(-3px) scale(1.02) !important;
        border-color: rgba(239, 68, 68, 0.5) !important;
        box-shadow: 
            0 10px 20px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    }
    
    .team-label {
        color: #d1d5db !important;
        font-size: 0.75rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin-bottom: 0.75rem !important;
        font-weight: 600 !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
    }
    
    .team-name {
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        margin: 0 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Enhanced vs styling */
    .vs-text {
        color: #ef4444 !important;
        font-weight: 900 !important;
        font-size: 1.5rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        height: 100% !important;
        text-shadow: 0 0 20px rgba(239, 68, 68, 0.5);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
    }
    
    /* Enhanced winner display */
    .winner-display {
        text-align: center !important;
        margin: 2rem 0 !important;
        padding: 2rem !important;
        background: linear-gradient(135deg, 
            rgba(239, 68, 68, 0.15), 
            rgba(220, 38, 38, 0.1)) !important;
        border: 2px solid rgba(239, 68, 68, 0.4) !important;
        border-radius: 1.5rem !important;
        backdrop-filter: blur(15px) !important;
        box-shadow: 
            0 10px 25px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        position: relative;
        overflow: hidden;
    }
    
    .winner-display::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(239, 68, 68, 0.2), 
            transparent);
        animation: winnerGlow 3s ease-in-out infinite;
    }
    
    @keyframes winnerGlow {
        0%, 100% { left: -100%; }
        50% { left: 100%; }
    }
    
    .winner-label {
        color: #d1d5db !important;
        font-size: 1rem !important;
        margin-bottom: 0.75rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
    }
    
    .winner-name {
        color: white !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
        animation: winnerText 2s ease-in-out infinite alternate;
    }
    
    @keyframes winnerText {
        0% { transform: scale(1); }
        100% { transform: scale(1.05); }
    }
    
    /* Advanced animations and effects */
    @keyframes fadeIn {
        from { 
            opacity: 0; 
            transform: translateY(30px) scale(0.95); 
        }
        to { 
            opacity: 1; 
            transform: translateY(0) scale(1); 
        }
    }
    
    @keyframes slideInLeft {
        from { 
            opacity: 0; 
            transform: translateX(-50px); 
        }
        to { 
            opacity: 1; 
            transform: translateX(0); 
        }
    }
    
    @keyframes slideInRight {
        from { 
            opacity: 0; 
            transform: translateX(50px); 
        }
        to { 
            opacity: 1; 
            transform: translateX(0); 
        }
    }
    
    @keyframes bounceIn {
        0% { 
            opacity: 0; 
            transform: scale(0.3) rotate(-10deg); 
        }
        50% { 
            opacity: 1; 
            transform: scale(1.05) rotate(2deg); 
        }
        70% { 
            transform: scale(0.9) rotate(-1deg); 
        }
        100% { 
            opacity: 1; 
            transform: scale(1) rotate(0deg); 
        }
    }
    
    .main .block-container > div {
        animation: fadeIn 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Column enhanced spacing and animations */
    .stColumn {
        padding: 0 0.75rem !important;
    }
    
    .stColumn:nth-child(1) {
        animation: slideInLeft 0.8s ease-out;
    }
    
    .stColumn:nth-child(3) {
        animation: slideInRight 0.8s ease-out;
    }
    
    /* Floating particles effect */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 25% 25%, rgba(239, 68, 68, 0.1) 0%, transparent 2%),
            radial-gradient(circle at 75% 75%, rgba(185, 28, 28, 0.08) 0%, transparent 2%),
            radial-gradient(circle at 60% 20%, rgba(220, 38, 38, 0.06) 0%, transparent 1.5%),
            radial-gradient(circle at 40% 80%, rgba(239, 68, 68, 0.05) 0%, transparent 1.5%),
            radial-gradient(circle at 90% 40%, rgba(185, 28, 28, 0.07) 0%, transparent 2%);
        background-size: 400px 400px, 300px 300px, 200px 200px, 250px 250px, 350px 350px;
        background-position: 0 0, 50px 50px, 100px 0, 0 100px, 150px 75px;
        animation: floatingParticles 20s linear infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes floatingParticles {
        0% { transform: translate(0, 0) rotate(0deg); }
        33% { transform: translate(30px, -30px) rotate(120deg); }
        66% { transform: translate(-20px, 20px) rotate(240deg); }
        100% { transform: translate(0, 0) rotate(360deg); }
    }
    
    /* Ensure content stays above particles */
    .main {
        position: relative;
        z-index: 1;
    }
    
    /* Enhanced focus states */
    *:focus-visible {
        outline: 2px solid rgba(239, 68, 68, 0.6) !important;
        outline-offset: 2px !important;
    }
    
    /* Smooth transitions for all interactive elements */
    * {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Page configuration
    st.set_page_config(
        page_title="NBA Game Predictor",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom CSS
    apply_custom_css()
    
    # Initialize session state
    if 'prediction_result' not in st.session_state:
        st.session_state.prediction_result = None
    if 'form_data' not in st.session_state:
        st.session_state.form_data = None
    if 'show_form' not in st.session_state:
        st.session_state.show_form = True
    
    # Main container
    with st.container():
        # Header section with enhanced styling
        st.markdown("""
        <div style='text-align: center; margin-bottom: 3rem; position: relative;'>
            <div style='
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 1rem;
                position: relative;
            '>
                <h1 class='gradient-text' style='
                    font-size: 2.8rem; 
                    margin: 0;
                    line-height: 1.2;
                    font-family: "Poppins", sans-serif;
                '>NBA Game Predictor</h1>
            </div>
            <p style='
                color: #d1d5db; 
                font-size: 1.1rem; 
                font-weight: 400; 
                margin: 0;
                opacity: 0.9;
                text-shadow: 0 1px 2px rgba(0,0,0,0.3);
            '>
                Predict NBA game outcomes with AI-powered analytics
            </p>
            <div style='
                position: absolute;
                top: -20px;
                left: 50%;
                transform: translateX(-50%);
                width: 100px;
                height: 2px;
                background: linear-gradient(90deg, transparent, #ef4444, transparent);
                opacity: 0.6;
            '></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Show form or results based on state
        if st.session_state.show_form and st.session_state.prediction_result is None:
            show_prediction_form()
        elif st.session_state.prediction_result is not None:
            show_results()

def show_prediction_form():
    """Display the prediction form"""
    
    # Form container with enhanced styling
    with st.form("prediction_form", clear_on_submit=False):
        # Enhanced section header
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h3 style='
                color: #f3f4f6;
                font-size: 1.4rem;
                font-weight: 700;
                margin-bottom: 0.5rem;
                font-family: "Poppins", sans-serif;
            '>Game Details</h3>
            <div style='
                width: 60px;
                height: 2px;
                background: linear-gradient(90deg, transparent, #ef4444, transparent);
                margin: 0 auto;
                opacity: 0.7;
            '></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Date input with enhanced styling
        st.markdown("**Game Date**")
        game_date = st.date_input(
            "Select the date of the NBA game",
            value=date.today(),
            label_visibility="collapsed"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Team selection with enhanced headers
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Home Team**")
            home_team_labels = ["Select home team"] + [team['label'] for team in NBA_TEAMS]
            home_team_selection = st.selectbox(
                "Choose the home team",
                home_team_labels,
                index=0,
                label_visibility="collapsed"
            )
            
        with col2:
            st.markdown("**Away Team**")
            away_team_labels = ["Select away team"] + [team['label'] for team in NBA_TEAMS]
            away_team_selection = st.selectbox(
                "Choose the away team",
                away_team_labels,
                index=0,
                label_visibility="collapsed"
            )
        
        # Check if form inputs have changed and clear prediction results
        current_form_values = {
            'date': game_date,
            'home_team': home_team_selection,
            'away_team': away_team_selection
        }
        
        # Store current form values for comparison
        if 'last_form_values' not in st.session_state:
            st.session_state.last_form_values = current_form_values
        elif st.session_state.last_form_values != current_form_values:
            # Form inputs changed - clear prediction results
            st.session_state.prediction_result = None
            st.session_state.show_form = True
            st.session_state.last_form_values = current_form_values
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Enhanced submit button
        submit_button = st.form_submit_button(
            "Predict Game Outcome",
            use_container_width=True
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
            
            # Enhanced loading state
            with st.spinner("Analyzing teams and making prediction..."):
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
    
    # Results header with enhanced styling
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2.5rem;'>
        <div style='
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 5rem;
            height: 5rem;
            background: linear-gradient(135deg, #ef4444, #dc2626);
            border-radius: 50%;
            margin-bottom: 1.5rem;
            box-shadow: 
                0 10px 25px rgba(239, 68, 68, 0.4),
                0 0 0 4px rgba(239, 68, 68, 0.2);
            animation: bounceIn 0.8s ease-out;
            position: relative;
        '>
            <span style='
                color: white; 
                font-size: 1.5rem; 
                font-weight: bold;
                filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
            '>✓</span>
            <div style='
                position: absolute;
                top: -10px;
                right: -10px;
                width: 20px;
                height: 20px;
                background: linear-gradient(135deg, #10b981, #059669);
                border-radius: 50%;
                border: 3px solid white;
                animation: pulse 2s ease-in-out infinite;
            '></div>
        </div>
        <h2 class='gradient-text' style='
            font-size: 2.2rem;
            margin-bottom: 1rem;
            line-height: 1.2;
            font-family: "Poppins", sans-serif;
        '>Prediction Results</h2>
        <div style='
            width: 80px;
            height: 2px;
            background: linear-gradient(90deg, transparent, #ef4444, transparent);
            margin: 0 auto;
            opacity: 0.7;
        '></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced game matchup section
    st.markdown("""
    <div style='text-align: center; margin-bottom: 1.5rem;'>
        <h3 style='
            color: #f3f4f6;
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 1rem;
            font-family: "Poppins", sans-serif;
        '>Game Matchup</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        st.markdown(f"""
        <div class='team-card'>
            <p class='team-label'>Away Team</p>
            <p class='team-name'>{form_data['away_team_label']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='vs-text' style='padding: 1rem;'>
            VS
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='team-card'>
            <p class='team-label'>Home Team</p>
            <p class='team-name'>{form_data['home_team_label']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Prediction results
    # Determine winner
    predicted_winner = result['predictedWinner']
    is_home_winner = predicted_winner == form_data['home_team']
    winner_label = form_data['home_team_label'] if is_home_winner else form_data['away_team_label']
    
    # Winner display
    st.markdown(f"""
    <div class='winner-display'>
        <p class='winner-label'>Predicted Winner</p>
        <p class='winner-name'>{winner_label}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced metrics section
    st.markdown("""
    <div style='text-align: center; margin: 2rem 0 1rem 0;'>
        <h4 style='
            color: #f3f4f6;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 1rem;
            font-family: "Poppins", sans-serif;
        '>Prediction Analytics</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class='metric-container'>
            <p style='color: #d1d5db; font-size: 0.9rem; margin-bottom: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;'>Win Probability</p>
            <p style='color: white; font-size: 1.8rem; font-weight: 800; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.3);'>{result['winProbability']}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-container'>
            <p style='color: #d1d5db; font-size: 0.9rem; margin-bottom: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;'>Confidence</p>
            <p style='color: white; font-size: 1.8rem; font-weight: 800; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.3);'>{result['confidence']}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Enhanced game date info
    st.info(f"**Game Date:** {form_data['date'].strftime('%B %d, %Y')}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Enhanced new prediction button
    if st.button("Make Another Prediction", use_container_width=True, key="new_prediction"):
        st.session_state.prediction_result = None
        st.session_state.form_data = None
        st.session_state.show_form = True
        st.rerun()

if __name__ == "__main__":
    main()
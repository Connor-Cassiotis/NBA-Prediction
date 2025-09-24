"""
Simple NBA Game Prediction API Server
Standalone version for testing
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import RidgeClassifier
import pickle
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)

# Simple mock prediction for testing
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': True,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/predict', methods=['POST'])
def predict_game():
    """Predict NBA game outcome - simplified version"""
    try:
        data = request.get_json()
        print(f"Received prediction request: {data}")
        
        # Validate input
        required_fields = ['date', 'home_team', 'away_team']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields: date, home_team, away_team'}), 400
        
        home_team = data['home_team']
        away_team = data['away_team']
        
        if home_team == away_team:
            return jsonify({'error': 'Home team and away team cannot be the same'}), 400
        
        # Mock prediction (for testing)
        # In a real scenario, this would use the actual ML model
        import random
        random.seed(hash(home_team + away_team))  # Consistent results for same teams
        
        win_probability = random.uniform(45, 80)  # Random between 45-80%
        predicted_winner = home_team if win_probability > 50 else away_team
        confidence = random.uniform(70, 90)
        
        result = {
            'predictedWinner': predicted_winner,
            'winProbability': round(win_probability, 1),
            'confidence': round(confidence, 1),
            'homeTeam': home_team,
            'awayTeam': away_team,
            'gameDate': data['date']
        }
        
        print(f"Prediction successful: {result}")
        return jsonify(result)
        
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

@app.route('/teams', methods=['GET'])
def get_teams():
    """Get list of available NBA teams"""
    teams = [
        "ATL", "BOS", "BRK", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW",
        "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK",
        "OKC", "ORL", "PHI", "PHX", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"
    ]
    return jsonify({'teams': teams})

if __name__ == '__main__':
    print("Starting Simple NBA Prediction API Server...")
    print("Server starting on http://localhost:5000")
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"Failed to start server: {str(e)}")
        import traceback
        traceback.print_exc()
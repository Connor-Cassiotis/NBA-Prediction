# NBA Game Predictor - Streamlit Version

A beautiful NBA game prediction application built with Streamlit that replicates the design and functionality of the original React frontend.

## Features

- **Elegant Dark Theme**: Matches the original React app's design with gradient backgrounds and animations
- **Team Selection**: Choose from all 30 NBA teams for home and away teams
- **Date Selection**: Pick any game date using the built-in date picker
- **AI Predictions**: Get win probability and confidence scores for game outcomes
- **Responsive Design**: Clean, modern interface optimized for the best user experience
- **Real-time Validation**: Form validation to prevent invalid selections

## Installation

1. **Clone or download the project**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
# Navigate to the project directory
cd NBA-Prediction

# Run the Streamlit app
streamlit run nba_predictor_streamlit.py

# Or using Python module syntax
python -m streamlit run nba_predictor_streamlit.py
```

The application will be available at: `http://localhost:8501`

## How to Use

1. **Select Game Date**: Choose the date for the NBA game you want to predict
2. **Choose Home Team**: Select the team playing at home from the dropdown
3. **Choose Away Team**: Select the visiting team from the dropdown
4. **Get Prediction**: Click "Predict Game Outcome" to get AI-powered predictions
5. **View Results**: See the predicted winner, win probability, and model confidence
6. **Make Another Prediction**: Use the "Make Another Prediction" button to start over

## Features Replicated from React Frontend

- **Dark theme with gradient backgrounds**
- **NBA team selection with all 30 teams**
- **Form validation and error handling** 
- **Loading states with spinners**
- **Results display with metrics**
- **Responsive layout and styling**
- **Smooth user experience**

## Technical Details

- **Framework**: Streamlit
- **Styling**: Custom CSS to match original design
- **Prediction Logic**: Mock prediction algorithm (same as Flask server)
- **Data**: NBA teams data structure converted from JavaScript
- **State Management**: Streamlit session state for managing app flow

## Comparison with Original

This Streamlit version provides the same user experience as the React frontend while being:
- **Easier to deploy** (single Python file)
- **No separate API server needed** (integrated backend)
- **Simpler maintenance** (one technology stack)
- **Quick to modify** (Python-based customization)

## Dependencies

- `streamlit>=1.50.0` - Web application framework
- `pandas>=1.4.0` - Data manipulation (if needed for future ML model)
- `numpy>=1.23.0` - Numerical computing (for predictions)

## Future Enhancements

- Integrate with real NBA prediction models
- Add historical game data
- Include team statistics and analytics  
- Add more advanced prediction algorithms
- Connect to live NBA APIs for real-time data
// API service for NBA prediction backend
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

export class APIError extends Error {
  constructor(message, status) {
    super(message);
    this.name = 'APIError';
    this.status = status;
  }
}

export const apiService = {
  async predictGame(gameData) {
    try {
      const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          date: gameData.date.toISOString().split('T')[0], // Format as YYYY-MM-DD
          home_team: gameData.homeTeam,
          away_team: gameData.awayTeam,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new APIError(
          data.message || data.error || 'Failed to get prediction',
          response.status
        );
      }

      return data;
    } catch (error) {
      if (error instanceof APIError) {
        throw error;
      }
      
      // Handle network errors
      if (error.name === 'TypeError' && error.message.includes('fetch')) {
        throw new APIError(
          'Cannot connect to prediction service. Please check if the backend is running.',
          0
        );
      }
      
      throw new APIError('An unexpected error occurred', 500);
    }
  },

  async healthCheck() {
    try {
      const response = await fetch(`${API_BASE_URL}/health`, {
        method: 'GET',
      });
      
      return response.ok;
    } catch (error) {
      return false;
    }
  }
};
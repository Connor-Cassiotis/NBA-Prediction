# NBA Game Prediction Frontend

A modern React application with TailwindCSS and Framer Motion for predicting NBA game outcomes using machine learning.

## Features

- 🎨 Modern rose-pink & black dark theme
- 📅 Interactive date picker for game dates
- 🏀 NBA team dropdowns with all current teams
- 🔮 Real-time prediction results with win probability
- ✨ Smooth animations and transitions
- 📱 Fully responsive design
- 🚀 Loading states and error handling

## Tech Stack

- **React** - Frontend framework
- **TailwindCSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **React DatePicker** - Date selection component

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- Backend NBA prediction API running

### Installation

1. Install dependencies:
   ```bash
   npm install
   ```

2. Configure environment variables:
   - Copy `.env` file and update `REACT_APP_API_URL` to your backend URL
   - Default: `http://localhost:5000`

3. Start the development server:
   ```bash
   npm start
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

### Backend Integration

The frontend expects a backend API with the following endpoint:

```
POST /predict
Content-Type: application/json

{
  "date": "2024-01-15",
  "home_team": "LAL",
  "away_team": "GSW"
}
```

Response format:
```json
{
  "predictedWinner": "LAL",
  "winProbability": 72.5,
  "confidence": 85.2
}
```

## Build for Production

```bash
npm run build
```

## Project Structure

```
src/
├── components/          # React components
│   ├── PredictionForm.js
│   └── ResultsDisplay.js
├── data/               # Static data
│   └── teams.js        # NBA teams data
├── services/           # API services
│   └── api.js          # Backend integration
├── App.js              # Main application
├── App.css             # Custom styles
└── index.css           # Global styles
```

## Customization

### Styling
- Modify `tailwind.config.js` for theme customization
- Update colors in the `rose` and `dark` palette
- Adjust animations and transitions

### Teams Data
- Update `src/data/teams.js` to modify team information
- Add team logos or additional metadata as needed

### API Integration
- Modify `src/services/api.js` for different backend endpoints
- Adjust request/response format as needed

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

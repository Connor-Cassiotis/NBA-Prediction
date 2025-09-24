import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import PredictionForm from './components/PredictionForm';
import ResultsDisplay from './components/ResultsDisplay';
import { apiService, APIError } from './services/api';
import './App.css';

function App() {
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [formData, setFormData] = useState(null);

  const handlePrediction = async (gameData) => {
    setIsLoading(true);
    setError(null);
    setPrediction(null);
    setFormData(gameData);

    try {
      const result = await apiService.predictGame(gameData);
      setPrediction(result);
    } catch (err) {
      if (err instanceof APIError) {
        setError(err.message);
      } else {
        setError('An unexpected error occurred. Please try again.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleNewPrediction = () => {
    setPrediction(null);
    setError(null);
    setFormData(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-dark-950 via-dark-900 to-dark-800">
      {/* Background Effects */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -inset-10 opacity-50">
          <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-red-900/10 rounded-full blur-3xl"></div>
          <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-red-800/5 rounded-full blur-3xl"></div>
        </div>
        
        {/* Animated Moving Bubbles */}
        <motion.div
          animate={{
            x: [0, 100, -50, 0],
            y: [0, -80, -30, 0],
          }}
          transition={{
            duration: 20,
            repeat: Infinity,
            ease: "linear"
          }}
          className="absolute top-1/3 left-1/6 w-32 h-32 bg-red-900/20 rounded-full blur-2xl"
        />
        <motion.div
          animate={{
            x: [0, -120, 80, 0],
            y: [0, 60, -40, 0],
          }}
          transition={{
            duration: 25,
            repeat: Infinity,
            ease: "linear"
          }}
          className="absolute top-2/3 right-1/4 w-48 h-48 bg-red-800/15 rounded-full blur-3xl"
        />
        <motion.div
          animate={{
            x: [0, 60, -90, 0],
            y: [0, -50, 70, 0],
          }}
          transition={{
            duration: 18,
            repeat: Infinity,
            ease: "linear"
          }}
          className="absolute bottom-1/3 left-1/3 w-24 h-24 bg-red-700/25 rounded-full blur-xl"
        />
        <motion.div
          animate={{
            x: [0, -80, 40, 0],
            y: [0, 90, -60, 0],
          }}
          transition={{
            duration: 22,
            repeat: Infinity,
            ease: "linear"
          }}
          className="absolute top-1/6 right-1/3 w-40 h-40 bg-red-900/12 rounded-full blur-2xl"
        />
        <motion.div
          animate={{
            x: [0, 110, -70, 0],
            y: [0, -40, 80, 0],
          }}
          transition={{
            duration: 28,
            repeat: Infinity,
            ease: "linear"
          }}
          className="absolute bottom-1/6 right-1/6 w-36 h-36 bg-red-800/18 rounded-full blur-3xl"
        />
        <motion.div
          animate={{
            x: [0, -40, 90, 0],
            y: [0, 70, -30, 0],
          }}
          transition={{
            duration: 16,
            repeat: Infinity,
            ease: "linear"
          }}
          className="absolute top-1/2 left-1/12 w-28 h-28 bg-red-900/22 rounded-full blur-xl"
        />
      </div>

      <div className="relative z-10 container mx-auto px-4 py-8 min-h-screen flex flex-col">
        <div className="max-w-6xl mx-auto flex-1 flex flex-col justify-start pt-16">
          {!prediction && !error && (
            <PredictionForm onSubmit={handlePrediction} isLoading={isLoading} />
          )}

          {(prediction || error) && (
            <div className="space-y-6">
              <ResultsDisplay 
                result={prediction} 
                error={error} 
                formData={formData} 
              />
              
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.5 }}
                className="flex justify-center"
              >
                <button
                  onClick={handleNewPrediction}
                  className="px-6 py-3 bg-dark-700 hover:bg-dark-600 text-white font-medium rounded-xl border border-dark-600 transition-all duration-200 hover:border-red-900/50"
                >
                  Make Another Prediction
                </button>
              </motion.div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;

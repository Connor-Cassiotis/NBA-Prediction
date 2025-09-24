import React from 'react';
import { motion } from 'framer-motion';
import { getTeamByValue } from '../data/teams';

const ResultsDisplay = ({ result, error, formData }) => {
  if (error) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="bg-red-900/20 border border-red-500/30 rounded-2xl p-6 shadow-lg max-w-md w-full mx-auto mt-6"
      >
        <div className="text-center">
          <motion.div
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ delay: 0.2, type: "spring" }}
            className="inline-flex items-center justify-center w-12 h-12 bg-red-500/20 rounded-full mb-4"
          >
            <svg className="w-6 h-6 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </motion.div>
          <h3 className="text-lg font-semibold text-red-400 mb-2">Prediction Failed</h3>
          <p className="text-red-300 text-sm">{error}</p>
        </div>
      </motion.div>
    );
  }

  if (!result) return null;

  const homeTeam = getTeamByValue(formData.homeTeam);
  const awayTeam = getTeamByValue(formData.awayTeam);
  
  // Assuming the result has winProbability and predictedWinner
  const winProbability = result.winProbability || result.confidence || 0;
  const predictedWinner = result.predictedWinner || result.winner;
  const isHomeWinner = predictedWinner === formData.homeTeam;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="bg-dark-800 border border-dark-700 rounded-2xl p-6 shadow-2xl max-w-md w-full mx-auto mt-6"
    >
      <div className="text-center">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.2, type: "spring" }}
          className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-r from-red-900 to-red-800 rounded-full mb-4"
        >
          <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
        </motion.div>

        <motion.h3
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="text-2xl font-bold bg-gradient-to-r from-red-900 to-red-800 bg-clip-text text-transparent mb-4"
        >
          Prediction Results
        </motion.h3>

        {/* Game Matchup */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="bg-dark-700 rounded-xl p-4 mb-6"
        >
          <div className="flex items-center justify-center space-x-4">
            <div className="text-center">
              <p className="text-dark-300 text-xs uppercase tracking-wide mb-1">Away</p>
              <p className="font-semibold text-white">{awayTeam?.label || 'Team'}</p>
            </div>
            <div className="text-red-900 font-bold text-lg">@</div>
            <div className="text-center">
              <p className="text-dark-300 text-xs uppercase tracking-wide mb-1">Home</p>
              <p className="font-semibold text-white">{homeTeam?.label || 'Team'}</p>
            </div>
          </div>
        </motion.div>

        {/* Prediction Result */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5 }}
          className="space-y-4"
        >
          <div>
            <p className="text-dark-300 text-sm mb-2">Predicted Winner</p>
            <p className="text-2xl font-bold text-white">
              {isHomeWinner ? homeTeam?.label : awayTeam?.label}
            </p>
          </div>

          <div>
            <p className="text-dark-300 text-sm mb-2">Win Probability</p>
            <div className="relative">
              <motion.div
                initial={{ width: 0 }}
                animate={{ width: `${winProbability}%` }}
                transition={{ delay: 0.6, duration: 1, ease: "easeOut" }}
                className="bg-gradient-to-r from-red-900 to-red-800 h-3 rounded-full"
              />
              <div className="absolute inset-0 bg-dark-600 rounded-full -z-10" />
            </div>
            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.8 }}
              className="text-3xl font-bold bg-gradient-to-r from-red-900 to-red-800 bg-clip-text text-transparent mt-2"
            >
              {Math.round(winProbability)}%
            </motion.p>
          </div>

          {/* Additional Info */}
          {result.confidence && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.9 }}
              className="text-xs text-dark-400 mt-4"
            >
              Model Confidence: {Math.round(result.confidence)}%
            </motion.div>
          )}
        </motion.div>

        {/* Game Date */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.0 }}
          className="mt-6 pt-4 border-t border-dark-600"
        >
          <p className="text-dark-400 text-xs">
            Game Date: {formData.date?.toLocaleDateString('en-US', { 
              weekday: 'long', 
              year: 'numeric', 
              month: 'long', 
              day: 'numeric' 
            })}
          </p>
        </motion.div>
      </div>
    </motion.div>
  );
};

export default ResultsDisplay;
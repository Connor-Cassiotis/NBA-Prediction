import React, { useState } from 'react';
import { motion } from 'framer-motion';
import DatePicker from 'react-datepicker';
import "react-datepicker/dist/react-datepicker.css";
import { NBA_TEAMS } from '../data/teams';

const PredictionForm = ({ onSubmit, isLoading }) => {
  const [formData, setFormData] = useState({
    date: new Date(),
    homeTeam: '',
    awayTeam: ''
  });

  const [errors, setErrors] = useState({});

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Reset errors
    setErrors({});
    
    // Validation
    const newErrors = {};
    if (!formData.homeTeam) newErrors.homeTeam = 'Please select a home team';
    if (!formData.awayTeam) newErrors.awayTeam = 'Please select an away team';
    if (formData.homeTeam === formData.awayTeam) {
      newErrors.general = 'Home team and away team cannot be the same';
    }
    
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }
    
    onSubmit(formData);
  };

  const handleInputChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }));
    
    // Clear errors when user starts typing
    if (errors[field]) {
      setErrors(prev => ({
        ...prev,
        [field]: ''
      }));
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="bg-dark-800 rounded-2xl p-8 shadow-2xl border border-dark-700 max-w-md w-full mx-auto"
    >
      <div className="text-center mb-8">
        <motion.h1 
          className="text-3xl font-bold bg-gradient-to-r from-red-900 to-red-800 bg-clip-text text-transparent mb-2"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
        >
          NBA Game Predictor
        </motion.h1>
        <p className="text-dark-300 text-sm">
          Predict NBA game outcomes with AI
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Date Picker */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.3 }}
        >
          <label className="block text-sm font-medium text-dark-200 mb-2">
            Game Date
          </label>
          <div className="relative">
            <DatePicker
              selected={formData.date}
              onChange={(date) => handleInputChange('date', date)}
              className="w-full px-4 py-3 bg-dark-700 border border-dark-600 rounded-xl text-white placeholder-dark-400 focus:outline-none focus:ring-2 focus:ring-red-900 focus:border-transparent transition-all"
              placeholderText="Select game date"
              dateFormat="MMMM d, yyyy"
            />
          </div>
        </motion.div>

        {/* Home Team Dropdown */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.4 }}
        >
          <label className="block text-sm font-medium text-dark-200 mb-2">
            Home Team
          </label>
          <select
            value={formData.homeTeam}
            onChange={(e) => handleInputChange('homeTeam', e.target.value)}
            className={`w-full px-4 py-3 bg-dark-700 border rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-red-900 focus:border-transparent transition-all appearance-none cursor-pointer ${
              errors.homeTeam ? 'border-red-500' : 'border-dark-600'
            }`}
          >
            <option value="">Select home team</option>
            {NBA_TEAMS.map((team) => (
              <option key={team.value} value={team.value} className="bg-dark-700">
                {team.label}
              </option>
            ))}
          </select>
          {errors.homeTeam && (
            <p className="text-red-400 text-xs mt-1">{errors.homeTeam}</p>
          )}
        </motion.div>

        {/* Away Team Dropdown */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.5 }}
        >
          <label className="block text-sm font-medium text-dark-200 mb-2">
            Away Team
          </label>
          <select
            value={formData.awayTeam}
            onChange={(e) => handleInputChange('awayTeam', e.target.value)}
            className={`w-full px-4 py-3 bg-dark-700 border rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-red-900 focus:border-transparent transition-all appearance-none cursor-pointer ${
              errors.awayTeam ? 'border-red-500' : 'border-dark-600'
            }`}
          >
            <option value="">Select away team</option>
            {NBA_TEAMS.map((team) => (
              <option key={team.value} value={team.value} className="bg-dark-700">
                {team.label}
              </option>
            ))}
          </select>
          {errors.awayTeam && (
            <p className="text-red-400 text-xs mt-1">{errors.awayTeam}</p>
          )}
        </motion.div>

        {/* General Error */}
        {errors.general && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-red-400 text-sm text-center bg-red-900/20 border border-red-500/30 rounded-lg p-3"
          >
            {errors.general}
          </motion.div>
        )}

        {/* Submit Button */}
        <motion.button
          type="submit"
          disabled={isLoading}
          className="w-full py-4 bg-gradient-to-r from-red-900 to-red-800 hover:from-red-800 hover:to-red-700 text-white font-semibold rounded-xl transition-all duration-200 transform hover:scale-[1.02] hover:shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none flex items-center justify-center gap-2"
          whileHover={{ scale: isLoading ? 1 : 1.02 }}
          whileTap={{ scale: isLoading ? 1 : 0.98 }}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.6 }}
        >
          {isLoading ? (
            <>
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
              Predicting...
            </>
          ) : (
            'Predict Game Outcome'
          )}
        </motion.button>
      </form>
    </motion.div>
  );
};

export default PredictionForm;
# 🏀 NBA Game Predictor - Deployment Guide

This guide will help you deploy your NBA Game Predictor application to various cloud platforms.

## 📋 Prerequisites

Before deploying, ensure you have:
- Git installed and your code in a Git repository
- A GitHub/GitLab account (for most platforms)
- Your code committed and pushed to a remote repository

## 🚀 Deployment Options

### Option 1: Deploy to Render (Recommended - Free & Easy)

**Render** is perfect for Streamlit apps and offers a free tier.

#### Steps:

1. **Sign up for Render**
   - Go to [https://render.com](https://render.com)
   - Sign up with your GitHub account

2. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `NBA-Prediction`
   - Select the repository

3. **Configure the Service**
   - **Name**: `nba-game-predictor` (or your preferred name)
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: Leave empty (or `NBA-Prediction` if nested)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

4. **Environment Variables** (Optional)
   - Add any environment variables if needed

5. **Deploy**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Your app will be available at: `https://nba-game-predictor.onrender.com`

**Free Tier Limitations:**
- App may sleep after 15 minutes of inactivity
- Takes 30-60 seconds to wake up
- 750 hours/month free

---

### Option 2: Deploy to Streamlit Community Cloud (Easiest)

**Streamlit Community Cloud** is specifically designed for Streamlit apps and is completely free!

#### Steps:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Sign up for Streamlit Cloud**
   - Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
   - Sign in with GitHub

3. **Deploy Your App**
   - Click "New app"
   - Select your repository: `Connor-Cassiotis/NBA-Prediction`
   - **Main file path**: `app.py`
   - Click "Deploy!"

4. **Your app will be live at:**
   - `https://[your-username]-nba-prediction.streamlit.app`

**Benefits:**
- ✅ Completely free
- ✅ No sleeping/cold starts
- ✅ Optimized for Streamlit
- ✅ Easy updates (just push to GitHub)

---

### Option 3: Deploy to Railway

**Railway** offers modern deployment with a generous free tier.

#### Steps:

1. **Sign up for Railway**
   - Go to [https://railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `NBA-Prediction` repository

3. **Configure**
   - Railway auto-detects Python
   - Add start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - Click "Deploy"

4. **Generate Domain**
   - Go to Settings → Generate Domain
   - Your app will be live!

---

### Option 4: Deploy to Heroku

**Heroku** is a classic platform with reliable deployment.

#### Steps:

1. **Install Heroku CLI**
   ```powershell
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```powershell
   heroku login
   ```

3. **Create Heroku App**
   ```powershell
   cd c:\Users\conno\Desktop\Nba-Predictor\NBA-Prediction
   heroku create nba-game-predictor
   ```

4. **Deploy**
   ```powershell
   git push heroku main
   ```

5. **Open Your App**
   ```powershell
   heroku open
   ```

---

### Option 5: Deploy to Vercel

**Vercel** is great for full-stack apps but requires some configuration for Streamlit.

⚠️ **Note**: Vercel is better suited for Flask/FastAPI. For Streamlit, use Streamlit Cloud or Render instead.

---

## 📁 Files Created for Deployment

Your project now includes these deployment files:

1. **`Procfile`** - Tells platforms how to start your app
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **`runtime.txt`** - Specifies Python version
   ```
   python-3.11.7
   ```

3. **`requirements.txt`** - Lists all Python dependencies (updated with specific versions)

4. **`.streamlit/config.toml`** - Streamlit configuration for production

---

## 🔧 Local Testing Before Deployment

Test your app locally to ensure it works:

```powershell
# Navigate to project directory
cd c:\Users\conno\Desktop\Nba-Predictor\NBA-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Visit `http://localhost:8501` to test.

---

## 🐛 Troubleshooting

### Issue: App crashes on startup
- **Solution**: Check that all `.pkl` model files are included in your repository
- Ensure `requirements.txt` has all dependencies

### Issue: Port binding errors
- **Solution**: The `Procfile` and `config.toml` are configured correctly for cloud platforms

### Issue: App is slow
- **Solution**: 
  - Use Streamlit Cloud (no cold starts)
  - On Render free tier, app sleeps after inactivity
  - Consider upgrading to paid tier for always-on service

### Issue: Missing files
- **Solution**: Ensure `.pkl` files are committed:
  ```powershell
  git add model.pkl scaler.pkl features.pkl feature_selector.pkl
  git commit -m "Add model files"
  git push
  ```

---

## 📊 Monitoring Your Deployment

- **Streamlit Cloud**: Built-in logs and analytics
- **Render**: View logs in the dashboard
- **Railway**: Real-time logs in project dashboard
- **Heroku**: Use `heroku logs --tail`

---

## 🔄 Updating Your Deployed App

After deploying, you can update your app by pushing changes:

```powershell
# Make your changes
git add .
git commit -m "Update: description of changes"
git push origin main
```

Most platforms auto-deploy on push to main branch!

---

## 🎉 Recommended Deployment Path

**For beginners**: → **Streamlit Community Cloud** (easiest, free, no cold starts)

**For production**: → **Render** (reliable, free tier available, good for multiple services)

**For enterprises**: → **AWS/Azure/GCP** (most scalable, requires more setup)

---

## 💡 Next Steps

1. Choose your deployment platform
2. Follow the steps for that platform
3. Share your live app URL!
4. Consider adding:
   - Custom domain
   - Analytics
   - User authentication
   - Database for storing predictions

---

## 📞 Need Help?

- **Streamlit Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app
- **Heroku Docs**: https://devcenter.heroku.com

---

Happy Deploying! 🚀🏀

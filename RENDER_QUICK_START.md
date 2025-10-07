# Quick Render Deployment Instructions

## Deploy to Render (5 minutes, more reliable than Streamlit Cloud)

1. **Go to Render**: https://render.com
2. **Sign up/Login** with GitHub
3. **Click "New +"** → "Web Service"
4. **Connect your repository**: `Connor-Cassiotis/NBA-Prediction`
5. **Configure**:
   - **Name**: `nba-predictor`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - **Instance Type**: `Free`
6. **Click "Create Web Service"**

✅ **Done!** Your app will be live at: `https://nba-predictor.onrender.com`

### Render Advantages:
- More stable deployment process
- Better error messages
- Free tier available
- No grayed-out button issues!

### Note:
Free tier sleeps after 15 min of inactivity (takes 30-60 sec to wake up).

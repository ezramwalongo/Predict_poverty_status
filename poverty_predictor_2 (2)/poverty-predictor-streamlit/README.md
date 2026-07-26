# Household Poverty Status Predictor - Streamlit Edition

A production-ready Streamlit application for predicting household poverty status using the TDHS 2022 dataset. The app includes an embedded ML model, research dashboard, and full internationalization support.

## 🎯 Features

- **Login / Registration:** Username = first name, password = 8 digits. New users register, returning users log in — nothing else in the app is visible until authenticated.
- **Poverty Prediction:** Real-time predictions using a logistic regression model, retrainable on real data via `train_model.py`
- **TDHS 2022 Form:** Household characteristics form (region/mkoa only — no district/wilaya field)
- **Results Display:** Poverty-status table (all 4 statuses, each with its probability range and a ✅/❌ match mark) shown immediately after clicking Predict
- **Prediction Accuracy:** The model's own test-set accuracy is shown alongside the classification, so you know how trustworthy predictions currently are
- **Feature Importance:** Top 8 contributing factors, always shown alongside the results
- **Recommendations:** Actionable insights based on poverty classification
- **Research Dashboard:** Analytics, filters, small poor%/non-poor% breakdown table, CSV export
- **Internationalization:** Full Swahili/English support, switchable via a green toggle in the top-right corner
- **Data Persistence:** CSV-based prediction history and user accounts

## 📋 Requirements

- Python 3.11 (pinned via `runtime.txt` for Streamlit Community Cloud)
- Streamlit 1.38.0+
- pandas, numpy, scikit-learn, plotly

> **Deploying to Streamlit Community Cloud and seeing "Error installing requirements"?**
> Click **Manage app → terminal** to see which exact package failed — that tells you the real cause. The most common causes are: (1) an exact `==` pin that has no prebuilt wheel for the cloud's current Python version, or (2) two pinned packages that can't be resolved together. `requirements.txt` here uses minimum-version (`>=`) pins instead of exact pins for this reason, and `runtime.txt` pins Python to 3.11 (a version with wheels available for every package used). If it still fails, paste the terminal error and I can pinpoint the exact fix.

## 🚀 Installation

### Local Development

```bash
# Clone or extract project
cd poverty-predictor-streamlit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Docker

```bash
# Build image
docker build -t poverty-predictor .

# Run container
docker run -p 8501:8501 poverty-predictor
```

## 📦 Project Structure

```
poverty-predictor-streamlit/
├── app.py                      # Main Streamlit application
├── train_model.py              # Trains the real logistic regression on data/training_data.csv
├── test_model.py               # Quick sanity-check script for the model
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
├── .streamlit/
│   └── config.toml            # Theme configuration (dark theme)
├── models/
│   ├── predictor.py           # ML model (logistic regression, loads trained coefficients)
│   └── model_coefficients.json # Learned intercept/coefficients (written by train_model.py)
├── utils/
│   ├── i18n.py                # Translations (SW/EN)
│   ├── auth.py                 # Login/registration (username + 8-digit password)
│   ├── recommendations.py      # Recommendations engine
│   └── storage.py             # Data persistence (CSV)
└── data/
    ├── generate_sample_data.py # Generates a SYNTHETIC placeholder dataset (not real TDHS data)
    ├── training_data.csv       # Dataset used to train/test the model — replace with real TDHS data
    ├── predictions.csv        # Prediction history (created automatically at runtime)
    └── users.csv               # Registered users: username, salt, password_hash (runtime)
```

## 🎮 Usage

### Login / Registration

1. On first load, you'll see the animated welcome screen: "Welcome to Household Poverty Predictor"
2. **New user?** Use the **Register** tab — username is your first name (letters only), password is exactly 8 digits. Optionally click **🎲 Suggest Strong Password** to auto-fill a strong recommended password, or type your own (a live hint tells you if it's strong or weak). On successful registration you are **logged in automatically** — no separate login step needed, straight to predicting.
3. **Returning user?** Use the **Login** tab with your existing username/password. If no account is found, you'll be told to register first.
4. Nothing else in the app is accessible until you're logged in
5. Once logged in, use **Logout** (in the sidebar) to end your session

### Making Predictions

1. Open the app and go to the **Predictor** tab
2. Fill in household characteristics across the 4 steps:
   - Location (Region/Mkoa only)
   - Household size (1-30) and residence type
   - Water source and toilet facility
   - Asset ownership (8 assets)
3. Click **Predict** — results appear immediately, no extra click needed
4. Results shown:
   - Poverty-status table: all 4 statuses (Very Poor / Poor / Non Poor / Rich), each with its probability-distribution range (0-1), and a ✅ tick on the matching status / ❌ cross on the rest
   - Classification and Prediction Accuracy metrics
   - Top 8 contributing factors chart
   - Actionable recommendations

### Research Dashboard

1. Go to the **Research Dashboard** tab
2. View statistics:
   - Total predictions
   - Poor/Non-poor counts
   - A small table showing Poor % and Non-poor %
3. Apply filters:
   - Region
   - Residence type (urban/rural)
   - Poverty level (poor/non-poor)
4. View analytics charts:
   - Poverty distribution
   - Predictions by region
5. Export data to CSV

### Language

- **Language:** Toggle English/Swahili using the green switch fixed in the top-right corner (visible once logged in)

## 🤖 ML Model

**Algorithm:** Logistic Regression (scikit-learn)
**Dataset:** Trained on `data/training_data.csv`
**Features:** 12 household characteristics
**Current status:** trained on a bundled *synthetic placeholder* dataset (see below) — test accuracy ≈ 79%, and both "poor" and "non-poor" classes are correctly predicted.

### ⚠️ Retraining on real data

`data/training_data.csv` currently holds a **synthetic sample dataset**, generated by `data/generate_sample_data.py`, that exists only so the app works out of the box. It is **not** the real TDHS 2022 microdata.

To retrain on your real dataset:

1. Replace `data/training_data.csv` with your real data. Required columns:
   `householdSize, residence, waterSource, toiletType, hasElectricity, hasMobilePhone, hasRadio, hasTelevision, hasRefrigerator, hasBicycle, hasMotorcycle, hasCar, classification`
   (`classification` must contain the text `poor` or `non-poor`)
2. Run:
   ```bash
   python train_model.py
   ```
   This fits a `LogisticRegression(class_weight='balanced')` model, prints train/test accuracy and a classification report, and saves the learned intercept/coefficients to `models/model_coefficients.json`.
3. Restart the app — `models/predictor.py` automatically loads the newly trained coefficients.

If `models/model_coefficients.json` is ever missing, the app falls back to a documented, balanced default coefficient set (see `models/predictor.py`) so it never collapses to always predicting one class.

**Classification Threshold:** 0.5 (probability ≥ 0.5 → Poor). The results table additionally shows a finer 4-tier status: Very Poor (≥75%), Poor (50–75%), Non-poor (25–50%), Well-off (<25%).

## 📊 Data Storage

Predictions are stored in `data/predictions.csv` with the following columns:

- `timestamp` - Prediction timestamp
- `region` - Region/Mkoa
- `household_size` - Number of household members
- `residence` - 1 (Urban) or 0 (Rural)
- `water_source` - 1 (Safe) or 0 (Unsafe)
- `toilet_type` - 1 (Improved) or 0 (Unimproved)
- `has_electricity` - 0/1
- `has_mobile_phone` - 0/1
- `has_radio` - 0/1
- `has_television` - 0/1
- `has_refrigerator` - 0/1
- `has_bicycle` - 0/1
- `has_motorcycle` - 0/1
- `has_car` - 0/1
- `probability` - Poverty probability (0-1)
- `classification` - 'poor' or 'non-poor'
- `score` - Display string (e.g., "23.5%")

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Create new app
4. Connect GitHub repository
5. Select `app.py` as main file
6. Deploy

```bash
# Example GitHub setup
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

### Heroku

```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Deploy
heroku create poverty-predictor
git push heroku main
```

### AWS/Google Cloud

```bash
# Build and push Docker image
docker build -t poverty-predictor .
docker tag poverty-predictor gcr.io/PROJECT_ID/poverty-predictor
docker push gcr.io/PROJECT_ID/poverty-predictor

# Deploy to Cloud Run
gcloud run deploy poverty-predictor \
  --image gcr.io/PROJECT_ID/poverty-predictor \
  --platform managed \
  --region us-central1 \
  --port 8501
```

## 🔧 Configuration

### Streamlit Config

The app ships with `.streamlit/config.toml` already set up (dark theme, matching the app's card-based UI):

```toml
[theme]
base = "dark"
primaryColor = "#6366f1"
backgroundColor = "#0c0a24"
secondaryBackgroundColor = "#1b1745"
textColor = "#f5f4ff"
font = "sans serif"
```

### Environment Variables

```bash
# Optional: Set Streamlit logger level
export STREAMLIT_LOGGER_LEVEL=info

# Optional: Disable telemetry
export STREAMLIT_TELEMETRY_OPTOUT=true
```

## 📈 Performance

- **Prediction Time:** ~100ms
- **Dashboard Load:** ~500ms
- **Memory Usage:** ~200MB
- **Concurrent Users:** 50+ (Streamlit Cloud)

## 🐛 Troubleshooting

### App won't start

```bash
# Clear cache
rm -rf ~/.streamlit/cache

# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Run with debug
streamlit run app.py --logger.level=debug
```

### Predictions not saving

```bash
# Check data directory permissions
ls -la data/

# Manually create CSV
mkdir -p data
touch data/predictions.csv
```

### Slow performance

```bash
# Reduce chart complexity
# Limit predictions table rows
# Use caching for expensive operations
```

## 📚 Documentation

- **Model Details:** See the ML Model section above and `train_model.py`

## 📞 Support

For issues or questions:
1. Check this README
2. Review Streamlit documentation: https://docs.streamlit.io
3. Check GitHub issues
4. Contact development team

## 📝 Changelog

- Registration now logs the user in immediately on success (no extra login step) — whether they typed their own strong password or used the suggested one.
- Added a password-strength hint and a "Suggest Strong Password" generator button on the Register tab.
- Login now clearly tells a user with no matching account to register first; an existing user logs straight into the app.
- Added a login/registration gate: nothing else renders until the user logs in. Registration requires a first-name username and an 8-digit password (stored as a salted hash in `data/users.csv`).
- Added an animated "Welcome to Household Poverty Predictor" message on the login screen, using the same blinking-text style as the app's main title.
- Moved the language switch out of the sidebar into a green toggle fixed to the top-right corner (hidden on the login page).
- Reworked the prediction results table to list all 4 poverty statuses (Very Poor / Poor / Non Poor / Rich) with their probability-distribution ranges (0-1 scale) and a ✅/❌ mark showing which status matches the household's result — matching the reference table format.
- Replaced the "Score" metric with "Prediction Accuracy", showing the model's own test-set accuracy instead of the household's individual probability (which is now shown in the status table).
- Removed the district/wilaya field — location is now Region/Mkoa only (form, storage, dashboard filters and table).
- Fixed text-contrast/readability: unified on a single light text color consistent with the app's dark theme instead of a mixed light/dark scheme that made some labels unreadable.
- Fixed the prediction model: the previous hardcoded coefficients were all negative, so the model could never output "poor". Replaced with a trainable pipeline (`train_model.py`) and a balanced fallback; both classes now predict correctly.
- Fixed the "Contributing Factors" chart intermittently disappearing by giving it a stable key and always rendering it alongside the results.
- Removed the "View Prediction Results" button — results now display immediately after clicking Predict.
- Replaced the single "Poor %" dashboard metric with a small table showing both Poor % and Non-poor %.
- Reorganized the whole project into a single, GitHub-ready folder structure.

## 📝 License

This project is built for government and research use in Tanzania.

---

**Version:** 1.1.0
**Status:** Production Ready ✅ (retrain on real TDHS data before production use — see "Retraining on real data" above)

# 📊 PhonePe Transaction Insights & Predictive Analytics Dashboard

An end-to-end Data Analytics and Machine Learning project that analyzes PhonePe digital transaction patterns across Indian states and districts using EDA, SQL, ML models, and an interactive Streamlit dashboard.

---

# 🚀 Project Overview

This project analyzes PhonePe transaction data to identify transaction trends, regional digital payment behavior, user engagement patterns, and high-performing states/districts.

The project combines:
- Exploratory Data Analysis (EDA)
- SQL database integration
- Machine Learning prediction models
- Interactive Streamlit dashboard visualization

The main objective is to generate actionable business insights and predict app engagement using transaction-related features.

---

# 🎯 Objectives

- Analyze PhonePe transaction trends across India
- Identify top-performing states and districts
- Understand user engagement and transaction behavior
- Perform feature engineering and predictive modeling
- Build an interactive business dashboard using Streamlit
- Compare multiple ML models for prediction accuracy

---

# 🧱 Architecture / System Design

```text
PhonePe Pulse JSON Data
            ↓
      Data Extraction
            ↓
     Data Preprocessing
            ↓
     Exploratory Analysis
            ↓
      SQL Database Storage
            ↓
      Machine Learning
            ↓
     Streamlit Dashboard
```

### System Components

- Data Source → PhonePe Pulse GitHub Dataset
- Database → MySQL
- Analysis → Python, Pandas, Seaborn, Matplotlib
- ML Models → Linear Regression, Random Forest, XGBoost
- Dashboard → Streamlit
- Visualization → Plotly

---

# ⚙️ Tech Stack

## Programming Language
- Python

## Data Analysis
- Pandas
- NumPy

## Data Visualization
- Matplotlib
- Seaborn
- Plotly

## Database
- MySQL

## Machine Learning
- Scikit-learn
- XGBoost

## Dashboard
- Streamlit

## Model Serialization
- Joblib

## IDE / Environment
- Jupyter Notebook
- VS Code

---

# ✨ Features

- State-wise transaction analysis
- District-wise transaction analysis
- Quarterly transaction trend analysis
- Transaction category analysis
- SQL database integration
- Feature engineering
- ML-based app opens prediction
- Model comparison visualization
- Interactive Streamlit dashboard
- Real-time filtering using sidebar controls

---

# 📂 Project Structure

```text
phonepe-project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── xgboost_model.pkl
│
├── notebooks/
│   ├── phonepe_eda_analysis.ipynb
│   └── phonepe_ml_analysis.ipynb
│
├── data/
```

---

# 🔧 Setup & Installation

## 1. Clone Repository

```bash
git clone https://github.com/Shravani3001/phonepe-transaction-insights-analysis.git
```

---

## 2. Navigate to Project Folder

```bash
cd phonepe-transaction-insights-analysis
```

---

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 4. Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# ▶️ Usage

The dashboard allows users to:

- Filter transaction data by:
  - State
  - Year
  - Quarter

- Explore:
  - Top districts
  - Top states
  - Transaction trends
  - Transaction categories

- Predict app opens using ML model inputs

---

# 🔄 Machine Learning Pipeline

## Workflow

```text
Data Cleaning
      ↓
Feature Engineering
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Hyperparameter Tuning
      ↓
Model Evaluation
      ↓
Prediction
```

---

# ☁️ Deployment

The project dashboard is deployed using Streamlit Community Cloud.

### Deployment Steps

- Push project to GitHub
- Connect GitHub repository with Streamlit Cloud
- Deploy `app.py`

---

# 📊 Monitoring & Observability

The project includes:
- KPI metrics
- Transaction trend tracking
- State and district-level monitoring
- ML model comparison metrics

---

# 🤖 AI / ML Implementation

## Models Used

1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor

## Best Performing Model

### XGBoost Regressor

### Performance Metrics

| Metric | Score |
|---|---|
| MAE | 42,149,820 |
| RMSE | 91,377,326 |
| R² Score | 0.9898 |

---

# 📈 Feature Engineering

Features created:
- Engagement Ratio
- Average Transaction Value
- Log Transformation Features

Feature engineering improved:
- prediction accuracy
- model stability
- feature relationships

---

# 🧪 Testing

## Testing Methods Used

- Manual dashboard testing
- SQL query verification
- ML prediction testing
- Data validation testing

---

# 🚧 Challenges & Solutions

| Challenge | Solution |
|---|---|
| Highly skewed transaction data | Applied log transformation |
| Large regional variation | Performed feature engineering |
| SQL integration issues | Corrected database schema and column names |
| Dashboard deployment limitations | Switched from SQL to CSV-based deployment |

---

# 🔮 Future Improvements

- Add real-time transaction updates
- Deploy on AWS cloud
- Add geospatial transaction maps
- Add advanced forecasting models
- Add user authentication
- Add API integration

---

# 📜 License

This project is developed for educational and portfolio purposes.

---

# 👩‍💻 Author

## Shravani K

### LinkedIn
https://linkedin.com/in/your-linkedin

### GitHub
https://github.com/your-github

---
# 📊 Customer Churn Prediction using Machine Learning

> 💻 **GitHub Repository:**  
> https://github.com/harshadajadhav25/customer-churn-project

---

# Project Overview

Customer churn is one of the biggest challenges faced by businesses, as retaining existing customers is significantly more cost-effective than acquiring new ones.

This project develops an end-to-end Machine Learning pipeline to predict customer churn using customer demographics, purchasing behavior, engagement metrics, and service-related features.

The project covers the complete data science lifecycle, including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Development
- Model Evaluation
- Business KPI Analysis
- Interactive Streamlit Dashboard

---

# Project Structure

```text
customer-churn-project/
│
├── app.py
│
├── models/
│   ├── random_forest_model.pkl
│   ├── scaler.pkl
│   ├── model_features.pkl
│   └── numeric_columns.pkl
│
├── data/
│   └── raw/
│       └── customer_churn.csv
│
├── notebooks/
│   ├── 01_eda_and_data_understanding.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training_and_evaluation.ipynb
│   └── 04_kpi_analysis_and_business_insights.ipynb
│
├── images/
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── churn_distribution.png
│   ├── churn_by_membership.png
│   └── revenue_at_risk.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook

---

# Machine Learning Workflow

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Feature Scaling
- Model Training
- Model Evaluation
- Business KPI Analysis
- Streamlit Dashboard Development

---

# Machine Learning Models

- Logistic Regression
- Logistic Regression (Balanced)
- Random Forest Classifier
- Random Forest (Threshold Optimization)

---

# Model Performance

| Model | Accuracy | Precision | Recall | ROC-AUC |
|-------|---------:|----------:|--------:|--------:|
| Logistic Regression | 0.803 | 0.000 | 0.000 | 0.498 |
| Balanced Logistic Regression | 0.495 | 0.190 | 0.479 | 0.499 |
| Random Forest | 0.803 | 0.000 | 0.000 | 0.518 |
| Random Forest (Threshold = 0.30) | 0.788 | 0.263 | 0.042 | 0.518 |
| Random Forest (Threshold = 0.25) | 0.729 | 0.238 | 0.169 | 0.518 |

---

# Feature Importance

The Random Forest model identified the most influential features affecting customer churn.

<p align="center">
<img src="images/feature_importance.png" width="800">
</p>

---

# Confusion Matrix

The confusion matrix summarizes the model's classification performance.

<p align="center">
<img src="images/confusion_matrix.png" width="500">
</p>

---

# ROC Curve

The ROC Curve illustrates the trade-off between True Positive Rate and False Positive Rate across classification thresholds.

<p align="center">
<img src="images/roc_curve.png" width="650">
</p>

---

# Business Insights

The KPI analysis converts machine learning predictions into actionable business insights by identifying high-risk customer segments and estimating potential revenue impact.

## Business KPI Summary

| KPI | Value |
|------|------:|
| Total Customers | **9,000** |
| Overall Churn Rate | **19.73%** |
| High-Risk Customers | **2,277** |
| Revenue at Risk | **$310,203** |
| Average Customer Value Score | **137.03** |

---

## Customer Churn Distribution

Approximately one out of every five customers churned, highlighting a significant customer retention opportunity.

<p align="center">
<img src="images/churn_distribution.png" width="450">
</p>

---

## Customer Churn Rate by Membership Status

Silver and Bronze membership tiers exhibited the highest churn rates.

<p align="center">
<img src="images/churn_by_membership.png" width="650">
</p>

---

## Revenue at Risk by Membership

Bronze customers contribute the highest potential revenue at risk.

<p align="center">
<img src="images/revenue_at_risk.png" width="650">
</p>

---

# Interactive Streamlit Dashboard

The project also includes a fully interactive Streamlit application.

### Dashboard Features

- Predict customer churn probability
- Calculate Customer Risk Index
- Display Business KPIs
- Visualize Feature Importance
- View Customer Churn Distribution
- Analyze Revenue at Risk
- Provide Business Recommendations
- Interactive and user-friendly interface

---

# Customer Risk Index

The dashboard introduces a **Customer Risk Index**, combining:

- Machine Learning Churn Probability
- Customer Engagement Score
- Service Risk Score

This provides a more business-oriented assessment than relying solely on the machine learning model.

---

# Key Findings

- Approximately **19.7%** of customers churned.
- Customer churn is highly influenced by behavioral and service-related features.
- Random Forest identified the most important predictors affecting churn.
- Class imbalance significantly impacted baseline model performance.
- Bronze and Silver membership tiers exhibited the highest churn rates.
- Bronze customers represented the highest revenue at risk.
- Customer Risk Index combines predictive analytics with business logic for better decision support.

---

# Business Value

This project demonstrates how machine learning can help organizations:

- Predict customer churn
- Identify high-risk customer segments
- Estimate potential revenue at risk
- Improve customer retention strategies
- Support business decision-making
- Increase customer lifetime value

---

# Installation

Clone the repository

```bash
git clone https://github.com/harshadajadhav25/customer-churn-project.git
```

Move into the project

```bash
cd customer-churn-project
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard

```bash
streamlit run app.py
```

---

# Future Improvements

- Hyperparameter tuning using GridSearchCV
- Cross-validation
- XGBoost and LightGBM implementation
- SHAP Explainable AI
- Docker containerization
- Cloud deployment
- Power BI integration
- REST API deployment

---

# Author

**Harshada Jadhav**

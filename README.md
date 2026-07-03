# Customer Churn Prediction using Machine Learning

## Project Overview

Customer churn is one of the biggest challenges faced by businesses, as retaining existing customers is significantly more cost-effective than acquiring new ones. This project develops an end-to-end machine learning pipeline to predict customer churn using customer demographics, purchasing behavior, engagement metrics, and service-related features.

The project covers the complete data science lifecycle, including data preprocessing, feature engineering, exploratory data analysis (EDA), predictive modeling, model evaluation, and business KPI analysis to support data-driven customer retention strategies.

---

## Project Structure

```text
customer-churn-project/
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
- Jupyter Notebook

---

# Machine Learning Workflow

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Scaling
- Model Training
- Model Evaluation
- Business KPI Analysis

---

# Machine Learning Models

- Logistic Regression
- Logistic Regression (Balanced Class Weights)
- Random Forest Classifier
- Random Forest with Threshold Optimization

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

The Random Forest model identified the most influential features contributing to customer churn prediction.

<p align="center">
    <img src="images/feature_importance.png" width="800">
</p>

---

# Confusion Matrix

The confusion matrix summarizes the model's classification performance by comparing predicted and actual customer churn outcomes.

<p align="center">
    <img src="images/confusion_matrix.png" width="500">
</p>

---

# ROC Curve

The ROC Curve illustrates the trade-off between the True Positive Rate (Sensitivity) and False Positive Rate across different classification thresholds.

<p align="center">
    <img src="images/roc_curve.png" width="600">
</p>

---

# Business Insights

The KPI analysis translates machine learning predictions into actionable business insights by identifying high-risk customer segments and estimating their potential financial impact.

---

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

Approximately one out of every five customers has churned, highlighting a significant opportunity for targeted customer retention strategies.

<p align="center">
    <img src="images/churn_distribution.png" width="450">
</p>

---

## Customer Churn Rate by Membership Status

Silver and Bronze membership tiers experience the highest churn rates, indicating that these customer groups require greater attention from retention and loyalty programs.

<p align="center">
    <img src="images/churn_by_membership.png" width="650">
</p>

---

## Revenue at Risk by Membership

Bronze membership customers contribute the largest share of potential revenue at risk, followed by Silver members. Prioritizing these segments can maximize the financial impact of retention efforts.

<p align="center">
    <img src="images/revenue_at_risk.png" width="650">
</p>

---

# Key Findings

- Approximately **19.7%** of customers churned, indicating a meaningful customer retention opportunity.
- Customer churn is strongly influenced by behavioral, engagement, and service-related features.
- Random Forest identified the most influential predictors affecting churn.
- Class imbalance significantly impacted baseline model performance, making threshold optimization essential.
- Bronze and Silver membership tiers exhibited the highest churn rates.
- Bronze customers represented the highest amount of revenue at risk.
- Predictive analytics can help businesses proactively identify at-risk customers and improve retention strategies.

---

# Business Value

This project demonstrates how machine learning can help organizations:

- Predict customers who are likely to churn.
- Identify high-risk customer segments.
- Estimate potential revenue at risk.
- Support targeted customer retention campaigns.
- Improve customer lifetime value through data-driven decision-making.

---

# Future Improvements

- Hyperparameter tuning using GridSearchCV
- Cross-validation
- XGBoost and LightGBM implementation
- Model deployment using Flask or Streamlit
- Real-time churn prediction dashboard
- Interactive business dashboard using Power BI or Tableau

---

# Author

**Harshada Jadhav**
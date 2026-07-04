import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------
# Load Model Files
# -----------------------------
model = joblib.load("models/random_forest_model.pkl")
scaler = joblib.load("models/scaler.pkl")
model_features = joblib.load("models/model_features.pkl")
numeric_columns = joblib.load("models/numeric_columns.pkl")

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f4f6f8;
}

.block-container {
    padding-top: 1.5rem;
}

.header {
    background: linear-gradient(90deg, #5b1f2e, #8b2f45);
    padding: 1.5rem 2rem;
    border-radius: 18px;
    color: white;
    margin-bottom: 1.5rem;
}

.header h1 {
    margin: 0;
    font-size: 2.4rem;
}

.header p {
    margin-top: 0.5rem;
    font-size: 1rem;
}

.kpi-card {
    background-color: white;
    padding: 1.2rem;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.10);
    text-align: center;
    border-left: 6px solid #f28c28;
}

.kpi-number {
    font-size: 2rem;
    font-weight: 800;
    color: #f28c28;
}

.kpi-label {
    font-size: 0.95rem;
    color: #5b1f2e;
    font-weight: 700;
}

.section-card {
    background-color: white;
    padding: 1.4rem;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 1.2rem;
}

.result-high {
    background-color: #fdecea;
    color: #b42318;
    padding: 1.2rem;
    border-radius: 14px;
    font-size: 1.1rem;
    font-weight: 800;
}

.result-medium {
    background-color: #fff4e5;
    color: #b54708;
    padding: 1.2rem;
    border-radius: 14px;
    font-size: 1.1rem;
    font-weight: 800;
}

.result-low {
    background-color: #e8f5e9;
    color: #166534;
    padding: 1.2rem;
    border-radius: 14px;
    font-size: 1.1rem;
    font-weight: 800;
}

.explanation-box {
    background-color: white;
    color: #374151;
    padding: 1.2rem;
    border-radius: 14px;
    border-left: 6px solid #5b1f2e;
    font-size: 1rem;
    margin-top: 1rem;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="header">
    <h1>📊 Customer Churn Prediction Dashboard</h1>
    <p>
        A machine learning dashboard that predicts customer churn risk and supports
        business retention decisions using customer behavior, engagement, and service experience.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# KPI Cards
# -----------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-number">9,000</div>
        <div class="kpi-label">Total Customers</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-number">19.73%</div>
        <div class="kpi-label">Overall Churn Rate</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-number">2,277</div>
        <div class="kpi-label">High-Risk Customers</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-number">$310K</div>
        <div class="kpi-label">Revenue at Risk</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3 = st.tabs([
    "📌 Project Overview",
    "📈 Business Insights",
    "🔮 Predict Churn"
])

# -----------------------------
# Tab 1: Overview
# -----------------------------
with tab1:
    st.markdown("""
    <div class="section-card">
        <h3>About This Project</h3>
        <p>
        This project predicts whether a customer is likely to churn using machine learning.
        It uses customer demographics, purchase behavior, engagement activity, and service
        experience features to estimate customer churn risk.
        </p>
        <p>
        The project includes data preprocessing, feature engineering, model training,
        model evaluation, and KPI-based business analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="section-card">
            <h3>Machine Learning Workflow</h3>
            <ul>
                <li>Data Cleaning</li>
                <li>Exploratory Data Analysis</li>
                <li>Feature Engineering</li>
                <li>Feature Scaling</li>
                <li>Random Forest Model Training</li>
                <li>Model Evaluation</li>
                <li>Business Risk Analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-card">
            <h3>Model and Risk Logic</h3>
            <ul>
                <li>Model: Random Forest Classifier</li>
                <li>ML output: churn probability</li>
                <li>Final output: Customer Risk Index</li>
                <li>The risk index combines ML probability, engagement, and service risk</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# Tab 2: Business Insights
# -----------------------------
with tab2:
    st.markdown("## Business Insight Visualizations")

    image_paths = {
        "Customer Churn Distribution": "images/churn_distribution.png",
        "Churn Rate by Membership": "images/churn_by_membership.png",
        "Revenue at Risk by Membership": "images/revenue_at_risk.png",
        "Feature Importance": "images/feature_importance.png"
    }

    for title, path in image_paths.items():
        if Path(path).exists():
            st.markdown(f"### {title}")
            st.image(path, use_container_width=True)
        else:
            st.warning(f"Image not found: {path}")

# -----------------------------
# Tab 3: Prediction
# -----------------------------
with tab3:
    st.markdown("## Predict Customer Churn Risk")
    st.write(
        "Enter customer information below. The app will calculate the ML churn probability "
        "and a combined Customer Risk Index."
    )

    with st.form("churn_form"):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 👤 Customer Profile")
            age = st.number_input("Age", min_value=18, max_value=100, value=30)
            gender = st.selectbox("Gender", ["Female", "Male", "Other"])
            region = st.selectbox("Region", ["North", "South", "East", "West"])
            membership_status = st.selectbox(
                "Membership Status",
                ["Bronze", "Silver", "Gold", "Platinum"]
            )

            st.markdown("### 💳 Purchase Behavior")
            annual_income = st.number_input("Annual Income (USD)", min_value=0.0, value=50000.0)
            total_purchases = st.number_input("Total Purchases", min_value=0, value=5)
            avg_purchase_value = st.number_input("Average Purchase Value", min_value=0.0, value=100.0)

        with col2:
            st.markdown("### 🌐 Engagement")
            website_visits = st.number_input("Website Visits Last Month", min_value=0, value=10)
            avg_time = st.number_input("Average Time Per Visit (Minutes)", min_value=0.0, value=10.0)
            referred_friends = st.number_input("Referred Friends", min_value=0, value=0)

            st.markdown("### 🛠 Service Experience")
            support_tickets = st.number_input("Support Tickets Last 6 Months", min_value=0, value=1)
            satisfaction_score = st.slider("Satisfaction Score", 1, 5, 3)
            days_since_purchase = st.number_input("Days Since Last Purchase", min_value=0, value=30)
            payment_method = st.selectbox(
                "Preferred Payment Method",
                ["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]
            )

        submitted = st.form_submit_button("Predict Churn")

    if submitted:
        # -----------------------------
        # Feature Engineering
        # -----------------------------
        engagement_score = (
            website_visits * 0.4 +
            avg_time * 0.4 +
            referred_friends * 0.2
        )

        customer_value_score = (
            total_purchases * 0.5 +
            avg_purchase_value * 0.5
        )

        service_risk_score = (
            support_tickets * 0.7 +
            (5 - satisfaction_score) * 0.3
        )

        input_data = pd.DataFrame(0.0, index=[0], columns=model_features)

        input_values = {
            "Age": age,
            "Annual_Income_USD": annual_income,
            "Total_Purchases": total_purchases,
            "Avg_Purchase_Value": avg_purchase_value,
            "Website_Visits_Last_Month": website_visits,
            "Avg_Time_Per_Visit_Minutes": avg_time,
            "Support_Tickets_Last_6_Months": support_tickets,
            "Satisfaction_Score": satisfaction_score,
            "Referred_Friends": referred_friends,
            "Days_Since_Last_Purchase": days_since_purchase,
            "Engagement_Score": engagement_score,
            "Customer_Value_Score": customer_value_score,
            "Service_Risk_Score": service_risk_score
        }

        for col, value in input_values.items():
            if col in input_data.columns:
                input_data.loc[0, col] = value

        categorical_mappings = [
            f"Gender_{gender}",
            f"Membership_Status_{membership_status}",
            f"Preferred_Payment_Method_{payment_method}",
            f"Region_{region}"
        ]

        for col in categorical_mappings:
            if col in input_data.columns:
                input_data.loc[0, col] = 1

        input_data[numeric_columns] = scaler.transform(input_data[numeric_columns])

        # -----------------------------
        # ML Probability
        # -----------------------------
        churn_probability = model.predict_proba(input_data)[0][1]
        ml_score = churn_probability * 100

        # -----------------------------
        # Customer Risk Index
        # -----------------------------
        engagement_risk = max(0, 100 - (engagement_score * 10))
        service_risk_scaled = min(service_risk_score * 5, 100)

        customer_risk_index = (
            ml_score * 0.40 +
            engagement_risk * 0.25 +
            service_risk_scaled * 0.35
        )

        if customer_risk_index >= 60:
            final_risk = "High Risk"
        elif customer_risk_index >= 35:
            final_risk = "Medium Risk"
        else:
            final_risk = "Low Risk"

        # -----------------------------
        # Results
        # -----------------------------
        st.markdown("---")
        st.markdown("## Prediction Result")

        r1, r2, r3, r4 = st.columns(4)

        with r1:
            st.metric("ML Churn Probability", f"{churn_probability:.2%}")

        with r2:
            st.metric("Engagement Score", f"{engagement_score:.2f}")

        with r3:
            st.metric("Service Risk Score", f"{service_risk_score:.2f}")

        with r4:
            st.metric("Customer Risk Index", f"{customer_risk_index:.1f}/100")

        st.progress(customer_risk_index / 100)

        if final_risk == "High Risk":
            st.markdown(
                '<div class="result-high">🔴 Final Risk Level: High Risk</div>',
                unsafe_allow_html=True
            )
            st.write(
                "Recommended Action: Prioritize this customer for immediate retention outreach, "
                "offer personalized incentives, and investigate service issues."
            )

        elif final_risk == "Medium Risk":
            st.markdown(
                '<div class="result-medium">🟠 Final Risk Level: Medium Risk</div>',
                unsafe_allow_html=True
            )
            st.write(
                "Recommended Action: Monitor this customer closely, send targeted engagement offers, "
                "and encourage loyalty program participation."
            )

        else:
            st.markdown(
                '<div class="result-low">🟢 Final Risk Level: Low Risk</div>',
                unsafe_allow_html=True
            )
            st.write(
                "Recommended Action: Continue regular engagement and maintain positive customer experience."
            )

        st.markdown("""
        <div class="explanation-box">
            <b>How the Customer Risk Index is calculated:</b><br><br>
            The final risk level combines three signals:
            <ul>
                <li><b>ML Churn Probability</b>: Prediction from the Random Forest model</li>
                <li><b>Engagement Risk</b>: Lower engagement increases churn risk</li>
                <li><b>Service Risk</b>: More support issues and low satisfaction increase churn risk</li>
            </ul>
            This provides a more business-friendly risk score than relying only on the ML probability.
        </div>
        """, unsafe_allow_html=True)

        with st.expander("View Risk Score Components"):
            st.write(f"ML Score: {ml_score:.2f}")
            st.write(f"Engagement Risk: {engagement_risk:.2f}")
            st.write(f"Service Risk Scaled: {service_risk_scaled:.2f}")
            st.write(
                "Formula: Customer Risk Index = "
                "(ML Score × 0.40) + (Engagement Risk × 0.25) + (Service Risk × 0.35)"
            )
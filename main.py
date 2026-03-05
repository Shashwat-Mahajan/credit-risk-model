import streamlit as st
from prediction_helper import predict

# Page config
st.set_page_config(
    page_title="Credit Risk Modelling",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Risk Modelling Dashboard")
st.markdown("AI powered credit risk evaluation system")

st.divider()

# -------- INPUT SECTION --------

st.subheader("Applicant Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=28)

with col2:
    income = st.number_input("Annual Income (₹)", min_value=0, value=1200000)

with col3:
    loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=2560000)

# Loan Ratio
loan_to_income_ratio = loan_amount / income if income > 0 else 0

st.metric(
    label="Loan to Income Ratio",
    value=f"{loan_to_income_ratio:.2f}"
)

st.divider()

# -------- LOAN DETAILS --------

st.subheader("Loan Details")

col4, col5, col6 = st.columns(3)

with col4:
    loan_tenure_months = st.number_input(
        "Loan Tenure (Months)",
        min_value=1,
        value=36
    )

with col5:
    avg_dpd_per_delinquency = st.number_input(
        "Average DPD",
        min_value=0,
        value=20
    )

with col6:
    num_open_accounts = st.number_input(
        "Open Loan Accounts",
        min_value=1,
        max_value=4,
        value=2
    )

st.divider()

# -------- CREDIT BEHAVIOR --------

st.subheader("Credit Behaviour")

col7, col8 = st.columns(2)

with col7:
    delinquency_ratio = st.slider(
        "Delinquency Ratio",
        0, 100, 30
    )

with col8:
    credit_utilization_ratio = st.slider(
        "Credit Utilization Ratio",
        0, 100, 30
    )

st.divider()

# -------- ADDITIONAL DETAILS --------

st.subheader("Additional Details")

col9, col10, col11 = st.columns(3)

with col9:
    residence_type = st.selectbox(
        "Residence Type",
        ["Owned", "Rented", "Mortgage"]
    )

with col10:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Education", "Home", "Auto", "Personal"]
    )

with col11:
    loan_type = st.selectbox(
        "Loan Type",
        ["Unsecured", "Secured"]
    )

st.divider()

# -------- PREDICTION --------

if st.button("🔍 Calculate Risk", use_container_width=True):

    probability, credit_score, rating = predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_delinquency,
        delinquency_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
    )

    st.subheader("📊 Risk Assessment Result")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric(
            label="Default Probability",
            value=f"{probability:.2%}"
        )

    with r2:
        st.metric(
            label="Credit Score",
            value=credit_score
        )

    with r3:
        st.metric(
            label="Risk Rating",
            value=rating
        )

    st.progress(probability)

st.divider()

st.caption("Built with Streamlit • Credit Risk Prediction Model")
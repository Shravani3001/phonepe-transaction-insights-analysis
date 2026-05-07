# ============================================================
# PHONEPE TRANSACTION INSIGHTS DASHBOARD
# ============================================================

# Importing Required Libraries

import streamlit as st
import pandas as pd
import plotly.express as px
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PhonePe Transaction Dashboard",
    layout="wide"
)


# ============================================================
# DASHBOARD TITLE
# ============================================================

st.title("📊 PhonePe Transaction Insights Dashboard")

st.markdown(
    "Analyze PhonePe transaction trends across states and districts"
)


# ============================================================
# LOADING DATA FROM SQL
# ============================================================

aggregated_df = pd.read_csv("aggregated_transaction.csv")

map_df = pd.read_csv("map_transaction.csv")


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("Filter Data")

selected_state = st.sidebar.selectbox(
    "Select State",
    sorted(map_df['state'].unique())
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(map_df['year'].unique())
)

selected_quarter = st.sidebar.selectbox(
    "Select Quarter",
    sorted(map_df['quarter'].unique())
)


# ============================================================
# FILTERING DATA
# ============================================================

filtered_map_df = map_df[
    (map_df['state'] == selected_state) &
    (map_df['year'] == selected_year) &
    (map_df['quarter'] == selected_quarter)
]

filtered_agg_df = aggregated_df[
    (aggregated_df['state'] == selected_state) &
    (aggregated_df['year'] == selected_year) &
    (aggregated_df['quarter'] == selected_quarter)
]


# ============================================================
# KPI METRICS SECTION
# ============================================================

st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:

    total_transactions = int(
        filtered_map_df['transaction_count'].sum()
    )

    st.metric(
        "Total Transactions",
        total_transactions
    )

with col2:

    total_amount = float(
        filtered_map_df['transaction_amount'].sum()
    )

    st.metric(
        "Transaction Amount",
        f"₹ {total_amount:,.0f}"
    )

with col3:

    total_districts = filtered_map_df['district'].nunique()

    st.metric(
        "Active Districts",
        total_districts
    )


# ============================================================
# TOP DISTRICTS BY TRANSACTION AMOUNT
# ============================================================

st.subheader("🏆 Top Districts by Transaction Amount")

top_districts = filtered_map_df.sort_values(
    by='transaction_amount',
    ascending=False
).head(10)

fig1 = px.bar(
    top_districts,
    x='district',
    y='transaction_amount',
    color='transaction_amount',
    title='Top 10 Districts by Transaction Amount'
)

st.plotly_chart(fig1, use_container_width=True)


# ============================================================
# TRANSACTION CATEGORY ANALYSIS
# ============================================================

st.subheader("💳 Transaction Category Analysis")

category_df = filtered_agg_df.groupby('category')[
    'transaction_amount'
].sum().reset_index()

fig2 = px.pie(
    category_df,
    names='category',
    values='transaction_amount',
    title='Transaction Amount by Category'
)

st.plotly_chart(fig2, use_container_width=True)


# ============================================================
# QUARTER-WISE TRANSACTION TREND
# ============================================================

st.subheader("📈 Quarter-wise Transaction Trend")

quarter_df = aggregated_df.groupby(
    ['year', 'quarter']
)['transaction_amount'].sum().reset_index()

quarter_df['year_quarter'] = (
    quarter_df['year'].astype(str)
    + '-Q' +
    quarter_df['quarter'].astype(str)
)

fig3 = px.line(
    quarter_df,
    x='year_quarter',
    y='transaction_amount',
    markers=True,
    title='Transaction Growth Trend'
)

st.plotly_chart(fig3, use_container_width=True)


# ============================================================
# STATE-WISE TRANSACTION ANALYSIS
# ============================================================

st.subheader("🌍 State-wise Transaction Analysis")

state_df = aggregated_df.groupby('state')[
    'transaction_amount'
].sum().reset_index()

state_df = state_df.sort_values(
    by='transaction_amount',
    ascending=False
).head(10)

fig4 = px.bar(
    state_df,
    x='state',
    y='transaction_amount',
    color='transaction_amount',
    title='Top States by Transaction Amount'
)

st.plotly_chart(fig4, use_container_width=True)


# ============================================================
# MACHINE LEARNING PREDICTION SECTION
# ============================================================

st.subheader("🤖 ML Prediction - App Opens Forecast")

model = joblib.load(
    "models/xgboost_model.pkl"
)

registered_users = st.number_input(
    "Registered Users",
    min_value=0
)

transaction_count = st.number_input(
    "Transaction Count",
    min_value=0
)

transaction_amount = st.number_input(
    "Transaction Amount",
    min_value=0.0
)

engagement_ratio = st.number_input(
    "Engagement Ratio",
    min_value=0.0
)

avg_transaction_value = st.number_input(
    "Average Transaction Value",
    min_value=0.0
)

quarter = st.selectbox(
    "Quarter",
    [1, 2, 3, 4]
)

year = st.selectbox(
    "Year",
    sorted(map_df['year'].unique())
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button("Predict App Opens"):

    input_data = pd.DataFrame({
        'registered_users': [registered_users],
        'transaction_count': [transaction_count],
        'transaction_amount': [transaction_amount],
        'engagement_ratio': [engagement_ratio],
        'avg_transaction_value': [avg_transaction_value],
        'quarter': [quarter],
        'year': [year]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted App Opens: {int(prediction[0]):,}"
    )


# ============================================================
# MODEL COMPARISON SECTION
# ============================================================

st.subheader("📊 Model Comparison")

comparison_df = pd.DataFrame({
    'Model': [
        'Linear Regression',
        'Random Forest',
        'XGBoost'
    ],
    'R2 Score': [
        0.8010,
        0.9806,
        0.9864
    ]
})

fig5 = px.bar(
    comparison_df,
    x='Model',
    y='R2 Score',
    color='R2 Score',
    title='Model Performance Comparison'
)

st.plotly_chart(fig5, use_container_width=True)


# ============================================================
# BUSINESS INSIGHTS SECTION
# ============================================================

st.subheader("📌 Business Insights")

st.markdown(
    """
    - High transaction states contribute significantly to digital payment growth.
    - District-level analysis helps identify strong engagement regions.
    - Transaction amount strongly influences app engagement.
    - XGBoost achieved the best prediction performance among all models.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    "PhonePe Transaction Insights Dashboard using Streamlit"
)
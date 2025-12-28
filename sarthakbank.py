import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="HDFC Bank - AI Credit Evaluation",
    page_icon="🏦",
    layout="wide"
)

# --- Custom Styling (Optional CSS) ---
st.markdown("""
    <style>
    .big-font { font-size:20px !important; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: Loan Details ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/28/HDFC_Bank_Logo.svg", width=150)
    st.header("Loan Application Details")
    st.markdown("**Borrower:** Maruti Suzuki India Ltd")
    st.markdown("**Industry:** Automotive (OEM)")
    st.markdown("**Loan Amount:** ₹3.3 Crores")
    st.markdown("**Facility:** Unsecured Term Loan")
    st.markdown("---")
    st.markdown("**Analyst:** Credit AI Team")
    st.markdown("**Date:** Dec 28, 2025")

# --- Main Title ---
st.title("🛡️ AI-Based Credit Score Card")
st.markdown("### Corporate Credit Assessment Model (CCAM v4.0)")
st.divider()

# --- Section 1: The Riskometer & Top Metrics ---
col1, col2 = st.columns([1, 2])

with col1:
    # 1. Gauge Chart (Riskometer)
    score = 985
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "AI Credit Score", 'font': {'size': 24}},
        delta = {'reference': 750, 'increasing': {'color': "green"}},
        gauge = {
            'axis': {'range': [0, 1000], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#003366"}, # HDFC Blue
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 500], 'color': '#ffcccb'},  # High Risk (Red)
                {'range': [500, 750], 'color': '#fff4cc'}, # Moderate (Yellow)
                {'range': [750, 1000], 'color': '#d4edda'} # Low Risk (Green)
            ],
            'threshold': {
                'line': {'color': "green", 'width': 4},
                'thickness': 0.75,
                'value': 985
            }
        }
    ))
    fig_gauge.update_layout(height=300, margin=dict(l=10, r=10, t=50, b=10))
    st.plotly_chart(fig_gauge, use_container_width=True)

with col2:
    # 2. Key Metrics Cards
    st.subheader("⚠️ Risk Assessment Summary")
    
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Risk Rating", value="A1 (Low Risk)", delta="Stable")
    m2.metric(label="Prob. of Default (12M)", value="0.01%", delta="-0.05%", delta_color="inverse")
    m3.metric(label="Credit Limit Rec.", value="₹3,500 Cr", delta="High Cap")
    
    st.info("""
    **AI Verdict:** The borrower is in the **Safe Zone**. 
    Repayment probability is exceptionally high based on current liquidity velocity.
    """)

# --- Section 2: Factor Breakdown (Radar/Bar Chart) ---
st.divider()
st.subheader("📊 Factor Weightage & Performance")

c1, c2 = st.columns([1, 1])

# Data for Factors
data = {
    'Category': ['Repayment History', 'Cash Flow Velocity', 'Forensic Accounting', 'Sentiment Analysis', 'Macro Factors'],
    'Score': [100, 99, 96, 92, 95],
    'Weight': [30, 25, 20, 15, 10]
}
df_factors = pd.DataFrame(data)

with c1:
    # Radar Chart
    fig_radar = px.line_polar(df_factors, r='Score', theta='Category', line_close=True, 
                              range_r=[0, 100], title="Scoring Radar")
    fig_radar.update_traces(fill='toself', line_color='#003366')
    st.plotly_chart(fig_radar, use_container_width=True)

with c2:
    # Bar Chart for Contribution
    fig_bar = px.bar(df_factors, x='Score', y='Category', orientation='h', 
                     color='Score', color_continuous_scale='Blues',
                     title="Category Performance (0-100)")
    fig_bar.update_layout(xaxis_range=[0, 110])
    st.plotly_chart(fig_bar, use_container_width=True)

# --- Section 3: Advanced Diagnostics (O-Score / Z-Score) ---
st.divider()
st.subheader("🔬 Advanced Forensic Diagnostics")

d1, d2, d3 = st.columns(3)

with d1:
    st.markdown("### Altman Z-Score")
    st.markdown("<h1 style='text-align: center; color: green;'>8.9</h1>", unsafe_allow_html=True)
    st.progress(0.99)
    st.caption("Benchmark: > 2.99 (Safe Zone)")
    st.markdown("**Interpretation:** Bankruptcy is virtually impossible.")

with d2:
    st.markdown("### Ohlson O-Score")
    st.markdown("<h1 style='text-align: center; color: green;'>-3.5</h1>", unsafe_allow_html=True)
    st.progress(0.1)
    st.caption("Benchmark: Lower is Better")
    st.markdown("**Interpretation:** Probability of default < 1%.")

with d3:
    st.markdown("### Piotroski F-Score")
    st.markdown("<h1 style='text-align: center; color: green;'>9 / 9</h1>", unsafe_allow_html=True)
    st.progress(1.0)
    st.caption("Benchmark: 9 is Perfect")
    st.markdown("**Interpretation:** High operational efficiency & quality.")

# --- Section 4: Sentiment & Final Verdict ---
st.divider()
st.subheader("📰 AI Sentiment & News Scraping")

with st.expander("View Detailed NLP Insights", expanded=True):
    st.write("""
    * **Positive Signals (+):** Strong sales volume for 'Grand Vitara'; successful export growth to Africa/LatAm; declared dividends.
    * **Neutral Signals (=):** EV production timeline pushed to FY25; Hybrid tax debates.
    * **Negative Signals (-):** None significant. Small car segment volume decline (offset by SUV growth).
    """)

# Final Recommendation Block
st.divider()
st.markdown("### 🏁 Final Recommendation")

final_container = st.container()
final_container.success("""
    ## ✅ APPROVED
    **Recommendation:** Sanction the loan of ₹3.3 Crores.
    
    **Rationale:** 1. Zero-debt balance sheet.
    2. Perfect Piotroski Score (9/9).
    3. Strategic value for HDFC Bank > Loan Interest Income.
""")

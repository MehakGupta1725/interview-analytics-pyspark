import streamlit as st
import plotly.express as px
from analytics import analyze_data
from recommender import generate_recommendation

# ---------- PAGE CONFIG ----------

st.set_page_config(
    page_title="AI Interview Intelligence Platform",
    layout="wide"
)

# ---------- CSS ----------

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------- TITLE ----------

st.title("🚀 AI Interview Intelligence Platform")

# ---------- FILE UPLOAD ----------

uploaded_file = st.file_uploader(
    "Upload Interview Dataset",
    type=["csv"]
)

if uploaded_file:

    with open("uploaded.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    (
        df,
        _,
        _,
        _,
        _,
        _,
        _
    ) = analyze_data("uploaded.csv")

    pdf = df.toPandas()

    # ---------- SIDEBAR FILTERS ----------

    st.sidebar.header("Analytics Filters")

    category_filter = st.sidebar.multiselect(
        "Select Category",
        options=sorted(pdf["Category"].unique()),
        default=sorted(pdf["Category"].unique())
    )

    experience_filter = st.sidebar.slider(
        "Experience Range",
        int(pdf["Experience"].min()),
        int(pdf["Experience"].max()),
        (
            int(pdf["Experience"].min()),
            int(pdf["Experience"].max())
        )
    )

    search_candidate = st.sidebar.text_input(
        "Search Candidate"
    )

    # ---------- APPLY FILTERS ----------

    filtered_pdf = pdf.copy()

    filtered_pdf = filtered_pdf[
        filtered_pdf["Category"].isin(category_filter)
    ]

    filtered_pdf = filtered_pdf[
        (
            filtered_pdf["Experience"] >= experience_filter[0]
        )
        &
        (
            filtered_pdf["Experience"] <= experience_filter[1]
        )
    ]

    if search_candidate:

        filtered_pdf = filtered_pdf[
            filtered_pdf["Candidate"].str.contains(
                search_candidate,
                case=False,
                na=False
            )
        ]

    # ---------- EMPTY CHECK ----------

    if filtered_pdf.empty:

        st.warning(
            "No records match current filters."
        )

        st.stop()

    # ---------- RECALCULATE EVERYTHING ----------

    avg_score = filtered_pdf["Score"].mean()

    avg_confidence = filtered_pdf["Confidence"].mean()

    category_pdf = (
        filtered_pdf
        .groupby("Category")["Score"]
        .mean()
        .reset_index()
    )

    category_pdf.columns = [
        "Category",
        "Average Score"
    ]

    leaderboard_pdf = (
        filtered_pdf
        .groupby("Candidate")
        .agg({
            "Score":"mean",
            "Confidence":"mean",
            "Experience":"mean"
        })
        .reset_index()
        .sort_values(
            by="Score",
            ascending=False
        )
    )

    trend_pdf = (
        filtered_pdf
        .groupby("Date")["Score"]
        .mean()
        .reset_index()
    )

    trend_pdf.columns = [
        "Date",
        "Daily Avg"
    ]

    trend_pdf = trend_pdf.sort_values(
        by="Date"
    )

    heatmap_pdf = (
        filtered_pdf
        .groupby(
            ["Candidate","Category"]
        )["Score"]
        .mean()
        .reset_index()
    )

    # ---------- AI RECOMMENDATION ----------

    recommendation = generate_recommendation(
        avg_score,
        avg_confidence
    )

    # ---------- KPI DASHBOARD ----------

    st.subheader(
        "📊 Executive KPI Dashboard"
    )

    best_category = category_pdf.sort_values(
        by="Average Score",
        ascending=False
    ).iloc[0]["Category"]

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric(
        "Candidates",
        len(filtered_pdf)
    )

    c2.metric(
        "Avg Score",
        round(avg_score,2)
    )

    c3.metric(
        "Avg Confidence",
        round(avg_confidence,2)
    )

    c4.metric(
        "Top Category",
        best_category
    )

    c5.metric(
        "Readiness",
        recommendation["readiness"]
    )

    st.divider()

    # ---------- VISUALIZATIONS ----------

    left,right = st.columns(2)

    with left:

        st.subheader(
            "🏆 Category Leaderboard"
        )

        fig1 = px.bar(
            category_pdf,
            x="Category",
            y="Average Score",
            color="Category",
            title="Average Performance by Domain"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with right:

        st.subheader(
            "📈 Confidence vs Score"
        )

        fig2 = px.scatter(
            filtered_pdf,
            x="Confidence",
            y="Score",
            color="Category",
            size="Experience",
            hover_name="Candidate"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ---------- LEADERBOARD ----------

    st.divider()

    st.subheader(
        "🥇 Candidate Leaderboard"
    )

    st.dataframe(
        leaderboard_pdf,
        use_container_width=True
    )

    # ---------- TREND ANALYTICS ----------

    st.divider()

    st.subheader(
        "📈 Interview Trend Analytics"
    )

    fig3 = px.line(
        trend_pdf,
        x="Date",
        y="Daily Avg",
        markers=True,
        title="Daily Performance Trend"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # ---------- HEATMAP ----------

    st.divider()

    st.subheader(
        "🔥 Candidate Skill Heatmap"
    )

    fig4 = px.density_heatmap(
        heatmap_pdf,
        x="Candidate",
        y="Category",
        z="Score",
        color_continuous_scale="Viridis"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # ---------- AI PREDICTION ----------

    st.divider()

    st.subheader(
        "🤖 AI Prediction Engine"
    )

    st.info(
f"""
Readiness Level:
{recommendation['readiness']}

Predicted Interview Success:
{recommendation['prediction']}%

Recommendation:

{recommendation['recommendation']}
"""
    )

    # ---------- EXPORT REPORT ----------

    st.divider()

    st.subheader(
        "📥 Export Analytics Report"
    )

    csv_data = filtered_pdf.to_csv(
        index=False
    )

    st.download_button(
        label="Download Analytics Report",
        data=csv_data,
        file_name="analytics_report.csv",
        mime="text/csv"
    )

    # ---------- CLOUD ARCHITECTURE ----------

    st.divider()

    st.subheader(
        "☁ Cloud Architecture"
    )

    st.code(
"""
GitHub Repository
        ↓
Jenkins CI/CD Pipeline
        ↓
AWS EC2 Deployment
        ↓
Streamlit Dashboard
        ↓
PySpark Analytics Engine
"""
    )

    # ---------- RAW DATA ----------

    st.divider()

    st.subheader(
        "📄 Raw Dataset"
    )

    st.dataframe(
        filtered_pdf,
        use_container_width=True
    )

    # ---------- FOOTER ----------

    st.markdown(
"""
---
Built using

PySpark | Streamlit | AWS | Jenkins | Python
"""
    )
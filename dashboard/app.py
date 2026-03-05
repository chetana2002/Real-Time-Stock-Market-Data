import streamlit as st
import pandas as pd
import psycopg2
import time
import plotly.express as px

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Real-Time Stock Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Real-Time Stock Market Analytics Dashboard")

st.markdown("Live streaming stock data analytics using **Kafka + Spark + PostgreSQL + Streamlit**")

# -------------------------------
# Database Connection
# -------------------------------

@st.cache_resource
def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="stockdb",
        user="postgres",
        password="postgres"
    )
    return conn


# -------------------------------
# Fetch Data
# -------------------------------

def load_data():
    conn = get_connection()
    query = """
        SELECT *
        FROM stock_events
        ORDER BY event_time DESC
        LIMIT 1000
    """
    df = pd.read_sql(query, conn)
    return df


# -------------------------------
# Auto Refresh
# -------------------------------

refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", 2, 30, 5)

# -------------------------------
# Main Loop
# -------------------------------

placeholder = st.empty()

while True:

    with placeholder.container():

        df = load_data()

        if df.empty:
            st.warning("No streaming data available yet...")
        else:

            # Convert timestamp
            df["event_time"] = pd.to_datetime(df["event_time"])

            # -------------------------------
            # KPIs
            # -------------------------------

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Trades",
                len(df)
            )

            col2.metric(
                "Unique Stocks",
                df["symbol"].nunique()
            )

            col3.metric(
                "Average Price",
                round(df["price"].mean(), 2)
            )

            col4.metric(
                "Total Volume",
                int(df["volume"].sum())
            )

            st.divider()

            # -------------------------------
            # Price Trend Chart
            # -------------------------------

            st.subheader("📊 Stock Price Trend")

            price_chart = px.line(
                df.sort_values("event_time"),
                x="event_time",
                y="price",
                color="symbol",
                title="Stock Price Over Time"
            )

            st.plotly_chart(price_chart, use_container_width=True)

            # -------------------------------
            # Volume Chart
            # -------------------------------

            st.subheader("📦 Trade Volume")

            volume_chart = px.bar(
                df,
                x="symbol",
                y="volume",
                color="symbol",
                title="Volume per Stock"
            )

            st.plotly_chart(volume_chart, use_container_width=True)

            # -------------------------------
            # Latest Trades Table
            # -------------------------------

            st.subheader("🧾 Latest Trades")

            st.dataframe(
                df.sort_values("event_time", ascending=False),
                use_container_width=True
            )

    time.sleep(refresh_rate)
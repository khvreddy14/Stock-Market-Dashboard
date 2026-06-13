import yfinance as yf
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

st.title("📈 Stock Market Dashboard")

ticker = st.text_input(
    "Enter Stock Symbol",
    "AAPL"
)

stock = yf.Ticker(ticker)

try:
    info = stock.info

    st.subheader(f"{info['longName']} ({ticker.upper()})")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Current Price",
        f"${info.get('currentPrice', 'N/A')}"
    )

    col2.metric(
        "Market Cap",
        f"{info.get('marketCap', 'N/A')}"
    )

    col3.metric(
        "52 Week High",
        f"${info.get('fiftyTwoWeekHigh', 'N/A')}"
    )

    st.subheader("Historical Stock Data")

    data = stock.history(period="1y")

    st.line_chart(data["Close"])

    st.subheader("Recent Data")

    st.dataframe(data.tail())

except Exception as e:
    st.error(f"Error: {e}")
import yfinance as yf
import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# Auto-refresh every 10 seconds
st_autorefresh(interval=10 * 1000, key="refresh")

st.title("📈 Real-Time Financial Market Dashboard")

ticker = st.text_input("Enter Ticker (e.g. AAPL, EURUSD=X, GC=F)", value="AAPL")

if ticker:
    data = yf.download(ticker, period="1d", interval="1m")  # Intraday data

    if not data.empty:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines+markers', name='Close Price'))
        fig.update_layout(title=f"{ticker} - Intraday (1m)", xaxis_title="Time", yaxis_title="Price")
        st.plotly_chart(fig)

        st.write("📊 Live Stats:")
        st.write(data['Close'].describe())
    else:
        st.warning("No data found for the entered ticker.")

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# Display data
st.write("""
""")
st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)

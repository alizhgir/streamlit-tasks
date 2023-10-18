import yfinance as yf
import streamlit as st

st.write("""
# Простое приложение для котировок Apple

## Показывает графики цен закрытия торгов и объема торгов акциями компании Apple

""")

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits


st.write('Котировки закрытия')
st.line_chart(tickerDf.Close)


st.write('Объем продаж акций')
st.line_chart(tickerDf.Volume)
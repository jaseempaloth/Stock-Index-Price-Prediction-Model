import yfinance as yf
import pandas as pd

def load_data(ticker):
    # Load historical data for the given ticker from Yahoo Finance
    data = yf.Ticker(ticker)
    history = data.history(period="max")
    history = history.drop(columns=['Dividends', 'Stock Splits'])
    return history

def preprocess_data(data):
    # Preprocess data for modeling
    data['Tomorrow'] = data['Close'].shift(-1)
    data['Target'] = (data['Tomorrow'] > data['Close']).astype(int)
    return data.dropna()

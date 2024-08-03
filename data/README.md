# Data Information for Nifty 50 Forecasting

## Overview

This project uses historical stock price data for the Nifty 50 index, obtained from Yahoo Finance. The data includes daily trading information, which is crucial for forecasting future stock prices using machine learning techniques.

## Data Source

- **Source**: Yahoo Finance
- **Ticker Symbol**: `^NSEI` (Nifty 50 Index)

## Data Description

The dataset contains the following columns:

- **Open**: The price at which the stock opened on that day.
- **High**: The highest price reached during the trading day.
- **Low**: The lowest price reached during the trading day.
- **Close**: The price at which the stock closed on that day.
- **Volume**: The total number of shares traded on that day.

The dataset excludes the following columns:

- **Dividends**: Any dividend payments made to shareholders.
- **Stock Splits**: Adjustments made to the stock price and shares outstanding due to stock splits.

## Data Loading

Data is fetched programmatically using the `load_data` function from the `data_loader.py` module, which utilizes the `yfinance` library to fetch historical data for the specified ticker symbol.

## Preprocessing

The `preprocess_data` function is used to prepare the data for modeling by:

1. Creating a new column, **Tomorrow**, which holds the closing price for the next trading day.
2. Generating a **Target** column that indicates whether the closing price for the next day is higher than the current day's closing price.

This preprocessing step is crucial for transforming the raw data into a format suitable for machine learning algorithms.

## Usage

The data is utilized for forecasting stock prices using machine learning techniques, and the preprocessing steps prepare the data for use in various models.

## Notes

- Ensure that you have an active internet connection when running the code, as it fetches data directly from Yahoo Finance.
- The data is subject to Yahoo Finance's terms of service and should be used accordingly.
- Please refer to the main project README for more information on the overall workflow and code structure.
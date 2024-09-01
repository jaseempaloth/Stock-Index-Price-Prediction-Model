import pandas as pd
from sklearn.preprocessing import StandardScaler

def create_features(data, horizons, target_column='Target', price_column='Close'):
    # Error Handling: Check for required columns
    if target_column not in data.columns:
        raise ValueError(f"Column '{target_column}' not found in DataFrame.")
    if price_column not in data.columns:
        raise ValueError(f"Column '{price_column}' not found in DataFrame.")

    # Create additional features based on rolling averages and trends
    new_predictors = []

    for horizon in horizons:
        # Rolling Averages
        rolling_averages = data[price_column].rolling(horizon).mean()

        # Feature 1: Close Price Ratio to Rolling Average
        ratio_column = f'{price_column}_Ratio_{horizon}'
        data[ratio_column] = data[price_column] / rolling_averages

        # Feature 2: Target Variable Trend
        trend_column = f'{target_column}_Trend_{horizon}'
        data[trend_column] = data[target_column].shift(1).rolling(horizon).sum()

        # Exponential Moving Average (EMA)
        ema_column = f'EMA_{horizon}'
        data[ema_column] = data['Close'].ewm(span=horizon, adjust=False).mean()

        # Volatility (Rolling Standard Deviation)
        volatility_column = f'Volatility_{horizon}'
        data[volatility_column] = data['Close'].rolling(horizon).std()

        # Momentum
        momentum_column = f'Momentum_{horizon}'
        data[momentum_column] = data[price_column] - data[price_column].shift(horizon)

        new_predictors.extend([ratio_column, trend_column, ema_column, volatility_column, momentum_column])

    # Feature Scaling: Apply StandardScaler
    scaler = StandardScaler()
    data[new_predictors] = scaler.fit_transform(data[new_predictors])

    return data.dropna(), new_predictors
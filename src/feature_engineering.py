import pandas as pd

def create_features(data, horizons):
    # Create additional features based on rolling averages and trends
    new_predictors = []

    for horizon in horizons:
        rolling_averages = data.rolling(horizon).mean()
        ratio_column = f'Close_Ratio_{horizon}'
        data[ratio_column] = data['Close'] / rolling_averages['Close']

        trend_column = f'Trend_{horizon}'
        data[trend_column] = data.shift(1).rolling(horizon).sum()['Target']

        new_predictors += [ratio_column, trend_column]

    return data.dropna(), new_predictors
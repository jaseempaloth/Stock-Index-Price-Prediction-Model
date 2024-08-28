import pandas as pd
from src.model import predict


def backtest(data, model, predictors, start=2500, step=250):
    # Perform backtesting on the model
    all_predictions = []

    for i in range(start, data.shape[0], step):
        train = data.iloc[0:i].copy()
        test = data.iloc[i:(i+step)].copy()
        preds = predict(model, test, predictors)
        combined = pd.concat([test['Target'], pd.Series(preds, index=test.index, name='Prediction')], axis=1)
        all_predictions.append(combined)

    return pd.concat(all_predictions)



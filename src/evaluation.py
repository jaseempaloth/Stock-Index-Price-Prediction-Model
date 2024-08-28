from sklearn.metrics import precision_score
import pandas as pd

def evaluate_model(test_data, predictions):
    # Evaluate the model using precision
    precision = precision_score(test_data['Target'], predictions)
    return precision

def visualize_prediction(test_data, preds):
    # Visualize actual vs predicted values
    combined = pd.concat([test_data['Target'], pd.Series(preds, index=test_data.index, name='Prediction')], axis=1)
    combined.plot()
    

    



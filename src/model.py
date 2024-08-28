from sklearn.ensemble import RandomForestClassifier

def train_model(train_data, predictors):
    # Train the Random Forest model
    model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)
    model.fit(train_data[predictors], train_data['Target'])
    return model

def predict(model, test_data, predictors):
    # Make predictions using the trained model
    preds = model.predict(test_data[predictors])
    return preds


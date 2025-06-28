# Training a model that can predict the next day's closing price of Nvidia stock
# using data from a csv file containing stock information till the 10th June 2025

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def nvidia_prediction():
    # Load dataset from .csv file
    stock_info = pd.read_csv("Nvidia_stock_data.csv")

    # Test if dataset is properly loaded
    if stock_info.empty:
        raise ValueError("The dataset is empty")
    else:
        print("Dataset loaded successfully")

    # Feature selection
    features = stock_info[["Open", "High", "Low", "Volume"]]
    target = stock_info["Close"]

    # Use data of last 2 years for training
    stock_info["Date"] = pd.to_datetime(stock_info["Date"])
    stock_info = stock_info[stock_info["Date"] >= (pd.to_datetime("today") - pd.DateOffset(years=2))]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.5, random_state=42)

    # Model training
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Predict closing price for next day
    last_row = stock_info.iloc[-1][["Open", "High", "Low", "Volume"]].to_numpy().reshape(1, -1)
    next_day_prediction = model.predict(last_row)
    print(f"Predicted closing price for the next day: {next_day_prediction[0]:.2f}")
    
    # Model evaluation
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared: {r2:.2f}")

if __name__ == "__main__":
    try:
        nvidia_prediction()
    except Exception as e:
        print(f"An error occurred: {e}")
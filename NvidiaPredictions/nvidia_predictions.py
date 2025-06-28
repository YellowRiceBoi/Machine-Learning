import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def nvidia_prediction():
    # Load dataset from .csv file
    stock_info = pd.read_csv("Nvidia_stock_data.csv")

    # Test if dataset is properly red
    if stock_info.empty:
        raise ValueError("The dataset is empty")
    else:
        print("Dataset loaded successfully")

    # Feature selection
    features = stock_info[["Open", "High", "Low", "Volume"]]
    target = stock_info["Close"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Model training
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)

    # Predict the stock price for the next day
    next_day_features = pd.DataFrame({
        "Open": [142],
        "High": [150],
        "Low": [136],
        "Volume": [1000000]
    })

    # Predict the stock price for the next month based on the data
    next_month_features = pd.DataFrame({
        "Open": [145],
        "High": [155],
        "Low": [140],
        "Volume": [1200000]
    })

    # Make prediction for the next day
    next_day_prediction = model.predict(next_day_features)
    print(f"Predicted stock price for next day: {next_day_prediction[0]:.2f}")
    
    # Make prediction for the next month
    next_month_prediction = model.predict(next_month_features)
    print(f"Predicted stock price for next month: {next_month_prediction[0]:.2f}")
    
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
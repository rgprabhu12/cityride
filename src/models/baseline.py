import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from src.config import PROCESSED_DIR

def train_baseline():
    df = pd.read_parquet(PROCESSED_DIR / "model_dataset.parquet")

    features = ["hour", "day_of_week", "is_weekend", "lag_1", "lag_4"]
    X = df[features]
    y = df["demand"]

    split = int(len(df) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = RandomForestRegressor(n_estimators=50)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds, squared=False)

    print(f"Baseline RMSE: {rmse:.2f}")

if __name__ == "__main__":
    train_baseline()

import pandas as pd
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
    root_mean_squared_error
)
import pickle
import json
import os


def test_model(
    test_data_path="./data/processed/test_processed.csv",
    model_path="./model/model.pkl",
    metrics_path="./model_performance/metrics.json"
):
    try:
        # Load test data
        test_data = pd.read_csv(test_data_path)

        # Split features and target
        x_test = test_data.drop(columns=["SMPEA"])
        y_test = test_data["SMPEA"]

        # Load trained model
        with open(model_path, "rb") as file:
            model = pickle.load(file)

        # Make predictions
        y_pred = model.predict(x_test)

        # Calculate metrics
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = root_mean_squared_error(y_test, y_pred)

        metrics_dict = {
            "R2 Score": r2,
            "Mean Absolute Error": mae,
            "Mean Squared Error": mse,
            "Root Mean Squared Error": rmse
        }

        # Create directory for metrics
        metrics_dir = os.path.dirname(metrics_path)

        if metrics_dir:
            os.makedirs(metrics_dir, exist_ok=True)

        # Save metrics as JSON
        with open(metrics_path, "w") as file:
            json.dump(metrics_dict, file, indent=4)

        print("Model evaluation completed.")
        print(f"Metrics saved to: {metrics_path}")

        return metrics_dict

    except Exception as e:
        print(f"Error while evaluating model: {e}")

metrics = test_model()
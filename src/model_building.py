import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

def train_and_save_model(
    train_path = "./data/processed/train_processed.csv",
    model_path = "./model/model.pkl",
    target_column = "SMPEA",
    n_estimators = 500,
    n_jobs = -1
):
    train_data = pd.read_csv(train_path)

    x_train = train_data.drop(columns = [target_column])
    y_train = train_data[target_column]

    # Create and train model
    model = RandomForestRegressor(n_estimators = n_estimators, random_state = 42, n_jobs = n_jobs)
    model.fit(x_train, y_train)
 
    model_dir = os.path.dirname(model_path)

    if model_dir:
        os.makedirs(model_dir, exist_ok=True)

    with open(model_path, "wb") as file:
        pickle.dump(model, file)

    print(f"Model saved to: {model_path}")
    return model

model = train_and_save_model()
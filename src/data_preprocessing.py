import os
import pandas as pd

def remove_missing_column(df: pd.DataFrame):
    try:
        df = df.dropna()
        return df
    except Exception as e:
        print(e)

def preprocess_data(df: pd.DataFrame):
    try:
        for i in df.columns:
            df[i] = pd.to_numeric(df[i], errors = 'coerce')

        return df
    except Exception as e:
        print(e)

def main():
    try:
        train_data = pd.read_csv('./data/raw/train.csv')
        test_data = pd.read_csv('./data/raw/test.csv')

        train_data = remove_missing_column(train_data)
        test_data = remove_missing_column(test_data)

        train_processed = preprocess_data(train_data)
        test_processed = preprocess_data(test_data)

        data_path = os.path.join('./data', 'processed')
        os.makedirs(data_path, exist_ok = True)

        train_processed.to_csv(os.path.join(data_path, "train_processed.csv"), index = False)
        test_processed.to_csv(os.path.join(data_path, "test_processed.csv"), index = False)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
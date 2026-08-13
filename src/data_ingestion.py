import os
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(data_path: str):
    try:
        df = pd.read_csv(data_path, low_memory = False)
        return df
    except Exception as e:
        print(e)

def remove_column(df: pd.DataFrame, column_name):
    try:
        remove_df_column  = [col for col in column_name if col in df.columns]
        df = df.drop(columns = remove_df_column)
        return df
    except Exception as e:
        print(e)

def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str):
    try:
        raw_data = os.path.join(data_path, 'raw')
        os.makedirs(raw_data, exist_ok = True)
        train_data.to_csv(os.path.join(raw_data, "train.csv"), index = False)
        test_data.to_csv(os.path.join(raw_data, "test.csv"), index = False)
    except Exception as e:
        print(e)

def main():
    try:
        data_path = "https://raw.githubusercontent.com/amankharwal/Website-data/master/electricity.csv"
        df = load_data(data_path = data_path)
        column_name = ['DateTime', 'Holiday', 'HolidayFlag', 'DayOfWeek', 'WeekOfYear', 'Year', 'PeriodOfDay']
        df = remove_column(df, column_name)
        train_data, test_data = train_test_split(df, test_size = 0.2, random_state = 42)
        save_data(train_data, test_data, data_path = './data')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
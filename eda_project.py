import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = input('Insert the path of your dataframe: ')
file_format = input('What is your data format? (csv or xlsx): ')

def load_data(file_path, file_format):
    if file_format == 'csv':
        df = pd.read_csv(file_path)
    elif file_format == 'xlsx':
        df = pd.read_excel(file_path)
    return df

def data_inspection(df):
    print('Data types:\n', df.dtypes)
    print('Null data:\n', df.isnull().sum())

    categorical = [col for col in df.columns if df[col].dtype == 'O']
    numerical = [col for col in df.columns if df[col].dtype != 'O']

    print('Categorical columns:', categorical)
    print('Numerical columns:', numerical)

def preprocess_data(df):
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns

    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    df[categorical_columns] = df[categorical_columns].fillna('Unknown')

    return df

def visualize_data(df, target_column):
    column_data = df[target_column]

    if column_data.dtype == 'int64' or column_data.dtype == 'float64':
        plt.figure(figsize=(8, 6))
        plt.hist(column_data, bins=20)
        plt.title(f'Histogram of {target_column}')
        plt.xlabel(target_column)
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()
    elif column_data.dtype == 'object':
        plt.figure(figsize=(8, 6))
        column_data.value_counts().plot(kind='bar')
        plt.title(f'Frequency of {target_column}')
        plt.xlabel(target_column)
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

def main():
    df = load_data(file_path, file_format)
    data_inspection(df)
    preprocessed_data = preprocess_data(df)
    target_column = input('Choose column to visualize: ')
    visualize_data(preprocessed_data, target_column)

if __name__ == '__main__':
    main()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_explore_dataset(file_path):
    # Load the dataset from the CSV file
    dataset = pd.read_csv(file_path)

    # Explore the dataset
    print(dataset.head())  # Display the first few records of the dataset
    print(dataset.info())  # Display information about the dataset

    return dataset

def plot_numeric_distribution(data, column):
    plt.figure(figsize=(12, 6))
    sns.histplot(data=data, x=column, kde=True, color='skyblue')
    plt.title(f'Distribution of {column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def plot_categorical_count(data, column):
    plt.figure(figsize=(12, 6))
    if data[column].nunique() > 10:
        top_categories = data[column].value_counts().nlargest(10).index
        data[column] = data[column].where(data[column].isin(top_categories), 'Other')

    sns.countplot(data=data, x=column, palette='plasma', saturation=0.75)
    plt.title(f'Count of {column}')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def analyze_and_visualize_dataset(file_path, columns_to_analyze):
    dataset = load_and_explore_dataset(file_path)

    for col in columns_to_analyze:
        if dataset[col].dtype == 'int64' or dataset[col].dtype == 'float64':
            plot_numeric_distribution(dataset, col)
        else:
            plot_categorical_count(dataset, col)

# Example usage:
file_path = 'dataset.csv'
columns_to_analyze = ['show_id', 'type', 'title', 'director', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in']
analyze_and_visualize_dataset(file_path, columns_to_analyze)

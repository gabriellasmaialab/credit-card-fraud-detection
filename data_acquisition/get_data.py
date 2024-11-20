import kagglehub
import pandas as pd
import os

def load_kaggle_dataset_to_dataframe(dataset_name, csv_filename):
    """
    Downloads a dataset from Kaggle using kagglehub and loads a specified CSV file into a pandas DataFrame.

    Parameters:
    - dataset_name (str): The Kaggle dataset identifier in the format 'owner/dataset-name' (e.g., 'mlg-ulb/creditcardfraud').
    - csv_filename (str): The name of the CSV file in the dataset folder to load into a DataFrame.

    Returns:
    - pd.DataFrame: A pandas DataFrame containing the data from the specified CSV file.

    Raises:
    - FileNotFoundError: If the specified CSV file does not exist in the downloaded dataset folder.

    Example:
    ```
    df = load_kaggle_dataset_to_dataframe("mlg-ulb/creditcardfraud", "creditcard.csv")
    print(df.head())
    ```
    """
    # Download the dataset
    print(f"Downloading dataset '{dataset_name}'...")
    path = kagglehub.dataset_download(dataset_name)
    print("Dataset downloaded to:", path)

    # Construct the full path to the CSV file
    csv_file = os.path.join(path, csv_filename)

    # Check if the file exists
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"The file '{csv_filename}' was not found in the dataset directory: {path}")

    # Load the CSV file into a pandas DataFrame
    print(f"Loading file '{csv_filename}' into a DataFrame...")
    df = pd.read_csv(csv_file)
    print("Dataset loaded successfully!")

    return df
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file.
    """
    df = pd.read_csv(path)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning.
    """

    # Remove column with too many missing values
    if "Cabin" in df.columns:
        df = df.drop(columns=["Cabin"])

    # Fill missing Age values with median
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())

    # Fill missing Embarked values with mode
    if "Embarked" in df.columns:
        df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Remove duplicates
    df = df.drop_duplicates()

    return df

def save_clean_data(df: pd.DataFrame, path: str):
    """
    Save cleaned dataset.
    """
    df.to_csv(path, index=False)

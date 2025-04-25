import pandas as pd

def fill_missing_numeric(df: pd.DataFrame, columns: list, method="zero"):
    """fill NA in numeric columns using a specified method."""
    if method == "zero":
        df[columns] = df[columns].fillna(0)
    elif method == "mean":
        for col in columns:
            df[col] = df[col].fillna(df[col].mean())
    elif method == "median":
        for col in columns:
            df[col] = df[col].fillna(df[col].median())
    return df

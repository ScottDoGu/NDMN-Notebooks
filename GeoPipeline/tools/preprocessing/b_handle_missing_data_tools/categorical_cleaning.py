import pandas as pd

def fill_missing_categorical(df: pd.DataFrame, columns: list, fill_value="Not_Applicable"):
    """
    fill NA values in specified categorical columns with a default value using safe indexing.
    """
    df.loc[:, columns] = df[columns].fillna(fill_value)
    return df

import matplotlib.pyplot as plt 
import pandas as pd

def plot_missing_values(df: pd.DataFrame, title: str = "Missing Values by Column (Ascending Order)"):
    """
    Plot missing value counts for columns in ascending order and display exact counts.
    """
    # Count and sort missing values
    na_count = df.isna().sum()
    na_count_filtered = na_count[na_count > 0].sort_values(ascending=True)

    # Plot
    plt.figure(figsize=(8, 5))
    bars = na_count_filtered.plot(kind='barh', color='skyblue')
    plt.title(title)
    plt.xlabel('Count of Missing Values')
    plt.ylabel('Column')

    # Annotate each bar
    for index, value in enumerate(na_count_filtered):
        plt.text(value + 0.1, index, str(value), va='center')

    plt.tight_layout()
    plt.show()

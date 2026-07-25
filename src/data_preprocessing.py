import pandas as pd


def load_data():
    """Load the diabetes dataset."""
    return pd.read_csv("data/raw/diabetes.csv")


def explore_data(df):
    """Display basic information about the dataset."""
    print("\nFirst 5 Rows:\n")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nDataset Information:\n")
    df.info()

    print("\nStatistical Summary:\n")
    print(df.describe())

    print("\nMissing Values:\n")
    print(df.isnull().sum())


def check_hidden_missing_values(df):
    """Count medically impossible zero values."""
    columns = [
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI"
    ]

    print("\nNumber of Zero Values:\n")

    for column in columns:
        print(f"{column}: {(df[column] == 0).sum()}")


def main():
    df = load_data()
    explore_data(df)
    check_hidden_missing_values(df)


if __name__ == "__main__":
    main()
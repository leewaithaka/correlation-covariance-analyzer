import pandas as pd


def analyze_data():

    df = pd.read_csv("dataset.csv")

    print("\nDataset:\n")
    print(df)

    print("\nCovariance Matrix:\n")
    print(df.cov())

    print("\nCorrelation Matrix:\n")
    print(df.corr())

    print("\nInterpretation:")
    print("Correlation close to 1 → strong positive relationship")
    print("Correlation close to -1 → strong negative relationship")
    print("Correlation close to 0 → weak relationship")


if __name__ == "__main__":
    analyze_data()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

pd.plotting.scatter_matrix(df, figsize=(8,8))

plt.suptitle("Scatter Matrix of Variables")

plt.savefig("scatter_matrix.png")

plt.show()

import pandas as pd

dataset = pd.read_csv("cirrhosis.csv")

null_values=dataset.isnull()

null_counts=dataset.isnull().sum()

print("null values in the dataset:")
print(null_counts)


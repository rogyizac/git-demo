import pandas as pd

df = pd.read_csv(r"data\Iris_preprocessed.csv")
#4566
#Feature creation
df["Sepal_Area"] = df["SepalLengthCm"] * df["SepalWidthCm"]

df.to_csv(r"data\Iris.csv", index = False)

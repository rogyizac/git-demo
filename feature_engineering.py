import pandas as pd
#123
df = pd.read_csv(r"data\Iris_preprocessed.csv")
#456634
#Feature creation
df["Sepal_Area"] = df["SepalLengthCm"] * df["SepalWidthCm"]

df.to_csv(r"data\Iris.csv", index = False)

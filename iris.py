import pip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pip.main(["install","numpy"])
pip.main(["install","pandas"])

df = pd.read_csv("~/documents/iris.csv")

print(df.to_string())

print("df is:\n{}".format(df))

pip.main(["install","matplotlib"])

df.plot(kind='bar',x= 'sepal_length', y='sepal_width', color='red', ylabel="QTY", xlabel="Sepal Length")

print(df.dtypes)

#df["sepalArea"] = df["sepal_length"] * df["sepal_width"]
#df["petalArea"] = df["sepal_length"] * df["sepal_width"]
df.head()

#df.plot(kind="scatter",x="sepalArea", y="petalArea")

import matplotlib.pyplot as plt
#import seaborn as sns

df.plot(kind="scatter",x="sepal_length", y="sepal_width", c=df["species"].map({'Iris-setosa':'red','Iris-versicolor':'blue','Iris-virginica':'green'}))
print(df["species"].unique())

df.plot(kind='hist', x="sepal_length")
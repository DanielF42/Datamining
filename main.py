import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris_df = pd.read_csv(filepath_or_buffer='iris.data', names=['Sepal length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class'])

print(iris_df.head())

means = iris_df.iloc[:, :2].mean()
print(means)

sns.pairplot(iris_df)
plt.show()
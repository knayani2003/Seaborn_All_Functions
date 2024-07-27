import seaborn as sns
import matplotlib.pyplot as plt

# Pair Plot
data = sns.load_dataset("iris")
sns.pairplot(data, hue="species")
plt.show()

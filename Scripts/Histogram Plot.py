import seaborn as sns
import matplotlib.pyplot as plt

# Histogram Plot
data = sns.load_dataset("tips")
sns.histplot(data, x="day", hue="sex", kde=True)
plt.show()

data = sns.load_dataset("titanic")
sns.histplot(data, x="age", hue="who", kde=True)
plt.show()

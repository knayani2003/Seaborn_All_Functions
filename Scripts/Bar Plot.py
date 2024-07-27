import seaborn as sns
import matplotlib.pyplot as plt

# Bar Plot
data = sns.load_dataset("tips")
sns.barplot(data=data, x="day", y="tip", hue="sex", palette="spring")
plt.show()
sns.barplot(data=data, x="day", y="tip", hue="sex", palette="spring", errorbar=("ci", 0))
plt.show()

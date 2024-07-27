import seaborn as sns
import matplotlib.pyplot as plt

# Count Plot
data = sns.load_dataset("tips")
sns.countplot(data=data, x="day", palette="rainbow", edgecolor="black")
plt.show()

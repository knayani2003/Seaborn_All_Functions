import seaborn as sns
import matplotlib.pyplot as plt

# Box Plot
data = sns.load_dataset("tips")
sns.boxplot(data=data, x="day", y="tip", orient="v", palette="bright")
plt.show()

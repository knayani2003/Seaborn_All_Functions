import seaborn as sns
import matplotlib.pyplot as plt

# Categorical Plot
data = sns.load_dataset("tips")
sns.catplot(data=data, x="day", y="tip")
plt.show()

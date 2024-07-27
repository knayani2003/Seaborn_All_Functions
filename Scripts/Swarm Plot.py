import seaborn as sns
import matplotlib.pyplot as plt

# Swarm Plot
data = sns.load_dataset("tips")
sns.swarmplot(data=data, x="day", y="total_bill", palette="colorblind")
plt.show()

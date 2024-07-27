import seaborn as sns
import matplotlib.pyplot as plt

# Heatmap Plot
data = sns.load_dataset("tips")
gb = data.groupby("day").agg({"tip": "mean"})
sns.heatmap(gb)
plt.show()
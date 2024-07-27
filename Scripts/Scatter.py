import seaborn as sns
import matplotlib.pyplot as plt

# Scatter Plot
data = sns.load_dataset("tips")
sns.scatterplot(data=data, x="total_bill", y="tip", hue="day", size="size")
plt.show()

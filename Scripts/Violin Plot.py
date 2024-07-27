import seaborn as sns
import matplotlib.pyplot as plt

# Violin Plot
data = sns.load_dataset("tips")
sns.violinplot(data=data, x="total_bill", palette="pink")
plt.show()

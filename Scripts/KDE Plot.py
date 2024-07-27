import seaborn as sns
import matplotlib.pyplot as plt

# KDE Plot
data = sns.load_dataset("tips")
sns.kdeplot(data=data, x="total_bill", hue="day")
plt.show()
sns.kdeplot(data=data, x="total_bill", hue="day", multiple="stack")
plt.show()

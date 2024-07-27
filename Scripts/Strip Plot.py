import seaborn as sns
import matplotlib.pyplot as plt

# Strip Plot
data = sns.load_dataset("tips")
sns.stripplot(data=data, x="day", y="total_bill", hue='sex', dodge=True, palette="dark")
plt.show()
sns.stripplot(data=data, x="day", y="total_bill", hue='sex', dodge=True, palette="dark", jitter=0.4)
plt.show()

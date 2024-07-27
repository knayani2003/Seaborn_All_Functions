import seaborn as sns
import matplotlib.pyplot as plt

# Style & Color in Plots
data = sns.load_dataset("exercise")
c = ["blue", "orange", "green"]
sns.set_style(style="darkgrid")
sns.barplot(data=data, x="time", y="pulse", palette=c, errorbar=("ci", 0))
plt.show()

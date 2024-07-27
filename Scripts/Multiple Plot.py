import seaborn as sns
import matplotlib.pyplot as plt

# Multiple Plot
data = sns.load_dataset("tips")
a = sns.FacetGrid(data, col="smoker")
a.map(sns.barplot, "day", "tip")
plt.show()

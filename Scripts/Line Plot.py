import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Line Plot with simple data
data = {"Days": [1, 2, 3, 4, 5], "Peo": [50, 40, 60, 30, 44]}
sns.lineplot(data=data, x="Days", y="Peo")
plt.show()

# Line Plot with dataset
data = pd.read_csv("Downloads/Employee.csv")
df = pd.DataFrame(data)
color = sns.color_palette("dark")
sns.lineplot(data=data, x="City", y="Age", hue="Gender", palette=color)
plt.show()

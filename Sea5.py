# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns 

tips = sns.load_dataset("tips")

# Create the boxplot
ax = sns.boxplot(x="total_bill", data=tips)

# Set title
ax.set_title("boxplot")

# Show the plot
plt.show()

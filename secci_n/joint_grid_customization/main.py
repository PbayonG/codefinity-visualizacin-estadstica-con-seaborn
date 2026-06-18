import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/penguins_upd.csv')

# Set the style and background
sns.set_style('ticks', {'figure.facecolor': 'lightcyan'})

# 1. Create a JointGrid variable
g = sns.JointGrid(
    # Set the x
    x='bill_length_mm',
    # Set the y
    y='bill_depth_mm',
    # Set the hue
    hue='species',
    # Set the palette
    palette='viridis',
    # Set the data
    data=df
)

# 2. Set the inside plot (Joint)
g.plot_joint(
    # Plotting function
    sns.scatterplot,
    # Set transparency
    alpha=0.5,
    # Set border color
    edgecolor='pink',
    # Set border width
    linewidth=1
)

# 3. Set the outside plots (Marginals)
g.plot_marginals(
    # Plotting function
    sns.histplot,
    # Enable KDE
    kde=True
)

# Display the plot
plt.show()
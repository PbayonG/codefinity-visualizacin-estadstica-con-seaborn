import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/penguins.csv')

# Set the style and background
sns.set_style('white', {'axes.facecolor': 'aliceblue'})

# Create a catplot
sns.catplot(
    # Set the x
    x='species',
    # Set the y
    y='body_mass_g',
    # Set the hue
    hue='sex',
    # Split into rows
    row='island',
    # Set the palette
    palette='viridis',
    # Set the transparency
    alpha=0.6,
    # Configure legend position
    legend_out=False,
    # Set the data
    data=df
)

# Display the plot
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/tips.csv')

# Set the style and background
sns.set_style('whitegrid', {'axes.facecolor': 'cornsilk'})

# 1. Create a FacetGrid variable
g = sns.FacetGrid(
    # Set the data
    df,
    # Set the col
    col='day',
    # Set the row
    row='smoker',
    # Set the height
    height=3
)

# 2. Build histplots using the .map() function
g.map(
    # Plotting function
    sns.histplot,
    # Variable to plot
    'total_bill',
    # Set the color
    color='olive',
    # Enable KDE
    kde=True,
    # Disable fill
    fill=False,
    # Set binwidth
    binwidth=4
)

# Display the plot
plt.show()
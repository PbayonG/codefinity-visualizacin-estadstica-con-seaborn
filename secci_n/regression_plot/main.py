import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/tips.csv')

# Set the style and background colors
sns.set_style('darkgrid', {
    'figure.facecolor': 'tan',
    'axes.facecolor': 'cornsilk'
})

# Create a regplot
sns.regplot(
    # Set the x
    x='total_bill',
    # Set the y
    y='tip',
    # Set the marker
    marker='+',
    # Set the color
    color='green',
    # Disable the regression line
    fit_reg=False,
    # Set the data
    data=df
)

# Display the plot
plt.show()
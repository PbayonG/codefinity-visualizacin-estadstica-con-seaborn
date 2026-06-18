import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/tips.csv')

# Set the style and background
sns.set_style('darkgrid', {'figure.facecolor': 'lightpink'})

# Create a lmplot
sns.lmplot(
    # Set the x
    x='total_bill',
    # Set the y
    y='tip',
    # Set the hue
    hue='smoker',
    # Set the col
    col='sex',
    # Set the markers
    markers=['o', 'x'],
    # Set the palette
    palette='crest',
    # Set the data
    data=df
)

# Display the plot
plt.show()
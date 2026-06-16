import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/flights.csv')

# Reshaping the data (Matrix creation)
upd_df = df.pivot_table(index='month', columns='year', values='passengers')

# Set the style and background
sns.set_style('ticks', {'figure.facecolor': 'seagreen'})

# Create a heatmap
sns.heatmap(
    # Add the data (upd_df)
    upd_df,
    # Set the colormap
    cmap='viridis',
    # Enable annotations
    annot=True,
    # Set the number format
    fmt='0.99g',
    # Set the line color
    linecolor='plum'
)

# Display the plot
plt.show()
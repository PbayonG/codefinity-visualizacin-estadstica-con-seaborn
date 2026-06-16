import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/flights.csv')
upd_df = df.pivot_table(index='month', columns='year', values='passengers')

# Set the style and background
sns.set_style('ticks', {'figure.facecolor': 'seagreen'})

# Create a clustermap
sns.clustermap(
    # Add the data
    upd_df,
    # Set the colormap
    cmap='vlag',
    # Normalize the data
    standard_scale=1,
    # Set the clustering method
    method='single',
    # Set the distance metric
    metric='correlation',
    # Enable annotations
    annot=True,
    # Set the limits
    vmin=0,
    vmax=10
)

# Display the plot
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/66ba0c8e-8422-413c-b7e1-74bd24c61656/penguins_upd.csv')
df = df.drop(['Unnamed: 0'], axis=1)

# Set the style and background
sns.set_style('ticks', {'figure.facecolor': 'lightpink'})

# 1. Create a PairGrid variable
g = sns.PairGrid(
    # Set the data
    df,
    # Set the hue
    hue='species',
    # Set the palette
    palette='rocket_r',
    # Independent Y-axis for diagonal
    diag_sharey=False
)

# 2. Set diagonal plots
g.map_diag(
    # Plotting function
    sns.histplot,
    # Enable KDE
    kde=True
)

# 3. Set off-diagonal plots
g.map_offdiag(
    # Plotting function
    sns.scatterplot,
    # Set border width
    linewidth=0.9,
    # Set border color
    edgecolor='purple'
)

# Adding the legend
g.add_legend()

# Display the plot
plt.show()
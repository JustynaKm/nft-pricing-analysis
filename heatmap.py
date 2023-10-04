import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('bored_apes.csv')

import matplotlib.pyplot as plt
import seaborn as sns

# Load your data into the 'df' DataFrame
# Assuming you've already loaded your data

# Filter out non-numeric columns
numerical_columns = df.select_dtypes(include=[np.number])

# Calculate the correlation matrix
corr_matrix = numerical_columns.corr()

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Customize the plot (e.g., add a title)
plt.title("Correlation Heatmap")

# Show the plot
plt.show()

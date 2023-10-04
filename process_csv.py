import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load your dataset
df = pd.read_csv('bored_apes.csv')

# Create a plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Custom function to format y-axis labels
def format_y_labels(positions, labels):
    new_labels = []
    for label in labels:
        words = label.get_text().split()
        if len(words) >= 2:
            new_labels.append(f"{words[0][:2]} {words[1][:2]}")
        elif len(words) == 1:
            new_labels.append(f"{words[0][:2]}")
        else:
            new_labels.append(label.get_text())
    return new_labels

# Your plot code here...

# Get the current y-axis ticks and labels
y_ticks = plt.gca().get_yticks()
y_labels = plt.gca().get_yticklabels()

# Modify the y-axis labels using the custom function
formatted_y_labels = format_y_labels(y_ticks, y_labels)

# Set the modified y-axis labels
plt.gca().set_yticklabels(formatted_y_labels)

# Show the plot
plt.show()

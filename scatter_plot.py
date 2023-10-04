import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset
df = pd.read_csv('bored_apes.csv')

# Create a scatter plot to visualize the Last Sale Price by Eyes Rarity and Hat Rarity
plt.figure(figsize=(12, 8))
scatter = plt.scatter(
    df['EyesRarity'], 
    df['HatRarity'], 
    c=df['LastSalePrice'], 
    cmap='viridis', 
    s=df['LastSalePrice'] * 2,  # Size of the points based on Last Sale Price
    alpha=0.6
)
plt.colorbar(scatter, label='Last Sale Price')
plt.xlabel('Eyes Rarity')
plt.ylabel('Hat Rarity')
plt.title('Last Sale Price by Eyes Rarity and Hat Rarity')
plt.grid(True)
plt.show()

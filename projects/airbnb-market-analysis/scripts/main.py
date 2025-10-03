import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data
data = pd.DataFrame({
    'ListingID': range(1, 31),
    'Neighborhood': np.random.choice(['Downtown', 'Uptown', 'Suburbs'], 30),
    'Price': np.random.randint(50, 500, 30),
    'Bedrooms': np.random.randint(1, 6, 30),
    'MinimumNights': np.random.randint(1, 20, 30),
    'Availability': np.random.randint(0, 365, 30)
})

# Summary statistics
total_listings = data['ListingID'].nunique()
total_bedrooms = data['Bedrooms'].sum()
avg_min_nights = data['MinimumNights'].mean()
print(f"Total Listings: {total_listings}")
print(f"Total Bedrooms: {total_bedrooms}")
print(f"Average Minimum Nights: {avg_min_nights:.2f}")

# Neighborhood stats
neighborhood_stats = data.groupby('Neighborhood').agg({
    'Price': ['mean', 'median', 'max', 'min'],
    'Availability': 'mean'
}).reset_index()
print("\nNeighborhood Stats:\n", neighborhood_stats)

# Visualizations
sns.set_style('whitegrid')
plt.figure(figsize=(8,5))
sns.barplot(x='Neighborhood', y=('Price','mean'), data=neighborhood_stats)
plt.title('Average Price by Neighborhood')
plt.savefig('avg_price_by_neighborhood.png')
plt.close()

plt.figure(figsize=(8,5))
sns.histplot(data['Price'], bins=10)
plt.title('Price Distribution')
plt.savefig('price_distribution.png')
plt.close()

plt.figure(figsize=(8,5))
sns.scatterplot(x='Bedrooms', y='Price', hue='Neighborhood', data=data)
plt.title('Price vs Bedrooms')
plt.savefig('price_vs_bedrooms.png')
plt.close()

# Correlations
corr = data.corr()
print("\nCorrelation Matrix:\n", corr)

print("\nAirbnb Market Analysis Project Completed!")

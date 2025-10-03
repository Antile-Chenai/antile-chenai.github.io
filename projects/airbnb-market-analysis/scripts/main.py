import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1. Load Sample Data
# -------------------------
np.random.seed(42)
neighborhoods = ['Downtown', 'Suburb', 'Beachside', 'Historic', 'Airport']
data = pd.DataFrame({
    'ListingID': range(1, 201),
    'Neighborhood': np.random.choice(neighborhoods, 200),
    'Price': np.random.randint(50, 1000, 200),
    'Bedrooms': np.random.randint(1, 5, 200),
    'MinimumNights': np.random.randint(1, 30, 200),
    'Availability': np.random.randint(0, 365, 200)
})

# -------------------------
# 2. Data Overview
# -------------------------
print("Summary Statistics:\n", data.describe())
print("\nListings per Neighborhood:\n", data['Neighborhood'].value_counts())

plt.figure(figsize=(8,5))
sns.countplot(x='Neighborhood', data=data)
plt.title('Listings per Neighborhood')
plt.savefig('listings_per_neighborhood.png')
plt.close()

# -------------------------
# 3. Price Analysis
# -------------------------
plt.figure(figsize=(8,5))
sns.histplot(data['Price'], bins=30, kde=True)
plt.title('Price Distribution')
plt.savefig('price_distribution.png')
plt.close()

avg_price_by_neighborhood = data.groupby('Neighborhood')['Price'].mean().reset_index()
print("\nAverage Price by Neighborhood:\n", avg_price_by_neighborhood)

plt.figure(figsize=(8,5))
sns.barplot(x='Neighborhood', y='Price', data=avg_price_by_neighborhood)
plt.title('Average Price by Neighborhood')
plt.savefig('avg_price_by_neighborhood.png')
plt.close()

# -------------------------
# 4. Bedrooms vs Price
# -------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x='Bedrooms', y='Price', data=data)
plt.title('Price vs Bedrooms')
plt.savefig('price_vs_bedrooms.png')
plt.close()

# -------------------------
# 5. Correlations
# -------------------------
correlations = data[['Price','Bedrooms','MinimumNights','Availability']].corr()
print("\nCorrelations:\n", correlations)

# -------------------------
# 6. Scatter Plots
# -------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(x='Bedrooms', y='Price', hue='Neighborhood', data=data)
plt.title('Price vs Bedrooms Scatter Plot')
plt.savefig('price_vs_bedrooms_scatter.png')
plt.close()

plt.figure(figsize=(8,5))
sns.scatterplot(x='MinimumNights', y='Price', hue='Neighborhood', data=data)
plt.title('Price vs Minimum Nights Scatter Plot')
plt.savefig('price_vs_min_nights.png')
plt.close()

# -------------------------
# 7. Summary Metrics
# -------------------------
total_listings = len(data)
total_bedrooms = data['Bedrooms'].sum()
avg_min_nights = data['MinimumNights'].mean()

print(f"\nTotal Listings: {total_listings}")
print(f"Total Bedrooms: {total_bedrooms}")
print(f"Average Minimum Nights: {avg_min_nights:.2f}")

print("\nAirbnb Market Analysis Project Completed!")

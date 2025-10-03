import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = pd.DataFrame({
    'ListingID': range(1, 31),
    'Neighborhood': np.random.choice(['Downtown','Suburb','Uptown'], 30),
    'Price': np.random.randint(50, 500, 30),
    'Bedrooms': np.random.randint(1, 5, 30),
    'MinimumNights': np.random.randint(1, 30, 30)
})

neigh_summary = data.groupby('Neighborhood').agg({
    'Price':'mean',
    'Bedrooms':'sum',
    'MinimumNights':'mean'
}).reset_index()

plt.figure(figsize=(8,5))
sns.barplot(x='Neighborhood', y='Price', data=neigh_summary)
plt.title('Average Price per Neighborhood')
plt.savefig('avg_price_neigh.png')
plt.close()

plt.figure(figsize=(8,5))
sns.scatterplot(x='Bedrooms', y='Price', hue='Neighborhood', data=data)
plt.title('Price vs Bedrooms')
plt.savefig('price_vs_bedrooms.png')
plt.close()

total_listings = data.shape[0]
total_bedrooms = data['Bedrooms'].sum()
avg_min_nights = data['MinimumNights'].mean()
print(f"Total Listings: {total_listings}")
print(f"Total Bedrooms: {total_bedrooms}")
print(f"Average Minimum Nights: {avg_min_nights:.2f}")
print("Airbnb Market Analysis Project Completed!")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
    'ListingID': range(1, 21),
    'Neighborhood': ['Downtown','Suburb','Downtown','Suburb','Downtown','Suburb','Downtown','Suburb','Downtown','Suburb',
                     'Downtown','Suburb','Downtown','Suburb','Downtown','Suburb','Downtown','Suburb','Downtown','Suburb'],
    'Price': [120,80,150,95,130,85,160,100,125,90,140,88,155,92,135,87,150,98,145,93],
    'Bedrooms':[1,2,1,3,2,2,1,3,1,2,2,2,1,3,2,2,1,3,2,2],
    'Bathrooms':[1,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1],
    'MinimumNights':[2,3,1,5,2,4,3,2,1,3,2,4,2,5,3,4,2,2,3,3],
    'Availability':[180,200,150,100,170,190,160,120,180,200,150,100,170,190,160,120,180,200,150,100]
})
print("Missing values per column:\n", data.isnull().sum())
data['PricePerBedroom'] = data['Price'] / data['Bedrooms']
data['AvailabilityRate'] = data['Availability'] / 365

avg_price = data.groupby('Neighborhood')['Price'].mean()
avg_bedrooms = data.groupby('Neighborhood')['Bedrooms'].mean()
max_price = data['Price'].max()
min_price = data['Price'].min()

print("\nAverage Price by Neighborhood:\n", avg_price)
print("\nAverage Bedrooms by Neighborhood:\n", avg_bedrooms)
print(f"\nMaximum Price: {max_price}")
print(f"Minimum Price: {min_price}")

top_expensive = data.sort_values('Price', ascending=False).head(5)
print("\nTop 5 Most Expensive Listings:\n", top_expensive[['ListingID','Price','Neighborhood']])

sns.set_style('whitegrid')
plt.figure(figsize=(8,5))
sns.barplot(x=avg_price.index, y=avg_price.values)
plt.title('Average Airbnb Price by Neighborhood')
plt.ylabel('Price ($)')
plt.savefig('avg_price_by_neighborhood.png')
plt.close()

plt.figure(figsize=(8,5))
sns.scatterplot(x='Bedrooms', y='Price', hue='Neighborhood', data=data)
plt.title('Price vs Bedrooms')
plt.savefig('price_vs_bedrooms.png')
plt.close()

plt.figure(figsize=(8,5))
sns.histplot(data['Price'], bins=10, kde=True)
plt.title('Distribution of Prices')
plt.savefig('price_distribution.png')
plt.close()

total_listings = data['ListingID'].nunique()
total_bedrooms = data['Bedrooms'].sum()
avg_min_nights = data['MinimumNights'].mean()

print(f"\nTotal Listings: {total_listings}")
print(f"Total Bedrooms: {total_bedrooms}")
print(f"Average Minimum Nights: {avg_min_nights:.2f}")
print("\nAirbnb Market Analysis Project Completed!")

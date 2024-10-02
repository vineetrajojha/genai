# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Dummy dataset for packaged food products
data = {
    'Product Name': ['Oats', 'Chocolate Bar', 'Potato Chips', 'Apple Juice', 'Protein Bar'],
    'Product Qty': ['500g', '50g', '100g', '1L', '75g'],
    'Brand Name': ['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E'],
    'Weight (g/ml)': [500, 50, 100, 1000, 75],
    'Calories': [200, 500, 550, 100, 250],
    'Fat (g)': [5, 30, 35, 0, 10],
    'Sugar (g)': [1, 40, 2, 20, 5],
    'Sodium (mg)': [150, 10, 500, 5, 250],
    'Category': ['Nutritional', 'Recreational', 'Recreational', 'Nutritional', 'Nutritional'],
    'Proprietary Claims': ['Sugar-free', 'Contains sugar', 'Low sodium', 'No added sugar', 'High protein']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Packaged Food Dataset:")
print(df)

# Normalize the dataset for clustering (excluding non-numeric columns)
numeric_columns = ['Weight (g/ml)', 'Calories', 'Fat (g)', 'Sugar (g)', 'Sodium (mg)']
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[numeric_columns])

# KMeans clustering to categorize products based on their nutritional content
kmeans = KMeans(n_clusters=3, random_state=0)
df['Health Category'] = kmeans.fit_predict(df_scaled)

# Add health analysis based on nutritional data
def health_analysis(row):
    if row['Calories'] > 400 or row['Fat (g)'] > 20 or row['Sugar (g)'] > 30:
        return "Unhealthy"
    elif row['Sugar (g)'] < 5 and row['Fat (g)'] < 10 and row['Sodium (mg)'] < 200:
        return "Healthy"
    else:
        return "Moderate"

df['Health Analysis'] = df.apply(health_analysis, axis=1)

# Generate user-specific nudges
def generate_nudge(row):
    if row['Health Analysis'] == "Unhealthy":
        return "Consider choosing a healthier option with less sugar and fat."
    elif row['Health Analysis'] == "Moderate":
        return "This product is okay but could be consumed less frequently."
    else:
        return "This product is a healthy choice, great for regular consumption!"

df['Nudge'] = df.apply(generate_nudge, axis=1)

# Display the final dataframe with health analysis and recommendations
print("\nFinal Dataset with Health Analysis and Nudges:")
print(df[['Product Name', 'Brand Name', 'Calories', 'Fat (g)', 'Sugar (g)', 'Sodium (mg)', 'Health Analysis', 'Nudge']])

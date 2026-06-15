import pandas as pd

df = pd.read_csv("SuperMarket-Analysis.csv")
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Sales by Branch
print("\nTotal Sales by Branch:")
print(df.groupby('Branch')['Sales'].sum().sort_values(ascending=False))

# Sales by Product Line
print("\nTotal Sales by Product Line:")
print(df.groupby('Product_line')['Sales'].sum().sort_values(ascending=False))

# Purchases by Gender
print("\nPurchases by Gender:")
print(df['Gender'].value_counts())

# Sales by Month
print("\nSales by Month:")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
print(df.groupby('Month')['Sales'].sum())

# Average Rating
print("\nAverage Customer Rating:")
print(round(df['Rating'].mean(), 2))
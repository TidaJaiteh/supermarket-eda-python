# Import our libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("SuperMarket-Analysis.csv")

# First look at the data
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())
print("\nBasic stats:")
print(df.describe())

# ---- DATA CLEANING ----

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Convert Date column to proper date format
df['Date'] = pd.to_datetime(df['Date'])

# Extract Month and Day from Date (useful for analysis)
df['Month'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day_name()

# Drop gross margin percentage
df = df.drop(columns=['gross margin percentage'])

# Rename columns to be cleaner (remove spaces)
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Confirm cleaned data
print("\nCleaned column names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)

# ---- ANALYSIS & VISUALIZATIONS ----

# Set visual style
sns.set_theme(style="whitegrid")

# --- Chart 1: Total Sales by Branch ---
plt.figure(figsize=(8, 5))
branch_sales = df.groupby('Branch')['Sales'].sum().reset_index()
sns.barplot(data=branch_sales, x='Branch', y='Sales', palette='Blues_d')
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('chart1_sales_by_branch.png')
plt.show()
print("Chart 1 saved!")

# --- Chart 2: Sales by Product Line ---
plt.figure(figsize=(10, 5))
product_sales = df.groupby('Product_line')['Sales'].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=product_sales, x='Sales', y='Product_line', palette='Greens_d')
plt.title('Total Sales by Product Line')
plt.xlabel('Total Sales ($)')
plt.ylabel('Product Line')
plt.tight_layout()
plt.savefig('chart2_sales_by_product.png')
plt.show()
print("Chart 2 saved!")

# --- Chart 3: Sales by Gender ---
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Gender', palette='Set2')
plt.title('Number of Purchases by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('chart3_purchases_by_gender.png')
plt.show()
print("Chart 3 saved!")

# --- Chart 4: Sales Trend by Month ---
plt.figure(figsize=(8, 5))
month_order = ['January', 'February', 'March']
month_sales = df.groupby('Month')['Sales'].sum().reindex(month_order).reset_index()
sns.lineplot(data=month_sales, x='Month', y='Sales', marker='o', color='coral')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('chart4_monthly_trend.png')
plt.show()
print("Chart 4 saved!")

# --- Chart 5: Customer Rating Distribution ---
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Rating', bins=20, kde=True, color='purple')
plt.title('Customer Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('chart5_rating_distribution.png')
plt.show()
print("Chart 5 saved!")

print("\nAll charts saved successfully!")

# ---- KEY BUSINESS SUMMARY ----
print("\n" + "="*50)
print("KEY BUSINESS INSIGHTS SUMMARY")
print("="*50)

# Top performing branch
top_branch = df.groupby('Branch')['Sales'].sum().idxmax()
top_branch_sales = df.groupby('Branch')['Sales'].sum().max()
print(f"\n Top Branch: {top_branch} with ${top_branch_sales:,.2f} in sales")

# Best product line
top_product = df.groupby('Product_line')['Sales'].sum().idxmax()
top_product_sales = df.groupby('Product_line')['Sales'].sum().max()
print(f" Best Product Line: {top_product} with ${top_product_sales:,.2f} in sales")

# Most common payment method
top_payment = df['Payment'].value_counts().idxmax()
print(f" Most Used Payment Method: {top_payment}")

# Gender with most purchases
top_gender = df['Gender'].value_counts().idxmax()
print(f" Most Frequent Customer: {top_gender}")

# Best month
top_month = df.groupby('Month')['Sales'].sum().idxmax()
print(f" Best Performing Month: {top_month}")

# Average rating
avg_rating = round(df['Rating'].mean(), 2)
print(f" Average Customer Rating: {avg_rating}/10")

print("\n" + "="*50)

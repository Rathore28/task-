# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load CSV file
df = pd.read_csv("sales_data.csv")

# Step 3: Quick look at the data
print(df.head())

# Step 4: Total sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print(sales_by_product)

# Step 5: Total sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()
print(sales_by_region)

# Step 6: Plot sales by product
sales_by_product.plot(kind="bar", color="skyblue", title="Total Sales by Product")
plt.ylabel("Sales")
plt.show()

# Step 7: Plot sales by region
sales_by_region.plot(kind="pie", autopct="%1.1f%%", figsize=(6,6), title="Sales Share by Region")
plt.ylabel("")
plt.show()

# Step 8: Trend over time
df["Date"] = pd.to_datetime(df["Date"])
sales_over_time = df.groupby("Date")["Sales"].sum()
sales_over_time.plot(kind="line", marker="o", title="Sales Over Time")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

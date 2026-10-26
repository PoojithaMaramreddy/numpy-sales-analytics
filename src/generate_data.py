import numpy as np

# --------------------------------------------------
# STEP 1: Generate random units sold
# --------------------------------------------------

# Create a random number generator with seed 42.
# Using the same seed produces the same random results
# every time we run the program.
rng = np.random.default_rng(42)

# Generate 500 random integers between 1 and 10 (inclusive).
# Each integer represents the quantity sold in one transaction.
units = rng.integers(1, 11, size=500)

# Display the first 10 values and total array shape.
print(units[0:10])
print(units.shape)


# --------------------------------------------------
# STEP 2: Define product information
# --------------------------------------------------

# List of 8 products available in our retail store.
products = np.array([
    'Laptop', 'Smartphone', 'Headphones', 'T-Shirt',
    'Jeans', 'Shoes', 'Notebook', 'Pen'
])

# Category corresponding to each product.
# The order must match the products array.
categories = np.array([
    'Electronics', 'Electronics', 'Electronics',
    'Clothing', 'Clothing', 'Footwear',
    'Stationery', 'Stationery'
])

# Unit price (in INR) corresponding to each product.
# These prices must follow the same order as products.
prices = np.array([
    45000, 18000, 1500, 799,
    1999, 2499, 80, 20
])


# --------------------------------------------------
# STEP 3: Randomly select products for 500 transactions
# --------------------------------------------------

# Generate 500 random indices between 0 and 7.
# Each index points to one of the 8 available products.
product_indices = rng.integers(0, 8, size=500)

# Display the first 5 randomly generated product indices.
print(product_indices[0:5])

# Use NumPy advanced indexing to select product details.
# We use the SAME indices for products, categories and prices
# to ensure that each product has its correct category and price.
selected_products = products[product_indices]
selected_categories = categories[product_indices]
selected_prices = prices[product_indices]

# Verify the selected product details and array shapes.
print(selected_products[:5])
print(selected_products.shape)

print(selected_categories[:5])
print(selected_categories.shape)

print(selected_prices[:5])
print(selected_prices.shape)


# --------------------------------------------------
# STEP 4: Generate random transaction dates for 2026
# --------------------------------------------------

# Define January 1, 2026 as the starting date.
start_date = np.datetime64('2026-01-01')

# Generate 500 random day offsets between 0 and 364.
# 2026 has 365 days, so this covers the entire year.
day_offsets = rng.integers(0, 365, size=500)

# Convert integer offsets into NumPy day durations.
# 'D' represents days.
day_durations = day_offsets.astype('timedelta64[D]')

# Add each duration to the starting date.
# This generates 500 random dates within 2026.
date = start_date + day_durations

# Verify the generated dates.
print("First 5 dates:", date[:5])
print("Dates shape:", date.shape)
print("Earliest date:", date.min())
print("Latest date:", date.max())


# --------------------------------------------------
# STEP 5: Combine all columns into one dataset
# --------------------------------------------------

# Convert datetime64 dates into strings.
# This is necessary because np.column_stack() cannot
# directly combine datetime64 values with string arrays.
date = date.astype(str)

# Combine the five arrays column by column.
# Each row represents one retail sales transaction.
sales_data = np.column_stack((
    date,
    selected_products,
    selected_categories,
    units,
    selected_prices
))

# Verify the final dataset.
# Expected shape: (500, 5)
# 500 rows = transactions, 5 columns = transaction details.
print("Dataset shape:", sales_data.shape)

# Display the first five transactions.
print("First 5 transactions:")
print(sales_data[:5])

# --------------------------------------------------
# STEP 6: Save the generated sales dataset to CSV
# --------------------------------------------------

# Export all 500 transactions to a CSV file.
# Include column headers and separate values with commas.

np.savetxt(
    "data/sales_data.csv",
    sales_data,
    delimiter=",",
    fmt="%s",
    header="Date,Product,Category,Units,Unit Price",
    comments=""
)

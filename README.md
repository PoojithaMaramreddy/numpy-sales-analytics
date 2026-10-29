
# NumPy Sales Analytics

A retail sales analytics project built using **Python and NumPy** to analyze sales transactions, identify business trends, and generate automated reports.

## Project Overview

This project analyzes 500 synthetic retail sales transactions from 2026 using NumPy.

The goal is to practice data manipulation, filtering, aggregation, statistical calculations, and report generation without using Pandas.

## Technologies Used

- Python 3.13
- NumPy
- Jupyter Notebook
- Git and GitHub

## Dataset

The dataset contains 500 synthetic transactions across 8 products and 4 categories.

**Dataset columns:**

| Column | Description |
|---|---|
| Date | Transaction date |
| Product | Product name |
| Category | Product category |
| Units | Number of units sold |
| Unit Price | Price per unit |

**Categories:** Electronics, Clothing, Footwear, Stationery.

## Project Features

- Generate synthetic retail sales data using NumPy
- Calculate total revenue and units sold
- Analyze average transaction revenue
- Identify highest and lowest revenue transactions
- Perform product-wise sales analysis
- Perform category-wise revenue analysis
- Analyze monthly sales trends
- Calculate revenue contribution percentages
- Identify top-performing products and categories
- Validate revenue calculations
- Generate CSV and TXT reports

## Key Business Insights

| Metric | Result |
|---|---|
| Total Revenue | ₹2,62,74,491 |
| Total Units Sold | 2,741 |
| Total Transactions | 500 |
| Average Transaction Revenue | ₹52,548.98 |
| Highest Revenue Product | Laptop |
| Lowest Revenue Product | Pen |
| Highest Revenue Category | Electronics |
| Lowest Revenue Category | Stationery |
| Highest Revenue Month | November |
| Lowest Revenue Month | February |

### Additional Findings

- Laptop generated ₹1,75,05,000 in revenue, approximately 66.62% of total sales revenue.
- Electronics was the highest revenue-generating category.
- November recorded the highest monthly revenue at ₹30,34,891.
- February recorded the lowest monthly revenue at ₹14,93,340.

## Project Structure

```text
numpy-sales-analytics/
├── data/
│   └── sales_data.csv
├── src/
│   ├── generate_data.py
│   └── sales_analysis.ipynb
├── reports/
│   ├── product_sales_report.csv
│   ├── category_sales_report.csv
│   ├── monthly_sales_report.csv
│   └── sales_summary.txt
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/PoojithaMaramreddy/numpy-sales-analytics.git
   ```

2. Navigate to the project folder:

   ```bash
   cd numpy-sales-analytics
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Generate the dataset:

   ```bash
   python src/generate_data.py
   ```

5. Open `src/sales_analysis.ipynb` in VS Code or Jupyter Notebook.

6. Run all notebook cells to perform the analysis and generate reports.

## Generated Reports

| Report | Description |
|---|---|
| product_sales_report.csv | Product-wise units, revenue, and revenue contribution |
| category_sales_report.csv | Category-wise revenue and contribution |
| monthly_sales_report.csv | Monthly sales revenue |
| sales_summary.txt | Summary of key business findings |

## Skills Demonstrated

- NumPy arrays and structured arrays
- Boolean indexing and filtering
- Aggregation and statistical analysis
- Array manipulation
- Data validation
- CSV file handling
- Business insight generation
- Git version control

## Project Status

**Completed — October 2026**

## Author

Poojitha Maramreddy

GitHub: https://github.com/PoojithaMaramreddy
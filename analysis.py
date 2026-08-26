"""
Retail Sales Analysis
----------------------
Exploratory analysis of a synthetic retail sales dataset (jewellery, watches,
accessories and custom grillz) using pandas, matplotlib and seaborn.

Run with:  python analysis.py
Outputs:   prints summary statistics to the console and writes three charts
           (monthly_revenue.svg, category_revenue.svg, revenue_distribution.svg)
           """

import pandas as pd
import matplotlib
matplotlib.use("svg")
matplotlib.rcParams["svg.fonttype"] = "none"
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# ---------------------------------------------------------------------------
# 1. Load and clean
# ---------------------------------------------------------------------------
df = pd.read_csv("retail_sales.csv", parse_dates=["Date"])

# Basic data-quality checks
assert df["OrderID"].is_unique, "Duplicate order IDs found"
assert (df["Revenue"] - (df["UnitsSold"] * df["UnitPrice"])).abs().max() < 0.01, \
    "Revenue does not match UnitsSold * UnitPrice for some rows"
assert df.isnull().sum().sum() == 0, "Unexpected missing values"

df["Month"] = df["Date"].dt.to_period("M").astype(str)

print("Dataset shape:", df.shape)
print("Date range:", df["Date"].min().date(), "to", df["Date"].max().date())
print()

# ---------------------------------------------------------------------------
# 2. Summary statistics
# ---------------------------------------------------------------------------
print("Revenue summary statistics:")
print(df["Revenue"].describe().round(2))
print()

print("Total revenue by category:")
by_category = df.groupby("Category")["Revenue"].agg(["sum", "count", "mean"]).round(2)
by_category.columns = ["total_revenue", "order_count", "avg_order_value"]
by_category = by_category.sort_values("total_revenue", ascending=False)
print(by_category)
print()

print("Monthly revenue trend:")
monthly = df.groupby("Month")["Revenue"].sum().round(2)
print(monthly)
print()

# ---------------------------------------------------------------------------
# 3. Correlation: does unit price predict units sold?
# ---------------------------------------------------------------------------
corr = df["UnitPrice"].corr(df["UnitsSold"])
print(f"Correlation between unit price and units sold: {corr:.3f}")
print()

# ---------------------------------------------------------------------------
# 4. Outlier detection (orders more than 3 std dev above mean revenue)
# ---------------------------------------------------------------------------
mean_rev, std_rev = df["Revenue"].mean(), df["Revenue"].std()
outliers = df[df["Revenue"] > mean_rev + 3 * std_rev]
print(f"High-value outlier orders (> mean + 3*std): {len(outliers)}")
if len(outliers):
    print(outliers[["OrderID", "Category", "Product", "Revenue"]].to_string(index=False))
print()

# ---------------------------------------------------------------------------
# 5. Charts
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.5))
monthly.plot(kind="line", marker="o", ax=ax, color="#7A5C3E")
ax.set_title("Monthly Revenue Trend — 2025")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (£)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("monthly_revenue.svg")
plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 4.5))
by_category["total_revenue"].plot(kind="bar", ax=ax, color="#B08D57")
ax.set_title("Total Revenue by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Revenue (£)")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig("category_revenue.svg")
plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 4.5))
sns.histplot(df["Revenue"], bins=25, kde=True, ax=ax, color="#4C6B8A")
ax.set_title("Distribution of Order Revenue")
ax.set_xlabel("Revenue (£)")
plt.tight_layout()
plt.savefig("revenue_distribution.svg")
plt.close(fig)

print("Charts written: monthly_revenue.svg, category_revenue.svg, revenue_distribution.svg")

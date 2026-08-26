# Python Retail Sales Analysis

Exploratory data analysis of a synthetic retail sales dataset (jewellery, watches, accessories and custom grillz) using **pandas**, **matplotlib** and **seaborn**.

## What's in this repo

• **`retail_sales.csv`** — 320 orders across 2025, with date, region, category, product, units sold, unit price, revenue and customer segment.

• **`analysis.py`** — loads and validates the data, computes summary statistics and group-bys, checks correlation between price and units sold, flags high-value outlier orders, and generates three charts (monthly revenue trend, revenue by category, revenue distribution).

Run it yourself:

```bash
pip install pandas matplotlib seaborn
python analysis.py
```

## Data validation

Before analysing anything, the script checks that order IDs are unique, that `Revenue == UnitsSold * UnitPrice` for every row (to within rounding), and that there are no missing values — a habit carried over from working with lab data, where you check instrument output makes sense before you trust it.

## Findings

**Revenue by category**

| Category | Total Revenue | Orders | Avg Order Value |
|---|---|---|---|
| Custom Grillz | £139,773.10 | 87 | £1,606.59 |
| Watches | £74,775.05 | 79 | £946.52 |
| Jewellery | £34,225.78 | 75 | £456.34 |
| Accessories | £9,330.01 | 79 | £118.10 |

**Monthly revenue trend (2025)**

| Month | Revenue | Month | Revenue |
|---|---|---|---|
| Jan | £21,914 | Jul | £10,729 |
| Feb | £28,291 | Aug | £25,198 |
| Mar | £22,334 | Sep | £13,120 |
| Apr | £18,705 | Oct | £21,238 |
| May | £19,631 | Nov | £27,141 |
| Jun | £13,382 | Dec | £36,422 |

Revenue peaks in February (Valentine's Day) and climbs through November–December (gifting season), with a summer lull — a pattern worth planning stock and staffing around.

**Price vs. units sold correlation:** 0.003 — essentially no relationship in this dataset, i.e. higher-priced items don't sell in systematically different quantities to lower-priced ones once category is ignored.

**Outlier detection:** 8 orders sit more than 3 standard deviations above the mean order value (£806.57), all Custom Grillz or Watches orders over £3,650 — consistent with those being the highest-ticket product lines rather than data errors.

## Skills demonstrated

Data loading and validation · `groupby`/aggregation · datetime handling and resampling · correlation analysis · outlier detection (z-score style) · data visualisation with matplotlib/seaborn.

# Analyzing Customer Orders Using Python

A course-end project that demonstrates core Python data structures — lists, tuples, dictionaries, and sets — through a realistic e-commerce order analysis pipeline. The script ingests raw order data and produces a full business insights report covering revenue, customer segmentation, and product analytics.

---

## Project Overview

| Attribute | Details |
|-----------|---------|
| Language | Python 3 |
| Concepts | Lists, tuples, dicts, sets, comprehensions, functions |
| Input | Hard-coded order dataset (10 customers, 21 orders) |
| Output | Console report with revenue, rankings, and segmentation |

---

## Features

- **Order storage** — customer name → product list dictionary built from raw tuple data
- **Category classification** — products mapped to Electronics, Clothing, or Home Essentials
- **Spending analysis** — total spend computed per customer with High / Moderate / Low-Value buyer classification
- **Business insights** — revenue by category, top 3 spenders, unique product catalogue
- **Set operations** — customers who bought from multiple categories, and intersection of Electronics + Clothing buyers
- **Formatted console report** — aligned tables and summary block printed at runtime

---

## Project Structure

```
customer_orders_analysis/
└── customer_orders.py      # Single-file script containing all 5 tasks + final report
```

---

## Tasks Breakdown

### Task 1 — Store Customer Orders
Defines `customer_names` (list), `order_details` (list of tuples), and builds `customer_orders` (dict mapping each customer to their product list).

### Task 2 — Classify Products by Category
Creates `product_category` (dict) and `unique_categories` (set) from the order data.

### Task 3 — Analyze Customer Orders
Computes `customer_spending` per customer and classifies each into:

| Tier | Condition |
|------|-----------|
| High-Value Buyer | Total spend > $100 |
| Moderate Buyer | $50 ≤ Total spend ≤ $100 |
| Low-Value Buyer | Total spend < $50 |

### Task 4 — Generate Business Insights
- Total revenue per product category
- Unique products sold across all orders
- Customers who purchased Electronics (list comprehension)
- Top 3 highest-spending customers

### Task 5 — Organize and Display Data
- Full customer summary sorted by spend (descending)
- Customers who shopped across multiple categories (set comprehension)
- Intersection: customers who bought both Electronics **and** Clothing

---

## Sample Output

```
============================================================
       CUSTOMER ORDERS ANALYSIS REPORT
============================================================

--- Customer Spending & Classification ---
Customer    Total Spent  Classification
---------------------------------------------
  Alice      $1,024.99  High-Value Buyer
  Carol        $714.99  High-Value Buyer
  ...

============================================================
            KEY BUSINESS INSIGHTS
============================================================

  Total Revenue Generated   : $2,975.93
  Total Orders Placed       : 21
  Unique Products           : 21
  Unique Categories         : 3
  Best-Performing Category  : Electronics ($2,524.96)
  Top Spender               : Alice ($1,024.99)

  High-Value Buyers (8)   : ['Alice', 'Bob', 'Carol', ...]
  Moderate Buyers   (1)   : ['Henry']
  Low-Value Buyers  (1)   : ['Jack']
============================================================
```

---

## How to Run

**Prerequisites:** Python 3.6 or higher (no external dependencies).

```bash
# Clone or download the file, then run:
python customer_orders.py
```

The full report prints directly to the console.

---

## Dataset

The script uses a built-in dataset of 21 orders across 10 customers and 3 product categories.

| Category | Products |
|----------|---------|
| Electronics | Laptop, USB Hub, Smartphone, Phone Case, Headphones, Tablet, Smart Watch |
| Clothing | T-Shirt, Jeans, Sneakers, Dress, Polo Shirt, Jacket |
| Home Essentials | Blender, Toaster, Microwave, Bedsheets, Kettle, Yoga Mat, Desk Lamp, Curtains |

To use your own data, replace the `order_details` list with tuples in the format:
```python
("CustomerName", "ProductName", price_as_float, "Category")
```

---

## Concepts Demonstrated

- Building and querying **dictionaries** with `.get()`, iteration, and comprehensions
- Using **sets** for deduplication and intersection operations (`&`)
- **List comprehensions** and **set comprehensions** for concise filtering
- **Tuple unpacking** in `for` loops
- **Lambda functions** as sort keys (`key=lambda x: -x[1]`)
- **f-string formatting** with alignment specifiers (`:<`, `:>`, `:.2f`)
- Encapsulating logic in a **helper function** (`classify_customer`)

---

## License

This project is for educational purposes. Feel free to use and adapt it freely.

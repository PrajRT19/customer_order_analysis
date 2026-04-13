# ============================================================
#   Analyzing Customer Orders Using Python
#   Course-End Project
# ============================================================

# ============================================================
# TASK 1: Store Customer Orders
# ============================================================

# 1a. List of customer names
customer_names = [
    "Alice", "Bob", "Carol", "David", "Eva",
    "Frank", "Grace", "Henry", "Isla", "Jack"
]

# 1b. Each customer's order details as tuples (name, product, price, category)
order_details = [
    ("Alice",  "Laptop",           999.99, "Electronics"),
    ("Alice",  "USB Hub",           25.00, "Electronics"),
    ("Bob",    "T-Shirt",           19.99, "Clothing"),
    ("Bob",    "Jeans",             49.99, "Clothing"),
    ("Bob",    "Sneakers",          89.99, "Clothing"),
    ("Carol",  "Smartphone",       699.99, "Electronics"),
    ("Carol",  "Phone Case",        15.00, "Electronics"),
    ("David",  "Blender",           45.00, "Home Essentials"),
    ("David",  "Toaster",           30.00, "Home Essentials"),
    ("Eva",    "Headphones",       199.99, "Electronics"),
    ("Eva",    "Dress",             75.00, "Clothing"),
    ("Frank",  "Microwave",        120.00, "Home Essentials"),
    ("Frank",  "Polo Shirt",        35.00, "Clothing"),
    ("Grace",  "Tablet",           349.99, "Electronics"),
    ("Grace",  "Bedsheets",         40.00, "Home Essentials"),
    ("Henry",  "Kettle",            22.00, "Home Essentials"),
    ("Henry",  "Jacket",            85.00, "Clothing"),
    ("Isla",   "Smart Watch",      249.99, "Electronics"),
    ("Isla",   "Yoga Mat",          30.00, "Home Essentials"),
    ("Jack",   "Desk Lamp",         18.00, "Home Essentials"),
    ("Jack",   "Curtains",          27.00, "Home Essentials"),
]

# 1c. Dictionary: customer name -> list of ordered products
customer_orders = {}
for name, product, price, category in order_details:
    if name not in customer_orders:
        customer_orders[name] = []
    customer_orders[name].append(product)

print("=" * 60)
print("       CUSTOMER ORDERS ANALYSIS REPORT")
print("=" * 60)

print("\n--- Customer Order Dictionary ---")
for customer, products in customer_orders.items():
    print(f"  {customer}: {products}")


# ============================================================
# TASK 2: Classify Products by Category
# ============================================================

# 2a. Dictionary mapping each product to its category
product_category = {name: cat for _, name, _, cat in order_details}

# 2b. Set of unique product categories
unique_categories = set(product_category.values())

# 2c. Display all available product categories
print("\n--- Available Product Categories ---")
for cat in sorted(unique_categories):
    print(f"  • {cat}")


# ============================================================
# TASK 3: Analyze Customer Orders
# ============================================================

# 3a. Calculate total spending per customer
customer_spending = {}
for name, product, price, category in order_details:
    customer_spending[name] = customer_spending.get(name, 0) + price

# 3b & 3c. Classify customers by spending
def classify_customer(total):
    if total > 100:
        return "High-Value Buyer"
    elif total >= 50:
        return "Moderate Buyer"
    else:
        return "Low-Value Buyer"

customer_classification = {
    name: classify_customer(total)
    for name, total in customer_spending.items()
}

print("\n--- Customer Spending & Classification ---")
print(f"{'Customer':<10} {'Total Spent':>12}  {'Classification'}")
print("-" * 45)
for name in customer_names:
    total  = customer_spending.get(name, 0)
    label  = customer_classification.get(name, "N/A")
    print(f"  {name:<10} ${total:>10.2f}  {label}")


# ============================================================
# TASK 4: Generate Business Insights
# ============================================================

# 4a. Total revenue per product category
category_revenue = {}
for _, product, price, category in order_details:
    category_revenue[category] = category_revenue.get(category, 0) + price

print("\n--- Total Revenue per Product Category ---")
for cat, rev in sorted(category_revenue.items(), key=lambda x: -x[1]):
    print(f"  {cat:<20}: ${rev:,.2f}")

# 4b. Unique products across all orders (using a set)
unique_products = {product for _, product, _, _ in order_details}
print(f"\n--- Unique Products Sold ({len(unique_products)} total) ---")
for p in sorted(unique_products):
    print(f"  • {p}")

# 4c. List comprehension: customers who purchased Electronics
electronics_customers = list({
    name
    for name, product, price, category in order_details
    if category == "Electronics"
})
print("\n--- Customers Who Purchased Electronics ---")
print(f"  {sorted(electronics_customers)}")

# 4d. Top 3 highest-spending customers
top3 = sorted(customer_spending.items(), key=lambda x: -x[1])[:3]
print("\n--- Top 3 Highest-Spending Customers ---")
for rank, (name, total) in enumerate(top3, 1):
    print(f"  #{rank}  {name:<10}  ${total:,.2f}")


# ============================================================
# TASK 5: Organize and Display Data
# ============================================================

# 5a. Summary already printed in Task 3 — here we repeat in a clean block
print("\n--- Full Customer Summary ---")
print(f"{'Customer':<10} {'Total Spent':>12}  {'Classification':<20}")
print("-" * 50)
for name, total in sorted(customer_spending.items(), key=lambda x: -x[1]):
    label = customer_classification[name]
    print(f"  {name:<10} ${total:>10.2f}  {label:<20}")

# 5b. Set operations: customers who purchased from multiple categories
customer_categories = {}
for name, product, price, category in order_details:
    if name not in customer_categories:
        customer_categories[name] = set()
    customer_categories[name].add(category)

multi_category_customers = {
    name for name, cats in customer_categories.items() if len(cats) > 1
}
print("\n--- Customers Who Purchased from Multiple Categories ---")
print(f"  {sorted(multi_category_customers)}")

# 5c. Common customers who bought BOTH Electronics AND Clothing
electronics_buyers = {
    name for name, _, _, cat in order_details if cat == "Electronics"
}
clothing_buyers = {
    name for name, _, _, cat in order_details if cat == "Clothing"
}
both_buyers = electronics_buyers & clothing_buyers

print("\n--- Customers Who Bought Both Electronics AND Clothing ---")
print(f"  {sorted(both_buyers)}")

# ============================================================
# FINAL BUSINESS INSIGHTS SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("            KEY BUSINESS INSIGHTS")
print("=" * 60)

total_revenue = sum(price for _, _, price, _ in order_details)
print(f"\n  Total Revenue Generated   : ${total_revenue:,.2f}")
print(f"  Total Orders Placed       : {len(order_details)}")
print(f"  Unique Products           : {len(unique_products)}")
print(f"  Unique Categories         : {len(unique_categories)}")

# Best performing category
best_cat = max(category_revenue, key=category_revenue.get)
print(f"  Best-Performing Category  : {best_cat} (${category_revenue[best_cat]:,.2f})")

# Top spender
top_customer, top_spent = top3[0]
print(f"  Top Spender               : {top_customer} (${top_spent:,.2f})")

# High-value buyer count
high_value = [n for n, c in customer_classification.items() if c == "High-Value Buyer"]
moderate   = [n for n, c in customer_classification.items() if c == "Moderate Buyer"]
low_value  = [n for n, c in customer_classification.items() if c == "Low-Value Buyer"]
print(f"\n  High-Value Buyers ({len(high_value)})   : {sorted(high_value)}")
print(f"  Moderate Buyers   ({len(moderate)})   : {sorted(moderate)}")
print(f"  Low-Value Buyers  ({len(low_value)})   : {sorted(low_value)}")
print("\n" + "=" * 60)
print("                  END OF REPORT")
print("=" * 60)

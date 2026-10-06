from pathlib import Path
import pandas as pd
import numpy as np

DATA_DIR = Path("data")
CUSTOMER_FILE = DATA_DIR / "customers.csv"
TRANSACTION_FILE = DATA_DIR / "transactions.csv"

customers = pd.read_csv(CUSTOMER_FILE)
transactions = pd.read_csv(TRANSACTION_FILE)

customers["join_date"] = pd.to_datetime(customers["join_date"], errors="coerce")
customers["join_year"] = customers["join_date"].dt.year

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"], errors="coerce"
)
transactions["amount"] = pd.to_numeric(transactions["amount"], errors="coerce")

print("Customers:", len(customers))
print("Transactions:", len(transactions))
print("Total value:", transactions["amount"].sum())
print("Average transaction value:", transactions["amount"].mean())

print("\nCustomer segments:")
print(
    customers.groupby("customer_segment")
    .agg(customers=("customer_id", "nunique"), average_age=("age", "mean"))
    .sort_values("customers", ascending=False)
)

print("\nCategories:")
print(
    transactions.groupby("category")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_value=("amount", "sum"),
        average_value=("amount", "mean"),
    )
    .sort_values("total_value", ascending=False)
)

print("\nChannels:")
print(
    transactions.groupby("channel")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_value=("amount", "sum"),
        average_value=("amount", "mean"),
        unique_customers=("customer_id", "nunique"),
    )
    .sort_values("total_value", ascending=False)
)

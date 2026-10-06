# Power BI DAX Measures

```DAX
Total Transaction Value =
SUM(transactions[amount])
```

```DAX
Total Transactions =
COUNTROWS(transactions)
```

```DAX
Customer Count =
DISTINCTCOUNT(transactions[customer_id])
```

```DAX
Average Transaction Value =
AVERAGE(transactions[amount])
```

```DAX
Average Value Per Customer =
DIVIDE([Total Transaction Value], [Customer Count])
```

```DAX
Debit Transaction Value =
CALCULATE(
    [Total Transaction Value],
    transactions[transaction_type] = "Debit"
)
```

```DAX
Credit Transaction Value =
CALCULATE(
    [Total Transaction Value],
    transactions[transaction_type] = "Credit"
)
```

```DAX
Active Customers =
DISTINCTCOUNT(transactions[customer_id])
```

```DAX
Inactive Customers =
COUNTROWS(customers) - [Active Customers]
```

## Date Table

Recommended columns:
- Date
- Month
- Month Number
- Year
- Year Month
- YearMonthSort

```DAX
YearMonthSort =
YEAR('DateTable'[Date]) * 100 + MONTH('DateTable'[Date])
```

Sort `Year Month` by `YearMonthSort`.

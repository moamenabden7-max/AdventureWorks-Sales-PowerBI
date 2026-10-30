# Revised model and measures

Source of truth: powerbi/AdventureWorks.SemanticModel/definition. This reference describes the revised PBIP, not the legacy PBIX.

Customers with null keys are filtered at refresh; valid keys are unique and all sales keys match. Customer filters flow to sales through a one-to-many relationship. Other business relationships are preserved.

DataFolder selects the local Data folder. Imported tables refresh from compressed snapshots; they are not the original raw source files.

## Measures in all data

### Min Retail Price

```dax
MIN(
			 'Product Lookup'[ProductPrice]
			)
```

### Quantity Sold

```dax
SUM(
			 'sales'[OrderQuantity]
			 )
```

### Quatity Returns

```dax
SUM('Returns Data'[ReturnQuantity])
```

### Total Customers

```dax
COUNT('Customer Lookup'[CustomerKey])
```

### Total orders

```dax
DISTINCTCOUNT(
			    sales[OrderNumber])
```

### Returns Rate

```dax
DIVIDE([Quatity Returns], [Quantity Sold])
```

### ALL

```dax
CALCULATE(
			    [Quantity Sold])
```

### Measure

```dax
CALCULATE([Quantity Sold],
			ALL(sales))
```

### active customer

```dax
DISTINCTCOUNT(sales[CustomerKey])
```

### max retail price

```dax
MAX('Product Lookup'[ProductPrice])
```

### Measure 2

```dax
BLANK()
```

### Aversge Retail Price

```dax
AVERAGE(
			    'Product Lookup'[ProductPrice])
```

### Total Returns

```dax
COUNTROWS(
			    'Returns Data'
			)
```

### Total Cost

```dax
SUMX(sales,
			    sales[OrderQuantity]  * RELATED('Product Lookup'[ProductCost]))
```

### Total Revenue

```dax
SUMX(sales,
			RELATED('Product Lookup'[ProductPrice]) * sales[OrderQuantity])
```

### profit

```dax
[Total Revenue] - [Total Cost]
```

### Profit margin

```dax
DIVIDE([profit], [Total Revenue])
```

### LM Profit

```dax
CALCULATE([profit], DATEADD('Calendar Lookup'[Date], -1, MONTH))
```

### LM Revenue

```dax
CALCULATE(
			 [Total Revenue],
			 DATEADD(
			 'Calendar Lookup'[Date],
			 -1,
			 MONTH
			 )
			)
```

### LM Return

```dax
CALCULATE(
			    [Total Returns],
			    DATEADD('Calendar Lookup'[Date],
			    -1,
			    MONTH
			    )
			)
```

### lm orders

```dax
CALCULATE(
			    [Total orders],
			    DATEADD('Calendar Lookup'[Date],
			    -1,
			    MONTH
			    ))
```

### Adjust Revenue

```dax
SUMX(
			     sales,
			        sales[OrderQuantity] * (1+'Qty sold selection'[Qty sold selection Value])
			        *
			        RELATED('Product Lookup'[ProductPrice])*(1+'Price selection'[Price selection Value])
			)
```

### Adjust cost

```dax
SUMX(
			    sales,
			    RELATED('Product Lookup'[ProductCost])  * sales[OrderQuantity] * (1+'Qty sold selection'[Qty sold selection Value]))
```

### Adjust Profit

```dax
'all data'[Adjust Revenue]- [Adjust cost]
```

### gap cost

```dax
[Adjust cost]- [Total Cost]
```

### gap revenue

```dax
[Adjust Revenue] - [Total Revenue]
```

### gap profit

```dax
[Adjust Profit] - [profit]
```

### Target Orders

```dax
[lm orders] * 1.1
```

### Target Revenue

```dax
[LM Revenue] * 1.1
```

### Target Profit

```dax
[LM Profit] * 1.1
```

### Gap orders

```dax
[Total orders] - [Target Orders]
```

### Measure 3

```dax
BLANK()
```

### Gap orders parametre

```dax
[Total orders] - [Target Orders]
```

### Gap Revenue Parametre

```dax
[Total Revenue]- [Target Revenue]
```

### Gap Profit Parametre

```dax
[profit] - [Target Profit]
```

### Average Quantity Sold

```dax
average(
			                        sales[OrderQuantity])
```

### adjudst average quantity sold

```dax
[Average Quantity Sold] * (1 + 'Qty sold selection'[Qty sold selection Value])
```

### Orders Gauge Maximum

```dax
MAX(1, MAX([Total orders], [Target Orders]) * 1.2)
```

### Revenue Gauge Maximum

```dax
MAX(1, MAX([Total Revenue], [Target Revenue]) * 1.2)
```

### Profit Gauge Maximum

```dax
MAX(1, MAX([profit], [Target Profit]) * 1.2)
```

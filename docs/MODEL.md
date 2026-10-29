# Model and measure reference

Extracted from the current PBIX. Measure names below are the existing names, including spelling inconsistencies. Formulas are documented as found, not endorsed as validated results.

## Relationships

| From | To | Cardinality | Filter | Active |
| --- | --- | --- | --- | --- |
| sales[OrderDate] | Calendar Lookup[Date] | M:1 | Single | Yes |
| Returns Data[ProductKey] | Product Lookup[ProductKey] | M:1 | Single | Yes |
| Product Lookup[ProductSubcategoryKey] | Product Subcategories Lookup[ProductSubcategoryKey] | M:1 | Single | Yes |
| Product Subcategories Lookup[ProductCategoryKey] | Product Categories Lookup[ProductCategoryKey] | M:1 | Single | Yes |
| Returns Data[TerritoryKey] | Territory Lookup[SalesTerritoryKey] | M:1 | Single | Yes |
| sales[TerritoryKey] | Territory Lookup[SalesTerritoryKey] | M:1 | Single | Yes |
| Customer Lookup[CustomerKey] | sales[CustomerKey] | M:M | Both | Yes |
| sales[ProductKey] | Product Lookup[ProductKey] | M:1 | Single | Yes |
| Returns Data[ReturnDate] | Calendar Lookup[Date] | M:1 | Single | Yes |

## Measures

### all data · Min Retail Price

```dax
MIN(
 'Product Lookup'[ProductPrice]
)
```

### all data · Quantity Sold

```dax
SUM(
 'sales'[OrderQuantity]
 )
```

### all data · Quatity Returns

```dax
SUM('Returns Data'[ReturnQuantity])
```

### all data · Total Customers

```dax

COUNT('Customer Lookup'[CustomerKey])
```

### all data · Total orders

```dax
DISTINCTCOUNT(
    sales[OrderNumber])
```

### all data · Returns Rate

```dax

[Quatity Returns]/[Quantity Sold]
```

### all data · ALL

```dax
CALCULATE(
    [Quantity Sold])
```

### all data · Measure

```dax
CALCULATE([Quantity Sold],
ALL(sales))
```

### all data · active customer

```dax
DISTINCTCOUNT(sales[CustomerKey])
```

### all data · max retail price

```dax
MAX('Product Lookup'[ProductPrice])
```

### all data · Measure 2

```dax
// Empty expression in the source model
```

### all data · Aversge Retail Price

```dax
AVERAGE(
    'Product Lookup'[ProductPrice])
```

### all data · Total Returns

```dax
COUNTROWS(
    'Returns Data'
)
```

### all data · Total Cost

```dax

    SUMX(sales,
    sales[OrderQuantity]  * RELATED('Product Lookup'[ProductCost]))
```

### all data · Total Revenue

```dax

SUMX(sales,
RELATED('Product Lookup'[ProductPrice]) * sales[OrderQuantity])
```

### all data · profit

```dax

    [Total Revenue] - [Total Cost]
```

### all data · Profit margin

```dax

    [profit] / [Total Revenue]
```

### all data · LM Profit

```dax
CALCULATE(
 [profit],
 DATEADD(
 'Calendar Lookup'[Date].[Date],
 -1,
 MONTH
 )
)
```

### all data · LM Revenue

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

### all data · LM Return

```dax
CALCULATE(
    [Total Returns],
    DATEADD('Calendar Lookup'[Date],
    -1,
    MONTH
    )
)
```

### all data · lm orders

```dax

CALCULATE(
    [Total orders],
    DATEADD('Calendar Lookup'[Date],
    -1,
    MONTH
    ))
```

### all data · Adjust Revenue

```dax
SUMX(
     sales,
        sales[OrderQuantity] * (1+'Qty sold selection'[Qty sold selection Value])
        *
        RELATED('Product Lookup'[ProductPrice])*(1+'Price selection'[Price selection Value])
)
```

### Price selection · Price selection Value

```dax
SELECTEDVALUE('Price selection'[Price selection], 0)
```

### Qty sold selection · Qty sold selection Value

```dax
SELECTEDVALUE('Qty sold selection'[Qty sold selection], 0)
```

### all data · Adjust cost

```dax
SUMX(
    sales,
    RELATED('Product Lookup'[ProductCost])  * sales[OrderQuantity] * (1+'Qty sold selection'[Qty sold selection Value]))
```

### all data · Adjust Profit

```dax
'all data'[Adjust Revenue]- [Adjust cost]
```

### all data · gap cost

```dax
[Adjust cost]- [Total Cost]
```

### all data · gap revenue

```dax
[Adjust Revenue] - [Total Revenue]
```

### all data · gap profit

```dax
[Adjust Profit] - [profit]
```

### all data · Target Orders

```dax

[lm orders] * 1.1
```

### all data · Target Revenue

```dax
[LM Revenue] * 1.1
```

### all data · Target Profit

```dax

[LM Profit] * 1.1 
```

### all data · Gap orders

```dax

[Total orders] - [Target Orders]
```

### all data · Measure 3

```dax
// Empty expression in the source model
```

### all data · Gap orders parametre

```dax

[Total orders] - [Target Orders]
```

### all data · Gap Revenue Parametre

```dax

[Total Revenue]- [Target Revenue]
```

### all data · Gap Profit Parametre

```dax

[profit] - [Target Profit]
```

### Qty Sold Selection  · Qty Sold Selection  Value

```dax
SELECTEDVALUE('Qty Sold Selection '[Qty Sold Selection ], 0)
```

### all data · Average Quantity Sold

```dax

                     average(
                        sales[OrderQuantity])
```

### all data · adjudst average quantity sold

```dax

                        [Average Quantity Sold] * (1+qu)
```

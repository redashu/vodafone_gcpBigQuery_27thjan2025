### Big query : all you need to Remember 

### Notice point 1 : 

<img src="nt1.png">

### Notice point 2 :

<img src="nt2.png">

### Notice point 3 

<img src="nt3.png">

### Notice point 4 

<img src="nt4.png">

### Creating UDF using SQL 

```sql
CREATE OR REPLACE FUNCTION `vodafonebigqproject-0011.ashu_finaldatasets.extract_domain`(email STRING) 
RETURNS STRING 
AS (
  SPLIT(email, "@")[SAFE_OFFSET(1)]
);

```

### analyzing most common email providers 

```sql
select `vodafonebigqproject-0011.ashu_finaldatasets.extract_domain`(email) AS domain,
COUNT(*) as user_count 
FROM `vodafonebigqproject-0011.ashu_finaldatasets.customer_emails`
GROUP BY domain 
ORDER BY user_count DESC

```

## Training lR model 

```sql
CREATE OR REPLACE MODEL `vodafonebigqproject-0011.ashu_finaldatasets.ashu_linear_house` OPTIONS(model_type='LINEAR_REG',
    input_label_cols=['price'] , early_stop=false, max_iterations=8, l2_reg=0.7, OPTIMIZE_STRATEGY="BATCH_GRADIENT_DESCENT") AS
SELECT
  avg_house_age,
  avg_rooms,
  avg_bedrooms,
  avg_income,
  population,
  price/100000 AS price

FROM  `vodafonebigqproject-0011.ashu_finaldatasets.ashu_usa_training` 
```

### to do evaluation use below query 

```sql
SELECT
  *
FROM
  ML.EVALUATE(MODEL `vodafonebigqproject-0011.ashu_finaldatasets.ashu_linear_house`)
```

### another way to evaluate 

```sql
-- fix this query
SELECT
    *
  FROM
    ML.EVALUATE(MODEL `vodafonebigqproject-0011.ashu_finaldatasets.ashu_linear_house`, TABLE `vodafonebigqproject-0011.ashu_finaldatasets.ashu_usa_eval`);
```

### doing evaluation 

```sql
-- fix this query
SELECT
    *
  FROM
    ML.EVALUATE(MODEL `vodafonebigqproject-0011.ashu_finaldatasets.ashu_linear_house`, (select * from `vodafonebigqproject-0011.ashu_finaldatasets.ashu_usa_eval`));
```

### predicting model 

```sql
SELECT
    *
  FROM
    ML.PREDICT(MODEL `vodafonebigqproject-0011.ashu_finaldatasets.ashu_linear_house`, (select * from `vodafonebigqproject-0011`.`ashu_finaldatasets`.`ashu_usa_eval`));
```
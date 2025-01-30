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


## architecture of BigQ

<img src="arch1.png">

### BigQuery connection options 

<img src="bq1.png">

### GCP --- cloud hierarchy 

<img src="gcp1.png">

### BigQ --- Client options 


<img src="cli1.png">

## Creating dataset / schema 

### SQL query 

```sql
create schema `vodafonebigqproject-0011.ashu_dataset003`
options(
  location="US",
  default_table_expiration_days=10,
  description="this is dataset created by ashutoshh"

);
```

### deleting empty dataset with no tables at all

```sql
drop schema `vodafonebigqproject-0011.ashu_dataset003`;
```

### Intro to table in BigQ

<img src="table1.png">

### Query example of table 

```sql
SELECT name , sum(count) as my_count 
FROM `vodafonebigqproject-0011.ashu_dataset001.ashu_table2` 
GROUP BY name 
ORDER BY my_count DESC LIMIT 10;
```

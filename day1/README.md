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


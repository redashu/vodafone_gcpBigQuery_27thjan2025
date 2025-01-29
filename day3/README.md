## Revision 

### Rev 1 

<img src="rev1.png">

### cleaning few datasets with all tables 

```sql
drop schema `vodafonebigqproject-0011.ashudataset_002` CASCADE;
```


### creating external table 

```sql
-- add autodetect schema options in this query
CREATE EXTERNAL TABLE
  `vodafonebigqproject-0011.ashudataset_day3.ashu_ext_table2`
OPTIONS (
    format = 'CSV',
    uris = ['gs://ashu_bucket001/auto_detect.txt']
  );
```

## INtro with BQ 

```
learntechbyme@cloudshell:~ (vodafonebigqproject-0011)$ pip list  | grep -i bigquery 
google-cloud-bigquery    3.29.0
learntechbyme@cloudshell:~ (vodafonebigqproject-0011)$ bq  version
This is BigQuery CLI 2.1.12
learntechbyme@cloudshell:~ (vodafonebigqproject-0011)$ 

```

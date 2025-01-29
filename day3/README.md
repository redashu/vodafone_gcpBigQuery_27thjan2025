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

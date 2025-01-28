## revision 

### info basic 

<img src="rev1.png">


### Collation in Bigquery 

[click_here](https://cloud.google.com/bigquery/docs/reference/standard-sql/collation-concepts)


### save and schedule query 

<img src="sv1.png">

### cron job 

<img src="cron1.png">


### External table and Wildcard table options 

<img src="wild1.png">

### query to wildcard table 

```
  -- i want print give details from 1930 to 1939 below temperature is in fohrenhight 
SELECT
  mo,
  da,
  year,
  max
FROM
  `bigquery-public-data.noaa_gsod.gsod193*`
WHERE 
  max != 9999.9 
ORDER BY
  max DESC
```

### using _TABLE_SUFFIX in bigquery wildcard tables options 

```sql
  -- i want print give details from 1930 to 1939 below temperature is in farenheit
SELECT
  mo,
  da,
  year,
  ROUND((max-32)*5/9,1) celsius,
  max
FROM
  `bigquery-public-data.noaa_gsod.gsod193*`
WHERE
  max != 9999.9
  AND ( _TABLE_SUFFIX = '1'
    OR _TABLE_SUFFIX = '3'
    OR _TABLE_SUFFIX = '7' )
ORDER BY
  max DESC
```

## Drive data url 
### Orginal URL: https://drive.google.com/file/d/1c46Al6C2dB8m6uV0orRPa_LfR6A1qW4h/view?usp=drive_link

# BIG query supported URL 

https://drive.google.com/open?id=1c46Al6C2dB8m6uV0orRPa_LfR6A1qW4h

### dataset data transfer options 

<img src="opt1.png">

## table alter options 

### changing data type of particular column to its compatible type 

```sql
ALTER TABLE
  `vodafonebigqproject-0011.ashudataset_002.ashu_table1_copy` ALTER COLUMN count
SET
  DATA type FLOAT64;
```

### changing existing column name 

```sql
ALTER TABLE
  `vodafonebigqproject-0011.ashudataset_002.ashu_table1_copy`
RENAME
  COLUMN name TO name_new
```

## Normalization vs DeNOM 

<img src="nm1.png">


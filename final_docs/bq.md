# TO start with bq we can set the project id 

### to set project id 

```
gcloud config set project ashu-new-project-445408
```

### list of datasets 

```
delvexdrive@cloudshell:~ (ashu-new-project-445408)$ bq ls
  datasetId   
 ------------ 
  dataset002  
  destdata    
  hellods
```

## OR

```
bq --project_id=ashu-new-project-445408 ls
  datasetId   
 ------------ 
  dataset002  
  destdata    
  hellods     
```

### Listing tables inside dataset

```
 bq ls --dataset_id=hellods
  tableId   Type    Labels   Time Partitioning   Clustered Fields  
 --------- ------- -------- ------------------- ------------------ 
  t2        TABLE                                                  
  table1    TABLE                                                  
  table2    TABLE                                                  
  table3    TABLE                                                  
```

### creating databaset 

```
bq --project_id=ashu-new-project-445408 mk --dataset --location=US newds_cli

Dataset 'ashu-new-project-445408:newds_cli' successfully created.
```

### checking dataset locations 

```
bq show --format=prettyjson ashu-new-project-445408:hellods
```

### creating table 

```
 bq mk --table --project_id=ashu-new-project-445408 --dataset_id=hellods hellods.table1001 name:STRING,gender:STRING,count:INTEGER
```

### table with required property 

```
echo '[{"name":"name","type":"STRING","mode":"REQUIRED"}, {"name":"gender","type":"STRING","mode":"NULLABLE"}]' > schema.json

===>
bq mk --table --schema=schema.json hellods.table3034

```

### removing table 

```
bq rm -t ashu-new-project-445408:hellods.table3034
```

### remove dataset 

```
bq rm -r -d ashu-new-project-445408:destdata
```

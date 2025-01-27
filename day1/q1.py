# import module 
from google.cloud import bigquery
# initial connection b/w gcp bigq and python 
ashu_client = bigquery.Client(project="vodafonebigqproject-0011")
# define query 
my_query = """ 
select name,gender,count 
FROM `vodafonebigqproject-0011.ashu_dataset001.ashu_table2` LIMIT 10;
"""

# runing query 
ashu_job = ashu_client.query(my_query)
#print(dir(ashu_job))
print(ashu_job)
for my_rows in ashu_job:
    print(my_rows)
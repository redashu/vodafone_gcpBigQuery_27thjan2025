from google.cloud import bigquery

client = bigquery.Client(project="vodafonebigqproject-0011")
dataset_ref = client.dataset("ashudataset_day3")
table_ref = dataset_ref.table("ashu_ext_table0077")

# Create an ExternalConfig object
external_config = bigquery.ExternalConfig("CSV")
external_config.source_uris = ["gs://ashu_bucket001/auto_detect.txt"]
external_config.autodetect = True

# Create a Table object
table = bigquery.Table(table_ref)

# Set the external data configuration
table.external_data_configuration = external_config

# Create the table
table = client.create_table(table)

print("External table created successfully")


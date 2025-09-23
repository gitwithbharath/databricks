# Databricks notebook source
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# COMMAND ----------

customer_schema = StructType(fields=[StructField("cust_id", StringType(), True),
                                     StructField("mem_id", StringType(), True),
                                     StructField("fst_name", StringType(), False),
                                     StructField("lst_name", StringType(), False),
                                     StructField("prm_status", StringType(), False),
                                     StructField("age", IntegerType(), False),
                                     StructField("state", StringType(), False),
                                     StructField("country", StringType(), False)
                                    
])

# COMMAND ----------

import datetime
def ingestDate():
    load_date = datetime.datetime.today() - datetime.timedelta(days=1)
    load_date_formatted = load_date.strftime ('%d%m%Y') 
    return load_date_formatted
    
 

# COMMAND ----------

data_loaded_on=ingestDate()
file_load_path="customer_data_"+str(data_loaded_on)+".csv"
final_file_path="/mnt/datasetbigdata/raw-data/lending_loan/" + file_load_path
print(final_file_path)

# COMMAND ----------

customer_df = spark.read \
.option("header", True) \
.schema(customer_schema) \
.csv(final_file_path)

# COMMAND ----------

display(customer_df)

# COMMAND ----------

raw_storage_path="/mnt/datasetbigdata/raw-data/lending_loan/"

# COMMAND ----------

# MAGIC % run '/Users/swecha34@outlook.com/2023-01-21 - DBFS Example'

# COMMAND ----------

f{raw_storage_path}

# COMMAND ----------

from pyspark.sql.functions import current_timestamp
def ingestDate(input_df):
    output_df=input_df.withColumn("ingest_date", current_timestamp())
    return output_df

# COMMAND ----------

final_df=ingestDate(input_df)
display(final_df)

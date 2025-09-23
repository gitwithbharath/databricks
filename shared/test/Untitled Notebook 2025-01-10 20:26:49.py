# Databricks notebook source
from pyspark.sql import functions as F
df = spark.range(1, 1000000).toDF("id").repartition(10).withColumn("square", F.expr("id * id")).cache()

df.take(10)

# COMMAND ----------

# MAGIC %fs
# MAGIC
# MAGIC ls dbfs:/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-calls.csv

# COMMAND ----------

fire_df = spark.read.format("csv") \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .load("dbfs:/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-calls.csv")

# COMMAND ----------

fire_df.show(5)

# COMMAND ----------

display(fire_df)

# COMMAND ----------

fire_df.createGlobalTempView("fire_service_calls_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from global_temp.fire_service_calls_view

# COMMAND ----------



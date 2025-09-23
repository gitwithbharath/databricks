# Databricks notebook source
data = [[1, "Kristeen", 1420],
[2, "Ashley", 2006],
[3, "Julia", 2210],
[4, "Maria", 3000]]

# COMMAND ----------

col = ["ID", "Name", "Salary"]

# COMMAND ----------

df = spark.createDataFrame(data, col)

# COMMAND ----------

df.show()

# COMMAND ----------

from pyspark.sql.functions import translate
df = df.withColumn("error_column", translate("Salary", "0", ""))

# COMMAND ----------

df.show()

# COMMAND ----------

from pyspark.sql.functions import avg,ceil,col
result = df.agg(ceil(avg(col("Salary"))- avg(col("error_column")))).alias("Result")
result.show()

# COMMAND ----------



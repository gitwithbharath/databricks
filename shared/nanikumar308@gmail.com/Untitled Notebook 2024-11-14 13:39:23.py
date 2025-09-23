# Databricks notebook source
from pyspark.sql import SparkSession
data=((1,"Keyboard",400,4),
(2, "Mouse",300,4),
(3,	"Monitor",12000,3),
(4,	"Keyboard",400,1),
(5,	"Mousepad",250,2))


columns = ("order_id", "item", "amount", "customer_id")



df = spark.createDataFrame(data, columns)

# COMMAND ----------

df.show()

# COMMAND ----------

from pyspark.sql import SparkSession

df.createTempView("temp_orders")
avg_value = spark.sql("""
                      SELECT AVG(AMOUNT) FROM orders""")

print(avg_value)

categorized_TABLE = spark.sql("""
                              SELECT order_id,amount,customer_id,
                              CASE WHEN amount > avg_value THEN "High_value_item" ELSE "LOW_value_item" END AS Category
                              FROM temp_orders""")

categorized_TABLE.show()

# COMMAND ----------


df.pivot(("AScore", "BScore", "Cscore").alias("Subject")).agg("Student","StudentName")

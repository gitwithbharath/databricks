# Databricks notebook source

dbutils.fs.help()

# COMMAND ----------

display(dbutils.fs.head("/databricks-datasets/retail-org/company_employees/company_employees.csv"))

# COMMAND ----------

dbutils.widgets.text("dept", "", "Department Name")

# COMMAND ----------

_dept = dbutils.widgets.get("dept")
print(_dept)

# COMMAND ----------

df = spark.read.csv("/databricks-datasets/retail-org/company_employees/company_employees.csv", header=True)
display(df)

# COMMAND ----------

df_filtered = df.where(f"upper(department) = upper('{_dept}') and active_record = '1'")
display(df_filtered)

# COMMAND ----------

_count = df_filtered.count()

if _count > 0:
    df_filtered.write.mode("overwrite").saveAsTable(f"dept_{_dept}")
    print(f"Data Written for {_dept}")
    display(spark.table(f"dept_{_dept}"))
else:
    print(f"No Data for {_dept}")

# COMMAND ----------



# Databricks notebook source
# MAGIC %md
# MAGIC 𝐒𝐜𝐡𝐞𝐦𝐚 𝐚𝐧𝐝 𝐃𝐚𝐭𝐚𝐬𝐞𝐭:
# MAGIC CREATE TABLE famous (user_id INT, follower_id INT);
# MAGIC
# MAGIC INSERT INTO famous VALUES
# MAGIC (1, 2), (1, 3), (2, 4), (5, 1), (5, 3), 
# MAGIC (11, 7), (12, 8), (13, 5), (13, 10), 
# MAGIC (14, 12), (14, 3), (15, 14), (15, 13);

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS famous;
# MAGIC CREATE TABLE famous (user_id INT, follower_id INT);
# MAGIC INSERT INTO famous VALUES
# MAGIC (1, 2), (1, 3), (2, 4), (5, 1), (5, 3), 
# MAGIC (11, 7), (12, 8), (13, 5), (13, 10), 
# MAGIC (14, 12), (14, 3), (15, 14), (15, 13);
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM famous;

# COMMAND ----------



# Databricks notebook source
initial_rdd = sc.textFile("dbfs:/FileStore/TrendyTech/Week10/bigdata_campaign_data.csv")

# initial_rdd.collect()

mappedInput = initial_rdd.map(lambda x:(float(x.split(",")[10]),x.split(",")[0]))

words = mappedInput.flatMapValues(lambda x:x.split(" "))

final_mapped = words.map(lambda x:(x[1].lower(), x[0]))

total = final_mapped.reduceByKey(lambda x,y: x+y).sortBy(lambda x:x[1], False)

result = total.take(50)

for a in result:
    print(a)

# COMMAND ----------

# import builtins

def loadBoringWords():
    boringWords = sc.textFile("dbfs:/FileStore/TrendyTech/Week10/boringwords.txt")
    boringWords_list = boringWords.flatMap(lambda x:x.split("\n")).collect()
    return boringWords_list
#     boringWords = set(line.strip() for line in open("/dbfs/FileStore/TrendyTech/Week10/boringwords.txt"))
#     return boringWords



name_set = sc.broadcast(loadBoringWords())

initial_rdd = sc.textFile("dbfs:/FileStore/TrendyTech/Week10/bigdata_campaign_data.csv")

mappedInput = initial_rdd.map(lambda x:(float(x.split(",")[10]),x.split(",")[0]))

words = mappedInput.flatMapValues(lambda x:x.split(" "))

final_mapped = words.map(lambda x:(x[1].lower(), x[0]))

filtered_rdd = final_mapped.filter(lambda x:x[0] not in name_set.value)

total = filtered_rdd.reduceByKey(lambda x,y: x+y).sortBy(lambda x:x[1], False)

result = total.take(50)

for a in result:
    print(a)

# COMMAND ----------

from sys import stdin

stdin.readline()

# COMMAND ----------

boringWords = sc.textFile("dbfs:/FileStore/TrendyTech/Week10/boringwords.txt")

boringWords.getNumPartitions

# COMMAND ----------

sc.defaultMinPartitions

# COMMAND ----------



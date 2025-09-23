# Databricks notebook source
from pyspark.sql.context import SparkContext

from pyspark import Sp

# sc = SparkContext("local[*]", "wordCount")

# df = spark.read.csv("dbfs:/mnt/mount_databricks-community-practice/linked_post1_data/dept.csv", header=True, inferSchema=True)

# df1 = spark.read.load("*.txt", format="text")

# COMMAND ----------

sc.setLogLevel("ERROR")
input = sc.textFile("dbfs:/FileStore/search_data.txt")

words = input.flatMap(lambda x:x.split(" "))

word_counts = words.map(lambda x:(x.lower(),1))

final_count = word_counts.reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], ascending=False )
# final_count = word_counts.countByValue()

# final_count.saveAsTextFile("dbfs:/FileStore/sparkoutput")
# result = final_count
result = final_count.collect()

# type(result)

for a in result:
    print(a)


# COMMAND ----------

rdd1 = sc.textFile("dbfs:/FileStore/TrendyTech/Week9/customerorders.csv")

rdd2 = rdd1.map(lambda x:(x.split(",")[0], float(x.split(",")[2])))

rdd3 = rdd2.reduceByKey(lambda x,y: x+y)

rdd4 = rdd3.sortBy(lambda x:x[1], ascending=False)

result = rdd4.collect()

for a in result:
    print(a)


# COMMAND ----------

lines = sc.textFile("dbfs:/FileStore/TrendyTech/Week9/moviedata.data")

# lines.collect()

ratings = lines.map(lambda x:(x.split("\t")[2],1))

result = ratings.reduceByKey(lambda x,y: x+y).sortBy(lambda x:x[1]).collect()

for a in result:
    print(a)

# COMMAND ----------

def parseLine(line):
    fields = line.split("::")
    age = int(fields[2])
    numFriends = int(fields[3])

    return (age, numFriends)


lines = sc.textFile("dbfs:/FileStore/TrendyTech/Week9/friendsdata.csv")

# lines.collect()
rdd = lines.map(parseLine)

# rdd.collect()

totalsByAge = rdd.mapValues(lambda x:(x,1)).reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1]))

averagesByAge = totalsByAge.mapValues(lambda x: x[0]/x[1])

result = averagesByAge.collect()

for a in result:
    print(a)


# COMMAND ----------



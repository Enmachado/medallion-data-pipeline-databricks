# Databricks notebook source
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

# COMMAND ----------

print(data[:2])

# COMMAND ----------

df = spark.createDataFrame(data)

display(df)

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

df = df.withColumn("date", current_timestamp())

# COMMAND ----------

df.write.format("delta") \
  .mode("append") \
  .saveAsTable("bronze_posts")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze_posts
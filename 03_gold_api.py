# Databricks notebook source
from pyspark.sql.functions import count

df = spark.read.table("silver_posts")

df_gold = (
    df.groupBy("userId")
      .agg(count("*").alias("qtd_posts"))
)

# COMMAND ----------

df_gold.write.format("delta") \
  .mode("overwrite") \
  .saveAsTable("gold_posts_por_usuario")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gold_posts_por_usuario
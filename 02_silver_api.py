# Databricks notebook source
from pyspark.sql.functions import col

df = spark.read.table("bronze_posts")

df_clean = (
    df.dropDuplicates(["id"])  # evita duplicação da API
)

# COMMAND ----------

df_clean.write.format("delta") \
  .mode("overwrite") \
  .saveAsTable("silver_posts")
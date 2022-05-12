from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def csv_malformed(spark: SparkSession) -> DataFrame:

    if Config.fabricName == "gamedayfabric":
        return spark.read\
            .schema(
              StructType([
                StructField("    col1", StringType(), True), StructField("col2", StringType(), True), StructField("col3", StringType(), True), StructField("col4", StringType(), True), StructField("col5", StringType(), True), StructField("col6", StringType(), True), StructField("col7", StringType(), True), StructField("col8", StringType(), True), StructField("col9", StringType(), True), StructField("col10", StringType(), True), StructField("col11", StringType(), True), StructField("col12", StringType(), True), StructField("col13", StringType(), True), StructField("col14", StringType(), True), StructField("col15", StringType(), True), StructField("col16", StringType(), True), StructField("col17", StringType(), True), StructField("col18", StringType(), True), StructField(" col19_", StringType(), True)
            ])
            )\
            .option("header", True)\
            .option("inferSchema", False)\
            .option("escape", "\"")\
            .option("quote", "\"")\
            .option("sep", ",")\
            .option("modifiedBefore", "2022-05-14")\
            .option("modifiedAfter", Config.last_run)\
            .option("pathGlobFilter", "*.csv")\
            .csv("dbfs:/Prophecy/anshuman@simpledatalabs.com/malformed_csv.csv")
    else:
        raise Exception("No valid dataset present to read fabric")

    if Config.fabricName == "anshuman":
        return spark.read\
            .schema(
              StructType([
                StructField("    col1", StringType(), True), StructField("col2", StringType(), True), StructField("col3", StringType(), True), StructField("col4", StringType(), True), StructField("col5", StringType(), True), StructField("col6", StringType(), True), StructField("col7", StringType(), True), StructField("col8", StringType(), True), StructField("col9", StringType(), True), StructField("col10", StringType(), True), StructField("col11", StringType(), True), StructField("col12", StringType(), True), StructField("col13", StringType(), True), StructField("col14", StringType(), True), StructField("col15", StringType(), True), StructField("col16", StringType(), True), StructField("col17", StringType(), True), StructField("col18", StringType(), True), StructField(" col19_", StringType(), True)
            ])
            )\
            .option("header", True)\
            .option("inferSchema", False)\
            .option("escape", "\"")\
            .option("quote", "\"")\
            .option("sep", ",")\
            .option("modifiedBefore", "2022-05-14")\
            .option("modifiedAfter", Config.last_run)\
            .option("pathGlobFilter", "*.csv")\
            .csv("dbfs:/Prophecy/anshuman@simpledatalabs.com/malformed_csv.csv")
    else:
        raise Exception("No valid dataset present to read fabric")

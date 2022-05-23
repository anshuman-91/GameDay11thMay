from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Source_0(spark: SparkSession) -> DataFrame:
    if Config.fabricName == "gamedayfabric":
        return spark.read\
            .schema(
              StructType([
                StructField("35", StringType(), True), StructField("85", StringType(), True), StructField("2342374324123", StringType(), True), StructField("12321", StringType(), True), StructField("-3123.123", StringType(), True), StructField("false", StringType(), True), StructField("45734.345341", StringType(), True), StructField("r#$%@#4!*&^()_=ASD~!425", StringType(), True), StructField("2015-06-06", StringType(), True), StructField("2015-08-07T10:20:44.000Z", StringType(), True)
            ])
            )\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/Prophecy/qa_data/csv/all_type_no_partition/")
    elif Config.fabricName == "anshuman2":
        return spark.read\
            .schema(
              StructType([
                StructField("490", StringType(), True), StructField("491", StringType(), True), StructField("2342374324123", StringType(), True), StructField("12321", StringType(), True), StructField("-3123.123", StringType(), True), StructField("false", StringType(), True), StructField("45734.345341", StringType(), True), StructField("r#$%@#4!*&^()_=ASD~!245", StringType(), True), StructField("2009-02-10", StringType(), True), StructField("2009-04-11T10:20:44.000Z", StringType(), True)
            ])
            )\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/Prophecy/anshuman@simpledatalabs.com/test_csv.csv")
    else:
        raise Exception("No valid dataset present to read fabric")

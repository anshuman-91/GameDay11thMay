from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Source_0(spark: SparkSession) -> DataFrame:
    if Config.fabricName == "gamedayfabric":
        return spark.read\
            .schema(StructType([StructField("id", StringType(), True), StructField("device", StringType(), True)]))\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/FileStore/rajp/export.csv")
    else:
        raise Exception("No valid dataset present to read fabric")

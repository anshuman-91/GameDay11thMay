from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Source_1(spark: SparkSession) -> DataFrame:
    if Config.fabricName == "gamedayfabric":
        return spark.read\
            .schema(StructType([StructField("format", StringType(), True), StructField("example", StringType(), True)]))\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/FileStore/data_engg/csv/timestamps_csv.csv")
    else:
        raise Exception("No valid dataset present to read fabric")

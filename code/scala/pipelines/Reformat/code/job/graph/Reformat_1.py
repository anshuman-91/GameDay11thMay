from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("format"), 
        col("example"), 
        when(col("example").isNotNull(), to_timestamp(col("example"), ""))\
          .otherwise(col("example"))\
          .alias("parsed_example")
    )

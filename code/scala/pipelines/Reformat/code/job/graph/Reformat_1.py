from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        when((length(col("format")) > lit(17)), lit("big")).otherwise(lit("small")).alias("how big").alias("how_big"), 
        when(col("example").isin(lit("aa"), lit("2018-08-20'T'13:20:10*633+0000")), lit(1111))\
          .otherwise(lit("a"))\
          .alias("f2"), 
        when((length(col("format")) > lit(18)), lit("big"))\
          .otherwise(when((length(col("format")) > lit(15)), lit("medium")).otherwise(lit("small")))\
          .alias("how big")\
          .alias("how_big2"), 
        to_timestamp(lit("06-24-2019 12:01:19.000"), "MM-dd-yyyy HH:mm:ss.SSSS").alias("cast"), 
        col("format"), 
        col("example"), 
        to_timestamp(lit("23 Apr 2017 10:32:35*311"), "dd MMM yyyy HH:mm:ss*SSS").alias("cast2")
    )

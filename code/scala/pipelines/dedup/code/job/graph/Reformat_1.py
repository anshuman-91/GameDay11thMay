from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        lit(35).alias("35"), 
        lit(85).alias("85"), 
        lit(34).alias("2342374324123"), 
        lit(12321).alias("12321"), 
        lit(False).alias("false"), 
        col(
            "`r#$%@#4!*&^()_=ASD~!425`"
          )\
          .alias(
          "r#$%@#4!*&^()_=ASD~!425"
        ), 
        col("`2015-06-06`").alias("2015-06-06"), 
        lit(45734.345341).alias("345341")
    )

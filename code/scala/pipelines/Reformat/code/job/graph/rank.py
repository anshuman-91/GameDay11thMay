from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def rank(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        regexp_replace(col("format"), "yyyy", "YYYY").alias("x"), 
        lit("rank().over(Window.partitionBy('example').orderBy('format'))").alias("y"), 
        col("format").alias("cc").alias("z")
    )

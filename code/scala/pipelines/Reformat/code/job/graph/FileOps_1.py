from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def FileOps_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    import os

    return in0

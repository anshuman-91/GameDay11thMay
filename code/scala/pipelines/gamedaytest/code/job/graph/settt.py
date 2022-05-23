from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def settt(spark: SparkSession, in0: DataFrame, in1: DataFrame, inDFs0: DataFrame) -> DataFrame:
    return in0.intersectAll(in1).intersectAll(inDFs0)

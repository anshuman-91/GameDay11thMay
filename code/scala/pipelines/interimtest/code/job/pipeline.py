from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Source_0 = Source_0(spark)
    df_Reformat_1 = Reformat_1(spark, df_Source_0)
    df_Filter_1 = Filter_1(spark, df_Reformat_1)
    df_SetOperation_1 = SetOperation_1(spark, df_Filter_1, df_Source_0)
    df_Filter_2 = Filter_2(spark, df_SetOperation_1)

def main():
    Utils.initializeFromArgs(Utils.parseArgs())
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    pipeline(spark)

if __name__ == "__main__":
    main()

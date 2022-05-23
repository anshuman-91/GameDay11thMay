from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Source_0 = Source_0(spark)
    df_Reformat_1 = Reformat_1(spark, df_Source_0)
    df_Reformat_2 = Reformat_2(spark, df_Reformat_1)
    df_OrderBy_1 = OrderBy_1(spark, df_Source_0)
    df_Deduplicate_1 = Deduplicate_1(spark, df_OrderBy_1)
    df_Reformat_4 = Reformat_4(spark, df_Deduplicate_1)
    df_Reformat_3 = Reformat_3(spark, df_Source_0)

def main():
    Utils.initializeFromArgs(Utils.parseArgs())
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    initialize(spark)
    pipeline(spark)

if __name__ == "__main__":
    main()

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Source_1 = Source_1(spark)
    df_FileOps_1 = FileOps_1(spark, df_Source_1)
    df_rank = rank(spark, df_Source_1)
    df_Reformat_5 = Reformat_5(spark, df_rank)
    df_Script_1 = Script_1(spark, df_Source_1)
    df_Aggregate_1 = Aggregate_1(spark, df_Source_1)
    df_Reformat_6 = Reformat_6(spark, df_Aggregate_1)
    df_Reformat_1 = Reformat_1(spark, df_Source_1)
    df_ref = ref(spark, df_Reformat_1)
    df_Reformat_3 = Reformat_3(spark, df_ref)
    df_Reformat_2 = Reformat_2(spark, df_Script_1)
    df_bug2 = bug2(spark, df_Source_1)
    df_Reformat_4 = Reformat_4(spark, df_bug2)
    df_bug = bug(spark, df_Source_1)

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

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Script_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    import os
    # for root, dirs, files in os.walk(".", topdown=False):
    #    print('################################%%%%%%%%%%%%%%')
    #    for name in files:
    #       print(os.path.join(root, name))
    #    for name in dirs:
    #       print(os.path.join(root, name))
    out0 = in0
    print(
        '################################%%%%%%%%%%%%%%'
    )
    print(os.walk("../../"))
    print(os.walk("/"))
    print("$$$$$$$$$$$$$$$$$$$")
    os.system("dbfs ls dbfs:/FileStore/")
    os.system("ls /dbfs/FileStore/data_engg/")
    print("$$$$$$$$$$$$$$$$$$$")
    out0 = out0.withColumn("haha", lit(str([x for x in os.walk(".")])))

    return out0

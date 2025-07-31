from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SeasonFrequency").getOrCreate()

exped = spark.read.csv("/home/id101567404/bigdata_project/Dim_Expeditions.csv", header=True, inferSchema=True)

result = exped.groupBy("season").count().orderBy("count", ascending=False)

result.show()

spark.stop()

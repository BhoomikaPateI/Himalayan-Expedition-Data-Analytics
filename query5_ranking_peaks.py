from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, sum as sum_func, col

spark = SparkSession.builder.appName("RankingNations").getOrCreate()

fact = spark.read.option("header", "true").option("inferSchema", "true").csv("/home/id101567404/bigdata_project/Fact_Expeditions.csv")
exped = spark.read.option("header", "true").option("inferSchema", "true").csv("/home/id101567404/bigdata_project/Dim_Expeditions.csv")

fact = fact.alias("fact")
exped = exped.alias("exped")

data = fact.join(exped, fact.expid == exped.expid, "inner").groupBy(exped.nation).agg(sum_func("Sum_smtmembers").alias("total_summiteers"))

window = Window.orderBy(col("total_summiteers").desc())

ranked_data = data.withColumn("rank", rank().over(window))

ranked_data.select("nation", "total_summiteers", "rank").show()

spark.stop()
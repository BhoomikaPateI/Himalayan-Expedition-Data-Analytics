from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import ntile, count

spark = SparkSession.builder.appName("BinningExpeditions").getOrCreate()

fact = spark.read.csv("/home/id101567404/bigdata_project/Fact_Expeditions.csv", header=True, inferSchema=True)

data = fact.select("Avg_Success_Rate", "Sum_totmembers").na.drop()

window_success = Window.orderBy("Avg_Success_Rate")
window_team = Window.orderBy("Sum_totmembers")
binned_data = data.withColumn("success_bin", ntile(3).over(window_success)) \
                  .withColumn("team_bin", ntile(3).over(window_team))

result = binned_data.groupBy("success_bin", "team_bin").agg(count("*").alias("expedition_count"))

result.orderBy("success_bin", "team_bin").show()

spark.stop()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CorrelationHeightSuccess").getOrCreate()

fact = spark.read.csv("/home/id101567404/bigdata_project/Fact_Expeditions.csv", header=True, inferSchema=True)
peaks = spark.read.csv("/home/id101567404/bigdata_project/Dim_Peaks.csv", header=True, inferSchema=True)

data = fact.join(peaks, "peakid").select("Avg_Success_Rate", "heightm")

correlation = data.stat.corr("Avg_Success_Rate", "heightm")

result = spark.createDataFrame([("Correlation Coefficient", correlation)], ["Metric", "Value"])

result.show()

spark.stop()
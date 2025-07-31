from pyspark.sql import SparkSession
from pyspark.sql.functions import min as min_func, max as max_func, avg as avg_func

# Initialize Spark session
spark = SparkSession.builder.appName("DurationRegionStats").getOrCreate()

# Read CSV files
fact = spark.read.option("header", "true").option("inferSchema", "true").csv("/home/id101567404/bigdata_project/Fact_Expeditions.csv")
peaks = spark.read.option("header", "true").option("inferSchema", "true").csv("/home/id101567404/bigdata_project/Dim_Peaks.csv")

fact = fact.alias("fact")
peaks = peaks.alias("peaks")

data = fact.join(peaks, fact.peakid == peaks.peakid, "inner").groupBy(peaks.region).agg(
    min_func("Avg_totdays").alias("min_days"),
    max_func("Avg_totdays").alias("max_days"),
    avg_func("Avg_totdays").alias("avg_days")
).orderBy("region")

# Show results in terminal
data.show()

# Stop Spark session
spark.stop()
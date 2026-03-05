from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg, sum
from pyspark.sql.types import StructType, StringType, DoubleType, IntegerType

# Create Spark Session
spark = SparkSession.builder \
    .appName("StockStreamingApp") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Define Schema
schema = StructType() \
    .add("event_id", StringType()) \
    .add("symbol", StringType()) \
    .add("price", DoubleType()) \
    .add("volume", IntegerType()) \
    .add("event_time", StringType()) \
    .add("market", StringType())

# Read from Kafka
# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "stock-events") \
    .load()

# Convert value from binary to string
json_df = df.selectExpr("CAST(value AS STRING)")

# Parse JSON
parsed_df = json_df.select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

# Aggregate
agg_df = parsed_df.groupBy("symbol") \
    .agg(
        avg("price").alias("avg_price"),
        sum("volume").alias("total_volume")
    )

# Output to console
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
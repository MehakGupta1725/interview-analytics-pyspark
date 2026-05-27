from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder \
    .appName("AIInterviewAnalytics") \
    .getOrCreate()

def analyze_data(file_path):

    df = spark.read.csv(
        file_path,
        header=True,
        inferSchema=True
    )

    avg_score = df.select(
        avg("Score")
    ).collect()[0][0]

    avg_confidence = df.select(
        avg("Confidence")
    ).collect()[0][0]

    category_rank = df.groupBy(
        "Category"
    ).agg(
        avg("Score").alias("Average Score")
    )

    leaderboard = df.orderBy(
        df["Score"].desc()
    )

    daily_trend = df.groupBy(
        "Date"
    ).agg(
        avg("Score").alias("Daily Avg")
    )

    heatmap = df.groupBy(
        "Candidate",
        "Category"
    ).agg(
        avg("Score").alias("Score")
    )

    return(
        df,
        avg_score,
        avg_confidence,
        category_rank,
        leaderboard,
        daily_trend,
        heatmap
    )
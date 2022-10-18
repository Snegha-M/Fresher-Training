from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-16").getOrCreate()

#16.Apply filter and display the column name ‘high’ greater than 500 and display only 5 rows of output.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.filter(data.High > 500).show(5)
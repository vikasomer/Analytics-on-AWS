import sys
import logging


def run_transform(bucket_name):	
	from pyspark.sql import SparkSession
	from pyspark.sql.types import StructType

	# Create a spark session
	spark = SparkSession \
	    .builder \
	    .appName("emr etl job") \
	    .getOrCreate()
	
	# Setup the logger to write to spark logs
	Logger= spark._jvm.org.apache.log4j.Logger
	mylogger = Logger.getLogger("TRANSFORM")

	mylogger.info("Spark session created")
	mylogger.info("Trying to read data now.")
	mylogger.info("Bucket name is {}".format(bucket_name))

	# Schema for the raw data json files
	raw_data_schema = StructType().add("uuid", "string") \
		.add("device_ts", "string") \
		.add("device_id", "integer") \
		.add("device_temp", "integer") \
		.add("track_id", "integer") \
		.add("activity_type", "string")


	# Schema for the reference data file
	reference_data_schema = StructType().add("track_id", "string") \
		.add("track_name", "string") \
		.add("artist_name", "string")


	# Read the raw data into a data frame 
	raw_data = spark.read \
		.schema(raw_data_schema) \
		.json('s3://{}/data/raw/*/*/*/*/'.format(bucket_name))
	
	# Read the reference data into a data frame
	reference_data = spark.read \
	.schema(reference_data_schema) \
	.json('s3://{}/data/reference_data/'.format(bucket_name))

	raw_data.printSchema()
	reference_data.printSchema()

	mylogger.info('raw_data (Count) = ' + str(raw_data.count()))
	mylogger.info('reference_data (Count) = ' + str(reference_data.count()))

	# Join the two datasets on track_id
	joined_data = raw_data.join(reference_data, 'track_id', 'inner')
	joined_data.printSchema()

	# Bucket the data by activity type
	# And write the results to S3 in overwrite mode
	joined_data \
		.write \
		.format("parquet") \
		.mode("overwrite") \
		.option("path", "s3://{}/data/emr-processed-data/".format(bucket_name)) \
		.save()

	spark.stop()


def main():
	# Accept bucket name from the arguments passed.
	# TO DO: Error handling when there are no arguments passed.
	BUCKET_NAME = sys.argv[1]

	# Run the tranform method
	run_transform(BUCKET_NAME)


if __name__ == '__main__':
	main()
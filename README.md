# Big data project on best buy data
## The motivation of this work:

With increasing data volume in each industry provides never-ending challenges in bigdata domain. There are traditional ways and modern ways of handling big data. In today’s competitive & complex business world the various aspects of business Change in one aspect has direct or indirect effect on another aspect.This complexity of data makes it difficult for any business to rely solely on experience (or intuition) to make decisions. We need to rely on data - structured,unstructured or semi-structured - to make any business decision. There are many technologies and tools like SAS, R, and Matlab to analyse data before making any decision. I wanted incorporate tranditional ETL(Extract, transform and load) process using AWS component, Hadoop, Nosql and Apache Spark as I think it provides more complete view for insight into the data with ease and it is easy to capture, store, manage and analyze. My motivation for this work is to get more knowledge on the data with a traditional process of handling big data with aws touch.

## The problem to address:

Nowadays, parts of bigdata are stored and processed in cloud and parts – on-premises, which can also be cost-effective.My goal is to resorting big data to data lakes and querying and analyzing one part at a time using Optimized algorithms or programs and combine the whole data to get the final details of the analysis.I tried to process data in a cost effective way without compromising the data quality. Also tried to address the problem of upscaling using this project. The pipeline included in this project gives no complexity of scaling up so the system’s performance doesn’t decline and stay within budget.

# The approach overview:

In the last few years, with the advancement of technologies and digitization, the amount of data generated rapidly increased from Terabytes to Zettabytes and by 2025, it is predicted there would a big and tremendous volume of data collections and that would be nearly 163 zettabytes. To handle this huge volume of data and process them to draw meaningful insights technologies like Hadoop and its ecosystem come to rescue. In the project, to explore on big data technologies – Hadoop and its ecosystem, we opted to work on e-commerce data (Best Buy store website).Data collected includes information on products such as Cellphones, Desktops and Laptops, customer ratings on these products and also in-store stock information across Canada. We aim to store and analyze this data to draw insights about availability of products online or in-store, Customer top rated products, items qualifying under clearance sale and so on.

I have used kinesis firehose to create a data stream for data ingestion into s3. I have choosen s3 over HDFS as s3 data is more scalable and always persistant and serves the purpose of building a datalake for the processed data stored in s3. After data ingestion into s3 , I am importing the data into no sql database MongoDB. After that, processing the data using Spark&Scala and loading the processed data into s3 bucket. Storing the data into an optimised data lake on s3 with amazon Athena acting as a metadata repository which provides query service for the data and then Tableau (which store a “cache” of that data into it's hyper engine) to visualize.

## Data ingestion using Kinesis Firehose:

Using Amazon kinesis firehose to load api data into AWS. The delivery stream load the data into the delivery stream and route it to S3.Behind the scenes, Kinesis Firehose take care of all of the monitoring, scaling, and data management.

First, one kinesis firehose stream needs to be created on aws.
Now, for acesssing firehose, I have added below iam roles to access kinesis firehose on my EC2 instance as I am using python code for data ingestion.
To put records into s3 bucket, I have created one bucket with public access to put records from external source in this case.
I have created a bucket in us east region and the name of the bucket is aws.storage.project which is the destination of the data from best buy api.

## Importing Unstructured data to MongoDB:
In order to put the data into mongodb there should be a connection between mongodb running on hadoop and s3 bucket. I have used boto3 to access the data in s3.

Since the data is embedded json data, importing the data into two collection one with all data into one collection and another product information into another collection after flattening the embedded json data for further analysis in this case.

## Extract and Transformation:
Apache Spark is a powerful processing engine designed for speed, ease of use, and analytics. Spark particularly excels when fast performance is required. MongoDB is a popular NoSQL database that enterprises rely on for real-time analytics from their operational data. The integration of Apache Spark extends analytics capabilities even further to perform real-time analytics. With Spark and MongoDB,functional applications are faster using a single database technology. MongoDB drivers to execute queries against the database, returning results to the application where additional analytics can be run using spark. I have used pyspark and programmed with scala and python to extract data from MongoDB.
There are some prerequisites in order to connect to mongoDB using scala and pyspark:

Scala :

sbt dependencies should be added before making connection to MongoDB.

pyspark:

Mongo-spark connector
pyspark --conf "spark.mongodb.input.uri=mongodb://127.0.0.1/bestbuy_data_db.best_buy?readPreference=primaryPreferred" --conf "spark.mongodb.output.uri=mongodb://127.0.0.1/bestbuy_data_db.best_buy" --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.1
Scala version : 2.11
pyspark version:2.4.5
Adding mongo-spark-connector 'mongo-spark-connector_2.11:2.4.1' from maven repository.

## Loading:
I am using pyspark and boto3 with python to load the data into s3 in aws after processing.

## Datalake:
Creating a datalake using aws glue with s3 before analyzing the data that addresses the challenges of dealing with large volumes of heterogeneous data. This data lake allows organizations to store all their data—structured and unstructured—in one centralized repository. Because data can be stored as it is and there is no need to convert it to a predefined schema.AWS Glue crawls the used data sources and constructs a data catalog using pre-built classifiers for any data formats.
In this project, I am creating a data lake in us-east-1 region.

## Visualization:
I have used Tableau for visualization as Athena provides a connection jar to connect with Tableau. It is a very good combination to visualize the data as it ensures the visualizations are taking advantage of the underlying Tableau Hyper engine, ensuring the maximize Tableau performance while minimizing AWS data lake and Athena costs. Tableau is very useful in dashboard creation as it provides feature to auto-update, data extract and job schedule as well as provides interacting dashboard feautures which helps to filter a specific data with just a click in that case we don't have to make any query changes in data lake or datawarehouse to see some particular result which is very efficient in production domain for continuous changes in data.Athena service optimizes and automates the configuration, processing, and loading of data to AWS Athena unlocking how users can return query results in Tableau.AWS Athena service simply push data from data lake and the service will automatically load it into your AWS Athena database for use in Tableau.
There is two prerequisite to establish one connection between aws athena and Tableau.

prerequisite
-- The below jdbc jar needs to be added in Tableau drivers.
-- One iam role should be created for aws Athena

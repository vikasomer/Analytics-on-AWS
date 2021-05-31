# Workshop: Analytics on AWS

Contributors:

* Vikas Omer | Amazon Web Services | [Linkedin](https://www.linkedin.com/in/vikas-omer/)
* Aneesh Chandra PN | Amazon Web Services | [Linkedin](https://www.linkedin.com/in/aneesh-chandra-pn/)

* Chatchai Komrangded | Amazon Web Services | [Linkedin](https://www.linkedin.com/in/chatchaikomrangded/)

![Architecture Diagram](../img/transform_glue_studio.png)

# Pre-requisites:  
Complete the previous modules   
* Ingest and Storage [link](../modules/ingest.md)
* Catalog Data [link](../modules/catalog.md)

# Transform Data with AWS Glue Studio

## What is AWS Glue Studio?
AWS Glue Studio is a new graphical interface that makes it easy to create, run, and monitor extract, transform, and load (ETL) jobs in AWS Glue. You can visually compose data transformation workflows and seamlessly run them on AWS Glue’s Apache Spark-based serverless ETL engine.

In this lab, We will do the same ETL process like [Transform Data with AWS Glue](../modules/transform_glue.md)

But This time We will leverage visual graphical interface in AWS Glue Studio!

## Learning outcomes from this workshop?
Use AWS Glue Data Studio, a graphical interface that makes it easy to create, run, and monitor extract, transform, and load (ETL) jobs in AWS Glue.

---
* Go to : https://console.aws.amazon.com/gluestudio/home?region=us-east-1
  * Click - **hamburger** icon in the left to expand menu

  ![Glue Studio](../img/glue_studio_0.png)
  
  * Click - **Jobs** and choose **Blank graph**

  * Click **Create**

![Glue Studio](../img/glue_studio_1.png)

* Click - **Source** and choose - **S3**

![Glue Studio](../img/glue_studio_2.png)

  * Click tab **Data source properties - S3** in configuration window on right side of the screen.
  * Under **S3 source type** choose **Data Catalog table** 
  * Select following values
      * Database - **analyticsworkshopdb**
      * Table - **raw**
  
![Glue Studio](../img/glue_studio_3.png)

* Now lets repeat same steps to add reference_data from S3. Click - **Source** and choose - **S3**

![Glue Studio](../img/glue_studio_2.png)

* Click tab **Data source properties - S3** in configuration window on right side of the screen.
* Under **S3 source type** choose **Data Catalog table** 
* Select following values
    * Database - **analyticsworkshopdb**
    * Table - **reference_data**
  
![Glue Studio](../img/glue_studio_4.png)

* Click any node on canvas i.e. any of the two S3 nodes

![Glue Studio](../img/glue_studio_5.png)

* Click **Transform** and choose **Join**

![Glue Studio](../img/glue_studio_6.png)

* You should get the visual diagram like in the screenshot below, and message on the right "Insufficient source nodes" because you need another node (Data source) to join

![Glue Studio](../img/glue_studio_7.png)

* Next, click on **Transform - Join** node and on **Node properties** on the right configuration window, select dropdown list and check all S3 data source as depicted in the screenshot below:
  
  ![Glue Studio](../img/glue_studio_8.png)

  - Click **Transform** tab with Join Node selected on the canvas
  
  - Click **Add condition**

  - Choose **track_id** column as join column as shown in the screenshot below.

![Glue Studio](../img/glue_studio_9.png)

* With **Join** node selected on canvas, click **Transform** and choose **ApplyMapping**

![Glue Studio](../img/glue_studio_10.png)

* You should get visual diagram like in the screenshot below

![Glue Studio](../img/glue_studio_11.png)

* We will drop unused columns and map new data type for following columns:
    * drop Columns
      * .track_id
      * parition_0
      * parition_1
      * parition_2
      * parition_3
    * Map New Data Type  
      * track_id **string** 

* Your selections should match the screenshot below   
  
![Glue Studio](../img/glue_studio_12.png)

* Click **Transform - ApplyMapping** node on the canvas
  
![Glue Studio](../img/glue_studio_13.png)

* Click **Target** and choose **S3** as shown in the screenshot below
  
![Glue Studio](../img/glue_studio_14.png)

* In **Data target properties - S3**, provide inputs as following:
    * Format: **Glue Parquet**
    * Compression Type: **Snappy**
    * S3 Target Location: **s3://yourname-analytics-workshop-bucket/data/processed-data2/**
    * Data Catalog update options
      * Choose **Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions**
    * Database: **analyticsworkshopdb**
    * Table name: **processed-data2**

![Glue Studio](../img/glue_studio_15.png)

* Click **Job details** and configure with following options
   * Name: **AnalyticsOnAWS-GlueStudio**
   * IAM Role: **AWSGlueServiceRoleDefault**
   * Number of workers: **2**
   * Job bookmark: **Disable**
   * Number of retries: **1**
   * Job timeout (minutes): **10**
   * Leave the rest as default value
   * Click **Save**
   
![Glue Studio](../img/glue_studio_16.png)

![Glue Studio](../img/glue_studio_16_2.png)

* Click **Save** and you should see **"Successfully created job"**. Start this ETL job by clicking **Run** on upper right hand corner of the screen.
   
![Glue Studio](../img/glue_studio_17.png)

* You should see **"Successfully started job"**. Click on **Run Details** to monitor your ETL job.
   
![Glue Studio](../img/glue_studio_18.png)

* Wait for a few seconds and you should see your ETL job Run Status **"Succeeded"** as shown in the screenshot below.

![Glue Studio](../img/glue_studio_19.png)

* You can see the Pyspark Code that Glue Studio has generated and reuse this code for other purposes, if needed.

![Glue Studio](../img/glue_studio_20.png)

* Go to Glue DataCatalog: https://console.aws.amazon.com/glue/home?region=us-east-1# and you should see **processed-data2** table created under **analyticsworkshopdb** database.

* **Well Done!!** You have finished an extra ETL lab with AWS Glue Studio. With AWS Glue Studio, you can visually compose data transformation workflows and seamlessly run them on AWS Glue’s Apache Spark-based serverless ETL engine.

* Bonus Knowledge, you can use AWS Glue Studio to get data from 3rd party data source from AWS Marketplace. For example, **AWS Glue Connector for Google BigQuery**. Read more about AWS Glue Connector for Google BigQuery here: https://aws.amazon.com/blogs/big-data/migrating-data-from-google-bigquery-to-amazon-s3-using-aws-glue-custom-connectors/

* To explore available connectors in AWS Glue Studio console, click **Marketplace**.

![Glue Studio](../img/glue_studio_22.png)


	
> Back to [main page](../readme.md)

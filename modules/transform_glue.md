# Workshop: Analytics on AWS

Contributors:

* Vikas Omer | Amazon Web Services | [LinkedIn](https://www.linkedin.com/in/vikas-omer/)
* Aneesh Chandra PN | Amazon Web Services | [LinkedIn](https://www.linkedin.com/in/aneesh-chandra-pn/)

![Architecture Diagram](../img/transform.png)

# Pre-requisites:  
Complete the previous modules:
* Ingest and Storage [link](../modules/ingest.md)
* Catalog Data [link](../modules/catalog.md)

# Transform Data

## Create Glue Development Endpoint
In this step you will be creating aa AWS Glue Dev Endpoint to interactively develop Glue ETL scripts using PySpark.

* Go to: https://console.aws.amazon.com/glue/home?region=us-east-1#etl:tab=devEndpoints
* Click **Add endpoint**
  * Development endpoint name: **analyticsDemoEndpoint1**
    * IAM role **AnalyticsDemoGlueRole**
    * Expand **Security configuration.. parameters**
      * Data processing units (DPUs): **2** (this reduces the cost of the running this lab)
  * Optionally add Tags, e.g.:
    * Demo: AnalyticsOnAWS
  * Click **Next**
  * Networking screen:
    * Choose **Skip networking information**
  * SSH public key:
    * Leave as defaults
    * Click **Next**
  * Review the settings
    * Click **Finish**

It will take up to 10 minutes for the new Glue console to spin up.

You have to wait for this step to complete before moving to next step.

## Create SageMaker Notebooks (Jupyter) for Glue Dev Endpoints

* Go to: https://console.aws.amazon.com/glue/home?region=us-east-1#etl:tab=notebooks
* Select tab: **Sagemaker notebooks**
* Click **Create notebook**
  * Notebook name: **AnalyticsDemoNotebook**
  * Attach to development endpoint: **analyticsDemoEndpoint1**
  * Choose: **Create an IAM role**
  * IAM Role: **AnalyticsDemoNotebookRole**
  * VPC (optional): **Leave blank**
  * Encryption key (optional): **Leave blank**
  * Optionally add Tags, e.g.:
    * Demo: AnalyticsOnAWS
  * Click **Create Notebook**

This will take few minutes: wait for this to finish

## Launch Jupyter Notebook
- Download and save this file locally on your laptop : [analytics-demo-notebook.ipynb](../analytics-demo-notebook.ipynb)
- Go to: https://console.aws.amazon.com/glue/home?region=us-east-1#etl:tab=notebooks
- Click **aws-glue-AnalyticsDemoNotebook**
- Click **Open**: this will open a new tab
- On Sagemaker Jupyter Notebook 
  - Click **Upload** (right top part of screen)
  - Browse and upload **analytics-demo-notebook.ipynb** which you downloaded earlier
  - Click **Upload** to confirm the download
  - Click on **analytics-demo-notebook.ipynb** to open the notebook
  - Make sure it says **'Sparkmagic (PySpark)'** on top right part of the notebook; this is the name of the kernel Jupyter will use to execute code blocks in this notebook

**Follow the instructions on the notebook**
- Read and understand the instructions as they explain important Glue concepts

## Validate - Transformed / Processed data has arrived in S3

Once the ETL script has ran successfully, return to the console: https://s3.console.aws.amazon.com/s3/home?region=us-east-1

* Click - **yourname-analytics-demo-bucket > data**
* Open the **processed-data** folder:
    * Ensure that `.parquet` files have been created in this folder.

Back to [main page](../readme.md)
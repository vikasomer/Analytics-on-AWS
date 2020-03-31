# Workshop: Analytics on AWS

Contributors:

* Vikas Omer | Amazon Web Services | [LinkedIn](https://www.linkedin.com/in/vikas-omer/)
* Aneesh Chandra PN | Amazon Web Services | [LinkedIn](https://www.linkedin.com/in/aneesh-chandra-pn/)


# Clean Up

Failing to do this will result in incurring AWS usage charges.

Make sure you bring down / delete all resources created as part of this lab

## Resources to delete
* Kinesis Firehose Delivery Stream
	* Go to: https://console.aws.amazon.com/firehose/home?region=us-east-1#/
	* Delete Firehose:  **analytics-demo-stream**
	
* Lambda
	* Go to: https://console.aws.amazon.com/lambda/home?region=us-east-1
	* Navigate to list of functions and select **AnalyticsDemo_top5Songs**.
	* Under **Actions** drop down menu, select **Delete**.
	
* Glue Database
	* Go to: https://console.aws.amazon.com/glue/home?region=us-east-1#catalog:tab=databases
	* Delete Database: **analyticsdemodb**
	
* Glue Crawler
	* Go to: https://console.aws.amazon.com/glue/home?region=us-east-1#catalog:tab=crawlers
	* Delete Crawler: **AnalyticsDemoCrawler**
	
* Glue Dev Endpoints
	* Go to: https://console.aws.amazon.com/glue/home?region=us-east-1#etl:tab=devEndpoints
	* Delete endpoint: **analyticsDemoEndpoint1**
	* Delete endpoint: **analyticsDemoEndpoint2**
	
* Sagemaker Notebook
	* You may wish you download the notebooks file locally on your laptop before deleting the notebook
	* Go to: https://console.aws.amazon.com/glue/home?region=us-east-1#etl:tab=notebooks
	* Stop and then Delete Notebook: **aws-glue-AnalyticsDemoRedshiftNotebook**
	* Stop and then Delete Notebook: **aws-glue-AnalyticsDemoNotebook**
	
* Delete Glue connection
	* Go to: https://us-east-1.console.aws.amazon.com/glue/home?region=us-east-1#catalog:tab=connections
	* Select **analytics_demo**
	* From **Actions** select **Delete Connection**
	* Click **Delete**
	
* Delete IAM Role
	* Go to: https://console.aws.amazon.com/iam/home?region=us-east-1#/roles
	* Search for AnalyticsDemoGlueRole
	* Delete Role: **AnalyticsDemoGlueRole**
	* Delete Role: **AnalyticsDemo_RedshiftRole**
	* Search for AnalyticsDemo_top5Songs in search box 
	* Select and delete this role. [**AnalyticsDemo_top5Songs-role-<id>**]
	
* Delete Redshift cluster
  * Go to: https://console.aws.amazon.com/redshiftv2/home?region=us-east-1
  * Select **redshift-cluster-1**
  * From **Actions** menu, select **Delete**. 
  * Uncheck **Create final snapshot**
  * Click **Delete**

* Delete S3 Gateway Endpoint
  * Go to: https://console.aws.amazon.com/vpc/home?region=us-east-1#Endpoints:sort=vpcEndpointId
  * Select **RedshiftS3EP**
  * From **Actions** select **Delete Endpoint**

* Revert Security Group rules
  * Go to: https://console.aws.amazon.com/vpc/home?region=us-east-1#SecurityGroups:sort=tag:Name
  * For the `default` security group:
      * Click on **Inbound Rules**
        * Click **Edit Rules**
        * Delete the row with S3 prefix list ID
        * Click **Save rules**
      * Click on **Outbound rules**
        * Click **Edit Rules**
        * Delete the self-referencing All TCP rule. 
        * Click **Save rules**

* Delete S3 bucket
	* Go to: https://s3.console.aws.amazon.com/s3/home?region=us-east-1
	* Delete Bucket: **yourname-analytics-demo-bucket**
	    * You may need to first **Empty** the bucket as prompted
	    * Once emptied, proceed to **Delete** the bucket
	
* Delete the Cognito CloudFormation Stack
	* Go to: https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/
	* Click: **Kinesis-Data-Generator-Cognito-User**
	* Click: **Actions** > **DeleteStack**
	* On confirmation screen: 
	    * Click **Delete**
	
* Close QuickSight account
	* Go to: https://us-east-1.quicksight.aws.amazon.com/en/admin#permissions
	* Click: **Unsubscribe**
	
* Cognito Userpool
	* Go to: https://us-west-2.console.aws.amazon.com/cognito/users/
	* Click **Kinesis Data-Generator Users**
	* Click **Delete Pool**


Back to [main page](../readme.md)
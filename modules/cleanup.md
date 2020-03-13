# Workshop: Analytics on AWS

Contributors:

* Vikas Omer | Amazon Web Services | [Linkedin](https://www.linkedin.com/in/vikas-omer/)
* Aneesh Chandra PN | Amazon Web Services | [Linkedin](https://www.linkedin.com/in/aneesh-chandra-pn/)


# Clean Up

Failing to do this will result in incuring AWS usage charges.

Make sure you bring down / delete all resources created as part of this lab

## Resources to delete
* Kinesis Firehose Delivery Stream
	* GoTo: https://console.aws.amazon.com/firehose/home?region=us-east-1#/
	* Delete Firehose:  **sg-summit-demo-stream**
	
* Lambda
	* GoTo: https://console.aws.amazon.com/lambda/home?region=us-east-1
	* Navigate to list of functions and select **top5Songs**.
	* Under **Actions** drop down menu, select **Delete**.
	
* Glue Database
	* GoTo: https://console.aws.amazon.com/glue/home?region=us-east-1#catalog:tab=databases
	* Delete Database: **summitdb**
	
* Glue Crawler
	* GoTo: https://console.aws.amazon.com/glue/home?region=us-east-1#catalog:tab=crawlers
	* Delete Crawler: **summitcrawler**
	
* Glue Dev Endpoint
	* GoTo: https://console.aws.amazon.com/glue/home?region=us-east-1#etl:tab=devEndpoints
	* Delete endpoint: **devendpoint1**
	* Delete endpoint: **Redshift-Lab**
	
* Sagemaker Notebook
	* You may wish you download the notebooks file locally on your laptop before deleting the notebook
	* GoTo: https://console.aws.amazon.com/glue/home?region=us-east-1#etl:tab=notebooks
	* Stop and then Delete Notebook: **aws-glue-notebook1**
	* Stop and then Delete Notebook: **redshfit-notebook**
	
* Delete Glue connection
	
	* GoTo: https://us-east-1.console.aws.amazon.com/glue/home?region=us-east-1#catalog:tab=connections
	* Select **redshift_lab**
	* From **Actions** select **Delete Connection**
	* Click **Delete**
	
* Delete IAM Role
	
	* GoTo: https://console.aws.amazon.com/iam/home?region=us-east-1#/roles
	* Search for AWSGlueServiceRoleDefault
	* Delete Role: **AWSGlueServiceRoleDefault**
	* Delete Role: **RedshiftLabRole**
	* Search for top5Songs in search box 
	* Select and delete this role. [**top5Songs-role-<id>**]
	
* Delete Redshift cluster

  * GoTo: https://console.aws.amazon.com/redshiftv2/home?region=us-east-1

  * Select **redshift-cluster-1**

  * From **Actions** menu, select **Delete**. 

  * Uncheck **Create final snapshot**

  * Click **Delete**

    *It will take around 5 mins to delete the cluster.*

* Delete S3 Gateway Endpoint

  * GoTo : https://console.aws.amazon.com/vpc/home?region=us-east-1#Endpoints:sort=vpcEndpointId
  * Select **RedshiftS3EP**
  * From **Actions** select **Delete Endpoint**

* Revert Security Group rules

  * GoTo : https://console.aws.amazon.com/vpc/home?region=us-east-1#SecurityGroups:sort=tag:Name
  * Click on **Inbound Rules**
    * Click **Edit Rules**
    * Delete the row with S3 prefix list ID
    * Click **Save rules**
  * Click on **Outbound rules**
    * Click **Edit Rules**
    * Delete the self-referencing All TCP rule. 
    *  Click **Save rules**

* Delete S3 bucket
	* GoTo: https://s3.console.aws.amazon.com/s3/home?region=us-east-1
	* Delete Bucket: **yourname-datalake-demo-bucket**
	
* Delete Cognito Setup :
	* Goto: https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/
	* Click: **Kinesis-Data-Generator-Cognito-User**
	* Click: **Actions** > **DeleteStack**
	* On confirmation screen: Click: **Delete**
	
* Close QuickSight account
	* GoTo: https://us-east-1.quicksight.aws.amazon.com/sn/admin#permissions
	* Click: **Unsubscribe**
	
* Cognito Userpool
	
	* GoTo: https://us-west-2.console.aws.amazon.com/cognito/users/?region=us-west-2#/


> Back to [main page](../readme.md)
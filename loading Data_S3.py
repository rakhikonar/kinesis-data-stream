import logging
import boto3
from botocore.exceptions import ClientError
import requests
import boto3
import json
import botocore
from pymongo import MongoClient
import requests
import json
import pandas as pd



AWSACCESSKEY="***********************"
AWSSECRETKEY="****************************************"
AWSTOKEN="FwoGZXIvYXdzEHgaDPdwEH+6BstDoTBtQSLDAaBRi9N8pXJpOiFDBSZWyYnalRYg94JJ42a60Hc/raKhBNq4ge7sEcMA0ua37jkcVUBzmDiPP2fml3lfKeVEEsq7oFl9spUKbAi3kSuMZeuSGxeJcCY6vgH9ngW+h+glpRWgIhNk741al9WxNQjDj6QPZN/oDz+PV4/GPUpAiyWh+NjJWMNLRwB48kJ0jg8nx6wmblav+3xTqBqeCNnxNBjQfCNJi8TTE+gYlBbgn3i72505E9eps9bL4MKtg4GO9T+CYijB9dj0BTItyXoi/OfjAUSFSFuJPRjInBDPBTziA/OEn7tdhtxZePJgRf5ZP/0DgUuW8Do+"



# Loading the processed file into s3 bucket

session = boto3.Session(profile_name='default')

def upload_to_aws(product, bucket, s3_file):
    s3 = boto3.client("s3",aws_access_key_id=AWSACCESSKEY, aws_secret_access_key=AWSSECRETKEY, 
                      aws_session_token=AWSTOKEN, region_name='us-east-1')


    try:
        s3.upload_file(product, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

uploaded = upload_to_aws('product', 'aws.storage.project', 'product_processed_file')

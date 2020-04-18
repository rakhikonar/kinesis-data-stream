# kinesis-data-stream
kinesis data stream

import requests
import boto3
import json
import botocore
from pymongo import MongoClient
import requests
import json
import pandas as pd



AWSACCESSKEY="A***************"
AWSSECRETKEY="*******************"
AWSTOKEN="FwoGZXIvYXdzEEQaDH6nKPMu+l9tUgBk4SLDAezzp9Oc+p9TqHL1BEg9z3YbC0iR/0lrAbSap36GnHSUvDbwLTNAhT0COZmqAlNLAA8eXr5YePe3rxTXl5ZUtFytpslyHxy+JBRleCvh/4H9uqGrto+/bV2nQ/7TplDCEXpLY41Ws11yf84pgi3rfQfAZaZlN5axMRtaqqZ9PZM0s5P8y0u3xrfHotqqmztCu2QPQXCBLliGPW0f6QLW1M5Kz9h2QgWdF0/hMeCK7SsB3qGM+dkHGLfNVgYrco5vV5PTkyiau830BTIt6938ly6DHoAScjvMc21pNBI8LWhKMsbfav7mI+O6rXjTN+I2XEjtYaBVGgb8"

session = boto3.Session(profile_name='default')

# Taking the json file from s3 bucket

s3 = boto3.client("s3",aws_access_key_id=AWSACCESSKEY, aws_secret_access_key=AWSSECRETKEY, aws_session_token=AWSTOKEN, region_name='us-east-1')
#bucket = s3.Bucket('aws.project')
object = s3.get_object(Bucket='aws.storage.project',Key='bestbuy.json')
serializedObject = object['Body'].read().decode('utf-8')
file_data = json.loads(serializedObject)
#print(file_data)


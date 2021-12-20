import boto3
from dotenv import load_dotenv
import os

class NexradS3:

    load_dotenv('.env')

    def __init__(self):
        self.resource_name = 'noaa-nexrad-level2' 
        access_key = os.getenv('AWS_ACCESS_KEY_ID')
        secret_key = os.getenv('AWS_SECRET_KEY_ID')
        self.s3_resource = boto3.resource(    
                    's3',
                    aws_access_key_id = access_key,
                    aws_secret_access_key = secret_key)
        self.s3_bucket = self.s3_resource.Bucket(self.resource_name)

    def get_bucket(self):
        return self.s3_bucket

    def get_resource(self):
        return self.s3_resource

    def get_bucket_name(self):
        return self.resource_name

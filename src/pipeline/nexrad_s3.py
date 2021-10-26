import boto3
from botocore.credentials import BotoProvider
import os


class NexradS3:

    def __init__(self, resource_name):
        self.resource_name = resource_name    
        
        session = boto3.Session()
        credentials = session.get_credentials()
        access_key = credentials.access_key
        secret_key = credentials.secret_key

        self.s3_resource = boto3.resource(    
                    's3',
                    aws_access_key_id = access_key,
                    aws_secret_access_key = secret_key)

        self.s3_bucket = self.s3_resource.Bucket(resource_name)

    def get_bucket(self):
        return self.s3_bucket

    def get_resource(self):
        return self.s3_resource

    def get_bucket_name(self):
        return self.resource_name


import nexrad_s3 as ns3
import boto3
import os
import random
import numpy
import json

conn = ns3.NexradS3('noaa-nexrad-level2')

def get_scan(conn, year, month, day, time, station):
    resource = conn.get_resource()
    key = f'{year}/{month}/{day}/{station}/{station}{year}{month}{day}_{time}.gz'

    obj = resource.Object(conn.get_bucket_name(), key)
   
        
        




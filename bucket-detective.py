import boto3
import logging
from botocore.exceptions import ClientError
import argparse
import json

parser = argparse.ArgumentParser(description='BucketHead Demo.', fromfile_prefix_chars='@')
parser.add_argument('-b', '--bucket',  help='enter the bucket name to scan.')

args = parser.parse_args()

bucket = args.bucket

def list_bucket():
    #s3 = boto3.resource('s3')
    
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
            return response


if __name__ == "__main__":
    list_bucket()
   
    

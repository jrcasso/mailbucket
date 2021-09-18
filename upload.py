#!/usr/local/bin/python
import boto3
import os
import sys

AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
BUCKET = os.getenv('S3_BUCKET')
ENDPOINT_URL = 'http://localstack:4566' if os.getenv('ENV') == 'dev' else None
EMAIL = sys.stdin.read()
S3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=ENDPOINT_URL,
    region_name=AWS_REGION,
)

if AWS_SECRET_ACCESS_KEY == None:
    sys.exit("Required environment variable AWS_SECRET_ACCESS_KEY has not been defined. Exiting.")
if AWS_ACCESS_KEY_ID == None:
    sys.exit("Required environment variable AWS_ACCESS_KEY_ID has not been defined. Exiting.")
if BUCKET == None:
    sys.exit("Required environment variable BUCKET has not been defined. Exiting.")

object = S3.put_object(
    Body=EMAIL,
    Bucket=BUCKET,
    Key=f'{sys.argv[1]}.eml'
)

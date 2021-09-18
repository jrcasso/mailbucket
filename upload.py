#!/usr/local/bin/python
import boto3
import os
import sys

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
BUCKET = os.getenv("S3_BUCKET")
ENDPOINT_URL = "http://localstack:4566" if os.getenv("ENV") == "dev" else None
EMAIL = sys.stdin.read()
S3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=ENDPOINT_URL,
    region_name=AWS_REGION,
)

if AWS_SECRET_ACCESS_KEY is None:
    sys.exit("Required environment AWS_SECRET_ACCESS_KEY is not defined.")
if AWS_ACCESS_KEY_ID is None:
    sys.exit("Required environment AWS_ACCESS_KEY_ID is not defined.")
if BUCKET is None:
    sys.exit("Required environment BUCKET is not defined.")

object = S3.put_object(Body=EMAIL, Bucket=BUCKET, Key=f"{sys.argv[1]}.eml")

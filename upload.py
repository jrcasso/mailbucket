#!/usr/local/bin/python

import sys

data = sys.stdin.readlines()
print("Email:", str(data))

# TODO implement simple boto3 upload to S3 via AWS environment variables

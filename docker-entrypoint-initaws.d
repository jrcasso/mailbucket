#!/bin/bash
set -x
awslocal s3 mb s3://mailbucket
awslocal s3 mb s3://mailbucket-test
set +x

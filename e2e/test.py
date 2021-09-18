import boto3
import os
import pytest
import smtplib
import time

SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = os.getenv("SMTP_PORT", 25)


class Test:
    @pytest.fixture()
    def s3_client(self):
        yield boto3.client(
            "s3",
            aws_access_key_id="test",
            aws_secret_access_key="test",
            endpoint_url="http://localstack:4566",
            region_name="us-east-1",
        )

    @pytest.fixture()
    def send_email(self):
        with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as smtp:
            smtp.noop()
            smtp.helo("foobar")
            smtp.sendmail(
                "alice@example.com", "bob@example.com", "This is a test message"
            )

    @pytest.fixture()
    def get_objects(self, s3_client):
        time.sleep(1)
        object_contents = s3_client.list_objects(Bucket="mailbucket")["Contents"]
        object_body = s3_client.get_object(
            Bucket="mailbucket", Key=object_contents[0]["Key"]
        )["Body"].read()
        yield [object_contents, str(object_body)]

    @pytest.fixture()
    def delete_objects(self, s3_client):
        print("preparing delete_objects")
        objects = s3_client.list_objects(Bucket="mailbucket")["Contents"]
        s3_client.delete_objects(
            Bucket="mailbucket",
            Delete={"Objects": list(map(lambda k: {"Key": k["Key"]}, objects))},
        )

    def test_email_upload(self, send_email, get_objects, delete_objects):
        assert len(get_objects[0]) == 1
        assert "From: alice@example.com" in get_objects[1]
        assert "foobar" in get_objects[1]
        assert "This is a test message" in get_objects[1]

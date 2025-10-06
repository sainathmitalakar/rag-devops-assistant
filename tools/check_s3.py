import os
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# AWS credentials
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET")

# Connect to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region
)

# List buckets
print(f"✅ Checking S3 connection for bucket: {bucket_name}")
buckets = s3.list_buckets()
for b in buckets["Buckets"]:
    print(f" - {b['Name']}")

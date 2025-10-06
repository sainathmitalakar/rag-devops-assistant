import os
import boto3
from dotenv import load_dotenv

# -------------------------------
# Step 1 — Load environment variables
# -------------------------------
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")

# -------------------------------
# Step 2 — Connect to S3
# -------------------------------
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# -------------------------------
# Step 3 — Upload embeddings.json
# -------------------------------
file_name = "embeddings.json"

try:
    s3.upload_file(file_name, S3_BUCKET, file_name)
    print(f"✅ Uploaded {file_name} to S3 bucket {S3_BUCKET}")
except Exception as e:
    print("❌ Failed to upload:", e)

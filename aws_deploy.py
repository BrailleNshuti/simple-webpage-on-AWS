import boto3
import botocore
import json
import os

"""
AWS credentials are NOT hard-coded.
They are provided via environment variables or IAM role.
This follows AWS security best practices.
"""

# Load region from environment
region = os.environ.get("AWS_DEFAULT_REGION", "eu-central-1").strip()



# Create S3 client with correct region
s3 = boto3.client("s3", region_name=region)

# Bucket name (must be globally unique)
bucket_name = "rusingiza-cloud-simple-webpage-2025"

# Simple HTML webpage
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Hello World - AWS</title>
</head>
<body>
    <h1>Hello World from AWS S3!</h1>
    <p>This webpage is hosted using Amazon S3.</p>
</body>
</html>
"""

# 1️⃣ Create S3 bucket (ONLY ONCE)
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": region
        }
    )
    print("Bucket created successfully.")
except botocore.exceptions.ClientError as e:
    if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
        print("Bucket already exists. Continuing.")
    else:
        raise

# 2️⃣ Upload HTML file
s3.put_object(
    Bucket=bucket_name,
    Key="index.html",
    Body=html_content,
    ContentType="text/html"
)

# 3️⃣ Output webpage URL
print("Deployment successful!")
print(f"Webpage URL:")
print(f"http://{bucket_name}.s3-website.{region}.amazonaws.com")


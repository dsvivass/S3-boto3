import boto3

s3 = boto3.resource('s3')

response = s3.buckets.all()

for bucket in response:
    print(bucket.name)
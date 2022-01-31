import boto3
from boto.s3.key import Key

s3_client = boto3.client('s3')

s3_client.delete_object(Bucket='bucket-prueba12345678987654567887678', Key='file.pdf')
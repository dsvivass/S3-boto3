import boto3

s3 = boto3.resource('s3')

bucket = s3.create_bucket(Bucket='bucket-cloud-dccad-drawing-test', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

# bucket.put_object(Key='carpeta1/subcarpeta/') # Creates a new folder in the bucket

# bucket.put_object(Key='prueba/pruebababa/pips/text.txt') # Creates a new object within the bucket
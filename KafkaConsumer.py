from kafka import KafkaConsumer
from json import loads
from s3fs import S3FileSystem
import json

#Creating the funcion to consume the data
consumer = KafkaConsumer(
    '<topic_name>',
    bootstrap_servers = ['<EC2_Public_IP>:9092'], #Add EC2 IP Here
    value_deserializer = lambda x: loads(x.decode('UTF-8')))

#Use the key and the secret from AWS
s3 = S3FileSystem(key='<aws_key_id>', secret='<aws_secret_key>')

#Storing data in real time to S3 bucket
for count, i in enumerate(consumer):
    with s3.open("s3://<s3_bucket_name>/covid_death_us_{}.json".format(count), 'w') as file: #Add Bucket Name Here
        json.dump(i.value, file)
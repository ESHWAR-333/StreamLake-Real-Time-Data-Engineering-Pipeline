import json
import boto3
from kafka import KafkaConsumer
from datetime import datetime

# Kafka Consumer
consumer = KafkaConsumer(
    'hepsiburada-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Connect to MinIO
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='admin',
    aws_secret_access_key='password123',
    region_name='us-east-1'
)

bucket_name = 'hepsiburada'

for message in consumer:
    data = message.value
    print("Received:", data)

    file_name = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.json"

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data)
    )

    print("Written to MinIO:", file_name)
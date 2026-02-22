import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open("data.json") as f:
    data = json.load(f)

for record in data:
    producer.send("hepsiburada-topic", record)

producer.flush()
print("Data sent to Kafka!")
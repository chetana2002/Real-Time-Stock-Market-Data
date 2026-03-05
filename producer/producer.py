import json
import time
import uuid
import random
from datetime import datetime
from kafka import KafkaProducer

# Kafka Configuration
KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "stock-events"

# Create Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Sample Stock Symbols
STOCK_SYMBOLS = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

def generate_stock_event():
    return {
        "event_id": str(uuid.uuid4()),
        "symbol": random.choice(STOCK_SYMBOLS),
        "price": round(random.uniform(100, 500), 2),
        "volume": random.randint(100, 5000),
        "event_time": datetime.utcnow().isoformat(),
        "market": "NASDAQ"
    }

if __name__ == "__main__":
    print("Starting Stock Producer...")
    while True:
        event = generate_stock_event()
        producer.send(TOPIC_NAME, value=event)
        producer.flush()
        print(f"Sent: {event}")
        time.sleep(1)
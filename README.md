![](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) 
![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) 
![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) 
![](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![](https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white)

# StreamLake- Real Time Data Engineering Pipeline (Kafka S3 Streaming Pipeline)

![](/images/architecture.png)

## 📌 Overview

A fully containerized, end-to-end real-time data pipeline that simulates production-grade streaming architectures. This project streams JSON data through **Apache Kafka** and persists it to **MinIO** — an S3-compatible object store — replacing traditional HDFS with modern, cloud-native storage.

> Mirrors real-world architectures used with **AWS S3**, **Google Cloud Storage**, and **Azure Blob Storage**.

---

* [docker-compose.yml](/docker-compose.yml)

* [Producer](/producer/)
    
    * [Kafka Producer](/producer/producer.py)

    * [Sample Data](/producer/data.json)

* [Consumer](/consumer/)

    * [Kafka Consumer + S3 Writer](/consumer/consumer.py)

---

## Architecture Overview


```
+------------+        +--------+        +-------------+        +--------+
|  Producer  | ──────▶| Kafka  | ──────▶|  Consumer   | ──────▶| MinIO  |
|  (Python)  |        |        |        |  (Python)   |        |  (S3)  |
+------------+        +--------+        +-------------+        +--------+
                          │
                     +----▼-----+
                     | Kafka UI |
                     | :8080    |
                     +----------+
```



**Data Flow:** Python Producer → Kafka Topic → Python Consumer → MinIO Bucket (timestamped JSON files)

---

## 🔹 Components

| Component | Role |
|-----------|------|
| **Apache Kafka** | Distributed streaming platform |
| **Zookeeper** | Kafka cluster coordination |
| **Kafka UI** | Web-based monitoring dashboard |
| **MinIO** | S3-compatible local object storage |
| **Python Producer** | Publishes JSON records to Kafka |
| **Python Consumer** | Reads from Kafka, writes to MinIO |

---

## 🛠️ Tech Stack

- **Infrastructure:** Docker & Docker Compose
- **Streaming:** Apache Kafka + Zookeeper
- **Storage:** MinIO (S3-compatible)
- **Language:** Python 3 (`kafka-python`, `boto3`)
- **Data Format:** JSON

---

## 📁 Project Structure

```
StreamLake/
│
├── docker-compose.yml          # Full infrastructure definition
│
├── producer/
│   ├── producer.py             # Kafka message publisher
│   └── data.json               # Sample data payload
│
└── consumer/
    └── consumer.py             # Kafka consumer → MinIO writer
```

---

## 🐳 Setup & Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/ESHWAR-333/StreamLake-Real-Time-Data-Engineering-Pipeline.git
cd YOUR_REPO
```

### 2. Start Infrastructure

```bash
docker compose down -v --remove-orphans   # Clean slate
docker compose up -d                       # Start all services
```

### 3. Verify Services

| Service | URL |
|---------|-----|
| Kafka UI | http://localhost:8080 |
| MinIO Console | http://localhost:9001 |

**MinIO credentials:**
```
Username: admin
Password: password123
```

### 4. Create Kafka Topic

```bash
docker exec -it kafka bash

kafka-topics --create \
  --topic hepsiburada-topic \
  --bootstrap-server kafka:29092 \
  --replication-factor 1 \
  --partitions 1

exit
```

### 5. Create MinIO Bucket

1. Open MinIO Console → http://localhost:9001
2. Log in with the credentials above
3. Create a new bucket named: `hepsiburada`

---

## 🐍 Running the Pipeline

### Install Python Dependencies

```bash
pip install kafka-python boto3
```

### Start the Producer

```bash
cd producer
python producer.py
```

Publishes JSON records to the `hepsiburada-topic` Kafka topic.

### Start the Consumer

```bash
cd consumer
python consumer.py
```

Reads messages from Kafka and writes timestamped JSON files to the MinIO bucket.

---

## 📦 Output

Each consumed message is stored as an individual JSON file in the MinIO bucket:

```
MinIO → hepsiburada/
    ├── data_20260222_142523_123456.json
    ├── data_20260222_142524_789012.json
    └── ...
```

Files are timestamped for traceability and idempotent storage.

---

## 🔥 Why MinIO Instead of HDFS?

Modern cloud data platforms have moved away from HDFS toward object storage:

| Cloud Provider | Object Storage |
|----------------|----------------|
| AWS | S3 |
| Google Cloud | Cloud Storage |
| Azure | Blob Storage |

MinIO replicates the S3 API locally, making this project:
- ✅ Cloud-native and production-relevant
- ✅ Lightweight and easy to run locally
- ✅ Compatible with Apple M1/M2 chips
- ✅ Drop-in replaceable with any S3-compatible service

---

## 🎯 What This Project Demonstrates

- Real-time streaming architecture design
- Kafka producer/consumer implementation patterns
- S3-compatible object storage integration
- Fully Dockerized infrastructure management
- End-to-end data flow from ingestion to storage
- Cloud-ready, portable architecture

---

## 🚀 Future Enhancements

- [ ] Add Spark Structured Streaming for real-time processing
- [ ] Convert JSON → Parquet for columnar storage efficiency
- [ ] Implement data partitioning (by date/category)
- [ ] Build Bronze / Silver / Gold medallion architecture
- [ ] Add Apache Airflow orchestration
- [ ] Expose a FastAPI monitoring dashboard
- [ ] Deploy on AWS EC2 with real S3
- [ ] Integrate with Snowflake for analytics

---

## 📈 Learning Outcomes

After completing this project, you will understand:

- How Kafka topics, partitions, and consumer groups work
- How streaming data flows through a real pipeline
- How object storage integrates with data engineering systems
- How to build and manage Dockerized data infrastructure
- How production data architectures are structured at scale

---

## 🧠 Author

**Eshwar**  
Data Engineer — building production-grade data systems with open-source tools.

---

*⭐ If this project helped you, consider giving it a star on GitHub and forking it to extend it further.*

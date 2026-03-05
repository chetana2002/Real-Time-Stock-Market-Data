# 🚀 Real-Time Stock Market Data Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Kafka](https://img.shields.io/badge/Apache-Kafka-black)
![Spark](https://img.shields.io/badge/Apache-Spark-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

A **real-time data engineering project** that simulates stock market streaming data using **Apache Kafka**, processes it using **Apache Spark Structured Streaming**, stores it in **PostgreSQL**, and visualizes insights through an **interactive Streamlit dashboard**.

---

# 📌 Project Overview

This project demonstrates a **modern real-time data pipeline architecture** similar to those used in financial trading and analytics platforms.

The system:

1️⃣ Generates simulated stock market events  
2️⃣ Streams data into **Kafka**  
3️⃣ Processes data using **Spark Streaming**  
4️⃣ Stores processed data in **PostgreSQL**  
5️⃣ Displays analytics in a **Streamlit Dashboard**

---

# 🏗️ System Architecture

```
Stock Producer (Python)
        │
        ▼
   Apache Kafka
        │
        ▼
Spark Structured Streaming
        │
        ▼
    PostgreSQL
        │
        ▼
  Streamlit Dashboard
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|-------------|---------|
| Python | Data producer & dashboard |
| Apache Kafka | Real-time event streaming |
| Apache Spark | Streaming data processing |
| PostgreSQL | Data storage |
| Streamlit | Data visualization |
| Docker | Containerization |

---

# 📂 Project Structure

```
RealTime-Stock-Data
│
├── producer
│   └── producer.py
│
├── spark
│   └── spark_stream.py
│
├── dashboard
│   └── app.py
│
├── docker
│   └── docker-compose.yml
│
├── requirements.txt
│
└── README.md
```

---

# 📡 Data Pipeline Flow

### 1️⃣ Producer

Simulates real-time stock events such as:

- Stock Symbol
- Price
- Volume
- Timestamp

Example Event:

```json
{
  "symbol": "AAPL",
  "price": 187.23,
  "volume": 120,
  "event_time": "2026-03-04T10:32:14"
}
```

---

### 2️⃣ Kafka Streaming

Kafka receives and stores the incoming events in the topic:

```
stock-events
```

---

### 3️⃣ Spark Processing

Spark Structured Streaming:

- Reads events from Kafka
- Parses JSON data
- Performs transformations
- Writes results to PostgreSQL

---

### 4️⃣ Data Storage

Processed data is stored in PostgreSQL table:

```
stock_events
```

---

### 5️⃣ Dashboard

The **Streamlit dashboard** provides:

📊 Real-time stock price trends  
📦 Trading volume analytics  
📈 Market insights  
📋 Latest trades table  

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/RealTime-Stock-Data.git

cd RealTime-Stock-Data
```

---

# 📦 Install Dependencies

```
pip install -r requirements.txt
```

---

# 🐳 Start Docker Services

```
docker-compose up -d
```

This starts:

- Kafka
- Spark
- PostgreSQL

---

# ▶️ Run the Producer

```
python producer/producer.py
```

---

# ⚡ Run Spark Streaming Job

```
spark-submit spark/spark_stream.py
```

---

# 📊 Launch Dashboard

```
streamlit run dashboard/app.py
```

Open browser:

```
http://localhost:8501
```

---


# 💡 Key Features

✔ Real-time event streaming  
✔ Distributed data processing  
✔ Scalable architecture  
✔ Interactive analytics dashboard  
✔ Containerized infrastructure  

---

# 📈 Skills Demonstrated

This project highlights **data engineering skills** including:

- Real-time data pipelines
- Streaming architectures
- Distributed processing
- Data visualization
- Docker containerization

---

# 🔮 Future Improvements

- Add **Apache Airflow orchestration**
- Implement **Kafka partitions**
- Deploy to **AWS / GCP**
- Add **machine learning for stock prediction**

---

# 👩‍💻 Author

**Chetana Dharavathu**

---

# ⭐ If you like this project

Please **star the repository** ⭐

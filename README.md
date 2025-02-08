# Buzzline Kafka Consumer Project

## Overview

This project is a Kafka-based data pipeline that processes and visualizes real-time streaming data. The pipeline includes a Kafka producer, a custom Kafka consumer, and a visualization dashboard.

The custom Kafka consumer reads messages from the Kafka topic, processes the data to extract attributes like sentiment, message_length and keyword mentioned, and stores the data in an SQLite database (buzz,sqlite). This setup supports real-time data processing and analysis.

### Key Features:
- **Producer**: Sends JSON messages to the Kafka topic `buzzline`.
- **Consumer**: Reads messages from the Kafka topic, processes them and stores them in an SQLite database.
- **Visualization**: Provides a dashboard for analyzing the processed data.

### Prerequisites
- Python 3.11 or later
- Kafka and Zookeeper installed and running
- `kafka-python` and `sqlite3` libraries
- Other required Python packages (see `requirements.txt`)

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/drodmay1/buzzline-05-davidrm

2. **Create a Virtual Environment**:
   ```python -m venv .venv
   source .venv/bin/activate

3. **Install Dependencies**:
```
pip install -r requirements.txt`
```
4. **Start Kafka and Zookeeper**:
- Start Zookeeper
```
./bin/zookeeper-server-start.sh config/zookeeper.properties`
```

- Start Kafka
```
./bin/kafka-server-start.sh config/server.properties`
```

5. **Create the Kafka Topic**:
```
./bin/kafka-topics.sh --create --topic buzzline --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
```

### Custom Kafka Consumer
The custom Kafka consumer:

* Reads messages from the buzzline Kafka topic.
* Processes and enriches data to extract:
  - sentiment
  - message_length
  - keyword_mentioned
  - Stores the processed data in an SQLite database (buzz.sqlite).
  - Handles errors gracefully and ensures Kafka services and topics are available before consumption.

### Visualization
The processed data is visualized using matplotlib in the dashboard_visualization.py script. This dashboard includes:
  - Sentiment score distribution.
  - Message length distribution.
  - Keyword mentions.
  - Sentiment trend over time.

### Running the project
1. **Run the producer**
```
python producers/kafka_producer.py
```

2. **Run the consumer**
```
python consumers/kafka_consumer_davidrm.py
```

3. **Run the Viualization Dashboard**
```
python consumers/dashboard_visualization.py
```

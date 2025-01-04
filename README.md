## Streaming Data Pipeline with Apache Kafka on AWS EC2
This project demonstrates the implementation of a real-time Streaming Data Pipeline using Apache Kafka deployed on an AWS EC2 instance. It showcases how to process streaming data from a CSV file and store it in an AWS S3 Bucket for scalable and reliable data handling.

![streaming_Architecture](https://github.com/user-attachments/assets/fd4fd145-531d-49d5-8709-39406170db36)

# Key Features:
- Data Simulation: Simulates real-time data streams using a Python script to read data incrementally from a CSV file.
- Kafka Integration: Utilizes Apache Kafka for efficient and scalable data streaming and message queuing.
- Producer: Sends simulated streaming data to Kafka topics.
- Consumer: Consumes and processes data from Kafka topics.
- AWS EC2 Deployment: Hosts Apache Kafka on an AWS EC2 instance to ensure flexibility and scalability.
- AWS S3 Storage: Processes and stores the streamed data into an S3 Bucket for long-term storage and analysis.
# Architecture Overview:
- Data Source: A CSV file serves as the initial source of data.
- Streaming Simulator: A Python-based solution simulates real-time streaming data.
- Kafka Cluster: Hosted on AWS EC2, Kafka manages the producer-consumer pipeline.
- S3 Bucket: Final processed data is securely stored in AWS S3 for future use.
#Use Cases:
- Real-time data processing for analytics or reporting.
- Scalable and distributed data pipelines for enterprise applications.
- Data ingestion and storage for machine learning pipelines or cloud-based workflows.
#Technologies Used:
- Apache Kafka for real-time data streaming.
- Python for data simulation and script automation.
- AWS EC2 for deploying Kafka in the cloud.
- AWS S3 for cloud storage.
#How It Works:
- The Python script streams data from the CSV file to the Kafka producer.
- The Kafka producer sends the data to a topic managed by Kafka on the EC2 instance.
- The Kafka consumer processes the data and forwards it to the S3 bucket.

# **Real-time Irrigation Monitoring Pipeline** 🌟  
This project is an end-to-end pipeline for **real-time irrigation monitoring** using **AWS services** and **Azure OpenAI**. Combining IoT, machine learning, and AI, this solution aims to revolutionize agriculture 🌱 by providing intelligent insights for efficient water usage.  

![Topic  sensor-data (13)](https://github.com/user-attachments/assets/1f7fe0e6-5801-4dc9-94d2-18f13ee640f7)
![Capture d'écran 2024-11-26 224036](https://github.com/user-attachments/assets/e3891f36-f4a2-4386-b46a-ba1056319340)

---
## **Link for demo video**  

https://www.linkedin.com/posts/nouha-ben-hamada-333898242_iot-ai-machinelearning-activity-7268588738392322048-CBPe?utm_source=share&utm_medium=member_desktop

---

## **Project Overview**  
The pipeline processes sensor data in real-time, applies machine learning models for predictions, and leverages advanced AI for data interpretation. The insights are visualized on a dashboard for actionable decision-making.  

### **Key Features**:  
- **IoT Data Integration**: Collects data from sensors.  
- **Real-Time Processing**: Utilizes Kafka and AWS Kinesis for seamless data streaming.  
- **Machine Learning**: Employs Amazon SageMaker for training and predictions.  
- **AI-Powered Insights**: Azure OpenAI's GPT-3.5 Turbo provides meaningful interpretations.  
- **Data Visualization**: Grafana displays real-time dashboards powered by Athena queries.  

---

## **Pipeline Workflow**  

1. **Sensor Data Generation**:  
   - Simulated sensor data is generated using a Python script and sent to a Kafka consumer.  

2. **Kafka Stream**:  
   - Sensor data enters a Kafka topic and is forwarded to a Kafka producer.  

3. **Amazon Kinesis Data Stream**:  
   - Kafka producer sends the data to Amazon Kinesis for streaming into the pipeline.  

4. **AWS Lambda Function**:  
   - **Trigger**: The Lambda function is triggered by the incoming data from Kinesis.  
   - **Processing**: The function applies a pre-trained machine learning model (stored in Amazon S3).  
   - **Predictions**: Predictions are saved back into Amazon S3.  

5. **Model Training** (Amazon SageMaker):  
   - Sensor data is used to train the machine learning model in Amazon SageMaker.  
   - The trained model is stored in Amazon S3.  

6. **Data Interpretation** (Azure OpenAI):  
   - Predictions saved in S3 are sent to the Azure OpenAI GPT-3.5 Turbo model.  
   - The model interprets the predictions and generates insights, which are then saved back into Amazon S3.  

7. **Data Structuring and Storage** (AWS Glue):  
   - AWS Glue crawlers organize the data into a structured table.  
   - The table is stored in AWS Glue Data Catalog.  

8. **Querying with Athena**:  
   - AWS Athena queries the structured data for analysis.  

9. **Visualization with Grafana**:  
   - NGINX hosts the Grafana web server.  
   - Grafana queries Athena and visualizes the data on interactive dashboards.  

---

## **Technologies Used**  
- **AWS Services**: Kinesis, Lambda, SageMaker, S3, Glue, Athena  
- **Azure OpenAI**: GPT-3.5 Turbo for data interpretation  
- **Kafka**: For real-time data streaming  
- **Grafana**: For dashboard visualization  
- **NGINX**: To host the web server  
- **IoT Simulated Data**: Python script to generate sensor data  

---

## **Architecture Diagram**  
The project architecture is shown below:  
![Topic  sensor-data (13)](https://github.com/user-attachments/assets/15c7a038-6b50-4ad0-969a-ac50cb4237ed)

---

## **Getting Started**  
### **Prerequisites**:  
- AWS and Azure accounts with the necessary services configured.  
- Python 3.x installed locally.  
- Kafka installed and configured.  
- Grafana and NGINX installed for dashboard visualization.  

### **Setup Steps**:  
1. **Sensor Data Generation**:  
   - Run the Python script to simulate sensor data.  

2. **Kafka Stream Configuration**:  
   - Set up Kafka consumer, topic, and producer.  

3. **AWS Kinesis Setup**:  
   - Connect Kafka producer to Amazon Kinesis.  

4. **Deploy Lambda Function**:  
   - Upload the model to S3 and set up a Lambda function triggered by Kinesis.  

5. **SageMaker Training**:  
   - Use SageMaker to train the model and save it to S3.  

6. **Azure OpenAI Integration**:  
   - Set up GPT-3.5 Turbo to interpret predictions and save insights to S3.  

7. **AWS Glue and Athena**:  
   - Use Glue crawlers to organize data into structured tables.  
   - Query the data using Athena.  

8. **Visualization Setup**:  
   - Configure NGINX to host Grafana.  
   - Connect Grafana to Athena for dashboard visualization.  

---

## **Dashboard Example**  
Here’s an example of the Grafana dashboard, showcasing real-time irrigation insights:  
![Capture d'écran 2024-11-26 224036](https://github.com/user-attachments/assets/f2873680-c106-42d8-a18e-5cc884609064)

# IOTwithAWS

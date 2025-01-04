import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps

#Creating the producer function
producer = KafkaProducer(bootstrap_servers=['<13.53.130.162>:9092'], #Add EC2 IP Here
                         value_serializer=lambda x:
                         dumps(x).encode('UTF-8'))

#Reading the csv file
df = pd.read_csv('us_deaths.csv')

#Manipulation of data as a streaming data and sending to kafka
while True:
    dict_deaths = df.sample(1).to_dict(orient="records")[0]
    producer.send('<topic_name>', value = dict_deaths)
    sleep(1)

#To clear data from kafka server, uncomment below command
#producer.flush()
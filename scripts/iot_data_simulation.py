from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

import json
import random
import time



# Initialize the IoT client to communicate with AWS IoT Core
client = AWSIoTMQTTClient("EnergySensor01")  # Unique client ID for this sensor simulation
client.configureEndpoint("your-iot-endpoint.amazonaws.com", 8883)  # Replace with your AWS IoT Core endpoint
client.configureCredentials("root-ca.pem", "private.pem.key", "certificate.pem.crt")  # Paths to AWS IoT certificates



# Connect the client to AWS IoT Core
client.connect()


# Define the topic where energy data will be published
topic = "energy/data"



# Simulate data publishing
while True:
    # Create a payload with random energy consumption data
    payload = {
        "sensor_id": "Sensor01",  # ID of the sensor
        "timestamp": time.time(),  # Current timestamp
        "energy_consumption": round(random.uniform(100, 500), 2),  # Random energy value between 100 and 500 kWh
        "status": "active"  # Sensor status
    }

    # Publish the data to the topic
    client.publish(topic, json.dumps(payload), 1)  # QoS set to 1 for delivery guarantee
    print(f"Published: {payload}")  # Log the data sent
    time.sleep(5)  # Wait for 5 seconds before sending the next data point


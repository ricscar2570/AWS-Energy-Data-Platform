from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import random
import time

client = AWSIoTMQTTClient("EnergySensor01")
client.configureEndpoint("your-iot-endpoint.amazonaws.com", 8883)
client.configureCredentials("root-ca.pem", "private.pem.key", "certificate.pem.crt")
client.connect()

topic = "energy/data"

while True:
    payload = {
        "sensor_id": "Sensor01",
        "timestamp": time.time(),
        "energy_consumption": round(random.uniform(100, 500), 2),
        "status": "active"
    }
    client.publish(topic, json.dumps(payload), 1)
    print(f"Published: {payload}")
    time.sleep(5)

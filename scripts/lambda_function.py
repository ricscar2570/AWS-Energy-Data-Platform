import boto3
import json

sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            payload = json.loads(record['body'])
            consumption = payload.get('energy_consumption', 0)
            if consumption > 400:
                sns.publish(
                    TopicArn="arn:aws:sns:your-region:your-account-id:EnergyAlerts",
                    Message=f"High energy consumption detected: {consumption} kWh",
                    Subject="Energy Alert"
                )
                print(f"Alert sent: {consumption} kWh")
    except Exception as e:
        print(f"Error processing event: {e}")
        raise

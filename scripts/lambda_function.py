import boto3
import json



# Initialize the SNS client to send notifications
sns = boto3.client('sns')

def lambda_handler(event, context):
   """ AWS Lambda function to process energy data and send alerts for high consumption.

    Parameters:
    - event: The event data passed by the trigger (e.g., Kinesis, IoT Core, etc.)
    - context: Runtime information about the Lambda function


    Raises:
    - Exception: If any error occurs during processing

    """

    try:

        # Iterate over each record in the event
        for record in event['Records']:
            # Parse the record payload
            payload = json.loads(record['body'])  # Assuming the body contains JSON data
            consumption = payload.get('energy_consumption', 0)  # Extract the energy consumption value

            # If the energy consumption exceeds 400 kWh, send an alert
            if consumption > 400:
                sns.publish(
                    TopicArn="arn:aws:sns:your-region:your-account-id:EnergyAlerts",  # Replace with your SNS Topic ARN
                    Message=f"High energy consumption detected: {consumption} kWh",  # Notification message
                    Subject="Energy Alert"  # Notification subject
                )

                print(f"Alert sent: {consumption} kWh")  # Log the alert sent

    except Exception as e:
        # Log any errors that occur
        print(f"Error processing event: {e}")
        raise

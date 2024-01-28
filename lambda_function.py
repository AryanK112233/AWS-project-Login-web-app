import json
import boto3
from datetime import datetime

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'loginapptable'  # Replace with your DynamoDB table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Retrieve username and password from the event payload
    username = event.get('username')
    password = event.get('password')

    # Get current date and time
    current_datetime = datetime.now().isoformat()

    # In a secure environment, you should use a secure storage mechanism (not in-memory) and hash passwords
    # For demonstration purposes, storing in-memory and not hashing the password
    user_data = {
        'ID': username,
        'password': password,
        'login_datetime': current_datetime
    }

    # In a real-world scenario, you should securely store and manage user data
    # Store data in DynamoDB
    response = table.put_item(Item=user_data)

    # Assume successful login for this example
    result_message = f"User '{username}' logged in successfully at {current_datetime}!"

    # Return the result as a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': result_message})
    }

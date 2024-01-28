import json

def lambda_handler(event, context):
    # Retrieve username and password from the event payload
    username = event.get('username')
    password = event.get('password')

    # In a secure environment, you should use a secure storage mechanism (not in-memory) and hash passwords
    # For demonstration purposes, storing in-memory and not hashing the password
    user_data = {
        'username': username,
        'password': password
    }

    # In a real-world scenario, you should securely store and manage user data

    # Assume successful login for this example
    result_message = f"User '{username}' logged in successfully!"

    # Return the result as a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': result_message})
    }

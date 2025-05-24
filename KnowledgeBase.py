import boto3
import json

# Initialize the Bedrock client
client = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1',  # adjust as needed
    aws_access_key_id='AKIAROFCQCAMQO4BYUMO',
    aws_secret_access_key='QzgWgwlVkCd6PE0X7xAFD32MlnRXuZCJzXjDUMvX'
)

# Define your prompt or query
prompt = "What is the total claim amount for policy number 521585?"

# Construct the payload
payload = {
    "prompt": prompt,
    "max_tokens": 2000,
    "temperature": 0.5
}

# Invoke the model
response = client.invoke_model(
    modelId='cohere.embed-multilingual-v3',  # e.g., 'anthropic.claude-v1'
    body=json.dumps(payload),
    contentType='application/json'
)

# Parse and print the response
print(prompt)
result = json.loads(response['body'].read())
print(result['completion'])

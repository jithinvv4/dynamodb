import boto3

session = boto3.session.Session(
    aws_access_key_id="123",
    aws_secret_access_key="123",
)

dynamodb = session.resource('dynamodb', endpoint_url="http://localhost:8000")


table_creation_resp = dynamodb.create_table(
    TableName='Student',
    KeySchema=[
        {
            'AttributeName': 'dept',
            'KeyType': 'HASH'  # Partition Key
        },
        {
            'AttributeName': 'stud_id',
            'KeyType': 'RANGE'  # Sort Key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'dept',
            'AttributeType': 'S'  # string data type
        },
        {
            'AttributeName': 'stud_id',
            'AttributeType': 'S'  # string data type
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print(table_creation_resp)

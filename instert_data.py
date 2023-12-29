import boto3

session = boto3.session.Session(
    aws_access_key_id="123",
    aws_secret_access_key="123",
)

dynamodb = session.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Student')

# Example list of items to insert
items = [
    {
        'dept': 'Computer Science',
        'stud_id': '123',
        'name': 'John Doe',
        'age': 20
    },
    {
        'dept': 'Electrical Engineering',
        'stud_id': '456',
        'name': 'Jane Smith',
        'age': 22
    },
    # Add more items as needed
]

# Insert the items into the table
with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

print("Items inserted successfully.")
import boto3

session = boto3.session.Session(
    aws_access_key_id="123",
    aws_secret_access_key="123",
)

dynamodb = session.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Student')

# Specify the primary key of the item you want to delete
primary_key = {
    'dept': 'Computer Science',
    'stud_id': '123'
}

# Delete the item
table.delete_item(
    Key=primary_key
)

print("Item deleted successfully.")

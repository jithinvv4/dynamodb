import boto3

session = boto3.session.Session(
    aws_access_key_id="123",
    aws_secret_access_key="123",
)

dynamodb = session.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Student')

# Specify the primary key of the item you want to update
primary_key = {
    'dept': 'Computer Science',
    'stud_id': '123'
}

# Specify the attribute(s) to update
update_expression = 'SET age = :new_age'
expression_attribute_values = {':new_age': 21}

# Update the item
table.update_item(
    Key=primary_key,
    UpdateExpression=update_expression,
    ExpressionAttributeValues=expression_attribute_values
)

print("Item updated successfully.")

import json
import boto3
import decimal
import requests
def handler(event, context):
    for record in event['Records']:
       payload=record["body"]
       y = json.loads(payload)
       #print(str(payload))
	     response = requests.get("https://x07kfctuuh.execute-api.us-east-2.amazonaws.com/Stage")
	     x = (response.json())
	     uid = (x["vid"])
       num = (y["number"])
       dynamodb = boto3.resource('dynamodb')
       dynamoTable = dynamodb.Table('test_demo')
       dynamoTable.put_item(
          Item={
              'user_id': uid,
              'contact_number': num
              }
          )
       print("PutItem succeeded:")
print("test1")

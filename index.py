import json
import requests
y = {"name": "Swapnil"}
#print(str(payload))
print(y["name"])
response = requests.get("https://x07kfctuuh.execute-api.us-east-2.amazonaws.com/Stage")
print(response.status_code)
print(response.json())
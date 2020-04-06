import boto3
from datetime import datetime
import time
import json


session = boto3.Session(profile_name="babyowl", region_name="eu-west-3")
client = session.client('events')

detailJson={
    "amount":501,
    "account":{
        "name":"Thibaut CHARLIER",
        "address":"Rue de Neuvilles 31",
        "location":"Bievre",
        "zip":5555,
        "tel" :"0767876596"
    },
    "id": "abcd12345",
    "items":[{"id":"123456","quantity":1},{"id":"654321","quantity":2}]
}

response= client.put_events(
        Entries=[
            {
                'Time': datetime.now(),
                'Source': 'order',
                'DetailType': 'order',
                'EventBusName': 'demo',
                'Detail':json.dumps(detailJson)
            }
        ]
)
print(response)

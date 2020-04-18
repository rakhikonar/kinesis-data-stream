
import requests
import boto3
import json
import boto3

session = boto3.Session()
client = session.client('firehose',region_name='us-east-1')
DeliveryStreamName = "data_delivery"

celphones = "https://api.bestbuy.com/v1/products((categoryPath.id=pcmcat209400050001))?apiKey=qn3q3zdqzs223x2njxfv6jzx&pageSize=100&format=json"

BestBuydData = requests.get(celphones)
celphone_data = BestBuydData.json()
celphone = json.dumps(celphone_data,sort_keys=True, indent=4)

records = []
count = 1
for row in celphone_data:
        if count % 500 == 0:

            response  = client.put_record_batch(
                     DeliveryStreamName=DeliveryStreamName,
                     Records= records
            )
            print(response)
            print(len(records))
            records.clear()
        record = {
                   "Data": json.dumps(row)
        }
        records.append(record)
        count = count + 1
if len(records) > 0:
     print(len(records))
     response = client.put_record_batch(
            DeliveryStreamName=DeliveryStreamName,
            Records= records
           )
     print(response)

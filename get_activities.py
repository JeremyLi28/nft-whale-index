# Following Opensea API instructions here: https://docs.opensea.io/reference/retrieving-asset-events
import requests
import json
import sys

url = "https://api.opensea.io/api/v1/events"
querystring = {"only_opensea":"false","offset":"0","limit":"20", "account_address": str(sys.argv[1])}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
events = json.loads(response.text)
print(response.text)
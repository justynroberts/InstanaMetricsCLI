#Instana Metric CLI
import requests
import json
import os
import sys
import csv
import re


if len(sys.argv) != 6:
    print('Incorrect fields - Example - Specify queryinstana label from KubernetesNamespace WHERE entity.kubernetes.cluster.label:k8s-demo-cluster')
    sys.exit()

Attribute = sys.argv[1]
Output = sys.argv[2]
Metric = sys.argv[3]
Query = sys.argv[5]

APItoken = "{YOUR API TOKEN} from the Instana UI"
Instance = "{YOUR INSTANCE} eg. prod-customer"
Rollup = 1
WindowSize = 360000

#  SELECT label from KubernetesNamespace where query
#  SELECT count frorm KubernetesNamespace where query
def getmetrics():
    try:
        response = requests.post(
            url="https://" + Instance + ".instana.io/api/infrastructure-monitoring/metrics",
            headers={
                "Authorization": "apiToken "+APItoken,
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "timeFrame": {
                    "windowSize": WindowSize
                },
                "rollup": Rollup,
                "query": Query,
                "metrics": [
                    "cpu.user"
                ],
                "plugin": Metric
            })
        )
    except requests.exceptions.RequestException:
            print('HTTP Request failed')
    records = json.loads(response.content)
    return records

records = getmetrics()
fields = records['items']
csv =""

if Attribute=='count':
    a = len(fields)
    print (str(a))
else:
    for snapshot in fields:
        #Sometimes Labels have Friendly Names in Brackets). Using RE to get rid of
        unclean = (snapshot[Attribute])
        cleanfield = re.sub('\(.*\)','', unclean)
        print (cleanfield)
    if Output =="ascsv":
        csv = csv + cleanfield + ","
    else:
        print (cleanfield)

if Output =="ascsv":
    print (csv)
                


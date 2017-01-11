import datapackage
import io
import csv
from jsontableschema import infer

dp = datapackage.DataPackage()
dp.descriptor['name'] = 'australian-honours-statistics'
dp.descriptor['title'] = 'Statistics on the Australian Honours System'

filepath = './data/1998-2015-refined.csv'

with io.open(filepath) as stream:
    headers = stream.readline().rstrip('\n').split(',')
    values = csv.reader(stream)
    schema = infer(headers, values)
    dp.descriptor['resources'] = [
        {
            'name': 'data',
            'path': filepath,
            'schema': schema
        }
    ]

with open('datapackage.json', 'w') as f:
    f.write(dp.to_json())
import requests
from prettytable import PrettyTable
myParams = {'country':'IT'}
response = requests.get('https://www.peeringdb.com/api/ix', params=myParams)
myJSONData=response.json()['data']

myTable= PrettyTable()
myTable.field_names=['Name', 'City', 'Website']
for result in myJSONData:
    myTable.add_row([result['name'], result['city'], result['website']])

print(myTable)


import requests
import hashlib
import random

# host nel quale è in esecuzione la API demo di Learning Connections
HOST = '10.0.99.130'
PORT = 8000
URL = 'http://{H}:{P}/getToken'.format(H=HOST, P=PORT)

myHeaders = {'Content-Type': 'application/x-www-form-urlencoded',
             'Accept': 'application/json'
             }

"""

        l'utente invia tramite POST in formato x-www-form-urlencoded
        username, seed, hash = sha(seed+sha(pwd))

"""
mySeed = random.randint(100000,999999)
mySha = hashlib.sha1(b'Learning Connections').hexdigest()
myShaAgain = hashlib.sha1((str(mySeed)+str(mySha)).encode('utf-8')).hexdigest()
print('password hash: '+mySha+' sentHash '+myShaAgain)

myData = {'USERNAME':'Learning Connections',
          'SEED':mySeed,
          'HASH':  myShaAgain
          }
print("Sending POST request for getting JWT token:\n")

try:
    response = requests.post(URL, headers=myHeaders, data=myData)
    myToken = response.json()['TOKEN']
    print('Received token : \n' + myToken)

    print('Now sending a /list request for retrieving private data using token')

    URL = 'http://{H}:{P}/list'.format(H=HOST, P=PORT)
    myParams = {'token': myToken}
    response = requests.get(URL, params=myParams)
    print ('received data: ')
    print (response.json())
        
except:
    print('Error ')
    print(response)


    




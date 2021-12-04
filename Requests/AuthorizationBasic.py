
import requests

HOST = 'httpbin.org'
URL = 'https://{H}/basic-auth/Chuck%20Norris/guessme'.format(H=HOST)

myHeaders = {'Content-Type': 'application/json',
             'Accept': 'application/json'
             }

print("Sending request without authorization Basic data:\n")

try:
    response = requests.get(URL, headers=myHeaders)
    print(response.headers)
        
except:
    print('Errore nella richiesta')
    


# la sequenza 'base64Encoded' è la codifica in base64 della stringa 'Chuck Norris:guessme'
myHeaders = {'Content-Type': 'application/json',
             'Accept': 'application/json',
             'Authorization': 'Basic {base64Encoded}'.format(base64Encoded='Q2h1Y2sgTm9ycmlzOmd1ZXNzbWU=')
             }

print("\nSending request with authorization Basic data:\n")

try:
    response = requests.get(URL,headers = myHeaders)
    myJSON = response.json()
    print(myJSON)
    print(response.headers)
except:
    print('Errore nella richiesta')






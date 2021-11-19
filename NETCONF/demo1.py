from ncclient import manager
import xml.dom.minidom
import xmltodict
from pprint import pprint


print("""
Learning Connections (www.learningconnections.it)

Sample ncclient application

Retrieves usernames from Cisco DevNet host 'sandbox-iosxe-latest-1.cisco.com'

working....
""")
try:
    my_manager = manager.connect(host="sandbox-iosxe-latest-1.cisco.com", 
            username="developer",
             password="C1sco12345", 
            hostkey_verify=False)
except:
    print("unable to connect to Cisco DevNet Sandbox")
    exit()

result = my_manager.get_config(source='running')
result_pretty=xml.dom.minidom.parseString(result.xml)
users = result_pretty.getElementsByTagNameNS("http://cisco.com/ns/yang/Cisco-IOS-XE-native",'username')
for user in users:
    user_dict = xmltodict.parse( user.toxml() )
    print(user_dict['username']['name'])
	

# Script to open the PTZ Optics camera webpage and login. 
# Note all addresses and passwords are kept at default values and should be updated
# to suit your enviornment. 

import requests

# GET Request | Syntax: requests.get(url, params={key: value}, args)
#requestCamDashboard = requests.get('http://192.168.1.250') 
requestCamDashboard = requests.get('http://google.com')


# test request
print (requestCamDashboard) 
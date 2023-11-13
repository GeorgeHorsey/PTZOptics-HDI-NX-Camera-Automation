# Script to open the PTZ Optics camera webpage and login. 
# Note all addresses and passwords are kept at default values and should be updated
# to suit your enviornment. 

import requests

### Data Start ###

url = 'http://192.168.1.250/network.html' # IP address of the PTZ camera. 

siteAuthUser = 'admin'

siteAuthPass = 'admin'

setEnableStreamYes = {'rtmp1_video_en': '1'} # Key and Value to enable streaming option. (camera needs a reboot to apply this setting)

# setEnableStreamNo = {'rtmp1_video_en': '0'} # Key and Value to disable streaming option. (camera needs a reboot to apply this setting)

### Data End ###


#use the 'auth' parameter to send requests with HTTP Basic Auth:
postData = requests.post(url, data = setEnableStreamYes, auth = (siteAuthUser, siteAuthPass)) # auth = ('admin', 'admin')

print(postData.status_code)






# Archive 

# GET Request | Syntax: requests.get(url, params={key: value}, args)
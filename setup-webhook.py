from dotenv import load_dotenv
load_dotenv()

import os
from ringcentral_client import RestClient

rc = RestClient(os.getenv('RINGCENTRAL_CLIENT_ID'), os.getenv('RINGCENTRAL_CLIENT_SECRET'), os.getenv('RINGCENTRAL_SERVER_URI'))
rc.token = { 'access_token': os.getenv('RINGCENTRAL_ACCESS_TOKEN') }

r = rc.get('/restapi/v1.0/account/~/extension')
print(r.json())


# RINGCENTRAL_CLIENTID = os.getenv("RINGCENTRAL_CLIENT_ID")
# RINGCENTRAL_CLIENTSECRET = os.getenv("RINGCENTRAL_CLIENT_SECRET")
# RINGCENTRAL_SERVER = 

# RINGCENTRAL_USERNAME = '<YOUR ACCOUNT PHONE NUMBER>'
# RINGCENTRAL_PASSWORD = '<YOUR ACCOUNT PASSWORD>'
# RINGCENTRAL_EXTENSION = '<YOUR EXTENSION, PROBABLY "101">'

# DELIVERY_ADDRESS= '<https://XXXXXXXX.ngrok.io/webhookcallback>'

# rcsdk = SDK(RINGCENTRAL_CLIENTID, RINGCENTRAL_CLIENTSECRET, RINGCENTRAL_SERVER)
# platform = rcsdk.platform()
# platform.login(RINGCENTRAL_USERNAME, RINGCENTRAL_EXTENSION, RINGCENTRAL_PASSWORD)

# try:
#     eventFilters = ['/restapi/v1.0/account/~/extension/~/message-store/instant?type=SMS']
#     params = {
#         "eventFilters" : eventFilters,
#         "deliveryMode": {
#             "transportType": 'WebHook',
#             "address": DELIVERY_ADDRESS
#         }
#     }
#     res = platform.post("/subscription", params)
#     return res
# except Exception as e:
#     return e
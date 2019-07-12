from dotenv import load_dotenv
load_dotenv()

import os
from ringcentral_client import RestClient

rc = RestClient(os.getenv('RINGCENTRAL_CLIENT_ID'), os.getenv('RINGCENTRAL_CLIENT_SECRET'), os.getenv('RINGCENTRAL_SERVER_URI'))
rc.token = { 'access_token': os.getenv('RINGCENTRAL_ACCESS_TOKEN') }

r = rc.get('/restapi/v1.0/account/~/extension')
print(r.json())

# subscribe to message-store for ALL extensions
eventFilters = ['/restapi/v1.0/account/~/extension/' + str(extension['id']) + '/message-store' for extension in r.json()['records']]
print(eventFilters)

r = rc.post('/restapi/v1.0/subscription', {
    "eventFilters" : eventFilters,
    "deliveryMode": {
        "transportType": 'WebHook',
        "address": os.getenv('PUBLIC_ADDRESS') + '/webhookcallback'
    }
})
print(r.json())

from dotenv import load_dotenv
load_dotenv()

import os
from ringcentral_client import RestClient

rc = RestClient(os.getenv('RINGCENTRAL_CLIENT_ID'), os.getenv('RINGCENTRAL_CLIENT_SECRET'), os.getenv('RINGCENTRAL_SERVER_URI'))
rc.token = { 'access_token': os.getenv('RINGCENTRAL_ACCESS_TOKEN') }

# r = rc.get('/restapi/v1.0/account/~/extension')
# print(r.json())

# # subscribe to message-store for ALL extensions
# eventFilters = ['/restapi/v1.0/account/~/extension/' + str(extension['id']) + '/message-store' for extension in r.json()['records']]
# print(eventFilters)

r = rc.get('/restapi/v1.0/subscription')
print(r.json())


r = rc.post('/restapi/v1.0/account/~/extension/~/sms', {
    'to': [{'phoneNumber': '16504223279'}],
    'from': {'phoneNumber': '17203861295'},
    'text': 'Hello world'})
print(r.json())

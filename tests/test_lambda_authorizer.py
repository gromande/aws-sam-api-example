import sys, requests

# Read input params
if len(sys.argv) is not 4:
    print('Missing input arguments.')
    sys.exit()

apiId = sys.argv[1]
user = sys.argv[2]
effect = sys.argv[3]

# ************* REQUEST VALUES *************
endpoint = f"https://{apiId}.execute-api.us-east-1.amazonaws.com/Prod/hello"

headers = {"TokenHeader":f"user|{user};{effect}"}

print('\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++')
print('Request URL = ' + endpoint)
print('Request Headers = ' + str(headers))
r = requests.get(endpoint, headers=headers)

print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
print('Response code: %d\n' % r.status_code)
print(r.text)

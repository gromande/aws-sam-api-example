import sys, boto3, requests

client = boto3.client('cognito-idp')

# Input variables
user_pool_id = sys.argv[1]
apiId = sys.argv[2]
client_id = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]

response = client.initiate_auth(
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': username,
        'PASSWORD': password
    },
    ClientId=client_id,
    UserContextData={
        'EncodedData': 'string'
    }
)

id_token = ''
if 'ChallengeName' in response and response['ChallengeName'] == 'NEW_PASSWORD_REQUIRED':
    session = response['Session']
    print('Found challenge')

    response = client.admin_respond_to_auth_challenge(
        UserPoolId=user_pool_id,
        ClientId=client_id,
        ChallengeName='NEW_PASSWORD_REQUIRED',
        ChallengeResponses={
            'USERNAME': username,
            'NEW_PASSWORD': password
        },
        Session=session
    )

    id_token = response['AuthenticationResult']['IdToken']
else:
    id_token = response['AuthenticationResult']['IdToken']

endpoint = f"https://{apiId}.execute-api.us-east-1.amazonaws.com/Prod/hello"

headers = {'Authorization': id_token}

print('\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++')
print('Request URL = ' + endpoint)
print('Request Headers = ' + str(headers))
r = requests.get(endpoint, headers=headers)

print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
print('Response code: %d\n' % r.status_code)
print(r.text)

def generatePolicy(effect, methodArn):
    policyDocument = {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Sid': 'FirstStatement',
                'Action': 'execute-api:Invoke',
                'Effect': effect,
                'Resource': methodArn
            }
        ]
    }
    return policyDocument


def lambda_handler(event, context):
    print("event: " + str(event))

    auth_token = event['authorizationToken']

    # Validate token and produce principalID
    principalId = auth_token.split(";")[0]
    effect = auth_token.split(";")[1]

    authResponse = {}
    authResponse['principalId'] = principalId
    authResponse['policyDocument'] = generatePolicy(effect, event['methodArn'])
    authResponse['context'] = {
        'myAttr': 'myValue'
    }
    return authResponse

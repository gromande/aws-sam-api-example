import json, boto3

KEY_NAME = 'message_id'
KEY_VALUE = 'greeting'
ATTR_NAME = 'message'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('greetingTable')

def get_lambda_handler(event, context):
    response = table.get_item(
        Key={
            KEY_NAME: KEY_VALUE
        }
    )

    message = "Hello World!"

    if 'Item' in response:
        message = response['Item'][ATTR_NAME]

    return {
        "statusCode": 200,
        "body": json.dumps({
            ATTR_NAME: message
        })
    }

def post_lambda_handler(event, context):

    response = table.get_item(
        Key={
            KEY_NAME: KEY_VALUE
        }
    )

    body = json.loads(event['body'])

    message = body[ATTR_NAME]

    if 'Item' in response:
        table.update_item(
            Key={
                KEY_NAME: KEY_VALUE
            },
            AttributeUpdates={
                ATTR_NAME: {'Value': message}
            }
        )
    else:
        table.put_item(
            Item={
                KEY_NAME: KEY_VALUE,
                ATTR_NAME: message
            }
        )

    return {
        "statusCode": 200,
        "body": json.dumps({
            ATTR_NAME: message
        })
    }
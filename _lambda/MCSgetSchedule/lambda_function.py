import boto3
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendored'))
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

patch(['boto3'])

def lambda_handler(event, context):

    test_event = boto3.client('events')
    rule_Name = os.environ['RULE_NAME']
    
    response = test_event.describe_rule(
        Name = rule_Name
    )
    print(response['ScheduleExpression'])
    
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(response)
    }
    
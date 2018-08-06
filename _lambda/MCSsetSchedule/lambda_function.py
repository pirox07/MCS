import boto3
import os
import json
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendored'))
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

patch(['boto3'])

def lambda_handler(event, context):

    print(event['queryStringParameters']['a'])
    
    hh = (event['queryStringParameters']['a'])[:2]
    mm = (event['queryStringParameters']['a'])[3:5]
    print(hh)
    print(mm)
    
    test_event = boto3.client('events')
    rule_Name = os.environ['RULE_NAME']
    
    test_event.put_rule(
        Name = rule_Name,
        ScheduleExpression = 'cron(' + mm +' ' + hh + ' * * ? *)'
    )
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': "OK!!!"
    }
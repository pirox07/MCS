import boto3
import os
import json
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendored'))
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

patch(['boto3'])

client = boto3.client('events')

def lambda_handler(event, context):

    rule_Name = 'exec_time'

    response1 = client.disable_rule(
        Name = rule_Name
    )

    info_rule = client.describe_rule(
        Name = rule_Name
    )
    
    response2 = client.put_rule(
        Name='enable_exec_time',
        ScheduleExpression = info_rule['ScheduleExpression'] ,
#        EventPattern='string',
        State='ENABLED',
#        Description='string',
#        RoleArn='string'
    )
'''    
    client.put_targets(
        Rule = 'enable_exec_time',
        Targets=[
            {
                    'Id': 'cloud9-MCSenableRule-MCSenableRule-RUQ20ZIROEFC',
                    'Arn': 'arn:aws:lambda:us-east-1:086142515727:function:cloud9-MCSenableRule-MCSenableRule-RUQ20ZIROEFC'
            }
        ]
    )
'''
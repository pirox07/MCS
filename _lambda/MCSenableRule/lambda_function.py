import boto3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendored'))
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

patch(['boto3'])

client = boto3.client('events')

def lambda_handler(event, context):

    client.enable_rule(
        Name = 'call_time'
    )

    client.disable_rule(
        Name = 'enable_call_time'
    )

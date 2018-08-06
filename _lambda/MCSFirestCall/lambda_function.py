import boto3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendored'))
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

patch(['boto3'])

def lambda_handler(intent, session):
    client = boto3.client('connect', region_name=os.environ['CONTACT_REGION'])
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber=os.environ['DST_PHONE_NUMBER'],
        ContactFlowId=os.environ['CONTACT_FLOW_ID'],
        InstanceId=os.environ['INSTANCE_ID'],
#        ClientToken='string',
        SourcePhoneNumber=os.environ['SRC_PHONE_NUMBER'],
#       QueueId='string',
#        Attributes={'string': 'string'}
    )
'''
    //たぶんAlexa用の処理
    session_attributes = {}    //たぶんAlexa用
    reprompt_text = None
    should_end_session = True
    speech_output = u'ちょっと待ってね'
'''

'''
    //返り不要？
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
'''
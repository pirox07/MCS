import boto3

def lambda_handler(intent, session):
    client = boto3.client('connect', region_name='ap-southeast-2')
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber='+819019473068',
        ContactFlowId='88a67fb7-e18b-4766-94e6-4e0bcfa766fb',
        InstanceId='65e55b10-58a8-4182-a8b1-8c4775441a61',
#        ClientToken='string',
        SourcePhoneNumber='+815032014918',
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
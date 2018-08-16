import boto3
client = boto3.client('events')

def lambda_handler(event, context):

    client.enable_rule(
        Name = 'exec_time'
    )

    client.disable_rule(
        Name = 'enable_exec_time'
    )

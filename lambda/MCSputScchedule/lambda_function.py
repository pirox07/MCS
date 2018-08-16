import boto3
import json
def lambda_handler(event, context):

    print(event['queryStringParameters']['a'])
    
    hh = (event['queryStringParameters']['a'])[:2]
    mm = (event['queryStringParameters']['a'])[3:5]
    print(hh)
    print(mm)
    
    test_event = boto3.client('events', region_name='us-east-1')
    rule_Name = 'exec_time'
    
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
def lambda_handler(event, context):
    import boto3
    import json
    
    test_event = boto3.client('events', region_name='us-east-1')
    rule_Name = 'exec_time'
    
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
    
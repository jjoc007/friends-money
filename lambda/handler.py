def lambda_handler(event, context):
    """Return a simple greeting"""
    return {"statusCode": 200, "body": "hello"}

import boto3
import json


def my_handler(event, context):
    iam = boto3.client('iam')
    path = '/'
    role_name = 'MyCustom-Cloud-Admin-Role'
    description = 'IAM ROLE CREATION'
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    tags = [
        {
            'Key': 'Owner',
            'Value': 'Navaneeth'
        }
    ]
    try:
        response = iam.create_role(
            Path=path,
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description=description,
            MaxSessionDuration=3600,
            Tags=tags
        )
        print(response)
    except Exception as e:
        print(e)


def createpolicy():
        iam = boto3.client('iam')
        my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "logs:CreateLogGroup",
                "Resource": "RESOURCE_ARN"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:DeleteItem",
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:Scan",
                    "dynamodb:UpdateItem"
                ],
                "Resource": "RESOURCE_ARN"
            }
        ]
    }
        policy = iam.create_policy(
            PolicyName='myDynamoDBPolicy',
            PolicyDocument=json.dumps(my_managed_policy)
            )
        print(policy)
def attachpolicy():
    iam = boto3.client('iam')
    response = iam.attach_role_policy(
        RoleName='MyRole', PolicyArn='<arn of managed policy>')

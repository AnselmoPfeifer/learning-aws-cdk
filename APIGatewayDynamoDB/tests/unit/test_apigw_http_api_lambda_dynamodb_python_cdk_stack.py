import aws_cdk as core
import aws_cdk.assertions as assertions
from aws_cdk.assertions import Match

from stacks.apigw_http_api_lambda_dynamodb_python_cdk_stack import ApigwHttpApiLambdaDynamodbPythonCdkStack


def test_sqs_queue_created():
    app = core.App()
    stack = ApigwHttpApiLambdaDynamodbPythonCdkStack(app, "apigw-http-api-lambda-dynamodb-python-cdk")
    template = assertions.Template.from_stack(stack)


def test_dynamodb_table_has_tags():
    app = core.App()
    stack = ApigwHttpApiLambdaDynamodbPythonCdkStack(app, "apigw-http-api-lambda-dynamodb-python-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::DynamoDB::Table", 1)

    # Check if the DynamoDB table exists with the correct tags
    template.has_resource_properties("AWS::DynamoDB::Table", {
        "Tags": Match.array_with([
            {
                "Key": "Project",
                "Value": "DevOpsChallenge"
            }
        ]),
        "KeySchema": Match.array_with([
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ]),
        "AttributeDefinitions": Match.array_with([
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
        ])
    })

def test_dynanodb_table_has_point_in_time_recovery_enabled():
    app = core.App()
    stack = ApigwHttpApiLambdaDynamodbPythonCdkStack(app, "apigw-http-api-lambda-dynamodb-python-cdk")
    template = assertions.Template.from_stack(stack)

    # Check if the DynamoDB table has point in time recovery enabled
    template.has_resource_properties("AWS::DynamoDB::Table", {
        "PointInTimeRecoverySpecification": {
            "PointInTimeRecoveryEnabled": True
        }
    })

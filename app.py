#!/usr/bin/env python3

import aws_cdk as cdk

from learning_aws_cdk.learning_aws_cdk_stack import LearningAwsCdkStack


app = cdk.App()
LearningAwsCdkStack(app, "LearningAwsCdkStack")

app.synth()

import os
import argparse
#from sagemaker import get_execution_role

#role = get_execution_role()

import sagemaker as sage
import boto3

# argument parsing
parser = argparse.ArgumentParser()


# reading parameters
parser.add_argument("--algo_img", help="Algorithm Container image name")
parser.add_argument("--role", help="Execution")
parser.add_argument("--input_path", help="S3 bucket input path")
parser.add_argument("--output_path", help="S3 bucket output path")

# parse args
args = parser.parse_args()


#role = 'arn:aws:iam::421089506438:role/service-role/AmazonSageMaker-ExecutionRole-20190709T125386'
role = args.role

client = boto3.client('sagemaker')

sess = sage.Session()
common_prefix = "customer_churn_v3"
training_input = args.input_path
#training_input = "s3://sagemaker-us-east-1-421089506438/customer_churn/training-input-data"
account = sess.boto_session.client('sts').get_caller_identity()['Account']
region = sess.boto_session.region_name
#image = '{}.dkr.ecr.{}.amazonaws.com/churn-model-v3:latest'.format(account, region)
image = '{}.dkr.ecr.{}.amazonaws.com/{}'.format(account, region, args.algo_img)

tree = sage.estimator.Estimator(image,
                       role, 1, 'ml.c4.2xlarge',
                       #output_path="s3://mafsagemaker/modeloutput",
                       output_path=args.output_path,
                       sagemaker_session=sess
                    )
tree.fit(training_input)

from sagemaker.predictor import csv_serializer

model = tree.create_model()
predictor = tree.deploy(1, 'ml.t2.medium', serializer=csv_serializer)

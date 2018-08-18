#!/bin/bash

cd `dirname $0`
#source .env

cat swagger-template.yaml | sed "s/account_placeholder/${AWS_ACCOUNT}/g" \
                          | sed "s/region_placeholder/${AWS_REGION}/g" \
                          > swagger.yaml

cat sam-base.yaml | sed "s/bucket_placeholder/${AWS_BUCKET}/g" \
                  | sed "s/role_arn_MCS-lambda/${MCS_LAMBDA_ROLE_ARN}/g" \
                  | sed "s/rule_name_placeholder/${MCS_RULE_NAME}/g" \
                  > sam-template.yaml

aws cloudformation package --template-file sam-template.yaml --output-template-file ../sam-output.yaml --s3-bucket ${AWS_BUCKET} --s3-prefix lambda

rm sam-template.yaml
rm swagger.yaml

#sam deploy --template-file ../sam-output.yaml --stack-name TGIS --capabilities CAPABILITY_IAM

#!/bin/bash

cd `dirname $0`
#source .env

cat swagger-template.yaml | sed "s/account_placeholder/${AWS_ACCOUNT}/g" \
                          | sed "s/region_placeholder/${AWS_REGION}/g" \
                          > swagger.yaml

cat sam-base.yaml | sed "s/bucket_placeholder/${AWS_BUCKET}/g" \
                  | sed "s/role_arn_MCS-lambda/${MCS_LAMBDA_ROLE_ARN}/g" \
                  | sed "s/contact_region_placeholder/${MCS_CONTACT_REGION}/g" \
                  | sed "s/dst_phone_number_placeholder/${MCS_DST_PHONE_NUMBER}/g" \
                  | sed "s/src_phone_number_placeholder/${MCS_SRC_PHONE_NUMBER}/g" \
                  | sed "s/contact_flow_id_placeholder/${MCS_CONTACT_FLOW_ID}/g" \
                  | sed "s/instance_id_placeholder/${MCS_INSTANCE_ID}/g" \
                  > sam-template.yaml

aws cloudformation package --template-file sam-template.yaml --output-template-file ../sam-output.yaml --s3-bucket ${AWS_BUCKET} --s3-prefix lambda

rm sam-template.yaml
rm swagger.yaml

#sam deploy --template-file ../sam-output.yaml --stack-name TGIS --capabilities CAPABILITY_IAM

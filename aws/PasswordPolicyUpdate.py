import os 
import json
import cfnresponse
import boto3
import logging

from botocore.exceptions import ClientError
logger = logging.getLogger()
logger.setLevel(logging.INFO)
iam = boto3.resource('iam')
ec2 = boto3.client('ec2')
account_password_policy = iam.AccountPasswordPolicy()

def handler(event, context):
  logger.info("Received event: %s" % json.dumps(event))
  result = cfnresponse.SUCCESS
  try:
    if event['RequestType'] == 'Create' or event['RequestType'] == 'Update':
      result = policy_create()
    elif event['RequestType'] == 'Delete':
      result = policy_delete()
  except ClientError as e:
    logger.error('Error: %s', e)
    result = cfnresponse.FAILED
  cfnresponse.send(event, context, result, {})

def policy_create():
  account_password_policy = iam.create_account_password_policy(
      MinimumPasswordLength=14,
      RequireSymbols=True,
      RequireNumbers=True,
      RequireUppercaseCharacters=True,
      RequireLowercaseCharacters=True,
      AllowUsersToChangePassword=True,
      MaxPasswordAge=90,
      PasswordReusePrevention=24,
      HardExpiry=True
  )
  response = ec2.enable_ebs_encryption_by_default(
    DryRun = False
  )
  return cfnresponse.SUCCESS

def policy_delete():
  response = account_password_policy.delete()
  response = ec2.disable_ebs_encryption_by_default(
    DryRun = False
  )
  return cfnresponse.SUCCESS
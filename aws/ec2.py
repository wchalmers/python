import configparser
import boto3

client = boto3.client('ec2')

config = configparser.ConfigParser()
config = configparser.ConfigParser(comment_prefixes=';', allow_no_value=True)
config.read('var.ini')

##Debug code for var file
# for each_seciton in config.sections():
#     for (each_key, each_val) in config.items(each_section):

#     print (each_key)
#     print (each_val)


def create_instance():
    ec2.client = boto3.client('ec2', region_name='eu-west-2')
    instances = ec2_client.run_instances(
            ImageId=config['Webserver']['ami'],
            MinCount=1,
            MacCount=1,
            InstanceType=config['Webserver']['keypair'],
            KeyName=config['Webserver']['keypair'],
    )

    print(instances['Instances']['0']['InstanceId'])

def get_public_ip(instance_id):
    ec2_client = boto3.client('ec2', region_name='eu-west-2')
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get('Reservations')

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get('PublicIpAddress'))
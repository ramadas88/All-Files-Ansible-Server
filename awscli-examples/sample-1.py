import boto3

client = boto3.client('ec2')

response = client.describe_instances()

for r in response['Reservations']:
  for i in r['Instances']:
    print i['InstanceId'], i['Hypervisor']
    for b in i['BlockDeviceMappings']:
      print b['Ebs']['DeleteOnTermination']


import boto3
dryRun = False; # useful variable to put the script into dry run mode where the function allows it

#ec2Client = boto3.client('ec2')
ec2Resource = boto3.resource('ec2')

# Create the instance
instanceDict = ec2Resource.create_instances(
    DryRun = dryRun,
    ImageId = "ami-f2d3638a",
    KeyName = "ansible-1",
    InstanceType = "t1.micro",
    SecurityGroupIds = ["sg-bc030ec7"],
    #SecurityGroupIds = ["YOUR_SECURITY_GROUP_ID"],
    MinCount = 1,
    MaxCount = 1
)
# Wait for it to launch before assigning the elastic IP address
instanceDict[0].wait_until_running();




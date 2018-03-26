
import boto3




client =   boto3.client('ec2')
response =  client.stop_instances(InstanceIds=["i-02b5f644acc072878"])
print type(response)
print response

for r in  response['StoppingInstances']:
	print type(r)
	print r['InstanceId'] +":" + r['CurrentState']['Name']
	# r['InstanceId']
	#for k in r['CurrentState']:

	#	print r['CurrentState']['Name']

		


#inst_state = response[0].instances[0].state 
#print inst_state
#print response['StoppingInstances']
#print type(response['StoppingInstances'])
#print response['StoppingInstances']['InstanceId']


#foundItems = (key for key, vals in (response['StoppingInstances']) if item in vals)

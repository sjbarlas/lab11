# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2
import boto

url = 'http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key'
response 
# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = "http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key"
secret_access_key = "http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key"

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Get a list of the queues that exists and then print the list out
rs = conn.get_all_queues()
for q in rs:
	print q.id

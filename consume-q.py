import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

import boto

print boto.Version
import urllib2
import argparse

url = 'http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read().split(":")
print the_page

# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = the_page[0]
secret_access_key = the_page[1]

parser = argparse.ArgumentParser()
parser.add_argument("qname")
args = parser.parse_args()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
q = conn.get_queue(args.qname)

try:
	m = Message()
	m = q.read(60)
	str1 = m.get_body()
	print "Message has been read = ", str1
except:
	print "Can't read"
print boto.Version
try:
	q.delete_message(m)
	print "Message gone"
except:
	print "Can't delete"

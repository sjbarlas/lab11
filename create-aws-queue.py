import boto.sqs
import boto.sqs.queue
import argparse
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
sys.path.append('/data')
from keys import access_key_id, secret_access_key


parser = argparse.ArgumentParser()
parser.add_argument("qname")
args = parser.parse_args()

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

try:
	q=conn.create_queue(args.qname)
	print args.qname, "Queue created"
except:
	print "Can't do"

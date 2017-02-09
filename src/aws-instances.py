#!/usr/bin/env python
#
# aws-instances.py
#
# A simple Python script that wraps the AWS CLI (https://aws.amazon.com/cli/)
# and generates a table view of instantiated EC2 instances running on AWS.
#
import json
import subprocess
import sys

# FUNCTIONS
#
#

def awsdescribe():
    """Run aws ec2 describe-instances"""
    p = subprocess.Popen(["aws", "ec2", "describe-instances"], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    return output

# MAIN
#
#
desc = {}
try:
    desc = json.loads(awsdescribe())
except ValueError as ve:
    print "Oops! Something went wrong: {}".format(ve)
    sys.exit(1)

print "{0: <15} {1: <16} {2: <16} {3: <50} {4: <45} {5: <15} {6}".format(
    'Instance Type',
    'PublicIpAddress',
    'PrivateIpAddress',
    'PublicDnsName',
    'PrivateDnsName',
    'State',
    'Tag name'
)

for reservations in desc['Reservations']:
    for instances in reservations['Instances']:
        public_ip_address = instances.get('PublicIpAddress', "-") or "-"
        private_ip_address = instances.get('PrivateIpAddress', "-") or "-"
        public_dns_name = instances.get('PublicDnsName', "-") or "-"
        private_dns_name = instances.get('PrivateDnsName', "-") or "-"

        for tags in instances['Tags']:
            key = tags['Key']
            value = tags['Value']
            if key == 'Name':
                tag_name = "{}\t".format(value)

        print "{0: <15} {1: <16} {2: <16} {3: <50} {4: <45} {5: <15} {6}".format(
            instances['InstanceType'],
            public_ip_address,
            private_ip_address,
            public_dns_name,
            private_dns_name,
            instances['State']['Name'],
            tag_name
        )

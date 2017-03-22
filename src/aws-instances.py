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
import argparse

# FUNCTIONS
#
#

def columns_layout(extended=False):
    if extended:
        return "{0: <15} {1: <16} {2: <16} {3: <50} {4: <45} {5: <15} {6}"
    else:
        return "{0: <17} {1: <42} {2: <10} {3}"

def header(extended=False):
    if extended:
        return columns_layout(extended).format(
            'Instance Type',
            'PublicIpAddress',
            'PrivateIpAddress',
            'PublicDnsName',
            'PrivateDnsName',
            'State',
            'Tag name'
        )
    else:
        return columns_layout(extended).format(
            'PrivateIpAddress',
            'PrivateDnsName',
            'State',
            'Tag name'
        )

def to_table(extended=False):
    nodes = []
    nodes.append(header(extended))

    for reservations in desc['Reservations']:
        for instances in reservations['Instances']:
            public_ip_address = instances.get('PublicIpAddress', "-") or "-"
            private_ip_address = instances.get('PrivateIpAddress', "-") or "-"
            public_dns_name = instances.get('PublicDnsName', "-") or "-"
            private_dns_name = instances.get('PrivateDnsName', "-") or "-"

            tag_name = 'UNKNOWN'
            if 'Tags' in instances.keys():
                for tags in instances['Tags']:
                    key = tags['Key']
                    value = tags['Value']
                    if key == 'Name':
                        tag_name = "{}\t".format(value)

            if extended:
                nodes.append(columns_layout(extended).format(
                    instances['InstanceType'],
                    public_ip_address,
                    private_ip_address,
                    public_dns_name,
                    private_dns_name,
                    instances['State']['Name'],
                    tag_name
                ))
            else:
                nodes.append(columns_layout(extended).format(
                    private_ip_address,
                    private_dns_name,
                    instances['State']['Name'],
                    tag_name
                ))
    return nodes


def awsdescribe():
    """Run aws ec2 describe-instances"""
    p = subprocess.Popen(["aws", "ec2", "describe-instances"], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    return output

# MAIN
#
#

cmdargs = str(sys.argv)

desc = {}
try:
    desc = json.loads(awsdescribe())
except ValueError as ve:
    print "Oops! Something went wrong: {}".format(ve)
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('-e','--extended', help='Extended output', action='store_const', const=True)
args = parser.parse_args()

for line in to_table(args.extended == True):
    print line

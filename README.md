# aws-helpers
Set of neat little AWS helper scripts.

## aws-instances

You can easily list your AWS EC2 instances with `aws-instances`.

Prerequisites:
- Python 2.7 or higher
- [awsudo](https://github.com/makethunder/awsudo) installed
- AWS configuration

Run `aws-instances`:
```bash
$ awsudo -u my-aws-user ./bin/aws-instances
Instance Type   PublicIpAddress  PrivateIpAddress PublicDnsName                                      PrivateDnsName                                State           Tag name
t2.micro        -                10.9.8.7         -                                                  ip-10-9-8-7.eu-west-1.compute.internal        running         super-service-one
t2.micro        -                10.9.8.8         -                                                  ip-10-9-8-8.eu-west-1.compute.internal        running         super-service-two
```

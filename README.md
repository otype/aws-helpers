# aws-helpers
Set of neat little AWS helper scripts.

## aws-instances

You can easily list your AWS EC2 instances with `aws-instances`.

### Prerequisites

- Python 2.7 or higher
- [awsudo](https://github.com/makethunder/awsudo) installed
- AWS configuration

### Installation

1. Clone this repository.
2. Symlink `<aws-helpers-repo>/bin/aws-instances` to your `~/bin` directory (or any other directory that is in your `$PATH`).
3. Run `awsudo -u <your_aws_user> ~/bin/aws-instances`

### Using `aws-instances`

Run `aws-instances`:
```bash
$ awsudo -u my-aws-user ${AWS_HELPERS_REPO}/bin/aws-instances
PrivateIpAddress  PrivateDnsName                             State      Tag name
10.9.8.7          ip-10-9-8-7.eu-west-1.compute.internal     running    super-service-one
10.9.8.8          ip-10-9-8-8.eu-west-1.compute.internal     running    super-service-two
```

Or use the long version via `aws-instances -e|--extended`:
```bash
$ awsudo -u my-aws-user ${AWS_HELPERS_REPO}/bin/aws-instances --extended
Instance Type   PublicIpAddress  PrivateIpAddress PublicDnsName                                      PrivateDnsName                                State           Tag name
t2.micro        -                10.9.8.7         -                                                  ip-10-9-8-7.eu-west-1.compute.internal        running         super-service-one
t2.micro        -                10.9.8.8         -                                                  ip-10-9-8-8.eu-west-1.compute.internal        running         super-service-two
```


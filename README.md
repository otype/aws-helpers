# aws-helpers
Set of neat little AWS helper scripts.

### Prerequisites

- Python 2.7 or higher
- [awsudo](https://github.com/makethunder/awsudo) installed
- a working AWS configuration in `$HOME/.aws/**`

### Installation

Easily done through `pip`:

```bash
$ pip install --user git+https://github.com/otype/aws-helpers
```

## Helper scripts

Following helper scripts are available:

### aws-instances

You can easily list your AWS EC2 instances with `aws-instances`.

#### Using `aws-instances`

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


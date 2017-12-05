from setuptools import setup
setup(
    name='aws-helpers',
    description='Set of AWS helper scripts',
    url='https://github.com/otype/aws-helpers',
    author='Hans-Gunther Schmidt',
    author_email='hans@otype.de',
    version='0.1',
    install_requires=['awscli>=2.48.0', 'boto>=1.14.3'],
    dependency_links=[
        "git+ssh://git@github.com/makethunder/awsudo.git@egg=awsudo"
    ],
    scripts=['src/aws-instances', 'src/aws-instances.py']
 )

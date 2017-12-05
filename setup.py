from setuptools import setup
setup(
    name='aws-helpers',
    description='Set of AWS helper scripts',
    url='https://github.com/otype/aws-helpers',
    author='Hans-Gunther Schmidt',
    author_email='hans@otype.de',
    version='0.1',
    install_requires=['awscli==1.12.2'],
    scripts=['src/aws-instances', 'src/aws-instances.py']
 )

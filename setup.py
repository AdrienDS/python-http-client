import os
from setuptools import setup


long_description = 'Fork of sendgrid python-http-client using treq (twisted). \nPlease see the GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

base_url = 'https://github.com/AdrienDS/'
version = '0.1.0'
setup(
    name='tx_sendgrid_http_client',
    version=version,
    author='Adrien David',
    author_email='adrien.ooo@gmail.com',
    url='{0}tx_sendgrid_http_client'.format(base_url),
    download_url='{0}tx_sendgrid_http_client/tarball/{1}'.format(base_url, version),
    packages=['tx_sendgrid_http_client'],
    license='MIT',
    description='Sendgrid HTTP REST client for Twisted/Python',
    long_description=long_description,
    install_requires=['Twisted', 'treq'],
    keywords=[
        'Sendgrid',
        'Twisted',
        'HTTP',
        'API'],
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)

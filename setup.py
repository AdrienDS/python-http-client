import io
import os
from distutils.file_util import copy_file
from setuptools import setup


long_description = 'Fork of sendgrid python-http-client using treq (twisted). \nPlease see the GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

base_url = 'https://github.com/AdrienDS/'
version = '0.1.2'

dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.rst'), encoding='utf-8').read()

copy_file(os.path.join(dir_path, 'VERSION.txt'),
          os.path.join(dir_path, 'tx_sendgrid_http_client', 'VERSION.txt'),
          verbose=0)
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
    include_package_data=True,
    keywords=[
        'Sendgrid',
        'Twisted',
        'HTTP',
        'API'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)

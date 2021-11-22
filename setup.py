import json
from setuptools import setup, find_packages

with open('metainfo.json') as file:
    metainfo = json.load(file)

setup(
    name='ARISE',
    version='1.0',
    author=', '.join(metainfo['authors']),
    author_email=metainfo['email'],
    url=metainfo['url'],
    description=metainfo['title'],
    long_description=metainfo['description'],
    packages=find_packages(),
    install_requires=['numpy', 'scipy'],
)

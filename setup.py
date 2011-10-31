#!/usr/bin/env python
from distutils.core import setup

setup(
    name='djextras',
    version='1.0.2',
    description="Some extra django goodies",
    long_description = open('README.md').read(),
    author='Michael Prior',
    author_email='prior@cracklabs.com',
    url='https://github.com/prior/djextras',
    download_url='https://github.com/prior/djextras/tarball/v1.0.2',
    license='LICENSE.txt',
    packages=['djextras'],
    install_requires=[
        'nose==1.1.2',
        'unittest2==0.5.1',
        'Django==1.3',
        'sanetime==3.0.1'
    ],
    dependency_links = ['https://github.com/prior/sanetime/tarball/v3.0.1'],
)

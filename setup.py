# coding: utf-8
#!/usr/bin/env python

from setuptools import setup, find_packages

readme = open('README').read()

setup(
    name='essay_demo',
    version='${version}',
    description=readme.partition('\n')[0],
    long_description=readme,
    author='EssayTech',
    author_email='thefivefire@gmail.com',
    url='http://github.com/EssayTech/essay',
    packages=find_packages(exclude=['*.pyc']),
    include_package_data=True,
    install_requires=[
        ],
    entry_points={
        'console_scripts': [
            'essay_demo = essay_demo.main:main',
        ]
    },
)

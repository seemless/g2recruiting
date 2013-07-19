__author__ = 'Matthew Smith'


import os
from setuptools import setup


setup(
	name='g2recruiting',
	version='0.0.1',
	author='matt smith',
	description='Provide an external place for resumes to be uploaded.',
	#packages=find_packages(),
	packages=['g2recruiting'],
	zip_safe=True,
	install_requires=[
	'Flask>=0.6',
    'wtforms',
    'Flask-Bootstrap'
	]



)
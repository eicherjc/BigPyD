from setuptools import setup

setup(
  name='BigPyD',
  version='0.1.0',
  author='Chris Eicher',
  author_email='ceicher@bigid.com',
  packages=['BigPyD'],
  url='https://github.com/eicherjc/BigPyD',
  license='Apache 2.0',
  description='Python framework for BigID',
  long_description=open('README.md').read(),
  install_requires=[
      'pandas',
      'requests'
  ]
)
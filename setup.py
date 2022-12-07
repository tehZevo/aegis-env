from setuptools import setup, find_packages

setup(name='aegisenv',
  version='0.0.0',
  install_requires = [
    "numpy",
    "gym",
    "nd_to_json @ git+https://github.com/tehzevo/nd-to-json#egg=nd_to_json",
    "protopost @ git+https://github.com/tehzevo/protopost-python#egg=protopost"
  ],
  packages=find_packages())

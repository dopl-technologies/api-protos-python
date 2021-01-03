from setuptools import setup, find_namespace_packages

setup(
   name='dopltech-api-protos',
   version='0.1',
   description='Dopl Technologies API protos',
   author='Ryan James',
   author_email='ryan@dopltechnologies.com',
   packages=find_namespace_packages(include=['dopltech.*']),
   install_requires=['grpcio', 'grpcio-tools'],
)
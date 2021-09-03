from setuptools import setup

setup(
   name='getKhoa',
   version='0.0.0.1',
   description="Khoa data download",
   url='https://github.com/qkdrk7777775/getKhoa',
   author='chang je Cho',
   author_email='qkdrk7777775@gmail.com',
   license='MIT',
   packages=['getKhoa'],
   install_requires=['requests','pandas','numpy','re'],
   include_package_data=True,
   keywords = ['khoa','korea','ocean'],
   zip_safe=False)
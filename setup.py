from setuptools import setup

setup(
    name='fixer',
    version='1.1.2',
    description='fixer service packages: providing important worlds currencies.',
    url='https://github.com/mhgzadeh/fixer',
    author='Mohammad',
    author_email='m.hgzadeh@gmail.com',
    license='MTL',
    packages=['get_data', 'send_data'],
    install_requires=['requests'],
    zip_safe=False
)

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rithms',
    version='0.0.1',
    description='rithms is an algorithms and datastructures package made solely on Python for studying purposes',
    long_description=readme,
    author='Jorge Rodríguez',
    author_email='egroj97@gmail.com',
    url='https://github.com/egroj97/rithms',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

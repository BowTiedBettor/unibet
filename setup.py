import os
from setuptools import setup, find_packages

with open(os.path.join("requirements.txt")) as f:
    INSTALL_REQUIRES = f.read().splitlines()

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='unibetscraper',
    version='0.1.0',
    long_description=LONG_DESCRIPTION,
    author='BowTiedBettor',
    author_email='bowtiedbettor@gmail.com',
    url='https://github.com/BowTiedBettor/unibetscraper',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=INSTALL_REQUIRES,
)
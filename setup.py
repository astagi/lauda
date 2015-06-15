#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

extra_kwargs = {}
if sys.version_info >= (3,):
    extra_kwargs['setup_requires'] = ['setuptools']

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
]

setup(
    name="lauda",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    description="A very simple python module for measuring time.",
    license="MIT",
    author="Andrea Stagi",
    author_email="stagi.andrea@gmail.com",
    url="",
    keywords="time measurement",
    install_requires=[
    ],
    classifiers=classifiers,
    zip_safe=False,
    **extra_kwargs)
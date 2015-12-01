#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'ntplib',
]

test_requirements = [
    'mock',
    'coverage',
]

setup(
    name='ntpdatetime',
    version='0.1.5',
    description="Extend datetime module so it can return the time "
                "fetched from a NTP poolserver",
    long_description=readme + '\n\n' + history,
    author="Iwan in 't Groen",
    author_email='iwanintgroen@gmail.com',
    url='https://github.com/igroen/ntpdatetime',
    packages=[
        'ntpdatetime',
    ],
    package_dir={'ntpdatetime':
                 'ntpdatetime'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='ntpdatetime',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

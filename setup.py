#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup
'''
:author:  madkote
:contact: madkote(at)bluewin.ch

Setup script for the katestable module distribution.
'''

from setuptools import setup

from katestable import __version__ as katestable_version

module_name = 'katestable'

modules = [module_name]

with open('README.md') as f:
    _readme = f.read()

with open('LICENSE') as f:
    _license = f.read()

setup(
    # Distribution meta-data
    name=module_name,
    version=katestable_version,
    description='Python K-Testable machine module',
    long_description=_readme,
    author='Roman Schroeder',
    author_email='madkote(at)bluewin.ch',
    url='https://github.com/madkote/katestable',
    license=_license,
    py_modules=modules,
    classifiers=[
        'Development Status :: Production/Stable',
        'Intended Audience :: Computer Science',
        'Intended Audience :: Natural Language Processing',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        ]
    )

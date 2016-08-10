#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests.runtests
'''
:author:  madkote
:contact: madkote(at)bluewin.ch

KT tests runner
---------------
Execute all available tests
'''
import os
import sys
import unittest

# bootstrap
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


def load_tests(loader, tests, pattern):
    return loader.discover('.')

if __name__ == '__main__':
    unittest.main()

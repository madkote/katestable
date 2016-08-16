# katestable
K-testable machine
==================
K-testable languages with DFA.

Usage
=====
>>> from katestable import KTestable
>>> kt = KTestable.build(3, [...])
>>> kt.detect('abba')

Requirements
============
Works out-of-the-box.

Install
=======
>>> make test
>>> python setup.py install

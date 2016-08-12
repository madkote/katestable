#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests.test_kt
'''
:author:  madkote
:contact: madkote(at)bluewin.ch

KT tests
--------
unit and integration tests

:TODO write unit tests
'''

import unittest

from katestable import KTestable


class Test_KTestable(unittest.TestCase):

    def test_010_build_and_detect(self):
        # given
        k = 3
        language = ['a', 'aa', 'abba', 'abbbba', 'aaabbbbba']
        # initialize
        kt = KTestable.build(k, language)
        # tests
        tests = {x: True for x in language}
        tests.update({'aba': False,
                      'abc': False,
                      'aaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaa': False,
                      'aabbbaaac': False,
                      'aaaaabbbbbbbbba': True})
        # when ... then
        for x in sorted(tests):
            result = kt.detect(x)
            expected = tests[x]
            self.assertTrue(result == expected,
                            '%s :: got %s but expected %s' % (x,
                                                              result,
                                                              expected))

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests.test_kt
'''
:author:  madkote
:contact: madkote(at)bluewin.ch

KT tests
--------
unit and integration tests

Todo's
------
- write unit tests
'''

import unittest

from katestable.kt import KTMachine
from katestable.kt import KDFA


class Test_kt(unittest.TestCase):

    def test_010_build_and_detect(self):
        # given
        k = 3
        language = ["a", "aa", "abba", "abbbba", "aaabbbbba"]
        # initialize
        ktmachine = KTMachine.build(k, language)
        kdfa = KDFA.build(ktmachine)
        # tests
        tests = {x: True for x in language}
        tests.update({"aba": False,
                      "abc": False,
                      "aaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaa": False,
                      "aabbbaaac": False,
                      "aaaaabbbbbbbbba": True})
        # when ... then
        for x in sorted(tests):
            result = kdfa.detect(x)
            expected = tests[x]
            self.assertTrue(result == expected,
                            '%s :: got %s but expected %s' % (x,
                                                              result,
                                                              expected))

if __name__ == "__main__":
    unittest.main()

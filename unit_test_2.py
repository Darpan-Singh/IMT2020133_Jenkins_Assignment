#!/usr/bin/python3
# Failing Test case for fibonacci

import unittest
from fibonacci import my_fibonacci


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(my_fibonacci(-1), 1)

    def testCase2(self):
        self.assertEqual(my_fibonacci(2.5), 2)


if __name__ == '__main__':
    unittest.main()

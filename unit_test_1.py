#!/usr/bin/python3
# Passing Test case for checking factorial of numbers

import unittest
from fibonacci import my_fibonacci


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(my_fibonacci(0), 0)

    def testCase2(self):
        self.assertEqual(my_fibonacci(1), 1)

    def testCase3(self):
        self.assertEqual(my_fibonacci(5), 5)


if __name__ == '__main__':
    unittest.main()

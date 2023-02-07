#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import main

size_max_hash_truncate: int = 5
size_max_string: int = 8


class TestHashPoC(unittest.TestCase):

    def test_truncate_0(self):
        self.assertEqual(main.truncate("6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", -5), None)

    def test_truncate_1(self):
        self.assertEqual(main.truncate("6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", 5), '6b86b')

    def test_truncate_2(self):
        self.assertEqual(main.truncate("6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", 50),
                         '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c0')

    def test_generate_random_string_size_1(self):
        size_max: int = 50
        result: str = main.generate_random_string(size_max)
        if result is None:
            result_size = None
        else:
            result_size = len(result)
        self.assertEqual(result_size, size_max)

    def test_generate_random_string_size_2(self):
        size_max: int = -50
        result: str = main.generate_random_string(size_max)
        if result is None:
            result_size = None
        else:
            result_size = len(result)
        self.assertEqual(result_size, None)

    def test_generate_random_string_chars(self):
        size_max: int = 50
        result: str = main.generate_random_string(size_max)
        self.assertEqual(result.isalnum(), True)

    def test_collition_1(self):
        """
        Check 2 hash generated with random inputs
        :return:
        """
        result_random_1: str = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)
        result_random_2: str = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)
        while result_random_1 != result_random_2:
            result_random_1 = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)
            result_random_2 = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)

        print("result_random_1:", result_random_1)
        print("result_random_2:", result_random_2)
        self.assertEqual(result_random_1, result_random_2)

    def test_collition_2(self):
        """
        Check 2 hash, 1 generated with random input but other is knows
        :return:
        """
        hash_to_collition = '25bff8bbacd4f48a766863c1449f17f11ed841fe49144b628f22abc1d926d1ca'
        result_random: str = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)
        result_no_random: str = main.truncate(hash_to_collition, size_max_hash_truncate)
        while result_random != result_no_random:
            result_random = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)

        print("result_random:", result_random)
        print("result_no_random:", result_no_random)
        self.assertEqual(result_random, result_no_random)


if __name__ == '__main__':
    unittest.main()

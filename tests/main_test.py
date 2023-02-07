#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import main

size_max_hash_truncate: int = 4

class TestHashPoC(unittest.TestCase):

    # def test_truncate_1(self):
    #     self.assertEqual(main.truncate("6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", 5), '6b86b')
    #
    # def test_truncate_2(self):
    #     self.assertEqual(main.truncate("6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", 50),
    #                      '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c0')

    def test_generate_random_string_size(self):
        size_max: int = 50
        result: str = main.generate_random_string(size_max)
        self.assertEqual(len(result), size_max)

    def test_generate_random_string_chars(self):
        size_max: int = 50
        result: str = main.generate_random_string(size_max)
        self.assertEqual(result.isalnum(), True)

    def test_collition_1(self):
        size_max_string: int = 15
        #size_max_hash_truncate: int = 8
        result_random_1: str = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)
        result_random_2: str = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)
        while result_random_1 != result_random_2:
            result_random_1 = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)
            result_random_2 = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)

            print("result_random_1:", result_random_1)
            print("result_random_2:", result_random_2)
        self.assertEqual(result_random_1, result_random_2)

    def test_collition_2(self):
        size_max_string: int = 15
        #size_max_hash_truncate: int = 8
        hash_to_collition = 'c4ca4238a0b923820dcc509a6f75849b'
        result_random: str = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)
        result_no_random: str = main.truncate(hash_to_collition, size_max_hash_truncate)
        while result_random != result_no_random:
            result_random = main.generate_hash_truncated(main.generate_random_string(size_max_string), size_max_hash_truncate)

            print("result_random:", result_random)
            print("result_no_random:", result_no_random)
        self.assertEqual(result_random, result_no_random)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()

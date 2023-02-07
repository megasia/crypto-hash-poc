#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import random
import string

def generate_hash_sha256(input_string: str) -> str:
    result = hashlib.sha256(input_string.encode())
    return result.hexdigest()

def generate_hash_sha256_truncated(input_string: str, size: int) -> str:
    return truncate(generate_hash_sha256(input_string), size)

def generate_random_string(max_size: int) -> str:
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(max_size))

def truncate(input_string: str, size: int) -> str:
    if len(input_string) >= size:
        return input_string[:size]
    else:
        return None


if __name__ == '__main__':
    print(generate_hash_sha256(str(1)))
    print(truncate(generate_hash_sha256(str(1)), 50))
    print(generate_random_string(50))
    print(generate_random_string(10))

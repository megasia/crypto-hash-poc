#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import random
import string


def generate_hash(input_string: str) -> str:
    result = hashlib.sha256(input_string.encode())
    return result.hexdigest()


def generate_hash_truncated(input_string: str, size: int) -> str:
    return truncate(generate_hash(input_string), size)


def generate_random_string(max_size: int) -> str:
    if max_size > 0:
        letters = string.ascii_lowercase
        preimg = ''.join(random.choice(letters) for i in range(max_size))  # Creamos un preimg aleatorio
    else:
        return None
    return preimg


def truncate(input_string: str, size: int) -> str:
    if len(input_string) >= size and size > 0:
        return input_string[:size]
    else:
        return None


if __name__ == '__main__':
    print(generate_hash(str(1)))
    print(generate_hash(str(generate_random_string(8))))
    print(truncate(generate_hash(str(1)), 50))
    print(generate_random_string(50))
    print(generate_random_string(10))

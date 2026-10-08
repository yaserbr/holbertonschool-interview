#!/usr/bin/python3
"""Minimum operations module."""


def minOperations(n):
    """Return minimum number of operations."""
    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations

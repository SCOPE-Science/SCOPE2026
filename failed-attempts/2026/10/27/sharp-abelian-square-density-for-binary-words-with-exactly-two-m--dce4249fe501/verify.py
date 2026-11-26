#!/usr/bin/env python3
"""Reproduce finite checks for exact abelian-square factors with exactly two ones."""
from itertools import product

def described(a, b, c):
    m = max(a, b, c)
    unary = {'0' * (2 * r) for r in range(1, m // 2 + 1)}
    mixed = {
        '0' * i + '1' + '0' * b + '1' + '0' * j
        for i in range(a + 1)
        for j in range(c + 1)
        if abs(i - j) <= b and (i + j + b) % 2 == 0
    }
    return unary | mixed

def diagonal_count(a, b, c):
    result = max(a, b, c) // 2
    for d in range(-b, b + 1, 2):
        lower = max(0, d)
        upper = min(a, c + d)
        result += max(0, upper - lower + 1)
    return result

def direct(a, b, c):
    word = '0' * a + '1' + '0' * b + '1' + '0' * c
    result = set()
    for start in range(len(word)):
        for end in range(start + 2, len(word) + 1, 2):
            factor = word[start:end]
            half = len(factor) // 2
            if factor[:half].count('1') == factor[half:].count('1'):
                result.add(factor)
    return result

def run_checks():
    checked = 0
    for a, b, c in product(range(13), repeat=3):
        predicted = described(a, b, c)
        actual = direct(a, b, c)
        assert predicted == actual, (a, b, c, predicted ^ actual)
        assert diagonal_count(a, b, c) == len(actual), (a, b, c)
        checked += 1
    for k in range(1, 26):
        assert diagonal_count(3*k, 2*k, 3*k) == (
            4*k*k + 3*k + 1 + (3*k)//2
        ), k
    # Check the previously published asymmetric prototype as an overlap check.
    for k in range(1, 26):
        assert diagonal_count(k, k, 2*k) == (
            k + (k//2 + 1)**2 + (k+1)*((k+1)//2)
        ), k
    print('VERIFY_OK exact sets for', checked, 'triples; two closed forms 25 parameters each')

if __name__ == '__main__':
    run_checks()

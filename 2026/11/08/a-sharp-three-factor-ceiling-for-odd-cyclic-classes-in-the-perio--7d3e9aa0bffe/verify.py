"""Finite checks for odd-length cyclic classes in the period-doubling word.

The universal theorem follows from the written proof, not this finite test.
"""
from collections import Counter


def pd(level):
    word = '0'
    for _ in range(level):
        word = ''.join('01' if ch == '0' else '00' for ch in word)
    return word


def factors(word, n):
    return {word[i:i+n] for i in range(len(word)-n+1)}


def rotations(w):
    return {w[i:]+w[:i] for i in range(len(w))}


def check_odd_bound():
    a = pd(14)
    b = pd(15)
    for n in range(1, 130, 2):
        A = factors(a, n)
        B = factors(b, n)
        assert A == B, ('finite prefix saturation mismatch', n)
        for w in A:
            assert len(rotations(w) & A) <= 3, ('unexpected class', n, w)
    return 65


def check_sharp_constructions():
    s = pd(16)
    checks = 0
    for j in range(1, 6):
        B = pd(2*j)
        n = len(B)+1
        assert B.startswith('01') and B.endswith('00')
        assert B+B in s, ('doubled block absent', j)
        u = B+'0'
        v = '0'+B
        z = '00'+B[:-1]
        assert len({u,v,z}) == 3
        assert {u,v,z} <= factors(s,n)
        assert {u,v,z} <= rotations(u)
        checks += 1
    return checks


if __name__ == '__main__':
    a = check_odd_bound()
    b = check_sharp_constructions()
    print('VERIFY_OK odd_lengths={} sharp_constructions={}'.format(a,b))

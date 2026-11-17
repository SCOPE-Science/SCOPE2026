#!/usr/bin/env python3
"""Independent finite modular census for the pillow return maps.

This is a finite check of the stated determinant and summation formula.
The proof of the all-period theorem is analytical, not computational.
"""
from itertools import product
from math import gcd


def brute_pillow_fixed(q: int, reflected: bool) -> int:
    # Every pillow fixed class has a representative at these grid points:
    # the denominators divide q-1, q+1, or q*q-1.
    L = q*q - 1
    classes = set()
    for a, b in product(range(L), repeat=2):
        if reflected:
            aa, bb = q*a % L, -q*b % L
        else:
            aa, bb = q*a % L, q*b % L
        plus = aa == a and bb == b
        minus = aa == (-a) % L and bb == (-b) % L
        if plus or minus:
            opposite = ((-a) % L, (-b) % L)
            classes.add(min((a, b), opposite))
    return len(classes)


def word_counts(d: int, m: int, n: int):
    counts = []
    for word in product((1, 2), repeat=n):
        r = word.count(2)
        q = d**(n-r) * m**r
        counts.append((q, r, q*q + (-1 if r % 2 else 1)))
    return counts


def mobius(k):
    if k == 1:
        return 1
    p = 2
    count = 0
    while p*p <= k:
        if k % p == 0:
            k //= p
            if k % p == 0:
                return 0
            count += 1
        p += 1
    if k > 1:
        count += 1
    return -1 if count % 2 else 1


def test():
    singles = 0
    for q, reflected in ((2, False),(3, False),(4, False),(5, False),
                         (2, True),(3, True),(4, True),(5, True),
                         (6, True),(7, True),(7, False)):
        brute = brute_pillow_fixed(q, reflected)
        target = q*q + (-1 if reflected else 1)
        assert brute == target, (q, reflected, brute, target)
        singles += 1
    words_checked = 0
    for d,m in ((2,3),(3,2),(3,3),(2,4),(4,4)):
        D = d*d + m*m
        for n in range(1,9):
            counts = word_counts(d,m,n)
            assert sum(c for _,_,c in counts) == D**n, (d,m,n)
            assert sum(((-1)**r) for _,r,_ in counts) == 0
            assert sum(q*q for q,_,_ in counts) == D**n
            words_checked += len(counts)
            primitive_points = sum(mobius(n//k)*D**k for k in range(1,n+1) if n % k == 0)
            assert primitive_points >= 0 and primitive_points % n == 0
    print('VERIFY_OK modular_pillow_instances=%d binary_words=%d primitive_n_up_to=8' % (singles,words_checked))
    print('EXAMPLE_d2_m3 fixed_J_n_1_to_5', [13**n for n in range(1,6)])
    print('FINITE_CHECK_ONLY proof_of_all_periods_is_analytical')


if __name__ == '__main__':
    test()

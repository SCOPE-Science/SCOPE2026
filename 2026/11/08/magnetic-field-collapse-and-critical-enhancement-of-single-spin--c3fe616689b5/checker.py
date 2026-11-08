"""Exact finite-state checks for the wheel antiferromagnetic Ising stability counts.

Run: python checker.py
Only Python standard-library modules are required. Finite checks do not prove
all-size identities, which are established by the accompanying argument.
"""
from fractions import Fraction
from itertools import product
from math import comb


def perrin(n):
    a = [3, 0, 2]
    for j in range(3, n + 1):
        a.append(a[j-2] + a[j-3])
    return a[n]


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def cyclic_no_triples_count(n, positive_count):
    total = Fraction(0)
    for r in range(1, n+1):
        if 0 <= positive_count-r <= r and 0 <= n-positive_count-r <= r:
            total += Fraction(n, r)*comb(r, positive_count-r)*comb(r, n-positive_count-r)
    assert total.denominator == 1
    return int(total)


def formula(n, a):
    odd = n % 2 == 1
    if 0 < a < 1:
        return 2*perrin(n) - (0 if odd else 2)
    if a == 1:
        q = sum(cyclic_no_triples_count(n,k) for k in range((n+1)//2 + 1))
        return q + lucas(n) - (0 if odd else 2)
    if 1 < a < 2:
        return n+1 if odd else 3
    if 2 <= a < 3:
        return n+1 if odd else 3+n*(n-4)//4
    if a == 3:
        return 1+n+n*(n*n-1)//24 if odd else 3+n*n//4
    if 3 < a < n:
        return 1
    if a == n:
        return 2
    return 1


def direct_count(n, a):
    total = 0
    for spins in product((-1,1), repeat=n+1):
        center, ring = spins[0], spins[1:]
        if center*(a-sum(ring)) < 0:
            continue
        if any(ring[i]*(a-center-ring[(i-1)%n]-ring[(i+1)%n]) < 0
               for i in range(n)):
            continue
        total += 1
    return total


def independently_count_no_triples(n,k):
    return sum(sum(v==1 for v in ring)==k and
               all(not(ring[i] == ring[(i+1)%n] == ring[(i+2)%n])
                   for i in range(n))
               for ring in product((-1,1),repeat=n))


def run():
    tests = 0
    for n in range(5,15):
        for a in (Fraction(1,3), 1, Fraction(3,2), 2,
                  Fraction(5,2), 3, Fraction(7,2), n, n+Fraction(1,2)):
            got = direct_count(n,a)
            predicted = formula(n,a)
            assert got == predicted,(n,a,got,predicted)
            tests += 1
        for k in range(n+1):
            got = independently_count_no_triples(n,k)
            predicted = cyclic_no_triples_count(n,k)
            assert got == predicted,('run composition',n,k,got,predicted)
            tests += 1
    print('PASS: all',tests,'exact finite checks')


if __name__ == '__main__':
    run()

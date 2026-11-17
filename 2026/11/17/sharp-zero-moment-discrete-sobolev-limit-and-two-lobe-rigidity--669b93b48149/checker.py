#!/usr/bin/env python3
"""Exact arithmetic diagnostics for a real zero-moment discrete Sobolev bound.

The analytic proof, not this finite checker, establishes the universal statements.
"""
from fractions import Fraction as F
from itertools import product


def dirichlet_green(d, i, j):
    n = d + 1
    return F(min(i, j) * (n - max(i, j)), n)


def q_zero_moment(d, s):
    n = d + 1
    g = [F(i*(n-i), 2) for i in range(1, n)]
    h = F(n*(n*n-1), 12)
    val = sum(F(s[i-1]*s[j-1]) * dirichlet_green(d, i, j)
              for i in range(1, n) for j in range(1, n))
    z = sum(F(v)*g[i] for i,v in enumerate(s))
    return val - z*z/h


def witness(k):
    n = 2*k+1
    left = [F(i*(2*k*k+2*k+1 - n*i), 2*n) for i in range(1,k+1)]
    return [F(0)] + left + [-x for x in left[::-1]] + [F(0)]


def energy(a):
    return sum((y-x)**2 for x,y in zip(a,a[1:]))


def check():
    count = 0
    for k in range(1, 31):
        a = witness(k)
        d = 2*k
        assert len(a) == d+2
        assert sum(a) == 0
        assert all(x>0 for x in a[1:k+1])
        e = energy(a)
        mass = sum(abs(x) for x in a)
        assert e == mass
        assert mass == F(k*(k+1)*(k*k+k+1), 3*(2*k+1))
        assert all(2*a[i]-a[i-1]-a[i+1] == (1 if i<=k else -1)
                   for i in range(1,d+1))
        count += 5
    # For the small cases alone, enumerate every sign dual functional.
    # This is an exhaustive finite dimensional check, not an all-d theorem.
    for d in range(2, 11):
        values = [q_zero_moment(d,s) for s in product((-1,1), repeat=d)]
        kd2 = max(values)
        assert kd2 > 0
        if d%2==0:
            k = d//2
            assert kd2 == F(k*(k+1)*(k*k+k+1), 3*(2*k+1))
        else:
            assert kd2 < F((d+1)**3, 12)  # source's unconstrained squared constant is larger
        count += 2
    # An exact Green-kernel check; the polynomial kernel is the inverse of L.
    for d in range(2,21):
        for i in range(1,d+1):
            for j in range(1,d+1):
                val = 2*dirichlet_green(d,i,j)
                if i>1: val -= dirichlet_green(d,i-1,j)
                if i<d: val -= dirichlet_green(d,i+1,j)
                assert val == (1 if i==j else 0)
                count += 1
    print(f"EXACT_CHECKS_PASSED={count}")
    print("Theoretical claims require the independent written analytic proof.")


if __name__ == '__main__':
    check()

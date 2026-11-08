#!/usr/bin/env python3
"""Exact finite-state cross-checks for five-site early-warning sensor placements.

Requires only Python's standard library. This verifier is independent of the
closed-form Erlang survival calculation, using first-event SI transitions.
"""
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
from math import factorial


def erlang_survival_laplace_coefficients(dist):
    # ∫ exp(-z t) Pr(Gamma(dist,1)>t) dt, as a Fraction at z=1.
    return sum((Fraction(1, (2 ** (j + 1))) for j in range(dist)), Fraction(0))


def laplace_closed_form(n, sensors, z):
    # Laplace transform of the tail from independent left and right
    # first-passage times, integrated term by term.
    total = Fraction(0)
    for x in range(n):
        if x in sensors:
            continue
        left = [s for s in sensors if s < x]
        right = [s for s in sensors if s > x]
        a = x - max(left) if left else None
        b = min(right) - x if right else None
        if a is None or b is None:
            d = a if b is None else b
            total += sum((Fraction(1,(z+1)**(j+1)) for j in range(d)), Fraction(0))
        else:
            for i in range(a):
                for j in range(b):
                    total += Fraction(factorial(i+j),factorial(i)*factorial(j)*(z+2)**(i+j+1))
    return total / n


def direct_ctmc(n, sensors, z=None):
    S = frozenset(sensors)
    @lru_cache(None)
    def recur(left, right):
        if any(left <= s <= right for s in S):
            return Fraction(0) if z is None else Fraction(1)
        neighbors = []
        if left > 0: neighbors.append((left-1,right))
        if right < n-1: neighbors.append((left,right+1))
        rate=len(neighbors)
        if z is None:
            return (Fraction(1)+sum((recur(*c) for c in neighbors),Fraction(0)))/rate
        return sum((recur(*c) for c in neighbors),Fraction(0))/(rate+z)
    if z is None:
        return sum((recur(x,x) for x in range(n)),Fraction(0))/n
    return (1-sum((recur(x,x) for x in range(n)),Fraction(0))/n)/z


def check():
    expected={
      4:{(0,1):Fraction(3,4),(0,2):Fraction(3,8),
         (0,3):Fraction(3,8),(1,2):Fraction(1,2)},
      5:{(0,1):Fraction(6,5),(0,2):Fraction(7,10),
         (0,3):Fraction(1,2),(0,4):Fraction(3,5),
         (1,2):Fraction(4,5),(1,3):Fraction(1,2)}
    }
    count=0
    for n in (2,3,4,5):
        C=list(combinations(range(n),2))
        for sensors in C:
            m=direct_ctmc(n,sensors)
            rep=min(sensors,tuple(sorted(n-1-s for s in sensors)))
            if n in expected: assert m==expected[n][rep],(n,sensors,m)
            for z in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(3)):
                assert direct_ctmc(n,sensors,z)==laplace_closed_form(n,sensors,z), (n,sensors,z)
                count+=1
        if n==4:
            assert {S for S in C if direct_ctmc(n,S)==Fraction(3,8)}=={(0,2),(0,3),(1,3)}
        if n==5:
            assert {S for S in C if direct_ctmc(n,S)==Fraction(1,2)}=={(0,3),(1,3),(1,4)}
    print('PASS',count,'independent rational Laplace comparisons; all exact mean classes and sharp minima')
if __name__=='__main__':check()

#!/usr/bin/env python3
"""Exact finite tests for geometric vacancy-chain probabilities in path dimer parking.

Only Python standard library. The asymptotic statements need the analytic proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

def endpoint(m):
    assert m >= 1
    return sum((Fraction((-1)**j, factorial(j)) for j in range(m)), Fraction(0))

def terminal_occupied(n, priority):
    occupied = [False] * n
    for edge in priority:
        if not occupied[edge] and not occupied[edge + 1]:
            occupied[edge] = occupied[edge + 1] = True
    return occupied

def run():
    checks = 0
    for n in range(2, 10):
        chain_counts = {}
        start_counts = {}
        for priority in permutations(range(n - 1)):
            occ = terminal_occupied(n, priority)
            for k in range((n - 1)//3 + 1):
                for start in range(n - 3*k):
                    is_chain = all(not occ[start+3*j] for j in range(k+1))
                    if is_chain:
                        chain_counts[start,k] = chain_counts.get((start,k), 0) + 1
                        if start >= 3 and occ[start-3]:
                            start_counts[start,k] = start_counts.get((start,k),0) + 1
        den = factorial(n-1)
        for k in range((n-1)//3 + 1):
            for start in range(n-3*k):
                s = start+1
                expected = Fraction(1,3**k)*endpoint(s)*endpoint(n-s-3*k+1)
                actual = Fraction(chain_counts.get((start,k),0),den)
                assert actual == expected,(n,s,k,actual,expected)
                checks += 1
                if s>=4 and k>=1:
                    expected_start = Fraction(1,3**k)*(endpoint(s)-endpoint(s-3)/3)*endpoint(n-s-3*k+1)
                    actual_start = Fraction(start_counts.get((start,k),0),den)
                    assert actual_start==expected_start,(n,s,k,actual_start,expected_start)
                    checks += 1
        for m in range(2,n+1):
            lhs = (m-1)*endpoint(m)
            rhs = sum((endpoint(j) for j in range(1,m-1)),Fraction(0))
            assert lhs == rhs,(m,lhs,rhs)
            checks += 1
    print('PASS:', checks, 'exact assertions for n=2,...,9')

if __name__ == '__main__':
    run()

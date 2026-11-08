#!/usr/bin/env python3
"""Exact integer verification of Jacobsthal-triple formulas (finite corroboration)."""
from heapq import heappush, heappop
from math import gcd


def invariants_via_apery(a, b, c):
    """Shortest paths in Z/aZ give exact Apery representatives."""
    dist = [None] * a
    dist[0] = 0
    q = [(0, 0)]
    while q:
        weight, residue = heappop(q)
        if dist[residue] != weight:
            continue
        for generator in (b, c):
            new_residue = (residue + generator) % a
            new_weight = weight + generator
            if dist[new_residue] is None or new_weight < dist[new_residue]:
                dist[new_residue] = new_weight
                heappush(q, (new_weight, new_residue))
    assert all(v is not None for v in dist)
    frobenius = max(dist) - a
    genus = sum(dist) // a - (a - 1) // 2
    assert sum(dist) % a == (a * (a - 1) // 2) % a
    return frobenius, genus


def closed_invariants(n):
    j = lambda k: (2**k - (-1)**k) // 3
    a, b, c = j(n), j(n+3), j(n+4)
    assert 3*c == 8*a + 5*b
    assert gcd(a, b, c) == 1
    if n % 3 == 0:
        frobenius = a*b//3 - a - b + 2*c
        genus = (frobenius+1)//2
        assert frobenius % 2 == 1
    else:
        genus_numerator = (a-5)*(8-b)
        assert genus_numerator % 3 == 0
        genus = ((a-1)*(b-1))//2 + genus_numerator//3
        if a % 3 == 1:
            assert ((a+2) % 3) == 0
            frobenius = ((a+2)//3)*b+c-a
            assert 2*genus-frobenius-1 == 8*(a-10)//3
        else:
            assert a % 3 == 2 and (a+7) % 3 == 0
            frobenius = ((a+7)//3)*b-a
            assert 2*genus-frobenius-1 == 16*(a-5)//3
    return a,b,c,frobenius,genus


def verify():
    for n in range(3, 17):
        a,b,c,expected_f,expected_g = closed_invariants(n)
        f,g = invariants_via_apery(a,b,c)
        assert (f,g) == (expected_f,expected_g), (n, f, g,expected_f,expected_g)
        assert (f == 2*g-1) == (n % 3 == 0 or n == 4)
        if n%3:
            assert gcd(a,b)==1
            t = (5*pow(3,-1,a)) % a
            for k in range(a):
                candidates=[((k-t*y) % a)*b+y*c for y in range(3)]
                if a%3==1:
                    threshold=(a+5)//3
                    y=0 if k<threshold else (1 if k<2*threshold else 2)
                elif a==5:
                    y=0
                else:
                    u,t2=(a+10)//3,(2*a+5)//3
                    y=0 if k<u else (2 if k<t2 else 1)
                assert candidates[y] == min(candidates), (n,k,y,candidates)
    print('VERIFY_OK exact_apery_n=3..16, 14_full_shortest_path_checks, closed_form_F_g_and_symmetry, piecewise_minimizers')

if __name__=='__main__':
    verify()

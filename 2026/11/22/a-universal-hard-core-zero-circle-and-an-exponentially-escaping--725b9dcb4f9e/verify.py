"""Exact finite tests for a hard-core gas on a once-subdivided star.

Uses independent-set enumeration and exact real-root isolation; the
all-size complex-zero classification rests on the proof, not these tests.
"""
from fractions import Fraction
from math import comb
import sympy as sp

z = sp.Symbol('z')

def polynomial_from_graph(arms):
    # Vertex 0 is hub; each arm has inner vertex 2*i+1 and tip 2*i+2.
    N = 2*arms+1
    edges = [(0,2*i+1) for i in range(arms)] + [
        (2*i+1,2*i+2) for i in range(arms)]
    coeff = [0]*(arms+2)
    for mask in range(1<<N):
        if all(not ((mask>>a)&1 and (mask>>b)&1) for a,b in edges):
            coeff[mask.bit_count()] += 1
    return sp.Poly.from_list(coeff[::-1], gens=z)

def formula(arms):
    return sp.Poly((1+2*z)**arms+z*(1+z)**arms,z)

checks=0
for arms in range(1,8):
    assert polynomial_from_graph(arms)==formula(arms)
    checks+=1
for arms in range(1,17):
    p=formula(arms)
    assert p.degree()==arms+1 and sp.gcd(p,p.diff()).degree()==0
    assert p.count_roots(-sp.oo,-1)==1
    assert p.count_roots(-sp.Rational(1,2),0)==1
    assert p.count_roots(-1,-sp.Rational(1,2))==(1 if arms%2==0 else 0)
    assert p.eval(-1)!=0 and p.eval(-sp.Rational(1,2))!=0
    checks+=6
print('ALL_EXACT_CHECKS_PASSED',checks)

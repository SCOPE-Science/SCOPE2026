#!/usr/bin/env python3
"""Exact finite identities supporting the random-recursive-tree exponential-spine proof.

The infinite asymptotic statements rely on the analytic argument and a cited
maximal-displacement theorem; this checker certifies only the finite algebraic
identities that it tests.
"""
from fractions import Fraction
from itertools import product
from math import factorial
from sympy import symbols, expand, prod, simplify, diff, exp, sqrt

z,c,t = symbols('z c t')
assertions=0
for n in range(2,9):
    observed=[Fraction(0)]*n
    tree_count=0
    # Parent(j) ranges over 1,..,j-1 and is independent uniform.
    for choices in product(*(range(1,j) for j in range(2,n+1))):
        depth=[0]*n
        for child,p in enumerate(choices, start=2):
            depth[child-1]=depth[p-1]+1
        for dep in depth:
            observed[dep]+=Fraction(1,factorial(n-1))
        tree_count+=1
    assert tree_count==factorial(n-1)
    assertions+=1
    profile=prod(1+z/t for t in range(1,n))
    expanded=expand(profile)
    for k in range(n):
        assert simplify(expanded.coeff(z,k)-observed[k])==0
        assertions+=1
    # Gaussian tilt changes each lineage edge by mean +1.
    tilted=prod(1+c*z/t for t in range(1,n))
    assert simplify(tilted-sum(observed[k]*(c*z)**k for k in range(n)))==0
    assertions+=1
    # Normalized spine depth is a sum of independent Bernoulli(c/(t+c)).
    norm=prod(1+c/t for t in range(1,n))
    pgf=prod((t+c*z)/(t+c) for t in range(1,n))
    assert simplify(pgf-tilted/norm)==0
    assertions+=1
    # One-step Gaussian tilt has exact moments E[e^X X^r]/E[e^X]
    # equal to those of N(1,1), for r=0..6.
    for r in range(7):
        moment=simplify(diff(exp(t*t/2),t,r).subs(t,1)/exp(Fraction(1,2)))
        # Derivative of exp(t^2/2), evaluated at 1, divides by exp(1/2).
        assert simplify(moment-diff(exp(t+t*t/2),t,r).subs(t,0))==0
        assertions+=1
print(f'PASS: {assertions} exact finite identities, n=2..8; no infinite claim inferred from finite tests.')

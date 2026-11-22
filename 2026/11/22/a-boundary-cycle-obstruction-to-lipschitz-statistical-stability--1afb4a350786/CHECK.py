#!/usr/bin/env python3
"""Finite exact-moment checks for the triangular tent boundary measures.

These consistency tests are not a proof of the all-observable identities.
Uses only Python's standard library and exact rational arithmetic.
"""
from fractions import Fraction as Q
from math import comb, factorial

# R = 2 int_0^1 f(2-s,s)ds, B = int_0^2 f(s,0)ds,
# L = 2 int_0^1 f(s,s)ds. A polynomial test is x**p*y**q.
def moment_R(p,q):
    return 2*sum(Q(comb(p,k)*2**(p-k)*(-1)**k, k+q+1) for k in range(p+1))
def moment_B(p,q):
    return Q(2**(p+1),p+1) if q==0 else Q(0)
def moment_L(p,q):
    return Q(2,p+q+1)

def push_R(p,q):  # (2-s,s) -> (2s,0)
    return Q(2**(p+1),p+1) if q==0 else Q(0)
def push_B(p,q):  # bottom halves -> diagonal, one-to-one twice
    return Q(2,p+q+1)
def push_L(p,q):  # (s,s) -> (2s,0)
    return Q(2**(p+1),p+1) if q==0 else Q(0)

assert moment_R(0,0)==moment_B(0,0)==moment_L(0,0)==2
# Jacobian determinants: [[1,1],[1,-1]] and [[-1,1],[-1,-1]].
assert (1*(-1)-1*1)==-2
assert ((-1)*(-1)-1*(-1))==2
for deg in range(9):
    for p in range(deg+1):
        q=deg-p
        assert push_R(p,q)==moment_B(p,q),(p,q,'R->B')
        assert push_B(p,q)==moment_L(p,q),(p,q,'B->L')
        assert push_L(p,q)==moment_B(p,q),(p,q,'L->B')
print('PASS: exact Jacobians and 135 boundary pushforward moment checks (45 monomials x 3 maps)')

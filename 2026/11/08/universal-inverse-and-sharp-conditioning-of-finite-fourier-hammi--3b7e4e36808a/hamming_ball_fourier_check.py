#!/usr/bin/env python3
"""Standalone finite checks for support-ball Fourier inverse and norm bounds.
Requires Python 3, numpy, and sympy. Does not prove asymptotic assertions.
"""
from itertools import product
from math import comb, factorial, pi
import cmath
import numpy as np
import sympy as sp


def points(elements, n, r, zero):
    return [v for v in product(elements, repeat=n)
            if sum(a != zero for a in v) <= r]

def inverse_formula(x, y, n, r, q, pair):
    union = sum(a != 0 or b != 0 for a, b in zip(x, y))
    if union > r:
        return 0
    s = sum(comb(n-union, j) * (-(q-1)/q)**j
            for j in range(r-union+1))
    z = 1
    for a, b in zip(x, y):
        z *= pair(a, b).conjugate()
    return q**(-union) * z * s

def cyclic_pair(q):
    return lambda a,b: cmath.exp(2j*pi*(a*b % q)/q)

def klein_pair(a, b):
    return complex((-1)**(((a&1)*(b&1)+((a>>1)&1)*((b>>1)&1)) % 2))

def run_numeric(q, n, r, pair):
    pts = points(range(q), n, r, 0)
    H = np.array([[np.prod([pair(a,b) for a,b in zip(x,y)])
                   for y in pts] for x in pts], dtype=complex)
    E = np.array([[inverse_formula(x,y,n,r,q,pair) for y in pts]
                  for x in pts],dtype=complex)
    diff = np.max(abs(H@E - np.eye(len(pts))))
    assert diff < 2e-9, (q,n,r,diff)
    frob_sq = sum(comb(n,u) * (q*q-1)**u / q**(2*u)
                  * sum(comb(n-u,j) * (-(q-1)/q)**j
                  for j in range(r-u+1))**2
                  for u in range(r+1))
    assert abs(np.sum(np.abs(E)**2) - frob_sq)<2e-8
    print('NUMERIC',q,n,r,'size',len(pts),'inverse_residual',f'{diff:.2g}',
          'frob_relative_error',f'{abs(np.sum(np.abs(E)**2)-frob_sq)/frob_sq:.2g}')

def exact_pair_q4_cyclic(a,b):
    return sp.I**(a*b % 4)
def exact_pair_klein(a,b):
    return sp.Integer((-1)**(((a&1)*(b&1)+((a>>1)&1)*((b>>1)&1))%2))
def exact_pair_bin(a,b):
    return sp.Integer((-1)**(a*b))

def run_exact(q,n,r,pair):
    pts = points(range(q),n,r,0)
    H = sp.Matrix([[sp.prod(pair(a,b) for a,b in zip(x,y))
                   for y in pts] for x in pts])
    I = sp.zeros(len(pts))
    for i,x in enumerate(pts):
        for j,y in enumerate(pts):
            u=sum(a!=0 or b!=0 for a,b in zip(x,y))
            if u > r: continue
            val=sum(sp.binomial(n-u,t)*(-sp.Rational(q-1,q))**t
                    for t in range(r-u+1))/q**u
            I[i,j]=sp.prod(sp.conjugate(pair(a,b)) for a,b in zip(x,y))*val
    assert H*I == sp.eye(len(pts)), (q,n,r)
    assert I*H == sp.eye(len(pts)), (q,n,r)
    print('EXACT',q,n,r,'size',len(pts),'verified_both_products')

if __name__=='__main__':
    run_exact(2,4,2,exact_pair_bin)
    run_exact(4,2,1,exact_pair_q4_cyclic)
    run_exact(4,3,1,exact_pair_klein)
    for q,n,r in [(2,5,3),(3,3,2),(5,3,1),(6,2,2),(7,2,1)]:
        run_numeric(q,n,r,cyclic_pair(q))
    run_numeric(4,3,2,klein_pair)
    print('FOURIER_HAMMING_BALL_INVERSE_CHECKS_PASS')

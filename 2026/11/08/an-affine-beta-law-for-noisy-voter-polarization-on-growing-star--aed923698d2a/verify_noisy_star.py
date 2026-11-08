#!/usr/bin/env python3
"""Standalone checks for exact stationary noisy-voter statistics on a star.

The results are verified algebraically and against an independently built
finite-state Markov generator. Requires Python, sympy, numpy, scipy.
"""
from fractions import Fraction
from math import isclose
import sympy as sp
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def symbolic_checks():
    a, h, n, y = sp.symbols('a h n y', positive=True)
    k = 2*a + h
    alpha = 2*a*(a+h)/k**2
    beta = h**2/k**2
    assert sp.simplify(2*alpha+beta-1) == 0
    # Flux-balance identity, with unnormalised rho = y^(alpha-1)(1-y)^(alpha-1)
    # Divide both sides by rho to avoid non-rational symbolic exponent handling.
    gain_over_rho = sp.expand((alpha+beta*y)*(1-y) - (alpha+beta*(1-y))*y)
    assert sp.simplify(gain_over_rho-alpha*(1-2*y)) == 0
    # Pair correlations from the 2x2 stationary equations.
    A = h*h*(n+1)/(8*a*(a+h)*n + h*h*(n+1))
    C = h*(2*a+h)*(n+1)/(8*a*(a+h)*n + h*h*(n+1))
    assert sp.simplify((4*a+2*h)*A-2*h*C) == 0
    assert sp.simplify((4*a+2*h)*C - h*(1+sp.Rational(1,1)/n+(n-1)*A/n)) == 0
    var_n = sp.factor((1+(n-1)*A)/(4*n))
    var_lim = sp.factor(sp.limit(var_n,n,sp.oo))
    var_beta = sp.factor((h/k)**2 / (4*(2*alpha+1)))
    assert sp.simplify(var_lim-var_beta)==0
    assert sp.simplify(var_beta-h*h/(4*(8*a*(a+h)+h*h)))==0
    print('Symbolic identities: PASS')
    print('var finite n:', var_n)
    print('var infinite:', var_lim)


def stationary_exact_n(n, a, h):
    # States (H, k): hub bit H; number k of plus leaves.
    size = 2*(n+1)
    Q = lil_matrix((size,size),dtype=float)
    for H in range(2):
        for j in range(n+1):
            x = H*(n+1)+j
            up = (n-j)*(a+h*H)
            down = j*(a+h*(1-H))
            flip = a + h*(j/n if H==0 else (n-j)/n)
            if j < n: Q[x,x+1] += up
            if j > 0: Q[x,x-1] += down
            Q[x,(1-H)*(n+1)+j] += flip
            Q[x,x] -= (up+down+flip)
    T = Q.T.tolil()
    rhs = np.zeros(size)
    T[-1,:] = 1.
    rhs[-1]=1.
    pi = spsolve(T.tocsr(),rhs)
    assert min(pi) > -1e-9
    assert abs(sum(pi)-1)<1e-10
    states = np.tile(np.arange(n+1)/n,2)
    mean = float(np.dot(pi,states))
    variance = float(np.dot(pi,(states-.5)**2))
    A = h*h*(n+1)/(8*a*(a+h)*n+h*h*(n+1))
    expected = (1+(n-1)*A)/(4*n)
    assert abs(mean-.5)<1e-10,(n,mean)
    assert abs(variance-expected)<1e-10,(n,variance,expected)
    return variance


def main():
    symbolic_checks()
    for a,h in [(0.1,1.), (0.5,1.), (2.,3.)]:
        v = h*h/(4*(8*a*(a+h)+h*h))
        vals=[]
        for n in [2,3,5,9,30,100]:
            vals.append((n,round(stationary_exact_n(n,a,h),9)))
        assert abs(vals[-1][1]-v)<0.005
        print(f'noise={a},copy={h}; variances:',vals,'limiting',round(v,9))
    print('Exact Markov generator checks: PASS')

if __name__ == '__main__':main()

#!/usr/bin/env python3
"""Exact finite CRP checks and independent numerical checks of the moment identities.
No simulation is used to certify an infinite limit.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial, exp, gamma
import sympy as sp
from scipy.integrate import quad


def h(k, r):
    return sum(((-1) ** (j + 1)) * comb(k, j) * (1-r**j) / j for j in range(1, k+1))

def m(k, theta, s):
    H = sum(1/j for j in range(1, k+1))
    ans = exp(-theta*H)
    for j in range(1, s):
        v = quad(lambda r: j*r**(j-1)*exp(-theta*h(k, r)), 0, 1, epsabs=1e-12)[0]
        ans *= v
    return ans

def finite_crp(k, nmax, theta=1):
    # Exact CRP truncated count vector and accumulated zero-small-cycle count.
    state = {((1,) + (0,)*(k-1), 0): Fraction(1)}
    observations = []
    for n in range(1, nmax + 1):
        tot = sum(state.values())
        assert tot == 1
        mean = sum(Fraction(z,n)*p for (vec,z),p in state.items())
        second = sum(Fraction(z*z,n*n)*p for (vec,z),p in state.items())
        observations.append((n, mean, second))
        if n == nmax:
            break
        out = defaultdict(Fraction)
        denominator = theta+n
        for (vec, z), prob in state.items():
            # new cycle; size 1
            v = list(vec)
            v[0] += 1
            out[(tuple(v), z)] += prob*Fraction(theta, denominator)
            tracked = sum((i+1)*c for i,c in enumerate(vec))
            for i, c in enumerate(vec):
                if not c: continue
                v = list(vec)
                v[i] -= 1
                if i+1 < k: v[i+1] += 1
                v = tuple(v)
                new_z = z + (not any(v))
                out[(v, new_z)] += prob*Fraction((i+1)*c, denominator)
            tail = n-tracked
            if tail:
                out[(vec,z+(not any(vec)))] += prob*Fraction(tail,denominator)
        state = dict(out)
    return observations

def run():
    checks = 0
    r=sp.symbols('r',real=True)
    for k in range(1, 9):
        polynomial = sum(sp.Rational((-1)**(j+1)*comb(k,j),j)*(1-r**j) for j in range(1,k+1))
        assert sp.simplify(polynomial.subs(r,0)-sum(sp.Rational(1,j) for j in range(1,k+1))) == 0; checks+=1
        assert polynomial.subs(r,1) == 0; checks+=1
        assert sp.simplify(sp.diff(polynomial,r)+(1-(1-r)**k)/r)==0; checks+=1
        assert sp.diff(polynomial,r).subs(r,1)==-1; checks+=1
    for k in (1,2,3):
        for theta in (0.5,1.0,2.0):
            ms = [m(k,theta,s) for s in range(1,6)]
            assert all(0<z<=1 for z in ms); checks+=1
            assert all(ms[i+1] <= ms[i] +1e-12 for i in range(4)); checks+=1
            assert all(ms[i+2]*ms[i] >= ms[i+1]**2-1e-12 for i in range(3)); checks+=1
    assert abs(m(1,1,1)-exp(-1)) < 1e-12; checks+=1
    assert abs(m(1,1,2)-exp(-2)*(exp(1)-1)) <1e-12; checks+=1
    assert abs(m(1,1,2)-m(1,1,1)**2 - exp(-2)*(exp(1)-2))<1e-12; checks+=1
    for k in (1,2,3):
        finite=finite_crp(k,12)
        assert finite[0][1]==0; checks+=1
        for n,mean,second in finite:
            assert 0<=mean<=1 and mean*mean<=second<=mean; checks+=1
        print('k',k,'finite-n=12 mean/second:',[float(finite[-1][i]) for i in (1,2)],
              'limiting:',m(k,1,1),m(k,1,2))
    print('exact/symbolic/numerical assertions passed:',checks)
    print('derangement variance constant:',exp(-2)*(exp(1)-2))

if __name__ == '__main__': run()

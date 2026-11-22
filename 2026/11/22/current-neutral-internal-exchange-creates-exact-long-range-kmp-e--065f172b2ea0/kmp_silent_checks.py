"""Exact second-moment generator check for a finite boundary-driven energy-exchange network.

Run: python kmp_silent_checks.py
Requires sympy. All probabilities and moments are rational in the tested cases.
"""
from itertools import combinations
from math import comb, factorial
from fractions import Fraction
import sympy as sp


def basis(n):
    zero = (0,) * n
    terms = [zero]
    for i in range(n):
        a = list(zero); a[i] = 1; terms.append(tuple(a))
    for i in range(n):
        a = list(zero); a[i] = 2; terms.append(tuple(a))
    for i, j in combinations(range(n), 2):
        a = list(zero); a[i] = a[j] = 1; terms.append(tuple(a))
    return terms


def bath(m, i, temperature):
    k = m[i]
    if not k: return {m: sp.Integer(1)}
    ans = {}
    for s in range(k+1):
        e = list(m); e[i] = s
        ans[tuple(e)] = sp.Rational(comb(k,s)*factorial(k-s), k+1)*temperature**(k-s)
    return ans


def pair(m, i, j):
    a, b = m[i], m[j]
    if a+b == 0: return {m: sp.Integer(1)}
    k = a+b
    beta = sp.Rational(factorial(a)*factorial(b), factorial(k+1))
    ans = {}
    for s in range(k+1):
        e = list(m); e[i] = s; e[j] = k-s
        ans[tuple(e)] = beta*comb(k,s)
    return ans


def check(n, rate, ta, tb):
    terms = basis(n); indices = {m:i for i,m in enumerate(terms)}
    dim = len(terms)
    A = sp.zeros(dim-1,dim-1); b=sp.zeros(dim-1,1)
    for row, m in enumerate(terms[1:]):
        changes = {}
        def add(out, strength):
            for k,val in out.items(): changes[k] = changes.get(k,sp.Integer(0))+strength*val
        for i in range(n):
            add(bath(m,i,ta), sp.Integer(1))
            add(bath(m,i,tb), sp.Integer(1))
            add({m:sp.Integer(-2)}, sp.Integer(1))
        for i,j in combinations(range(n),2):
            add(pair(m,i,j),rate)
            add({m:sp.Integer(-1)},rate)
        for mon,coef in changes.items():
            if mon == terms[0]: b[row] -= coef
            else: A[row,indices[mon]-1] += coef
    y = A.inv()*b
    mean = sp.Rational(ta+tb, 2); delta=ta-tb
    target = rate*delta**2/(2*((3*n+1)*rate+12))
    for i in range(n):
        m = [0]*n; m[i]=1
        assert y[indices[tuple(m)]-1]==mean
    for i,j in combinations(range(n),2):
        m = [0]*n; m[i]=m[j]=1
        got = sp.factor(y[indices[tuple(m)]-1]-mean**2)
        assert got==target, (n,rate,i,j,got,target)
    for i in range(n):
        m=[0]*n; m[i]=2
        assert y[indices[tuple(m)]-1]==2*mean**2+delta**2*(rate+3)/((3*n+1)*rate+12)
    return dim-1


if __name__ == '__main__':
    count=0; matrices=0
    for n in (2,3,4,5):
        for v in (sp.Rational(0), sp.Rational(1,3), sp.Rational(2)):
            matrices+=1; count+=check(n,v,sp.Integer(3),sp.Integer(1))
    print(f'PASS: {matrices} exact independent generator systems, {count} exact moment equations; all moments and covariances agree.')

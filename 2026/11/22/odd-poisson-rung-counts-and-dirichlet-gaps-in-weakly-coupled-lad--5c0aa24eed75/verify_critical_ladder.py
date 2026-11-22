#!/usr/bin/env python3
"""Exact finite checks and numerical diagnostics for the weak-rung ladder theorem.

Run: python3 verify_critical_ladder.py. Python 3 standard library only.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, cos, pi, sin, sinh, sqrt, isclose

CHECKS = 0

def check(condition, message='check failed'):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def edges(n):
    rungs = [(i, n+i, i) for i in range(n)]
    rails = [(row*n+i, row*n+i+1, None)
             for row in range(2) for i in range(n-1)]
    return rungs+rails


def independent_tree_counts(n):
    ee = edges(n)
    result = Counter()
    for ids in combinations(range(len(ee)), 2*n-1):
        parent = list(range(2*n))
        def root(i):
            while parent[i] != i:
                i = parent[i]
            return i
        for idx in ids:
            a,b,_ = ee[idx]
            a,b = root(a),root(b)
            if a == b:
                break
            parent[a] = b
        else:
            rs = tuple(ee[i][2] for i in ids if ee[i][2] is not None)
            result[rs] += 1
    return result


def rung_ways(rs):
    out=1
    for a,b in zip(rs,rs[1:]):
        out *= 2*(b-a)
    return out


def inverse_fraction(A):
    n=len(A)
    mat=[[Fraction(A[i][j]) for j in range(n)] +
         [Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot=next(j for j in range(i,n) if mat[j][i])
        mat[i],mat[pivot]=mat[pivot],mat[i]
        d=mat[i][i]
        mat[i]=[x/d for x in mat[i]]
        for j in range(n):
            if j==i: continue
            c=mat[j][i]
            if c:
                mat[j]=[x-c*y for x,y in zip(mat[j],mat[i])]
    return [row[n:] for row in mat]


def det_fraction(A):
    n=len(A)
    if n==0: return Fraction(1)
    mat=[[Fraction(x) for x in row] for row in A]
    det=Fraction(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if mat[j][i]),None)
        if pivot is None: return Fraction(0)
        if pivot != i:
            mat[i],mat[pivot]=mat[pivot],mat[i]
            det=-det
        val=mat[i][i]
        det*=val
        for j in range(i+1,n):
            mult=mat[j][i]/val
            for k in range(i+1,n):
                mat[j][k] -= mult*mat[i][k]
            mat[j][i]=Fraction(0)
    return det


def kernel(n,c):
    B=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j: row.append(Fraction(int(i>0)+int(i<n-1))+2*c)
            elif abs(i-j)==1: row.append(Fraction(-1))
            else: row.append(Fraction(0))
        B.append(row)
    return [[2*c*x for x in row] for row in inverse_fraction(B)]


# Enumeration by arbitrary edge subsets: independent of the rung-cut formula.
for n in range(1,8):
    exhaustive=independent_tree_counts(n)
    by_k=Counter()
    check(len(exhaustive)==2**n-1,(n,'number of feasible rung sets'))
    for k in range(1,n+1):
        for rs in combinations(range(n),k):
            ways=rung_ways(rs)
            check(exhaustive[rs]==ways,(n,rs,'independent enumeration'))
            by_k[k]+=ways
        check(by_k[k]==2**(k-1)*comb(n+k-1,2*k-1),(n,k,'closed coefficient'))
    check(sum(exhaustive.values())==sum(by_k.values()),(n,'normalization'))

# Independently verify all 2^n rung inclusion events with transfer-current
# rational determinant for n <= 5, and several positive exact conductances.
for n in range(1,6):
    exhaustive=independent_tree_counts(n)
    for c in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(3)):
        K=kernel(n,c)
        norm=sum(Fraction(v)*c**len(rs) for rs,v in exhaustive.items())
        for k in range(n+1):
            for S in combinations(range(n),k):
                event=sum(Fraction(v)*c**len(rs) for rs,v in exhaustive.items()
                          if set(S).issubset(rs))
                sub=[[K[i][j] for j in S] for i in S]
                check(event/norm==det_fraction(sub),(n,c,S,'DPP inclusion'))
        for i in range(n):
            check(sum(K[i][j] for j in range(n))==1,(n,c,i,'constant eigenvector'))

# Spectral eigenvalues and odd-Poisson generating function at finite sizes;
# convergence tested numerically, not used as proof of infinite theorem.
for t in (Fraction(1,2),Fraction(2),Fraction(7)):
    x=sqrt(2*float(t))
    target=[x**(2*k-1)/(__import__('math').factorial(2*k-1)*sinh(x))
            for k in range(1,18)]
    check(abs(sum(target)-1.0)<1e-12,'odd-Poisson normalization')
    for n in (20,100,500):
        # stable finite weighted count via rescaled positive coefficients
        weights=[]
        for k in range(1,n+1):
            weights.append(2**(k-1)*comb(n+k-1,2*k-1)*float(t/n**2)**k)
        zz=sum(weights)
        check(zz>0,'finite normalization positive')
        d=max(abs(weights[k-1]/zz-target[k-1]) for k in range(1,9))
        if n==500:
            check(d<0.003,(t,n,d,'count limiting approximation'))
        q=[1.0]
        for m in range(1,n):
            q.append(2*float(t)/(2*float(t)+4*n*n*sin(m*pi/(2*n))**2))
        mean_from_eigen=sum(q)
        mean_from_weights=sum(k*w for k,w in enumerate(weights,1))/zz
        check(abs(mean_from_weights-mean_from_eigen)<2e-9,(t,n,'mean eigen check'))
    mean_limit=(1+x*__import__('math').cosh(x)/sinh(x))/2
    check(mean_limit>1,'limit mean')

# Compare conditional two-rung first-distance quadrature to its Dirichlet
# internal-spacing Beta(2,2) marginal limit (mean 1/2, second moment 3/10).
for n in (100,300):
    weights=[(j-i) for i in range(n) for j in range(i+1,n)]
    norm=sum(weights)
    mu=sum((j-i)**2 for i in range(n) for j in range(i+1,n))/norm/n
    sec=sum((j-i)**3 for i in range(n) for j in range(i+1,n))/norm/n**2
    check(abs(mu-.5)<1e-12,(n,'symmetry of interior gap'))
    if n==300:
        check(abs(sec-.3)<.003,(n,sec,'Dirichlet second moment'))

print('VERIFY_OK: {} exact assertions / bounded numerical checks'.format(CHECKS))

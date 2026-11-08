#!/usr/bin/env python3
"""Exact-rational verification of the windmill competitive-community phase diagram.

Use `python3 verify.py`. No third-party dependencies.
"""
from fractions import Fraction as F
from itertools import product


def mat(k, alpha, beta):
    n = 2*k+1
    B = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(1,n):
        B[0][i] = B[i][0] = beta
    for i in range(k):
        a,b = 2*i+1,2*i+2
        B[a][b] = B[b][a] = alpha
    return B


def solve(B,b):
    n=len(b)
    if not n: return []
    a=[row[:] + [b[i]] for i,row in enumerate(B)]
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None: return None
        a[j],a[p]=a[p],a[j]
        z=a[j][j]
        a[j]=[v/z for v in a[j]]
        for i in range(n):
            if i==j: continue
            z=a[i][j]
            if z:
                a[i]=[a[i][l]-z*a[j][l] for l in range(n+1)]
    return [a[i][-1] for i in range(n)]


def positive_definite(B):
    # Exact symmetric LDL^T factorization, positive pivots iff positive definite.
    n=len(B)
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    d=[F(0)]*n
    for j in range(n):
        d[j]=B[j][j]-sum(L[j][m]**2*d[m] for m in range(j))
        if d[j]<=0: return False
        L[j][j]=F(1)
        for i in range(j+1,n):
            L[i][j]=(B[i][j]-sum(L[i][m]*L[j][m]*d[m] for m in range(j)))/d[j]
    return True


def find_sinks(k,alpha,beta):
    B=mat(k,alpha,beta)
    n=len(B)
    sinks=[]
    for mask in range(1,1<<n):
        S=[i for i in range(n) if mask>>i&1]
        BS=[[B[i][j] for j in S] for i in S]
        x=solve(BS,[F(1)]*len(S))
        if x is None or min(x)<=0: continue
        if not positive_definite(BS): continue
        if any(F(1)-sum(B[i][j]*x[t] for t,j in enumerate(S))>=0
               for i in range(n) if i not in S): continue
        sinks.append(tuple(S))
    return set(sinks)


def formula_sinks(k,alpha,beta):
    center=frozenset([0])
    leaves=frozenset(range(1,2*k+1))
    choices=[frozenset(choice) for choice in product(*[(2*i+1,2*i+2) for i in range(k)])]
    if alpha<1:
        c=(1+alpha)/F(2*k)
        if beta<c: return {frozenset(range(2*k+1))}
        if beta<1: return {leaves}
        return {leaves,center}
    c=F(1,k)
    if beta<c: return {center | x for x in choices}
    if beta<1: return set(choices)
    return set(choices)|{center}


def main():
    total=0
    pars=[F(1,2),F(2,3),F(3,2),F(2)]
    bets=[F(1,10),F(1,5),F(2,5),F(3,5),F(4,5),F(6,5),F(3,2)]
    for k in (2,3,4):
        for alpha in pars:
            for beta in bets:
                if beta==1 or (alpha<1 and beta==(1+alpha)/F(2*k)) or (alpha>1 and beta==F(1,k)):
                    continue
                actual={frozenset(s) for s in find_sinks(k,alpha,beta)}
                expected=formula_sinks(k,alpha,beta)
                assert actual==expected,(k,alpha,beta,actual,expected)
                total+=1
    print(f'PASS: {total} independent exact-rational full-support census comparisons for k=2,3,4.')
    print('Each comparison checks all nonempty supports and their feasible eigen/invasion conditions.')

if __name__=='__main__':main()

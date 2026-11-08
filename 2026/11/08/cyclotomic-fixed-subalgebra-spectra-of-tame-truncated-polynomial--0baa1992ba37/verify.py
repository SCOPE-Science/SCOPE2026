#!/usr/bin/env python3
"""Direct finite-field checks of fixed subspace distribution for truncated one-variable algebras."""
from collections import Counter
from itertools import product
from math import gcd

def order(a,q):
    t=a % q
    d=1
    while t!=1:
        t=t*a % q
        d+=1
    return d

def compose_power_matrix(coeff,q,n):
    # The jth column is the coefficient vector of phi(t)^j modulo t^n.
    M=[[0]*n for _ in range(n)]
    P=[1]+[0]*(n-1)
    f=[0]+list(coeff)
    for j in range(n):
        for k in range(n):M[k][j]=P[k]
        Q=[0]*n
        for k in range(n):
            if P[k]:
                for ell in range(1,n-k):Q[k+ell]=(Q[k+ell]+P[k]*f[ell])%q
        P=Q
    return M

def fixed_dim(coeff,q,n):
    M=compose_power_matrix(coeff,q,n)
    A=[[(M[i][j]-(i==j))%q for j in range(n)] for i in range(n)]
    r=0
    for j in range(n):
        piv=next((i for i in range(r,n) if A[i][j]),None)
        if piv is None:continue
        A[piv],A[r]=A[r],A[piv]
        inv=pow(A[r][j],-1,q)
        for k in range(j,n):A[r][k]=A[r][k]*inv%q
        for i in range(r+1,n):
            fac=A[i][j]
            for k in range(j,n):A[i][k]=(A[i][k]-fac*A[r][k])%q
        r+=1
    return n-r

def predicted(q,n):
    result=Counter()
    for a in range(1,q):
        d=order(a,q)
        h=(n-2)//d
        L=(n-1)//d
        for j in range(1,h+1):
            result[1+j]+=(q-1)*q**(n-2-j)
        result[1+L]+=q**(n-2-h)
    return result

def actual(q,n):
    out=Counter()
    for a in range(1,q):
        for higher in product(range(q),repeat=n-2):
            coeff=(a,)+higher
            out[fixed_dim(coeff,q,n)]+=1
    return out

def main():
    # These direct matrix calculations do not invoke the proof's conjugacy reduction.
    for q,n in [(5,2),(5,3),(5,4),(7,3),(7,4),(7,5),(7,6),(11,3),(11,4)]:
        assert q>n
        found=actual(q,n); expected=predicted(q,n)
        assert found==expected,(q,n,found,expected)
        assert sum(found.values())==(q-1)*q**(n-2)
        print(f'EXHAUSTIVE_OK q={q} n={n} '+str(dict(sorted(found.items()))))
    print('VERIFY_OK')
if __name__=='__main__':main()

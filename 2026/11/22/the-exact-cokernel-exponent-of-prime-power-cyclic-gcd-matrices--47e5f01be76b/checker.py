#!/usr/bin/env python3
"""Exact integer/rational tests for an arithmetic circulant cokernel formula.
Requires only Python's standard library and SymPy for independent Smith checks.
"""
from fractions import Fraction
from math import gcd, lcm
from functools import reduce
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def matrix(p,k):
    n=p**k
    return [[gcd((i-j)%n,n) for j in range(n)] for i in range(n)]

def exponent_formula(p,k):
    ds=[p**(k-1)*(p-1), k*p**(2*k-2)*(p-1)*(p+k*(p-1))]
    ds += [p**(k+m-1)*(p-1)*m*(m+1) for m in range(1,k)]
    return lcm(*ds)

def inverse_formula(p,k):
    n=p**k
    l0=p**(k-1)*(p+k*(p-1))
    llast=p**(k-1)*(p-1)
    c0=Fraction(-1,l0*k*llast)
    cs=[c0]+[Fraction(-1,p**(2*k-j-1)*(p-1)*(k-j)*(k-j+1)) for j in range(1,k)]
    return [[sum((cs[j] for j in range(k) if (i-jj)%p**j==0), Fraction(int(i==jj),llast)) for jj in range(n)] for i in range(n)]

def rank_mod(A,p):
    M=[[x%p for x in row] for row in A]
    r=0
    for c in range(len(M[0])):
        pivot=next((j for j in range(r,len(M)) if M[j][c]%p),None)
        if pivot is None:continue
        M[pivot],M[r]=M[r],M[pivot]
        inv=pow(M[r][c],-1,p)
        M[r]=[(x*inv)%p for x in M[r]]
        for j in range(len(M)):
            if j!=r and M[j][c]%p:
                a=M[j][c]
                M[j]=[(x-a*y)%p for x,y in zip(M[j],M[r])]
        r+=1
    return r


def test():
    checks=0
    for p,k in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(5,1),(7,1)]:
        A=matrix(p,k); n=len(A);H=inverse_formula(p,k)
        for i in range(n):
            for j in range(n):
                v=sum((A[i][t]*H[t][j] for t in range(n)),Fraction(0))
                assert v==int(i==j),(p,k,i,j,v)
                checks+=1
        D=[abs(int(x)) for x in smith_normal_form(Matrix(A),domain=ZZ).diagonal()]
        exp=exponent_formula(p,k)
        assert D[-1]==exp,(p,k,D,exp)
        checks+=1
        assert lcm(*(x.denominator for row in H for x in row))==exp
        checks+=1
        assert rank_mod(A,p)==(p if k>=2 else p)
        checks+=1
        print(f'p={p},k={k},N={n},largest_SMITH={D[-1]},rank_mod_p={rank_mod(A,p)}')
    # Additional medium size inverse calculation without large SNF.
    p,k=3,3
    A=matrix(p,k);H=inverse_formula(p,k);n=len(A)
    for i in range(n):
        for j in range(n):
            assert sum((A[i][t]*H[t][j] for t in range(n)),Fraction(0))==int(i==j)
            checks+=1
    assert lcm(*(x.denominator for row in H for x in row))==exponent_formula(p,k)
    checks+=1
    assert rank_mod(A,p)==3;checks+=1
    print(f'p={p},k={k},N={n},predicted_exponent={exponent_formula(p,k)},rank_mod_p=3')
    print(f'PASS: {checks} independently evaluated exact assertions')

if __name__=='__main__':test()

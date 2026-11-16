#!/usr/bin/env python3
"""Standalone exact cyclotomic and finite-incidence checks for the spectral-pair theorem.

Uses Python 3 and SymPy; numpy is optional for eigenvalue tests.
It does not replace the all-order algebraic proof.
"""
from itertools import product
from math import prod
from sympy import Poly, cyclotomic_poly, symbols


def prime_factors(n):
    ans=[]
    d=2
    while d*d<=n:
        if n%d==0:
            ans.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:ans.append(n)
    return ans


def reduced_powers(n):
    """Represent powers of a primitive nth root in the integral cyclotomic basis."""
    x=symbols('x')
    ph=Poly(cyclotomic_poly(n,x),x)
    coeff=[int(ph.nth(j)) for j in range(ph.degree())]
    d=len(coeff)
    seq=[]
    a=[1]+[0]*(d-1)
    for _ in range(n):
        seq.append(tuple(a))
        a=[0]+a[:-1]
        last=seq[-1][-1]
        for k,c in enumerate(coeff): a[k]-=last*c
    return seq


def all_transversals(n,p):
    choices=[[j+p*k for k in range(n//p)] for j in range(p)]
    return list(product(*choices))


def is_zero_of_A(A,t,powers):
    d=len(powers[0]); N=len(powers)
    v=[0]*d
    for a in A:
        w=powers[(a*t)%N]
        for i in range(d):v[i]+=w[i]
    return not any(v)


def predicted(A,B,primes):
    p=primes[0]
    if len({x%p for x in A})!=p or len({x%p for x in B})!=p:return False
    return all(len({x%q for x in A})==1 or len({x%q for x in B})==1 for q in primes[1:])


def test_full(n):
    primes=prime_factors(n); p=primes[0]
    assert prod(primes)==n
    P=reduced_powers(n)
    T=all_transversals(n,p)
    Z=[]
    for A in T:
        Z.append({t for t in range(1,n) if is_zero_of_A(A,t,P)})
    observed=0
    for i,A in enumerate(T):
        expected_degree=prod(q**p if len({x%q for x in A})==1 else q for q in primes[1:])
        degree=0
        for B in T:
            diffs={(b-c)%n for b in B for c in B if b!=c}
            actual=all(t in Z[i] for t in diffs)
            theory=predicted(A,B,primes)
            assert actual==theory,(n,A,B,actual,theory)
            degree+=actual
        assert degree==expected_degree,(n,A,degree,expected_degree)
        observed+=degree
    expected=prod(2*q**(p+1)-q*q for q in primes[1:])
    assert observed==expected,(n,observed,expected)
    print('EXACT:',n,'vertices/side=',len(T),'pairs=',len(T)**2,'edges=',observed,'rank=',2**(len(primes)-1))
    return len(T)**2


def test_eigen(n):
    import numpy as np
    primes=prime_factors(n);p=primes[0];T=all_transversals(n,p)
    if len(T)>500:return
    M=np.fromiter((int(predicted(A,B,primes)) for A in T for B in T),dtype=float,count=len(T)**2).reshape(len(T),len(T))
    vals=np.linalg.eigvalsh(M)
    desired=[1.]
    for q in primes[1:]:
        rt=np.sqrt(4*q**(p+1)-3*q*q)
        new=[(q+rt)/2,(q-rt)/2]
        desired=[a*b for a in desired for b in new]
    got=vals[np.abs(vals)>1e-6]
    assert len(got)==len(desired),(n,len(got),len(desired))
    assert np.allclose(np.sort(got),np.sort(desired),rtol=1e-9,atol=1e-8)
    print('EIGEN:',n,'nonzero=',[round(y,8) for y in sorted(got)])


def test_sample_105():
    import random
    n=105;p=3;primes=[3,5,7]
    P=reduced_powers(n)
    choices=all_transversals(n,p)
    r=random.Random(314159)
    for _ in range(1200):
        A=r.choice(choices); B=r.choice(choices)
        actual=all(is_zero_of_A(A,(u-v)%n,P) for u in B for v in B if u!=v)
        assert actual==predicted(A,B,primes),(A,B)
    print('EXACT SAMPLE: 105 1200 CRT/Fourier matches')


if __name__=='__main__':
    count=0
    for n in (6,10,15,21,30,42):
        count+=test_full(n)
        test_eigen(n)
    test_sample_105()
    print('PASSED:',count,'exhaustive pair comparisons + 1200 samples; exact cyclotomic arithmetic')

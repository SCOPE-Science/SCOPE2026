#!/usr/bin/env python3
"""Exact finite checks for the two prime-progression certificates."""
from math import gcd, isqrt

def is_prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, isqrt(n)+1))

def direct(p, q, r):
    n = p * q * r
    return sum(gcd(m, n) == 1 and gcd((m-1)//2, n) == 1
               for m in range(1, n + 1, 2))

def certificate(p, q, r):
    P=p*q
    assert r > P and is_prime(r)
    G=[m for m in range(1,P+1)
       if m%p not in (0,1) and m%q not in (0,1)]
    O=sum(m%2 for m in G)
    # Independent direct inverse construction for each forbidden lift.
    inverse=pow(P,-1,r)
    B=sum((m+P*((c-m)*inverse%r))%2 for m in G for c in (0,1))
    # A second computation via the base-P CRT digit u.
    uinv=pow(r,-1,P)
    B2=0
    for m in G:
        for c in (0,1):
            u=((m-c)*uinv)%P
            assert 1 <= u < P
            k=(u*r+c-m)//P
            assert 0 <= k < r and (u*r+c-m)%P==0
            B2+=(m+P*k)%2
    assert B==B2
    T=len(G)*((r-1)//2)+O-B
    S=(p-2)*(q-2)*(r-2)
    assert 2*T-S==len(G)+2*O-2*B
    assert direct(p,q,r)==T
    return (len(G),O,B,S,T,2*T-S)

if __name__=='__main__':
    expected=[(5,23,349,(63,30,68,21861,10924,-13)),
              (7,17,269,(75,38,70,20025,10018,11))]
    for p,q,r,answer in expected:
        assert certificate(p,q,r)==answer
        print('PRIMARY_CERTIFICATE_OK',p,q,r,answer)
    for p,q,rs,delta in [(5,23,(349,809,1039),-13),
                          (7,17,(269,983),11)]:
        P=p*q
        assert all(is_prime(r) and r>P for r in rs)
        assert len({r%(2*P) for r in rs})==1
        for r in rs:
            assert certificate(p,q,r)[-1]==delta
        print('RESIDUE_PERIOD_SPOTCHECK_OK',p,q,rs)
    print('VERIFY_OK finite_certificates_only=True analytic_infinitude_uses_Dirichlet=True independent_audit=False')

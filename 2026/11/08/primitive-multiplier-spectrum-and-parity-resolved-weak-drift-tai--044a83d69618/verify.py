#!/usr/bin/env python3
"""Exact finite-prefix checks for positive-height primitive Dyck spectra."""
from collections import Counter
from itertools import product
from math import comb, gcd


def mobius(k):
    p=2
    out=1
    while p*p<=k:
        if k%p==0:
            k//=p
            if k%p==0:
                return 0
            out=-out
            while k%p==0:
                k//=p
        p+=1
    if k>1:
        out=-out
    return out


def fixed(M,n,d):
    if d<1 or d>n or (n-d)%2:
        return 0
    return comb(n,(n-d)//2)*M**((n+d)//2)


def primitive(M,n,d):
    ans=0
    for k in range(1,gcd(n,d)+1):
        if n%k==0 and d%k==0:
            ans+=mobius(k)*fixed(M,n//k,d//k)
    return ans


def run():
    cases=0
    for M,maxn in [(2,10),(3,8)]:
        alphabet=range(M+1)  # 0..M-1 left brackets, M generic right bracket
        for n in range(1,maxn+1):
            hist=Counter()
            for w in product(alphabet,repeat=n):
                d=2*sum(u<M for u in w)-n
                if d<=0:
                    continue
                period=next(k for k in range(1,n+1) if n%k==0 and all(w[i]==w[i%k] for i in range(n)))
                if period==n:
                    hist[d]+=1
            for d in range(1,n+1):
                assert hist[d]==primitive(M,n,d),(M,n,d,hist[d],primitive(M,n,d))
                if d%2==n%2:
                    assert primitive(M,n,d)>=0
                cases+=1
            if n%2==1:
                assert primitive(M,n,1)==comb(n,(n-1)//2)*M**((n+1)//2)
            else:
                m=n//2
                expected=comb(2*m,m-1)*M**(m+1)
                if m%2:
                    expected-=comb(m,(m-1)//2)*M**((m+1)//2)
                assert primitive(M,n,2)==expected
    print('DYCK_PRIMITIVE_MULTIPLIER_EXACT_OK', 'M=2,3', 'tested_cases=',cases)

if __name__=='__main__':
    run()

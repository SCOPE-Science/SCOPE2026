#!/usr/bin/env python3
"""Exact small-case checks for finite-poset one-point extensions.
Standard library only; not an infinite-size proof.
"""
from itertools import product
from fractions import Fraction
from math import comb


def direct_types(a, b, edges):
    """Independently close the full (a+b+1)-point strict order transitively."""
    n=a+b
    base={(i,a+j) for i,j in edges}
    out=0
    for states in product((0,1,2), repeat=n): # 0: ||, 1: parameter<x, 2: x<parameter
        reach=[0]*(n+1)
        for i,j in base: reach[i]|=1<<j
        for i,s in enumerate(states):
            if s==1:reach[i]|=1<<n
            elif s==2:reach[n]|=1<<i
        for k in range(n+1):
            for i in range(n+1):
                if (reach[i]>>k)&1:reach[i]|=reach[k]
        if any((reach[i]>>i)&1 for i in range(n+1)):continue
        if any(((reach[i]>>j)&1)!=((i,j) in base) for i in range(n) for j in range(n)):
            continue
        if any(((reach[i]>>n)&1)!=(states[i]==1) or ((reach[n]>>i)&1)!=(states[i]==2) for i in range(n)):
            continue
        out+=1
    return out


def formula_types(a,b,edges):
    E=set(edges)
    ans=0
    for X in range(1<<a):
        for Y in range(1<<b):
            # family 1: A only below; B only above
            if all((i,j) in E for i in range(a) if X>>i&1 for j in range(b) if Y>>j&1):
                ans+=1
    # family 2: some A above x, and no B below x
    for X in range(1,1<<a):
        for Y in range(1<<b): # B above x on Y, otherwise incomparable
            if all((i,j) not in E for i in range(a) if X>>i&1 for j in range(b) if not Y>>j&1):
                ans+=1
    # family 3: some B below x, and no A above x
    for Y in range(1,1<<b):
        for X in range(1<<a): # A below x on X, otherwise incomparable
            if all((i,j) not in E for i in range(a) if not X>>i&1 for j in range(b) if Y>>j&1):
                ans+=1
    return ans


def expected(a,b,p):
    q=1-p
    return (sum(comb(a,i)*(1+p**i)**b for i in range(a+1))
            +sum(comb(a,i)*(1+q**i)**b for i in range(1,a+1))
            +sum(comb(b,j)*(1+q**j)**a for j in range(1,b+1)))


def exact_moment(a,b,p):
    pairs=list(product(range(a),range(b)))
    q=1-p
    total=Fraction(0,1)
    for mask in range(1<<len(pairs)):
        edges={pairs[t] for t in range(len(pairs)) if mask>>t&1}
        count=mask.bit_count()
        total+=direct_types(a,b,edges)*(p**count)*(q**(a*b-count))
    return total


def deleted_matching(a,b,k):
    edges={(i,j) for i in range(a) for j in range(b) if i!=j or i>=k}
    return edges


def main():
    checked=0
    for a in range(1,4):
        for b in range(1,4):
            if a*b>9:continue
            pairs=list(product(range(a),range(b)))
            for mask in range(1<<len(pairs)):
                E={pairs[t] for t in range(len(pairs)) if mask>>t&1}
                assert direct_types(a,b,E)==formula_types(a,b,E),(a,b,E)
                checked+=1
    print('PASS direct versus disjoint-family count:',checked,'bipartite posets, parts <=3')
    samples=0
    for a in range(1,5):
        for b in range(1,5):
            for k in range(min(a,b)+1):
                got=direct_types(a,b,deleted_matching(a,b,k))
                pred=2**(a+b-2*k)*3**k+2**a+2**b-2+2*k
                assert got==pred,(a,b,k,got,pred)
                samples+=1
    print('PASS deleted-matching exact counts:',samples,'(a,b,k) triples with a,b<=4')
    samples=0
    for a,b in [(1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(3,3)]:
        for p in (Fraction(1,3),Fraction(2,3)):
            m=exact_moment(a,b,p)
            f=expected(a,b,p)
            assert m==f,(a,b,p,m,f)
            samples+=1
    print('PASS annealed exact expectation:',samples,'(a,b,p) checks using rational weights')
    for n in range(1,6):
        assert direct_types(n,n,deleted_matching(n,n,0)) == 4**n+2**(n+1)-2
        assert direct_types(n,n,deleted_matching(n,n,n)) == 3**n+2**(n+1)-2+2*n
    print('PASS complete and fully matching-deleted endpoints through n=5')
    print('VERIFY_OK')
if __name__=='__main__':main()

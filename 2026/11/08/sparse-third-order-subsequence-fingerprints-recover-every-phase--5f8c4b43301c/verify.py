#!/usr/bin/env python3
"""Self-contained finite checks of cyclic binary subsequence phase signatures.
Usage: python3 verify.py
"""
from math import gcd, comb
from itertools import product
from collections import Counter


def subseq_counts(w):
    # Independent one-pass dynamic programming for counts of every pattern <=3.
    d = {'': 1}
    for ch in w:
        for ell in (2,1,0):
            for x in product('01', repeat=ell):
                s = ''.join(x)
                d[s + ch] = d.get(s + ch,0) + d.get(s,0)
    return d


def sig(w):
    d = subseq_counts(w)
    return d.get('01',0), d.get('001',0)


def deck3(w):
    d = subseq_counts(w)
    return tuple(d.get(''.join(t), 0) for ell in (1,2,3) for t in product('01',repeat=ell))


def zword(a,b,m,s):
    return '0'*s + '1'*b + ('0'*a+'1'*b)*(m-1) + '0'*(a-s)


def oword(a,b,m,t):
    return '1'*t + ('0'*a+'1'*b)*(m-1) + '0'*a + '1'*(b-t)


def z_formula(a,b,m,s):
    p01 = b*m*s + a*b*m*(m-1)//2
    p001 = b*sum(comb(s+j*a,2) for j in range(m))
    return p01,p001


def o_formula(a,b,m,t):
    p01 = a*b*m*(m-1)//2 + a*m*(b-t)
    p001 = b*sum(comb(j*a,2) for j in range(1,m))+(b-t)*comb(m*a,2)
    return p01,p001


def run():
    tests=0
    pair_checks=0
    for a in range(1,13):
        for b in range(1,13):
            g=gcd(a,b)
            for m in range(1,6):
                p=a+b
                phases=[]
                first=[]
                for s in range(1,a+1):
                    w=zword(a,b,m,s)
                    assert len(w)==m*p
                    val=sig(w)
                    assert val==z_formula(a,b,m,s)
                    phases.append(val)
                    first.append(val[0])
                    tests+=1
                for t in range(1,b+1):
                    w=oword(a,b,m,t)
                    assert len(w)==m*p
                    val=sig(w)
                    assert val==o_formula(a,b,m,t)
                    phases.append(val)
                    first.append(val[0])
                    tests+=1
                assert len(set(phases))==p
                assert len(set(first))==p-g+1
                # Check sharp enumeration and exact gap, for every collision.
                collisions=0
                for s in range(1,a+1):
                    for t in range(1,b+1):
                        if z_formula(a,b,m,s)[0] == o_formula(a,b,m,t)[0]:
                            collisions+=1
                            lhs=o_formula(a,b,m,t)[1]-z_formula(a,b,m,s)[1]
                            assert 2*lhs == b*m*s*(a-s) and lhs>0
                        pair_checks+=1
                assert collisions==g-1
    # Existence of a four-run period with distinct 3-binomially equivalent conjugates.
    w='01100011'
    v=w[2:]+w[:2]
    assert w!=v and deck3(w)==deck3(v)
    for m in range(1,7):
        assert deck3(w*m)==deck3(v*m)
        assert w*m!=v*m
    print('PASS: %d direct pattern-count checks; %d cross-phase comparisons; %d four-run power cases' % (tests,pair_checks,6))
    print('PASS: all (a,b,m) in [1,12]^2 x [1,5] have %d tested parameter tuples' % (12*12*5))

if __name__=='__main__':
    run()

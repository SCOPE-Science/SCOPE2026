#!/usr/bin/env python3
"""Finite checks for binary truncated-polynomial multiplicative Davenport laws.
All computations are direct integer-bitmask arithmetic over F_2[t]/(t^n).
The mathematical proof is independent of this finite verifier.
"""
from itertools import combinations_with_replacement, product
from random import Random


def mul(a,b,n):
    mask=(1<<n)-1
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a=(a<<1)&mask
    return z


def valuation(a,n):
    return n if a==0 else ((a&-a).bit_length()-1)


def e_odd(j,n):
    e=0
    while j*(1<<e)<n:e+=1
    return e


def generators(n):
    return [(j,1+(1<<j),1<<e_odd(j,n)) for j in range(1,n,2)]


def group_d(n):
    return 1+sum(o-1 for j,g,o in generators(n))


def is_irreducible(seq,n):
    L=len(seq)
    full=1
    for a in seq:full=mul(full,a,n)
    for m in range((1<<L)-1):
        q=1
        for i,a in enumerate(seq):
            if m>>i&1:q=mul(q,a,n)
        if q==full:return False
    return True


def predicted_irreducible(seq,n):
    non=[a for a in seq if valuation(a,n)>0]
    units=[a for a in seq if valuation(a,n)==0]
    V=sum(valuation(a,n) for a in non)
    if V>=n:
        return not units and all(V-valuation(a,n)<n for a in non)
    modn=n-V
    # group subproduct identity modulo t^(n-V), from any nonempty unit subset
    for m in range(1,1<<len(units)):
        q=1
        for i,a in enumerate(units):
            if m>>i&1:q=mul(q,a,modn)
        if q==1:return False
    return True


def unit_extremal(n):
    return [g for j,g,o in generators(n) for _ in range(o-1)]


def check():
    checks=0
    for n in range(1,13):
        gs=generators(n)
        values={1}
        for j,g,order in gs:
            powers=[];q=1
            for _ in range(order):
                powers.append(q);q=mul(q,g,n)
            assert q==1
            old=values
            values={mul(a,b,n) for a in old for b in powers}
            assert len(values)==len(old)*order,(n,j)
            checks+=2
        assert values=={a for a in range(1,1<<n,2)}
        checks+=1
        d=group_d(n)
        assert d==1+sum(o-1 for _,_,o in gs)
        assert d==1+sum((m&-m) for m in range(1,n))
        checks+=2
        if n>=2:
            assert d-group_d(n-1)>=(1 if n%2==0 else 2)
            if n%2==0:assert d-group_d(n-1)==1
            checks+=1
        if n<=8:
            seq=unit_extremal(n)
            assert len(seq)==d-1
            assert is_irreducible(seq,n)
            checks+=2
            if n%2==0 and n>=4:
                seq=[2]+unit_extremal(n-1)
                assert len(seq)==d-1
                assert is_irreducible(seq,n)
                checks+=2
    # Exhaustively test the theorem's *reduction criterion* on all multisets of <=4 for n<=5.
    for n in range(1,6):
        elems=range(1<<n)
        for length in range(0,5):
            for seq in combinations_with_replacement(elems,length):
                assert is_irreducible(seq,n)==predicted_irreducible(seq,n),(n,seq)
                checks+=1
    # Independently verify Davenport cutoff for all full multisets for n<=4.
    for n in range(1,5):
        bound=max(group_d(n),n+1)
        witness=unit_extremal(n) if group_d(n)==bound else [2]*n
        assert len(witness)==bound-1 and is_irreducible(witness,n)
        checks+=1
        for seq in combinations_with_replacement(range(1<<n),bound):
            assert not is_irreducible(seq,n),(n,seq)
            checks+=1
    # Classify *all* extremal irreducible multisets at the small depths.
    for n in range(1,5):
        L=max(group_d(n),n+1)-1
        observed=set()
        for seq in combinations_with_replacement(range(1<<n),L):
            if not is_irreducible(seq,n):continue
            vals=tuple(sorted(valuation(x,n) for x in seq if valuation(x,n)>0))
            observed.add(vals)
        expected=({(1,)} if n==1 else
                  {(1,1)} if n==2 else
                  {(),(1,1,1)} if n==3 else
                  {(),(1,),(1,1,1,1)})
        assert observed==expected,(n,observed,expected)
        checks+=1
    # Independently enumerate each fixed-nonunit-count maximum at small depths.
    for n in range(1,5):
        observed={r:-1 for r in range(n+1)}
        for length in range(0,max(group_d(n),n+1)):
            for seq in combinations_with_replacement(range(1<<n),length):
                if is_irreducible(seq,n):
                    r=sum(valuation(a,n)>0 for a in seq)
                    observed[r]=max(observed[r],length)
        expected={r:(group_d(n)-1 if r==0 else
                     n if r==n else r+group_d(n-r)-1) for r in range(n+1)}
        assert observed==expected,(n,observed,expected)
        checks+=1
    # Test random longer sequences versus independent all-proper-subsequence routine.
    rng=Random(240618)
    for n in range(5,9):
        for _ in range(250):
            seq=tuple(rng.randrange(1<<n) for k in range(rng.randrange(0,10)))
            assert is_irreducible(seq,n)==predicted_irreducible(seq,n)
            checks+=1
    print('PASS',checks,'finite assertions; exact unit-group generation for n=1..12;')
    print('exhaustive irreducibility classification up to length 4 for n=1..5;')
    print('exhaustive Davenport cutoffs, inverse profiles and fixed-r maxima for n=1..4;')
    print('1000 random longer instances;')
    print('explicit extremal witnesses checked for n<=8.')
    print('n | D(U) | D(S)')
    for n in range(1,13):print(n,group_d(n),max(group_d(n),n+1))

if __name__=='__main__':check()

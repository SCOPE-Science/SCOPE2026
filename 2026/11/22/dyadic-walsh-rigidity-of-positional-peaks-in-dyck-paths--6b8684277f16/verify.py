#!/usr/bin/env python3
"""Exact integer checks for Walsh spectra of positional Dyck peaks.

All calculations use the ordinary, unnormalized binary Walsh transform.
The checks are finite corroboration of the separately written all-order proof.
"""
from math import comb


def catalan(n):
    return comb(2*n,n)//(n+1)


def paths(n):
    """Yield every Dyck word by independent balanced-prefix recursion."""
    def rec(u,d,seq):
        if u==d==n:
            yield tuple(seq)
        if u<n:
            yield from rec(u+1,d+0,seq+(1,))
        if d<u:
            yield from rec(u,d+1,seq+(0,))
    yield from rec(0,0,())


def incidence(word):
    return sum(1<<i for i in range(len(word)-1) if word[i:i+2]==(1,0))


def fwht(a):
    step=1
    while step<len(a):
        for start in range(0,len(a),2*step):
            for i in range(start,start+step):
                x,y=a[i],a[i+step]
                a[i],a[i+step]=x+y,x-y
        step*=2
    return a


def indie_coefficients(mask,width):
    """Counts of independent subsets of the selected vertices of a path."""
    no=[1]
    yes=[0]
    for i in range(width):
        joined=[(no[k] if k<len(no) else 0)+(yes[k] if k<len(yes) else 0)
                for k in range(max(len(no),len(yes)))]
        if (mask>>i)&1:
            new_yes=[0]+no
            no,yes=joined,new_yes
        else:
            no,yes=joined,[0]
    return [(no[k] if k<len(no) else 0)+(yes[k] if k<len(yes) else 0)
            for k in range(max(len(no),len(yes)))]


def formula(n,mask):
    return sum(c*(-2)**k*catalan(n-k)
               for k,c in enumerate(indie_coefficients(mask,2*n-1)) if c)


def valuation(x):
    assert x!=0
    return (abs(x)&-abs(x)).bit_length()-1


def check():
    # Strongest finite comparison: independent enumeration against the
    # Catalan-contraction formula for every Walsh character in small orders.
    for n in range(1,9):
        width=2*n-1
        f=[0]*(1<<width)
        dycks=list(paths(n))
        assert len(dycks)==catalan(n)
        for p in dycks:
            f[incidence(p)]+=1
        f=fwht(f)
        for mask,x in enumerate(f):
            assert formula(n,mask)==x,(n,mask,x)
        zeros=sum(x==0 for x in f)
        if n%2:
            v=valuation(catalan(n))
            assert all(x!=0 and valuation(x)==v for x in f)
        else:
            assert f[-1]==0
        print('EXHAUSTIVE',n,len(f),'characters',len(dycks),'paths','zeros',zeros)
    # Wider independently enumerated character sets; factorially cheaper
    # sample formula tests retain a direct Walsh transform of every path.
    for n in (9,10):
        width=2*n-1
        f=[0]*(1<<width)
        ct=0
        for p in paths(n):
            f[incidence(p)]+=1
            ct+=1
        assert ct==catalan(n)
        f=fwht(f)
        for mask in range(0,len(f),max(1,len(f)//2048)):
            assert formula(n,mask)==f[mask]
        if n%2:
            assert all(x!=0 and valuation(x)==valuation(catalan(n)) for x in f)
        else:
            assert f[-1]==0
        print('ALL-CHARACTERS',n,len(f),'characters',ct,'paths','zeros',sum(x==0 for x in f))
    # Check the key simultaneous contraction claim independently of the
    # Fourier transform: all compatible forced peak sets at a fixed order.
    n=6
    marks=[incidence(p) for p in paths(n)]
    for j in range(1<<(2*n-1)):
        if j&(j<<1):
            continue
        k=j.bit_count()
        assert sum((x&j)==j for x in marks)==catalan(n-k),(j,k)
    print('SIMULTANEOUS-PEAK-CONTRACTION',n,'all admissible forced masks')
    # The analytically exact valuation inequality for odd n depends only on
    # binary digit sums; these finite cases check its boundary conditions.
    s2=lambda x:x.bit_count()
    for n in range(1,501,2):
        for k in range(1,n+1):
            assert k+s2(n+1-k)>s2(n+1)
    print('BINARY-VALUATION-INEQUALITY','odd semilengths 1..499 and all k')
    print('PASS')


if __name__=='__main__':
    check()

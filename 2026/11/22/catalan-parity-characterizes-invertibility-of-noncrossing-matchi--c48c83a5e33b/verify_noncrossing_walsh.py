#!/usr/bin/env python3
"""Exact checks for Walsh singularity of noncrossing matching indicators.

All calculations use integer arithmetic. The full Walsh spectrum is checked
for n <= 4, and reflection-constructed zero certificates for n <= 30.
This is supplementary evidence, not a substitute for the all-size proof.
"""
from functools import lru_cache
from math import comb


def catalan(n):
    return comb(2*n, n)//(n+1)


def witness(n):
    """A frequency with vanishing transform when n is not 2**k-1."""
    if n < 1 or catalan(n) % 2:
        return None
    root = {(0, j) for j in range(1, n, 2)}
    if n % 2 == 0:
        return frozenset(root)
    m = (n-1)//2
    T = witness(m)
    assert T is not None
    for a,b in T:
        left = (a+1,b+1)
        right = (2*n-1-b, 2*n-1-a)
        root.add(left)
        root.add(right)
    return frozenset(root)


def signed_count(n, S):
    """Sum of characters over noncrossing perfect matchings on [0,2n)."""
    @lru_cache(None)
    def rec(a,b):
        if a == b:
            return 1
        if a > b or (b-a)%2:
            return 0
        total=0
        for j in range(a+1,b,2):
            sign=-1 if (a,j) in S else 1
            total+=sign*rec(a+1,j)*rec(j+1,b)
        return total
    return rec(0,2*n)


def all_matchings(n):
    @lru_cache(None)
    def rec(a,b):
        if a == b:return (frozenset(),)
        return tuple(frozenset({(a,j)}|set(x)|set(y))
                     for j in range(a+1,b,2)
                     for x in rec(a+1,j)
                     for y in rec(j+1,b))
    return rec(0,2*n)


def exhaustive_walsh(n):
    E=[(i,j) for i in range(2*n) for j in range(i+1,2*n)
       if (j-i)%2]
    mats=all_matchings(n)
    mapped=[]
    for M in mats:
        v=sum(1<<k for k,e in enumerate(E) if e in M)
        mapped.append(v)
    zero=0
    for freq in range(1<<len(E)):
        s=sum(1-2*((freq & v).bit_count()%2) for v in mapped)
        if s==0:zero+=1
        if len(mats)%2==1:assert s%2==1
    return len(E),len(mats),zero


def main():
    checked=0
    for n in range(1,31):
        expected=(n & (n+1))==0
        assert (catalan(n)%2==1)==expected
        w=witness(n)
        if expected:
            assert w is None
        else:
            assert w is not None
            assert all((b-a)%2 for a,b in w)
            assert signed_count(n,w)==0,(n,w)
            assert signed_count(n,frozenset())==catalan(n)
        checked+=1
    for n in range(1,5):
        dim,card,zero=exhaustive_walsh(n)
        assert card==catalan(n)
        assert (zero==0)==((n&(n+1))==0)
        print('full Fourier check n={}, admissible edges={}, Catalan={}, zeros={}'.format(n,dim,card,zero))
    print('PASS: reflection witnesses and parity for all 1 <= n <= 30;'
          ' exhaustive all frequencies through n=4; 30 dimension checks')


if __name__=='__main__':
    main()

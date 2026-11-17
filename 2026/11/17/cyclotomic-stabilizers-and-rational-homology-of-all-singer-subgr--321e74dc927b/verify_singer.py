#!/usr/bin/env python3
"""Finite arithmetic and small-field checks for Singer-building quotient formulas.

Standard-library-only. Does not certify a general topological theorem; the
unrestricted result uses the arguments in RESULT.md.
"""
from itertools import combinations, product
from math import gcd, lcm


def divisors(n):
    lo=[];hi=[]
    d=1
    while d*d<=n:
        if n%d==0:
            lo.append(d)
            if d*d!=n: hi.append(n//d)
        d+=1
    return lo+hi[::-1]


def primes(n):
    ans = []
    t = 2
    while t*t <= n:
        if n % t == 0:
            ans.append(t)
            while n % t == 0:
                n //= t
        t += 1
    if n > 1:
        ans.append(n)
    return ans


def mobius(n):
    p = primes(n)
    if any(n % (z*z) == 0 for z in p):
        return 0
    return (-1) ** len(p)


def cyclotomic_at(n, q):
    a = 1
    b = 1
    for d in divisors(n):
        e = mobius(n//d)
        if e == 1:
            a *= q**d - 1
        elif e == -1:
            b *= q**d - 1
    assert a % b == 0
    return a//b


def predicted(n, q, t):
    M = (q**n - 1)//(q - 1)
    assert M % t == 0
    phi = cyclotomic_at(n, q)
    assert M % phi == 0
    L = M//phi
    sizes = {d:(q**d-1)//(q-1) for d in divisors(n)}
    exact = {d:sum(mobius(d//e)*gcd(t,sizes[e]) for e in divisors(d))
             for d in divisors(n)}
    assert sum(exact.values()) == t and min(exact.values()) >= 0
    chi_signed = 0
    for d, count in exact.items():
        m = n//d
        fixed_reduced_chi = (-1 if m%2 else 1)*q**(d*(m*(m-1)//2))
        chi_signed += count*fixed_reduced_chi
    assert chi_signed % t == 0
    reduced_chi = chi_signed//t
    betti = reduced_chi*(1 if n%2 == 0 else -1)
    assert betti >= 0
    return (t//gcd(t,L), betti, exact)


def gf_mult(a, b, n, polynomial):
    mask = (1<<n)-1
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1<<n):
            a ^= polynomial
        a &= mask
    return out


def gf_pow(a, e, n, polynomial):
    o = 1
    while e:
        if e&1:
            o = gf_mult(o,a,n,polynomial)
        a = gf_mult(a,a,n,polynomial)
        e >>= 1
    return o


def enumerate_subspaces(n):
    """Canonical binary RREF bases, returned as (dimension, set of vector bits)."""
    for k in range(0,n+1):
        for pivots in combinations(range(n),k):
            free_positions = [(r,j) for r,p in enumerate(pivots)
                              for j in range(p+1,n) if j not in pivots]
            for bits in product((0,1),repeat=len(free_positions)):
                rows = [1<<p for p in pivots]
                for (r,j),b in zip(free_positions,bits):
                    if b:
                        rows[r] |= 1<<j
                span = {0}
                for v in rows:
                    span |= {w^v for w in list(span)}
                assert len(span)==(1<<k)
                yield k,frozenset(span)


def gaussian(m,k,Q):
    if k<0 or k>m:
        return 0
    top=bottom=1
    for j in range(k):
        top*=Q**(m-j)-1
        bottom*=Q**(k-j)-1
    assert top%bottom==0
    return top//bottom


def check_binary_field(n,poly):
    # The polynomial must be primitive: x has multiplicative order 2**n-1.
    alpha = 2
    assert gf_pow(alpha,(1<<n)-1,n,poly)==1
    for p in primes((1<<n)-1):
        assert gf_pow(alpha,((1<<n)-1)//p,n,poly)!=1
    subs=list(enumerate_subspaces(n))
    assert len(subs)=={4:67,6:2825}[n]
    elements=[gf_pow(alpha,j,n,poly) for j in range((1<<n)-1)]
    assert len(set(elements))==len(elements)
    buckets={d:0 for d in divisors(n)}
    representatives = {}
    for a in elements:
        deg=next(d for d in divisors(n) if gf_pow(a,1<<d,n,poly)==a)
        buckets[deg]+=1
        if deg in representatives:
            continue
        representatives[deg]=a
        rank_counts={k:0 for k in range(1,n)}
        for k,S in subs:
            if k in (0,n):
                continue
            # A subspace is invariant iff every basis element is carried in it,
            # equivalently all elements of the finite span are carried in it.
            if all(gf_mult(a,v,n,poly) in S for v in S):
                rank_counts[k]+=1
        for k in range(1,n):
            expected=gaussian(n//deg,k//deg,1<<deg) if k%deg==0 else 0
            assert rank_counts[k]==expected, (n,a,deg,k,rank_counts[k],expected)
    expected_counts=predicted(n,2,(1<<n)-1)[2]
    assert buckets==expected_counts,(buckets,expected_counts)
    print('DIRECT_FIELD',n,'proper subspaces',len(subs)-2,'degree buckets',buckets)
    if n==4:
        # Enumerate actual flags and action-orbits in the binary rank-four building.
        proper=[(k,S) for k,S in subs if 1<=k<n]
        bydim={k:[S for h,S in proper if h==k] for k in range(1,n)}
        flags=[]
        for length in range(1,n):
            for dimensions in combinations(range(1,n),length):
                for seq in product(*(bydim[d] for d in dimensions)):
                    if all(seq[j]<seq[j+1] for j in range(length-1)):
                        flags.append(seq)
        orbit_set=set()
        cell_orbits=[0]*(n-1)
        for seq in flags:
            canonical=min(tuple(tuple(sorted(gf_mult(a,v,n,poly) for v in S))
                                for S in seq) for a in elements)
            if canonical not in orbit_set:
                orbit_set.add(canonical)
                cell_orbits[len(seq)-1]+=1
        chi=sum(((-1)**k)*z for k,z in enumerate(cell_orbits))
        reduced_chi=chi-1
        assert reduced_chi==predicted(4,2,15)[1]
        print('DIRECT_FLAGS',n,'cell orbits',cell_orbits,'Euler',chi)


def main():
    for n in range(4,17):
        for q in (2,3,4,5,7):
            M=(q**n-1)//(q-1)
            L=M//cyclotomic_at(n,q)
            assert L==(lcm(*[q**(n//p)-1 for p in primes(n)])//(q-1))
            for t in divisors(M):
                group_order,betti,exact=predicted(n,q,t)
                assert group_order>=1 and betti>=0
                assert group_order==t//gcd(t,L)
    print('ARITHMETIC_OK', 'n=4..16', 'q=2,3,4,5,7', 'all subgroup orders')
    for n,poly in ((4,0b10011),(6,0b1000011)):
        check_binary_field(n,poly)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()

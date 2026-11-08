#!/usr/bin/env python3
"""Reproduce finite checks for the coset shattering polynomial.

Theorems for arbitrary moduli require the proof in RESULT.md; this script
checks small cases using explicit trace enumeration and independent local
counting, and tests selected larger structured supports.
"""
from itertools import combinations, product, permutations
from math import comb, factorial, gcd, prod


def prime_powers(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                a += 1
                n //= p
            out.append((p, a))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def private_count(p, a, r):
    q = p**a
    return q*(q-1) + q*(p**(r-2)-1)*sum(
        p**((b-1)*(r-2))*(q-p**b) for b in range(1, a)
    )


def coeff(n, r):
    if r == 0:
        return 1
    if r == 1:
        return n if n >= 2 else 0
    if r == 2:
        return comb(n, 2) if n >= 3 else 0
    f = prime_powers(n)
    raw = sum(
        (-1)**j * comb(r,j) * prod(
            p**(a*r)-j*private_count(p,a,r) for p,a in f
        ) for j in range(r+1)
    )
    assert raw % factorial(r) == 0
    return raw//factorial(r)


def coset_bits(n):
    return tuple(set(sum(1<<x for x in range(n) if x%d == v)
                     for d in range(1,n+1) if n%d==0 for v in range(d)))


def shattered(support, masks):
    required = (1 << (1 << len(support))) - 1
    found = 0
    for m in masks:
        pattern = sum((1<<j) for j,x in enumerate(support) if (m>>x)&1)
        found |= 1<<pattern
        if found == required:
            return True
    return False


def direct_coefficient(n, r, masks=None):
    if masks is None:
        masks = coset_bits(n)
    return sum(shattered(s,masks) for s in combinations(range(n),r))


def local_private_direct(p,a,r,i=0):
    q=p**a
    result=0
    for x in product(range(q),repeat=r):
        found=False
        for k in range(1,a+1):
            m=p**k
            others=[x[j]%m for j in range(r) if j!=i]
            if len(set(others)) == 1 and x[i]%m != others[0]:
                found=True
                break
        result+=found
    return result


def local_private_labels(p,a,r,x):
    labels=[]
    for i in range(r):
        for k in range(1,a+1):
            m=p**k
            other={x[j]%m for j in range(r) if j!=i}
            if len(other)==1 and x[i]%m not in other:
                labels.append(i)
                break
    return labels


def crt_lift(primes, residues):
    n=prod(primes)
    return next(v for v in range(n) if all(v%p==u for p,u in zip(primes,residues)))


def main():
    local=0
    for p,a,r in [(2,1,3),(2,2,3),(2,3,3),(3,2,3),
                  (2,1,4),(2,2,4),(3,1,4),(3,2,4),(2,2,5)]:
        expected=private_count(p,a,r)
        actual=local_private_direct(p,a,r)
        assert actual==expected, (p,a,r,actual,expected)
        q=p**a
        for x in product(range(q),repeat=r):
            assert len(local_private_labels(p,a,r,x)) <= 1, (p,a,r,x)
        local+=1
    print('LOCAL_PRIVATE_PRIME_ENUMERATION_PASS cases=',local)

    supports=0
    for n in range(1,19):
        masks=coset_bits(n)
        for r in range(min(5,n)+1):
            count=direct_coefficient(n,r,masks)
            assert count==coeff(n,r), (n,r,count,coeff(n,r))
            supports+=comb(n,r)
    print('SMALL_MODULI_DIRECT_TRACES_PASS supports=',supports)

    for n in (30,42,60,70,105):
        masks=coset_bits(n)
        actual=direct_coefficient(n,3,masks)
        expected=coeff(n,3)
        assert actual==expected, (n,actual,expected)
        assert expected==prod(private_count(p,a,3) for p,a in prime_powers(n))
        print('THREE_SUPPORT_CENSUS_PASS n=',n,' count=',actual)

    # For n=210, the formula gives 10080 four-supports; build the full
    # canonical CRT family for the top coefficient and check every support.
    primes=(2,3,5,7)
    lists=[[(common, outlier) for common in range(p)
            for outlier in range(p) if outlier!=common] for p in primes]
    masks=coset_bits(210)
    seen=set()
    for pairs in product(*lists):
        coords=[]
        for i in range(4):
            coords.append(tuple(pairs[j][1] if i==j else pairs[j][0]
                                for j in range(4)))
        s=tuple(sorted(crt_lift(primes, x) for x in coords))
        assert len(set(s))==4
        assert s not in seen
        assert shattered(s,masks),s
        seen.add(s)
    assert len(seen)==coeff(210,4)==10080
    assert coeff(210,3)==170520
    print('SQUAREFREE_MAXIMUM_CRT_CENSUS_PASS n=210 count=',len(seen))
    print('ALL_COSET_SHATTERING_CHECKS_PASS')

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Independent finite-field tests for null-filiform Zinbiel commuting-tuple formula.

Usage: python3 verify.py. Only the Python standard library is needed.
"""
from itertools import product
from math import comb


def predicted(q, n, k):
    h = n // 2
    return 1 + (q**k - 1) * (
        sum(q**(n - 2*r + r*k) for r in range(1, h + 1))
        + sum(q**(k*(n-r)) for r in range(h + 1, n + 1))
    )


def product_basis(i,j,n,q):
    return comb(i+j-1,j)%q if i+j<=n else 0


def native_commutes(a, b, q, n):
    """Check all coordinates of ab=ba using the original Zinbiel product."""
    for s in range(2, n+1):
        ab = sum(product_basis(i, s-i, n, q)*a[i-1]*b[s-i-1]
                 for i in range(1,s)) % q
        ba = sum(product_basis(i, s-i, n, q)*b[i-1]*a[s-i-1]
                 for i in range(1,s)) % q
        if ab != ba:
            return False
    return True


def valuation(a,n):
    for i,c in enumerate(a,1):
        if c:
            return i
    return n+1


def census(q,n):
    assert q > n and all(q%d for d in range(2, n+1)), (q,n)
    xs=list(product(range(q), repeat=n))
    masks=[]
    for a in xs:
        m=0
        for j,b in enumerate(xs):
            if native_commutes(a,b,q,n):
                m |= 1<<j
        masks.append(m)
    for i,a in enumerate(xs):
        r=valuation(a,n)
        expected=q**n if r==n+1 else q**(r+1 if 2*r<=n else r)
        assert masks[i].bit_count()==expected, ('centralizer',q,n,a,expected,masks[i].bit_count())
    pairs=sum(m.bit_count() for m in masks)
    triples=sum((masks[i]&masks[j]).bit_count()
                for i in range(len(xs))
                for j in range(len(xs)) if (masks[i]>>j)&1)
    assert pairs==predicted(q,n,2), ('pairs',q,n,pairs,predicted(q,n,2))
    assert triples==predicted(q,n,3), ('triples',q,n,triples,predicted(q,n,3))
    return pairs, triples


def identity(q,n):
    """Independently verify the defining Zinbiel identity on all basis triples."""
    for i,j,k in product(range(1,n+1),repeat=3):
        s=i+j+k
        if s>n:
            continue
        left=product_basis(i,j,n,q)*product_basis(i+j,k,n,q)%q
        right=(product_basis(j,k,n,q)+product_basis(k,j,n,q))*product_basis(i,j+k,n,q)%q
        assert left==right, (q,n,i,j,k,left,right)


def main():
    cases=[(3,2),(5,2),(5,3),(5,4),(7,3)]
    for q,n in cases:
        identity(q,n)
        p,t=census(q,n)
        print('exact q=%d n=%d commuting_pairs=%d commuting_triples=%d' % (q,n,p,t))
    print('VERIFY_OK 5 exhaustive independent pair/triple censuses and centralizer checks')

if __name__=='__main__':
    main()

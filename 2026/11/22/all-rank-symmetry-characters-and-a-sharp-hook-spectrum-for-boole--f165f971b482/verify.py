#!/usr/bin/env python3
"""Independent finite checks for rank-span Boolean equivariant homology."""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def integer_partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    for i in range(min(n, largest or n), 1 - 1, -1):
        for rest in integer_partitions(n - i, i):
            yield (i,) + rest


def cycle_poly(parts):
    # Product (2-t^l)-2 product (1-t^l), through t^n.
    n = sum(parts)
    a, b = [1] + [0]*n, [1] + [0]*n
    for ell in parts:
        aa = [0]*(n+1)
        bb = [0]*(n+1)
        for i in range(n+1):
            aa[i] += 2*a[i]
            bb[i] += b[i]
            if i + ell <= n:
                aa[i + ell] -= a[i]
                bb[i + ell] -= b[i]
        a, b = aa, bb
    return [x-2*y for x, y in zip(a,b)]


def char_top(parts, k):
    return (-1)**k*(sum(cycle_poly(parts)[:k+1])-1)


def hook_char(parts, r):
    n = sum(parts)
    c = [1] + [0]*n
    for ell in parts:
        d = c[:]
        for i in range(n+1-ell):
            d[i+ell] -= (-1)**ell*c[i]
        c = d
    return sum((-1)**(r-i)*c[i] for i in range(r+1))


def z_part(parts):
    out=1
    for p in set(parts):
        out *= p**parts.count(p)*factorial(parts.count(p))
    return out


def predicted_hook(n,k,r):
    return (n-k-2 if r == k else n-k-1 if r == k+1 else 0)


def fixed_chains_direct(n, parts, k):
    cycle_sets=[]
    start=0
    for ell in parts:
        cycle_sets.append(sum(1<<i for i in range(start,start+ell)))
        start += ell
    fixed=[]
    for bits in range(1, (1<<len(parts))-1):
        setbits=0
        for c, mask in enumerate(cycle_sets):
            if bits>>c&1: setbits |= mask
        fixed.append(setbits)
    fixed.sort(key=lambda x:x.bit_count())
    dim_counts=[0]*(k+1)
    for first in fixed:
        span0=first.bit_count()
        def rec(last,dim):
            dim_counts[dim] += 1
            if dim == k: return
            for nxt in fixed:
                if nxt != last and nxt & last == last and nxt.bit_count()-span0 <= k:
                    rec(nxt,dim+1)
        rec(first,0)
    return dim_counts


def predicted_faces(parts,k):
    # Count fixed chains by assigning distinct cycles to ordered increments.
    n=sum(parts)
    c=len(parts)
    counts=[2**c-2]+[0]*k
    for bits in range(1,1<<c):
        selected=[parts[i] for i in range(c) if bits>>i&1]
        if sum(selected)>k: continue
        m=len(selected)
        outside=2**(c-m)-2
        if outside<=0: continue
        for j in range(1,min(k,m)+1):
            # Number of surjections of m labelled cycles onto j increments.
            surj=sum((-1)**i*comb(j,i)*(j-i)**m for i in range(j+1))
            counts[j] += outside*surj
    return counts


def run():
    checked=0
    for n in range(3,11):
        parts=list(integer_partitions(n))
        for k in range(n-1):
            # Full rational hook spectrum from character orthogonality.
            for r in range(1,n):
                inner=sum((Fraction(char_top(p,k)*hook_char(p,r),z_part(p)) for p in parts),Fraction())
                exp=predicted_hook(n,k,r) if k>=1 else (1 if r==1 and n==2 else 0)
                # k=0 has many nonzero hooks, so only check k>=1.
                if k >= 1:
                    assert inner == exp, (n,k,r,inner,exp)
                    checked += 1
            if k>=1:
                trivial=sum((Fraction(char_top(p,k),z_part(p)) for p in parts),Fraction())
                assert trivial==0, (n,k,trivial)
            idtrace=char_top((1,)*n,k)
            if k==0:
                assert idtrace == 2**n-3
            else:
                prior=char_top((1,)*n,k-1)
                assert idtrace == comb(n,k)*(2**(n-k)-2)-prior, (n,k,idtrace,prior)
    direct_cases=0
    direct_faces=0
    for n in range(3,7):
        for p in integer_partitions(n):
            for k in range(n-1):
                exact=fixed_chains_direct(n,p,k)
                expect=predicted_faces(p,k)
                assert exact==expect, (n,p,k,exact,expect)
                assert char_top(p,k) == (-1)**k*(sum((-1)**j*value for j,value in enumerate(exact))-1)
                direct_cases +=1
                direct_faces +=sum(exact)
    print('VERIFY_OK hook_inner_products=%d direct_cases=%d fixed_simplices_checked=%d' %(checked,direct_cases,direct_faces))

if __name__=='__main__':run()

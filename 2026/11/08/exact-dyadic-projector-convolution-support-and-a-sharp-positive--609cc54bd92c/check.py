#!/usr/bin/env python3
"""Standalone exact integer check of the dyadic rank-one projector two-sum law."""
from collections import Counter


def projectors(n):
    # A trace-one 2x2 matrix with determinant zero is idempotent.
    return [(a,b,c) for a in range(n) for b in range(n) for c in range(n)
            if (a*(1-a)-b*c) % n == 0]


def valuation(a, k):
    return k if a == 0 else min(k, (a & -a).bit_length()-1)


def prediction(u, v, w, k):
    n=1 << k
    t=(u-1) % n
    j=min(valuation(t,k), valuation(v,k), valuation(w,k))
    if j == k:
        return 'exact', 3*(1 << (2*k-1))
    if j == 0:
        if t & 1 and not(v & 1 or w & 1):
            return 'bound', 1 << (k+1)
        return 'exact', 1 << (k+1)
    m=1 << (k-j)
    a=(t >> j) % m
    b=(v >> j) % m
    c=(w >> j) % m
    if a&1 and not(b&1 or c&1):
        return 'exact', 0
    det=(-a*a-b*c) % 2
    return 'exact', (1 << (k+j)) if det else (1 << (k+j+1))


def check(k):
    n=1 << k
    P=projectors(n)
    assert len(P)==3*(1 << (2*k-1))
    # Projectors are encoded by the first three entries, because the fourth is 1-a.
    r=Counter()
    for a,b,c in P:
        for e,f,g in P:
            r[((a+e)%n,(b+f)%n,(c+g)%n)]+=1
    holes=0
    minpos=min(r.values())
    for u in range(n):
        for v in range(n):
            for w in range(n):
                typ,pred=prediction(u,v,w,k)
                cnt=r[(u,v,w)]
                if typ=='exact':
                    assert cnt==pred, (k,(u,v,w),cnt,pred)
                else:
                    assert cnt>=pred, (k,(u,v,w),cnt,pred)
                if cnt==0: holes+=1
    assert holes==((1 << (3*(k-1)))-1)//7
    assert len(r)==n**3-holes
    assert minpos==(1 << (k+1))
    assert sum(r.values())==len(P)**2
    print('k=%d projectors=%d holes=%d support=%d minpos=%d exact' %
          (k,len(P),holes,len(r),minpos))


def main():
    for k in range(2,6):
        check(k)
    print('DYADIC_PROJECTOR_CONVOLUTION_SUPPORT_PASS')

if __name__=='__main__': main()

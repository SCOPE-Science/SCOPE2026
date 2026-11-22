#!/usr/bin/env python3
"""Independent finite checks of the sharp three-coin threshold formulas.

The mathematical proof is infinite; these computations test bounded parameters only.
"""
from math import gcd


def dptable(coins, N):
    cnt = [0] * (N + 1)
    cnt[0] = 1
    for c in coins:
        for i in range(c, N + 1):
            cnt[i] += cnt[i - c]
    return cnt


def direct_order_statistic(a,d,p):
    # Independent of the dynamic-programming representation count.
    # p+1-th smallest (with multiplicity) base coin amounts in each residue.
    b,c=a+d,a+2*d
    base_max=a*(p+a+d+10)+d*(2*a+1)
    rows=[[] for _ in range(a)]
    for y in range(base_max//b+1):
        for z in range((base_max-b*y)//c+1):
            w=b*y+c*z
            rows[w%a].append(w)
    return max(sorted(row)[p]-a for row in rows)


def check():
    cases = thresholds = 0
    boundary = []
    for a in range(5,91):
        m=a//2
        for d in range(2,min(m,28)+1):
            if gcd(a,d)!=1:continue
            lo=m+2
            hi=a+d
            p0=hi+1
            B=a*(p0+m-1)+d*(2*a-1)
            N=B+3*a
            counts=dptable((a,a+d,a+2*d),N)
            assert min(counts[N-a+1:])>p0,(a,d,'tail')
            # Check every formula in the entire new interval, not just samples.
            for p in range(lo,hi+1):
                g=max(i for i,x in enumerate(counts) if x<=p)
                expected=a*(p+m-1)+d*(2*a-1)
                assert g==expected, (a,d,p,g,expected)
                thresholds+=1
            g=max(i for i,x in enumerate(counts) if x<=p0)
            expected=B-(a-2*d)
            assert g==expected,(a,d,p0,g,expected)
            cases+=1
            if a<=17 and d<=4:
                by_order=direct_order_statistic(a,d,p0)
                assert by_order==g,(a,d,p0,by_order,g)
                boundary.append((a,d,p0,g))
    print('PASS',cases,'coprime (a,d) pairs;',thresholds,'affine-range thresholds plus',cases,'first-break thresholds')
    print('Independent two-variable order-statistic spotchecks:', len(boundary))
    print('First-break examples (a,d,p,g):', boundary)

if __name__=='__main__':check()

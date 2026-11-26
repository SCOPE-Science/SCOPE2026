#!/usr/bin/env python3
"""Independent exhaustive verification of binary two-lag deletion-count law."""
from collections import Counter
from itertools import product
from math import gcd, comb

def descendants(x, k):
    return {x[:j] + x[j+k:] for j in range(len(x)-k+1)}

def statistic(x,k):
    return 1 + sum(x[i]!=x[i+k] for i in range(len(x)-k))

def pmf_by_lags(n,b,c):
    counter=Counter()
    for bits in product('01',repeat=n):
        x=''.join(bits)
        db,dc=statistic(x,b),statistic(x,c)
        assert db==len(descendants(x,b))
        assert dc==len(descendants(x,c))
        counter[(db-1,dc-1)]+=1
    return counter

def predicted_critical_counts(n,b,c):
    g=gcd(b,c)
    assert n == b+c-g+1
    a=c//g
    d=b//g
    nb=n-b
    nc=n-c
    out=Counter()
    # independent baseline plus unique even-edge cycle contribution.
    # unnormalized (unnormalized coefficient of E z^B u^C multiplied by 2^n)
    for i in range(nb+1):
        for j in range(nc+1):
            base=comb(nb,i)*comb(nc,j)
            # Factor 2^n / 2^(nb+nc) can be fractional for n larger than b+c,
            # but at critical n, nb+nc=n-(g-1) <= n.
            out[(i,j)]+=base * 2**(n-nb-nc)
    # cycle term: ((1-z)/2)^a((1-u)/2)^d *
    # ((1+z)/2)^(nb-a)((1+u)/2)^(nc-d).
    for i in range(nb+1):
        for j in range(nc+1):
            vb= sum((-1)**r*comb(a,r)*comb(nb-a,i-r)
                 for r in range(max(0,i-(nb-a)),min(a,i)+1))
            vc= sum((-1)**r*comb(d,r)*comb(nc-d,j-r)
                 for r in range(max(0,j-(nc-d)),min(d,j)+1))
            out[(i,j)]+=vb*vc*2**(n-nb-nc)
    return +out

def check():
    tested=0
    for n in range(3,12):
        for b in range(1,n-1):
            for c in range(b+1,n):
                cnt=pmf_by_lags(n,b,c)
                norm=2**n
                mb=Counter();mc=Counter()
                for (i,j),v in cnt.items():
                    mb[i]+=v;mc[j]+=v
                for i in range(n-b+1):
                    assert mb[i]==2**(n-(n-b))*comb(n-b,i), (n,b,c,i)
                for j in range(n-c+1):
                    assert mc[j]==2**(n-(n-c))*comb(n-c,j), (n,b,c,j)
                thresh=b+c-gcd(b,c)+1
                independent=all(v*norm==mb[i]*mc[j] for (i,j),v in cnt.items())
                # Need also test zero-valued cells against product marginals.
                independent=all(cnt[(i,j)]*norm==mb[i]*mc[j]
                   for i in range(n-b+1) for j in range(n-c+1))
                assert independent==(n<thresh),(n,b,c,independent,thresh)
                if n==thresh:
                    pred=predicted_critical_counts(n,b,c)
                    assert cnt==pred, (n,b,c,cnt,pred)
                tested+=1
    print('VERIFIED',tested,'(n,b,c) parameter triples, 3<=n<=11, all binary strings; critical coefficients and independence thresholds')
if __name__=='__main__':check()

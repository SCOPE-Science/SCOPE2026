#!/usr/bin/env python3
"""Direct enumeration of the five-statistic convex-set polynomial for a standard-example poset."""
from collections import Counter
from itertools import combinations
from math import comb


def direct(n, complete=False, return_signatures=False):
    ans=Counter()
    indices=range(n)
    def leq(u,v):
        return u==v or (u<n and v>=n and (complete or u!=v-n))
    elements=range(2*n)
    signatures={}
    for mask in range(1<<(2*n)):
        X=[i for i in elements if mask>>i&1]
        # all subsets convex because height two, but verify directly
        for a in X:
            for b in X:
                if leq(a,b):
                    assert all((not (leq(a,c) and leq(c,b))) or c in X for c in elements)
        if not X:
            ans[(0,0,0,0,0)]+=1
            signatures[mask]=(0,0,0,0,0)
            continue
        lower=[u for u in X if not any(v!=u and leq(v,u) for v in X)]
        upper=[u for u in X if not any(v!=u and leq(u,v) for v in X)]
        down={v for u in upper for v in elements if leq(v,u)}
        up={v for u in lower for v in elements if leq(u,v)}
        sig=(len(lower),len(upper),len(down),len(up),len(X))
        ans[sig]+=1
        signatures[mask]=sig
    return signatures if return_signatures else ans


def formula(n):
    ans=Counter({(0,0,0,0,0):1})
    def put(c, minima,maxima,down,up,size):
        if c:ans[(minima,maxima,down,up,size)]+=c
    # Only one selected side.
    for a in range(1,n+1):
        put(comb(n,a),a,a,a,(n if a==1 else n+a),a)
    for b in range(1,n+1):
        put(comb(n,b),b,b,(n if b==1 else n+b),b,b)
    # Both sides selected, with at least two selected on each.
    for a in range(2,n+1):
        for b in range(2,n+1):
            put(comb(n,a)*comb(n,b),a,b,n+b,n+a,a+b)
    # Singleton lower, at least two upper.
    for b in range(2,n+1):
        put((n-b)*comb(n,b),1,b,n+b,n,b+1)
        put(b*comb(n,b),2,b,n+b,n+1,b+1)
    # Singleton upper, at least two lower.
    for a in range(2,n+1):
        put((n-a)*comb(n,a),a,1,n,n+a,a+1)
        put(a*comb(n,a),a,2,n+1,n+a,a+1)
    # A single lower and a single upper.
    put(n*(n-1),1,1,n,n,2)
    put(n,2,2,n+1,n+1,2)
    return ans

if __name__=='__main__':
    for n in range(2,8):
        d,f=direct(n),formula(n)
        assert d==f,(n,d-f,f-d)
        assert sum(d.values())==4**n
        print('DIRECT_OK', n, len(d), sum(d.values()))
    for n in range(2,9):
        a=direct(n,return_signatures=True)
        b=direct(n,complete=True,return_signatures=True)
        assert sum(a[k]==b[k] for k in a)==(2**n-n)**2
        sa=Counter(a.values())
        hb=Counter(b.values())
        assert sa[(2,2,n+1,n+1,2)]==n
        assert hb[(2,2,n+1,n+1,2)]==0
        print('PERTURBATION_OK',n,'unchanged', (2**n-n)**2, 'of',4**n)
    for n in range(2,101):
        f=formula(n)
        assert sum(f.values())==4**n
        assert f[(1,1,n,n,2)]==n*(n-1)
        assert f[(2,2,n+1,n+1,2)]==n
    print('FORMULA_IDENTITY_OK 2..100')
    print('VERIFY_OK')

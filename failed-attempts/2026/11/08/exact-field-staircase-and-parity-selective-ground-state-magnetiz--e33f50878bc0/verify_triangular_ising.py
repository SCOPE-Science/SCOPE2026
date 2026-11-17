#!/usr/bin/env python3
"""Reproduce finite checks for the field-dependent Ising model on L(K_n).

Standard-library-only; integer arithmetic is used throughout.
This verifies finite cases and exact difference identities. It does not
replace the all-n balancing argument in the accompanying proof.
"""
from itertools import combinations

def profile(n):
    assert n >= 3
    N = n*(n-1)//2
    out = []
    for m in range(N+1):
        q,r = divmod(2*m,n)
        d = 2*q-(n-1)
        out.append(((n-r)*d*d+r*(d+2)**2-n*(n-1))//2)
    return out

def predicted_slopes(n):
    if n%2==0:
        return {4*(2*q-n+2) for q in range(n-1)}
    return ({4*(2*q-n+2) for q in range(n-1)}
            | {4*(2*q-n+3) for q in range(0,n-2,2)})

def brute_strata(n):
    pairs=list(combinations(range(n),2))
    N=len(pairs)
    minimum=[10**10]*(N+1)
    count=[0]*(N+1)
    for bits in range(1<<N):
        degree=[0]*n
        m=bits.bit_count()
        for i,(a,b) in enumerate(pairs):
            if bits>>i&1:
                degree[a]+=1
                degree[b]+=1
        delta=[2*k-(n-1) for k in degree]
        interaction=(sum(x*x for x in delta)-n*(n-1))//2
        if interaction<minimum[m]:
            minimum[m]=interaction
            count[m]=1
        elif interaction==minimum[m]:
            count[m]+=1
    return minimum,count

def construct_balanced(n,m):
    pairs=list(combinations(range(n),2))
    E=set(pairs[:m])
    deg=[0]*n
    for u,v in E:
        deg[u]+=1;deg[v]+=1
    for _ in range(5*n*n*n):
        high=max(range(n),key=lambda u:deg[u])
        low=min(range(n),key=lambda u:deg[u])
        if deg[high]-deg[low]<=1:
            assert len(E)==m
            assert max(deg)-min(deg)<=1
            return
        found=False
        for w in range(n):
            if w==high or w==low:continue
            uw=tuple(sorted((high,w)))
            vw=tuple(sorted((low,w)))
            if uw in E and vw not in E:
                E.remove(uw)
                E.add(vw)
                deg[high]-=1
                deg[low]+=1
                found=True
                break
        assert found, ("switch unavailable",n,m,high,low)
    raise AssertionError("smoothing did not terminate")

def check():
    n_brute=0
    for n in range(3,7):
        expected=profile(n)
        actual,counts=brute_strata(n)
        assert actual==expected,(n,actual,expected)
        n_brute+=1<<len(list(combinations(range(n),2)))
    for n in range(3,101):
        E=profile(n)
        deltas=[E[m+1]-E[m] for m in range(len(E)-1)]
        assert deltas==sorted(deltas),n
        assert set(deltas)==predicted_slopes(n),n
        N=n*(n-1)//2
        zs=[2*m-N for m,e in enumerate(E) if e==min(E)]
        if n%2==0:
            assert zs==list(range(-n//2,n//2+1,2)),n
            assert min(E)==-n*(n-2)//2
        elif n%4==1:
            assert zs==[0] and min(E)==-n*(n-1)//2,n
        else:
            assert zs==[-1,1] and min(E)==-n*(n-1)//2+2,n
    switches=0
    for n in range(3,26):
        for m in range(n*(n-1)//2+1):
            construct_balanced(n,m)
            switches+=1
    print("PASS: exhaustive spin-configuration strata for n=3..6; "
          f"{n_brute} configurations checked")
    print("PASS: all finite-difference identities, convexity, critical fields, "
          "and zero-field magnetizations for n=3..100")
    print(f"PASS: {switches} independently constructed almost-regular graphs "
          "for n=3..25, all edge counts")

if __name__=="__main__":
    check()

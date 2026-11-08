#!/usr/bin/env python3
"""Independent checks of the cyclic-power two-neighbour convexity theorem.
Standard library only; no cached graphs or external data.
"""
from collections import Counter
from math import comb


def neighbors(n, r):
    return [sum(1 << j for j in range(n) if j != i and min((j-i)%n,(i-j)%n) <= r)
            for i in range(n)]


def p3_convex(mask, nb):
    return all((mask & nbr).bit_count() <= 1 for i, nbr in enumerate(nb) if not mask & (1 << i))


def separated_or_full(mask, n, r):
    if mask == (1 << n) - 1:
        return True
    selected = [i for i in range(n) if mask & (1 << i)]
    return all(min(j-i,n-j+i) >= 2*r+1
               for x,i in enumerate(selected) for j in selected[x+1:])


def coefficients(n,r):
    result = Counter({0:1,1:n,n:1})
    for k in range(2,n//(2*r+1)+1):
        count = n * comb(n-2*r*k-1,k-1)
        assert count%k==0
        result[k] = count//k
    return result


def hull(mask,nb):
    while True:
        additional=0
        for i,nbr in enumerate(nb):
            if not mask & (1<<i) and (mask&nbr).bit_count() >= 2:
                additional |= 1<<i
        if additional == 0:return mask
        mask |= additional


def verify_subsets():
    instances=0
    for r in range(2,7):
        for n in range(3,18 if r==2 else 15):
            nb=neighbors(n,r)
            observed=Counter()
            for mask in range(1<<n):
                ok=p3_convex(mask,nb)
                assert ok == separated_or_full(mask,n,r), (n,r,mask)
                if ok:observed[mask.bit_count()]+=1
            assert observed==coefficients(n,r),(n,r,observed,coefficients(n,r))
            instances+=1
    print('ORIGINAL_NEIGHBORHOOD_DEFINITION_EXHAUSTIVE_OK',instances,'instances')


def verify_pair_hulls():
    checks=0
    for r in range(2,11):
        for n in range(3,67):
            nb=neighbors(n,r)
            for i in range(n):
                for j in range(i+1,n):
                    d=min(j-i,n-j+i)
                    h=hull((1<<i)|(1<<j),nb)
                    expected=(1<<n)-1 if d<=2*r else (1<<i)|(1<<j)
                    assert h==expected, (n,r,i,j)
                    checks+=1
    print('DIRECT_TWO_NEIGHBOR_CLOSURE_PAIRS_OK',checks)


def verify_compositions():
    for r in range(2,13):
        for n in range(3,101):
            expected=coefficients(n,r)
            # Unrestricted compositions of n into k cyclic steps >= 2r+1;
            # count an oriented distinguished start vertex, then unmark.
            for k in range(2,n//(2*r+1)+1):
                m=n-(2*r+1)*k
                # Number of weak compositions of m into k slots, via DP.
                dp=[0]*(m+1);dp[0]=1
                for _ in range(k):
                    new=[0]*(m+1)
                    for s in range(m+1):
                        new[s]=sum(dp[:s+1])
                    dp=new
                assert (n*dp[m])%k==0
                assert n*dp[m]//k==expected[k],(n,r,k)
    print('INDEPENDENT_CYCLIC_GAP_COUNTS_OK')


def verify_sharp_radius():
    n=7;r=1;mask=3
    assert p3_convex(mask,neighbors(n,r))
    assert not separated_or_full(mask,n,r)
    print('RADIUS_ONE_EXCEPTION_OK')


if __name__=='__main__':
    verify_subsets()
    verify_pair_hulls()
    verify_compositions()
    verify_sharp_radius()
    print('VERIFY_OK')

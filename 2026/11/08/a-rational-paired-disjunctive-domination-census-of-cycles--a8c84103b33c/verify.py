#!/usr/bin/env python3
"""Independent graph-level and coefficient checks for paired disjunctive domination on cycles.
Uses plain graph distances, generic perfect-matching recursion and a separate rational-series recurrence.
No external dependencies. Does not read a ledger or other artifact.
"""
from collections import Counter
from functools import lru_cache
from math import ceil


def via_rational(nmax):
    """P_n(z) from A= sum_{q>=1} z^(2q)(x^(2q+1)+x^(2q+2)+x^(2q+3))."""
    A = {(0, 0): 1}
    for n in range(1, nmax + 1):
        for k in range(1, n // 2 + 1):
            A[n,k] = sum(A.get((n-j,k-1),0) for j in (2,3,4,5))
    out = {}
    for n in range(3, nmax + 1):
        C = {}
        for k in range(1, n // 2 + 1):
            count = sum(j*A.get((n-j,k-1),0) for j in (2,3,4,5))
            if n == 2*k:
                count -= 1
            if count:
                C[2*k] = count
        out[n]=C
    return out


def cycle_distances(n):
    adj=[(1<<((i+1)%n))|(1<<((i-1)%n)) for i in range(n)]
    distances=[]
    for origin in range(n):
        d=[-1]*n
        d[origin]=0
        wave=[origin]
        while wave:
            nextwave=[]
            for u in wave:
                for v in range(n):
                    if ((adj[u]>>v)&1) and d[v]<0:
                        d[v]=d[u]+1
                        nextwave.append(v)
            wave=nextwave
        distances.append(d)
    return adj,distances


def graph_polynomial(n):
    adj,dists=cycle_distances(n)
    nbr2=[sum(1<<j for j in range(n) if dists[i][j]==2) for i in range(n)]
    @lru_cache(None)
    def perfect_matching(mask):
        if not mask: return True
        vertex = (mask & -mask).bit_length()-1
        options=adj[vertex]&mask
        while options:
            low=options&-options
            options-=low
            if perfect_matching(mask^low^(1<<vertex)):
                return True
        return False
    C=Counter()
    for mask in range(1,1<<n):
        if mask.bit_count()%2:continue
        # Domination via graph neighbors/distances, independent of cyclic word encoding.
        valid=True
        for v in range(n):
            if mask>>v&1:continue
            if adj[v]&mask:continue
            if (nbr2[v]&mask).bit_count()>=2:continue
            valid=False
            break
        if valid and perfect_matching(mask): C[mask.bit_count()]+=1
    return dict(C)


def minimum_multiplicity(n):
    k=(n+4)//5
    d=5*k-n
    return [5,n,n*(k+1)//2,n*(k+1)*(k+2)//6,n*(k-1)*(k*k+7*k+18)//24][d]


def main():
    polys=via_rational(250)
    brute_subsets=0
    eligible_sets=0
    for n in range(3,18):
        observed=graph_polynomial(n)
        expected=polys[n]
        assert observed==expected,(n,observed,expected)
        brute_subsets+=(1<<n)-1
        eligible_sets+=sum(observed.values())
    for n in range(3,251):
        p=polys[n]
        k=(n+4)//5
        assert min(p)==2*k,(n,"minimum")
        assert set(p)==set(range(2*k, n+1, 2)),(n,"support")
        assert p[2*k]==minimum_multiplicity(n),(n,"minimum multiplicity")
        if n%2==0:
            assert p[n]==1
            if n>=4:assert p[n-2]==n*n//4
        else:
            assert p[n-1]==n
            if n>=5:assert p[n-3]==n*(n*n-1)//24
    print("VERIFY_OK graph_orders=3..17 candidate_nonempty_subsets=%s paired_disjunctive_sets=%s rational_coefficients_orders=3..250 minimum_residue=PASS support=PASS leading_coefficients=PASS"%(brute_subsets,eligible_sets))


if __name__=='__main__':main()

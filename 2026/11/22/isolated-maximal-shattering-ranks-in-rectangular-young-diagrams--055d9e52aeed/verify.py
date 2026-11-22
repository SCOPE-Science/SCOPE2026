#!/usr/bin/env python3
"""Finite, separate checks of isolated maximal Young-diagram shattering ranks.

Run: python3 verify.py
Requires only the Python standard library.
"""
from itertools import combinations
from collections import defaultdict
from math import comb


def expected(m):
    n = 2*m-2
    return {(m*(m+1)//2-1)+(h-1)*(m-2): h for h in range(1,m+1)}


def distinguished(m,h):
    n=2*m-2
    return frozenset(
        [(i,n-i+1) for i in range(1,h)] +
        [(i,m-i+1) for i in range(h+1,m+1)]
    )


def partitions(m,n):
    """All weakly decreasing m-tuples bounded by n, using a separate representation from the proof."""
    def rec(before, slots, acc):
        if slots == 0:
            yield tuple(acc)
        else:
            for a in range(before+1):
                yield from rec(a, slots-1, acc+[a])
    yield from rec(n,m,[])


def by_weight_ideals(m,n):
    out=defaultdict(list)
    for lam in partitions(m,n):
        # bit-coded cell incidences, row-major, 1-based geometric labels
        bit=0
        for i, row in enumerate(lam):
            for j in range(row):
                bit |= 1 << (i*n+j)
        out[sum(lam)].append(bit)
    return out


def all_antichains(m,n,r):
    # Grid antichains correspond to strictly increasing rows and
    # strictly decreasing columns.
    for rows in combinations(range(1,m+1),r):
        for cols0 in combinations(range(1,n+1),r):
            yield frozenset(zip(rows,cols0[::-1]))


def direct_shatter(rank_words, support, n):
    cells=sorted(support)
    masks=[]
    for i,j in cells:
        masks.append(1 << ((i-1)*n+(j-1)))
    traces=set()
    for w in rank_words:
        trace=0
        for a,mask in enumerate(masks):
            if w & mask: trace |=1<<a
        traces.add(trace)
        if len(traces)==1<<len(cells):return True
    return False


def closure_bounds(m,n,support):
    # Direct geometry over all mn grid points, not closed-form identities.
    down=0
    up=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            down += any(i<=a and j<=b for a,b in support)
            up += any(i>=a and j>=b for a,b in support)
    return down,m*n-up


def check():
    trace_checks=0
    for m in (3,4,5):
        n=2*m-2; w=by_weight_ideals(m,n)
        assert sum(map(len,w.values()))==comb(m+n,m)
        targets=expected(m)
        candidates=list(all_antichains(m,n,m-1)) + list(all_antichains(m,n,m))
        for s in candidates:
            ranks=[]
            lo,hi=closure_bounds(m,n,s)
            for k in range(m*n+1):
                hit=direct_shatter(w[k],s,n)
                assert hit==(lo<=k<=hi),(m,k,s)
                trace_checks+=1
                if hit:ranks.append(k)
            if len(s)==m:
                assert not ranks,(m,s,ranks)
            else:
                h=next(i for i in range(1,m+1) if i not in {a for a,b in s})
                assert ranks==([next(k for k,H in targets.items() if H==h)] if s==distinguished(m,h) else []),(m,s,ranks)
    # Wider parametric sweep: independent cell-by-cell closure counts for
    # every large candidate support; this is *not* substituted for proof.
    closure_checks=0
    for m in (6,7,8):
        n=2*m-2
        observed=defaultdict(list)
        for r in (m-1,m):
            for s in all_antichains(m,n,r):
                # Independent direct geometry counts both closure boundaries.
                lo,hi=closure_bounds(m,n,s)
                for k in range(lo,hi+1):observed[k].append(s)
                closure_checks+=1
        assert {k:len(v) for k,v in observed.items()}=={k:1 for k in expected(m)},(m,observed)
        for k,h in expected(m).items():
            assert observed[k]==[distinguished(m,h)],(m,k,observed[k])
    # A fixed-rank example with repeated emergence of top dimension.
    assert list(sorted(expected(6)))==[20,24,28,32,36,40]
    print('PASS direct rank-by-rank traces vs independent closures; cases=',trace_checks)
    print('PASS large-grid closure support census; supports=',closure_checks)
    print('PASS unique top support at each isolated rank for m=3,...,8')

if __name__=='__main__':
    check()

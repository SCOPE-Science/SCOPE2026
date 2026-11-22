#!/usr/bin/env python3
"""Independent finite checks of the open-neighborhood interval-graph theorem."""
from itertools import combinations

def pairings(items):
    if not items:
        yield ()
        return
    first=items[0]
    for j in range(1,len(items)):
        for tail in pairings(items[1:j]+items[j+1:]):
            yield ((first,items[j]),)+tail

def count(intervals):
    n=len(intervals)
    # Every possible auxiliary interval meets a fixed set of marked
    # intervals according only to its two endpoints' positions relative
    # to the marked endpoints. All endpoint-gap pairs are enumerated.
    traces=set()
    for a in range(2*n+1):
        for b in range(a,2*n+1):
            traces.add(sum(1<<i for i,(l,r) in enumerate(intervals)
                           if l<b and r>=a))
    # Marked vertices are already graph vertices, but must omit themselves.
    for i,(l,r) in enumerate(intervals):
        traces.add(sum(1<<j for j,(ll,rr) in enumerate(intervals)
                       if i!=j and ll<=r and l<=rr))
    return len(traces)

def expected(m):
    return (1 if m==0 else 2 if m==1 else m*(m+3)//2-1)

def main():
    for m in range(1,8):
        maximum=0
        cases=0
        for representation in pairings(tuple(range(2*m))):
            maximum=max(maximum,count(representation))
            cases+=1
        assert maximum==expected(m),(m,maximum,expected(m))
        print('exhaustive',m,cases,maximum,flush=True)
    # For a path, use 2m distinct endpoints in the order
    # L1,L2,R1,L3,R2,...,Lm,R(m-1),Rm;
    # direct geometry checks avoid relying on a pairing enumerator.
    for m in range(2,21):
        intervals=[(4*i,4*i+6) for i in range(m)]
        # Auxiliary traces: the coordinates are doubled to give private integer gaps.
        queries=set()
        for a in range(-2,4*m+10):
            for b in range(a,4*m+10):
                queries.add(sum(1<<i for i,(l,r) in enumerate(intervals)
                                if l<=b and a<=r))
        for i,(l,r) in enumerate(intervals):
            queries.add(sum(1<<j for j,(ll,rr) in enumerate(intervals)
                            if i!=j and ll<=r and l<=rr))
        assert len(queries)==expected(m),(m,len(queries),expected(m))
    print('INTERVAL_VERIFY_OK')

if __name__=='__main__': main()

#!/usr/bin/env python3
"""Independent finite checks for an exact gap-run theorem; standard library only."""
from collections import Counter
from heapq import heappush, heappop


def predicted(a):
    assert a >= 3 and a % 2 == 1
    m = (a-1)//2
    k,r = divmod(m,3)
    isolated = (12*k*k+3*k,12*k*k+11*k+3,12*k*k+19*k+6)[r]
    out = Counter({1:isolated})
    for j in range(m):
        if j%3 != 2:
            out[2*(m-j)] += 2
    return out


def independent_apery(a):
    gens = (a,2*a+2,4*a+6)
    dist = [None]*a
    dist[0]=0
    heap=[(0,0)]
    while heap:
        d,r=heappop(heap)
        if d!=dist[r]:
            continue
        for gen in gens[1:]:
            rr=(r+gen)%a
            nd=d+gen
            if dist[rr] is None or nd<dist[rr]:
                dist[rr]=nd
                heappush(heap,(nd,rr))
    assert all(x is not None for x in dist)
    return dist


def actual(a):
    dist=independent_apery(a)
    frob=max(dist)-a
    # Independent exact membership by additive dynamic programming, not the proof's digit formula.
    in_s=[False]*(frob+2)
    in_s[0]=True
    gens=(a,2*a+2,4*a+6)
    for v in range(1,frob+2):
        in_s[v]=any(v>=gen and in_s[v-gen] for gen in gens)
    assert all(in_s[v] == (v>=dist[v%a]) for v in range(frob+2))
    assert in_s[frob+1]
    gaps=Counter()
    run=0
    for v in range(frob+2):
        if not in_s[v]:
            run+=1
        elif run:
            gaps[run]+=1
            run=0
    assert run==0
    return gaps, frob, sum(not v for v in in_s)


def main():
    cases=0
    all_gaps=0
    all_run_blocks=0
    for a in range(3,252,2):
        x,frob,genus=actual(a)
        y=predicted(a)
        assert x==y, (a,x,y)
        assert sum(k*v for k,v in x.items()) == genus, (a,x,genus)
        assert x[1] == y[1]
        cases+=1
        all_gaps+=genus
        all_run_blocks+=sum(x.values())
    print(f'PASS: {cases} complete odd-parameter tests; {all_gaps} gaps; {all_run_blocks} maximal gap runs; last a=251')
    for a in (3,5,7,11,17):
        print(a,sorted(predicted(a).items()))

if __name__=='__main__':
    main()

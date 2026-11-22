"""Independent direct test of edge-open packings for matching-deleted bicliques.
Runs without third-party packages: python3 check_small.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def expected(m, n, t):
    p = Counter({0: 1, 1: m*n-t})
    f = Counter()
    degrees = [n-1]*t+[n]*(m-t)+[m-1]*t+[m]*(n-t)
    for d in degrees:
        f[d] += 1
        for k in range(2,d+1):
            p[k] += comb(d,k)
    p[2] += comb(t,2)
    f[2] += comb(t,2)
    return dict(p), dict(f)


def run(m,n,t):
    ed = [(i,j) for i in range(m) for j in range(n) if not (i==j and i<t)]
    q = len(ed)
    # Ground truth: for each pair, explicitly locate an actual third edge joining their endpoints.
    conflict = [0]*q
    for a,(i,j) in enumerate(ed):
        for b,(k,l) in enumerate(ed):
            if b<=a: continue
            e1={('L',i),('R',j)}
            e2={('L',k),('R',l)}
            for c,(x,y) in enumerate(ed):
                if c in (a,b): continue
                endpoints={('L',x),('R',y)}
                if (('L',x) in e1 and ('R',y) in e2) or (('R',y) in e1 and ('L',x) in e2):
                    conflict[a] |= 1<<b
                    conflict[b] |= 1<<a
                    break
    actual=Counter()
    facets=Counter()
    for mask in range(1<<q):
        good=True
        for a in range(q):
            if mask&(1<<a) and conflict[a]&mask:
                good=False
                break
        if not good: continue
        size=mask.bit_count()
        actual[size]+=1
        if all((mask&(1<<a)) or (conflict[a]&mask) for a in range(q)):
            facets[size]+=1
    ep, ef = expected(m,n,t)
    assert dict(actual)=={k:v for k,v in ep.items() if v}
    assert dict(facets)=={k:v for k,v in ef.items() if v}
    return q,sum(actual.values()),sum(facets.values()),dict(facets)

if __name__=='__main__':
    cases=[(3,3,t) for t in range(4)]+[(3,4,t) for t in range(4)]+[(4,4,t) for t in range(5)]+[(3,5,t) for t in range(4)]
    for m,n,t in cases:
        print(f'K_{m},{n}-M_{t}: (edges,total,facets,facet_polynomial)={run(m,n,t)}')
    print('PASS: direct third-edge tests coincide with both formulas for all',len(cases),'cases')

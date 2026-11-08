#!/usr/bin/env python3
"""Independent residue-graph check of shifted triangular Apéry formulas."""
from heapq import heappush, heappop
from math import isqrt

def triangulars(limit):
    out = [0]
    j = 1
    while j * (j + 1) // 2 <= limit:
        out.append(j * (j + 1) // 2)
        j += 1
    return out

def predicted(a):
    ts = triangulars(2*a)
    one = set(ts)
    two = {u + v for u in ts for v in ts if u + v < a}
    h = [0]
    for r in range(1, a):
        h.append(1 if r in one else (2 if r in two or r+a in one else 3))
    return [a*e + r for r,e in enumerate(h)],h

def independent_apery(a):
    ts=triangulars(3*a)
    coins=[a+t for t in ts]
    infinity=10**30
    dist=[infinity]*a
    dist[0]=0
    queue=[(0,0)]
    while queue:
        d,r=heappop(queue)
        if d!=dist[r]: continue
        for c in coins:
            s=(r+c)%a
            if d+c < dist[s]:
                dist[s]=d+c
                heappush(queue,(d+c,s))
    return dist

def main():
    tests=list(range(2,301))+[317,401,503,631,997,1000,1301,2000]
    residue_classes=0
    conduit=0
    for a in tests:
        computed=independent_apery(a)
        exact, h=predicted(a)
        assert computed==exact, (a,[(j,computed[j],exact[j]) for j in range(a) if computed[j]!=exact[j]][:10])
        genus=sum((w-r)//a for r,w in enumerate(computed))
        expect_genus=sum(h)
        assert genus==expect_genus
        conductor=max(computed)-a+1
        condition=h[-1]==3
        assert (conductor==3*a)==condition,(a,conductor,condition)
        residue_classes+=a-1
        conduit+=condition
    print('VERIFY_OK', 'parameter_values=',len(tests),'residue_classes=',residue_classes,'exact_apery=all','genus=all','conductor_criterion=all','three_a_conductors=',conduit)
    for a in (100, 300, 1000, 2000):
        ds,h=predicted(a)
        print('EXAMPLE',a,'genus',sum(h),'conductor',max(ds)-a+1,'layers',{i:h.count(i) for i in (1,2,3)})

if __name__=='__main__': main()

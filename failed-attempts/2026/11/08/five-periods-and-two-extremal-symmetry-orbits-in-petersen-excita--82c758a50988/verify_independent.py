#!/usr/bin/env python3
"""Independent tuple-by-tuple orbit tracing for KG(5,2) GHM, plus symmetry test."""
from itertools import product, combinations, permutations
from collections import Counter

E = list(combinations(range(5),2))
N = [tuple(j for j, y in enumerate(E) if not(set(x)&set(y))) for x in E]

def tick(x):
    v=[]
    for i, d in enumerate(x):
        if d == 1:v.append(2)
        elif d == 2:v.append(0)
        else:
            live=False
            for j in N[i]:
                if x[j]==1:live=True;break
            v.append(1 if live else 0)
    return tuple(v)

def symmetry_orbit(x):
    index={e:i for i,e in enumerate(E)}
    orb=set()
    for p in permutations(range(5)):
        y=[None]*10
        for j,(a,b) in enumerate(E):
            y[index[tuple(sorted((p[a],p[b])))]]=x[j]
        orb.add(tuple(y))
    return orb

def run():
    census=Counter(); periodic=set(); t6=set()
    for x in product((0,1,2), repeat=10):
        positions={}
        state=x
        while state not in positions:
            positions[state]=len(positions)
            state=tick(state)
        T=positions[state]
        P=len(positions)-T
        census[T,P]+=1
        if T==0:periodic.add(x)
        if T==6:t6.add(x)
    expected = {
       (0,1):1,(0,3):240,(0,4):240,(0,5):150,(0,8):480,
       (1,1):1023,(1,3):140,(1,4):1680,(1,5):4290,(1,8):2400,
       (2,1):2613,(2,3):580,(2,4):3900,(2,5):9780,(2,8):4320,
       (3,1):2242,(3,3):1360,(3,4):2400,(3,5):7050,(3,8):1440,
       (4,1):1960,(4,3):1220,(4,4):1620,(4,5):6000,(4,8):960,
       (5,3):840,(6,3):120,
    }
    assert census == expected,(census-expected, expected-census)
    for p in (1,3,4,5,8):
        assert sum(c for (t,q),c in census.items() if t==0 and p==q)%p==0
    reps = [ (1,2,2,2,1,1,0,0,0,0), (1,2,2,2,2,1,1,0,0,0) ]
    o1,o2=(symmetry_orbit(r) for r in reps)
    assert len(o1)==len(o2)==60 and not o1.intersection(o2)
    assert o1.union(o2)==t6
    assert all(len(N[i])==3 for i in range(10))
    assert len(periodic)==sum(c for (t,p),c in census.items() if t==0)
    print('INDEPENDENT_OK total=59049 periods=1,3,4,5,8 max_time=6 extremals=120 orbit_sizes=60,60 periodic='+str(len(periodic)))
    print('COUNTS',sorted(census.items()))
if __name__ == '__main__':run()

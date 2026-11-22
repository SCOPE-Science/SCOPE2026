"""Independently count and test every binary maximum cross-bibifix 3x3 code."""
from itertools import product
from collections import defaultdict, deque


def corners(m):
    return m[0],m[8]

def prefix2(m):
    return m[0],m[1],m[3],m[4]

def suffix2(m):
    return m[4],m[5],m[7],m[8]

def valid(C):
    return (not ({m[0] for m in C}&{m[8] for m in C})
            and not ({prefix2(m) for m in C}&{suffix2(m) for m in C}))


def analyze_orientation(start,end):
    V=[m for m in product(range(2),repeat=9) if corners(m)==(start,end)]
    adjacency={m:set() for m in V}
    for i,m in enumerate(V):
        for n in V[i+1:]:
            if prefix2(m)==suffix2(n) or prefix2(n)==suffix2(m):
                adjacency[m].add(n);adjacency[n].add(m)
    components=[]
    unused=set(V)
    while unused:
        seed=next(iter(unused));todo=[seed];comp=set()
        while todo:
            x=todo.pop()
            if x in comp:continue
            comp.add(x);todo.extend(adjacency[x]-comp)
        unused-=comp;components.append(comp)
    assert len(components)==4, [len(c) for c in components]
    choices=[]
    for component in components:
        L={m for m in component if m[4]==end}
        R=component-L
        assert len(L)==len(R)==16
        assert all(adjacency[m]==R for m in L)
        assert all(adjacency[m]==L for m in R)
        choices.append((L,R))
    maxima=[]
    for orientation in product(range(2),repeat=len(components)):
        C=set().union(*(choices[j][side] for j,side in enumerate(orientation)))
        assert len(C)==64 and valid(C)
        maxima.append(frozenset(C))
    assert len(set(maxima))==16
    return len(V),len(components),len(maxima)

if __name__=='__main__':
    for x,y in ((0,1),(1,0)):
        print('orientation',x,y,'vertices/components/maxima',analyze_orientation(x,y))
    lifts=[]
    for a,b in ((0,1),(1,0)):
        for center in (a,b):
            C=frozenset(m for m in product(range(2),repeat=9)
                        if (m[0],m[4],m[8])==(a,center,b))
            assert len(C)==64 and valid(C)
            lifts.append(C)
    assert len(set(lifts))==4
    print('BINARY_OPTIMA_32_CONFIRMED; CYLINDER_LIFTS_4; NONLIFTS_28')

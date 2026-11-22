#!/usr/bin/env python3
"""Standalone finite checks for the stated open-neighborhood trace theorem."""
from itertools import combinations

EIGHT_EDGES = [(0,1),(0,2),(1,2),(0,3),(1,4),(2,5),
               (0,6),(1,6),(2,6),(3,6),(5,7)]
# Vertices 0,1,2 are the parameters. Vertex 6 is the true twin of 0.
THIRTEEN_EDGES = [(0,1),(0,3),(0,7),(0,8),(0,9),(0,10),
    (1,2),(1,9),(1,11),(2,7),(2,8),(2,10),(2,11),(3,9),
    (4,11),(6,7),(7,8),(7,9),(7,10),(7,11),(8,9),(8,10),
    (8,11),(9,10),(10,11),(10,12),(4,5)]
FOUR_PARAMETERS = (7,10,0,11)

def neighbors(n,edges):
    nbr={i:set() for i in range(n)}
    for a,b in edges:
        assert 0<=a<n and 0<=b<n and a!=b
        nbr[a].add(b); nbr[b].add(a)
    return nbr

def traces(n,edges,parameters):
    nbr=neighbors(n,edges)
    return {tuple(int(x in nbr[v]) for x in parameters) for v in range(n)}

def peel_certificate(n,edges):
    """Explicit pendant/true-twin/false-twin/isolated elimination certificate."""
    nbr=neighbors(n,edges)
    remaining=set(range(n)); cert=[]
    while len(remaining)>1:
        options=[]
        for v in sorted(remaining):
            N=nbr[v]&remaining
            if len(N)<=1:
                w=next(iter(N)) if N else None
                options.append((0,v,'pendant' if N else 'isolated',w))
            for w in sorted(remaining-{v}):
                if (nbr[v]&remaining)-{w}==(nbr[w]&remaining)-{v}:
                    options.append((1,v,'true-twin' if w in N else 'false-twin',w))
        assert options, f'No DH reduction: {sorted(remaining)}'
        _,v,kind,w=min(options)
        cert.append((v,kind,w))
        remaining.remove(v)
    return cert

def connected(n,edges):
    nbr=neighbors(n,edges)
    seen={0};stack=[0]
    while stack:
        v=stack.pop()
        for w in nbr[v]-seen:seen.add(w);stack.append(w)
    return len(seen)==n

def verify():
    assert connected(8,EIGHT_EDGES)
    a=traces(8,EIGHT_EDGES,(0,1,2))
    assert a==set(__import__('itertools').product((0,1),repeat=3))
    c8=peel_certificate(8,EIGHT_EDGES)
    assert connected(13,THIRTEEN_EDGES)
    b=traces(13,THIRTEEN_EDGES,FOUR_PARAMETERS)
    assert len(b)==12, (len(b),b)
    c13=peel_certificate(13,THIRTEEN_EDGES)
    four_A=set(FOUR_PARAMETERS)
    base=traces(13,THIRTEEN_EDGES,FOUR_PARAMETERS)
    a_nbr=neighbors(13,THIRTEEN_EDGES)
    base_profiles={tuple(int(a in a_nbr[v]) for a in FOUR_PARAMETERS) for v in four_A}
    assert len(base_profiles)==3
    extra=[v for v in range(13) if v not in four_A]
    assert len(extra)==9 and len({tuple(int(a in a_nbr[v]) for a in FOUR_PARAMETERS) for v in extra})==9
    for r in range(10):
        keep=four_A|set(extra[:r])
        e=[(x,y) for x,y in THIRTEEN_EDGES if x in keep and y in keep]
        restricted=neighbors(13,e)
        traces_r={tuple(int(a in restricted[v]) for a in FOUR_PARAMETERS) for v in keep}
        assert len(traces_r)==3+r
    assert len(traces(4,[],(0,1,2,3)))==1
    assert len(traces(4,[(0,1),(0,2),(0,3)],(0,1,2,3)))==2
    # Cross-cut rank-one pattern bound: each side has at most two patterns
    # on the opposite pair of parameters. Check all possible strips.
    P={0,1,2,3}; M=0
    for i in range(3):
        for SX in combinations(P,i):
            for j in range(3):
                for SY in combinations(P,j):
                    covered={(x,y) for x in P for y in P if x in SX or y in SY}
                    M=max(M,len(covered))
                    assert len(covered)<=12
    assert M==12
    print(f'VERIFY_OK VC3_witness=8 four_trace_witness=13 four_spectrum=1..12 crosscut_max={M}')
    print('EIGHT_CERT', c8)
    print('THIRTEEN_CERT',c13)
    print('FOUR_TRACES',sorted(''.join(map(str,x)) for x in b))
if __name__=='__main__':verify()

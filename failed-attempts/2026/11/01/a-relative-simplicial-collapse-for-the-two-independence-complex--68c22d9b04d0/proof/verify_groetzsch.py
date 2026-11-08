#!/usr/bin/env python3
"""Exact certificates for the two-independence collapse of the eleven-vertex Mycielskian of C5.

Run: python3 verify_groetzsch.py
The two JSON certificates must be alongside this file.
Only Python standard-library modules are needed.
"""
from collections import Counter, deque
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
N=11
EDGES=set()
for i in range(5):
    j=(i+1)%5
    EDGES.add(frozenset((i,j)))
    for j in ((i-1)%5,(i+1)%5):
        EDGES.add(frozenset((5+i,j)))
    EDGES.add(frozenset((5+i,10)))
assert len(EDGES)==20


def independent_degree(s):
    """Largest component size of graph induced by bitmask s, by independent DFS."""
    todo=set(i for i in range(N) if (s>>i)&1)
    mx=0
    while todo:
        source=min(todo); todo.remove(source)
        q=[source]; size=0
        while q:
            x=q.pop();size+=1
            for y in list(todo):
                if frozenset((x,y)) in EDGES:
                    todo.remove(y);q.append(y)
        mx=max(mx,size)
    return mx


def simplices(r):
    return {s for s in range(1,1<<N) if independent_degree(s)<=r}


def faces(s):
    return [s^(1<<i) for i in range(N) if s>>i&1]


def fvector(F):
    D=Counter(s.bit_count()-1 for s in F)
    return tuple(D[d] for d in range(max(D)+1))


def check_complex(F):
    for s in F:
        assert all(t==0 or t in F for t in faces(s))


def certificate(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))


def check_relative_collapse(big,small,pairs):
    active=big.copy()
    assert small <= active and len(pairs)*2==len(big)-len(small)
    for i,(lo,hi) in enumerate(pairs):
        assert lo not in small and hi not in small, ('target face',i)
        assert lo in active and hi in active,('reused face',i)
        assert hi in [lo|(1<<j) for j in range(N) if not lo>>j&1],('codimension',i)
        # Direct check: lo belongs to exactly one proper containing face, namely hi.
        strict_superfaces=[t for t in active if t!=lo and t&lo==lo]
        assert strict_superfaces==[hi],('not a genuine free face',i,strict_superfaces)
        active.difference_update((lo,hi))
        assert small <= active
    assert active==small
    return len(pairs)


def check_morse(F,pairs,critical):
    matched=set();pairset=set()
    for i,(lo,hi) in enumerate(pairs):
        assert lo in F and hi in F and lo!=hi
        assert lo in faces(hi),('not a Hasse edge',i)
        assert lo not in matched and hi not in matched,('matching conflict',i)
        matched.add(lo);matched.add(hi);pairset.add((lo,hi))
    assert set(critical)==F-matched
    assert len(matched)+len(critical)==len(F)
    indeg={s:0 for s in F}; arcs={s:[] for s in F}
    for hi in F:
        for lo in faces(hi):
            if lo==0:continue
            # Ordinary Hasse orientation: upper -> lower; matched edges are reversed.
            u,v=(lo,hi) if (lo,hi) in pairset else (hi,lo)
            arcs[u].append(v);indeg[v]+=1
    total_arcs=sum(len(x) for x in arcs.values())
    queue=deque(s for s in F if indeg[s]==0)
    removed=0
    while queue:
        u=queue.popleft();removed+=1
        for v in arcs[u]:
            indeg[v]-=1
            if indeg[v]==0:queue.append(v)
    assert removed==len(F),('directed cycle',len(F)-removed)
    assert sorted(s.bit_count()-1 for s in critical)==[0,2]
    return total_arcs


def ranks_mod2(F):
    by_dim={d:sorted(s for s in F if s.bit_count()-1==d) for d in range(max(s.bit_count()-1 for s in F)+1)}
    ranks={}
    for d in range(1,max(by_dim)+1):
        row={s:i for i,s in enumerate(by_dim[d-1])}
        pivots={}
        for t in by_dim[d]:
            vector=0
            for s in faces(t): vector^=1<<row[s]
            while vector:
                p=vector.bit_length()-1
                if p not in pivots:
                    pivots[p]=vector;break
                vector^=pivots[p]
        ranks[d]=len(pivots)
    betti={d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in by_dim}
    return ranks,betti


def main():
    F1=simplices(1);F2=simplices(2)
    check_complex(F1);check_complex(F2)
    assert len(F1)==102 and len(F2)==312 and F1 <= F2
    assert fvector(F1)==(11,35,40,15,1)
    assert fvector(F2)==(11,55,110,95,36,5)
    rel=certificate('relative_collapse.json')
    morse=certificate('morse_pairs.json')
    assert rel['simplex_encoding']==morse['simplex_encoding']=='integer bitmask of vertices 0..10'
    n=check_relative_collapse(F2,F1,rel['pairs'])
    arcs=check_morse(F1,morse['pairs'],morse['critical'])
    r1,b1=ranks_mod2(F1);r2,b2=ranks_mod2(F2)
    assert [b1.get(i,0) for i in range(6)] == [b2.get(i,0) for i in range(6)] == [1,0,1,0,0,0]
    assert sum((-1)**d*v for d,v in enumerate(fvector(F1)))==2
    assert sum((-1)**d*v for d,v in enumerate(fvector(F2)))==2
    print('GRAPH vertices=11 edges=20')
    print('IND1 f_vector=',list(fvector(F1)),'faces=',len(F1))
    print('IND2 f_vector=',list(fvector(F2)),'faces=',len(F2))
    print('RELATIVE_COLLAPSE pairs=',n,'result=Ind1','status=PASS')
    print('MORSE_MATCHING pairs=',len(morse['pairs']),'critical=',sorted(morse['critical']),'oriented_hasse_edges=',arcs,'acyclic=PASS')
    print('MOD2_BETTI_IND1=',b1,'BOUNDARY_RANKS=',r1)
    print('MOD2_BETTI_IND2=',b2,'BOUNDARY_RANKS=',r2)
    print('INTEGRAL_HOMOTOPY Ind2 => Ind1 => S2 status=PASS')
    print('GROETZSCH_2_INDEPENDENCE_RELATIVE_COLLAPSE_VERIFIED')

if __name__=='__main__':main()

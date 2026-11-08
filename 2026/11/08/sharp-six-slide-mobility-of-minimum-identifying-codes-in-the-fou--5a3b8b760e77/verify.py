#!/usr/bin/env python3
"""Exhaustive independent reconstruction of minimum identifying-code reconfiguration.
Run: python3 verify.py [--certificate]
Only Python's standard library is required.
"""
from itertools import combinations
from collections import Counter, deque
import sys

DELTA={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def adjacency(kind):
    A=[0]*16
    for x in range(4):
        for y in range(4):
            v=4*x+y
            for a in range(4):
                for b in range(4):
                    w=4*a+b
                    if v != w and ((kind=='S' and ((a-x)%4,(b-y)%4) in DELTA)
                       or (kind=='R' and (x==a or y==b))):
                        A[v] |= 1<<w
    assert all(t.bit_count()==6 for t in A)
    assert all((A[i]>>j)&1 == (A[j]>>i)&1 for i in range(16) for j in range(16))
    return A

def is_code(C,closed):
    seen=set()
    for B in closed:
        t=B&C
        if not t or t in seen: return False
        seen.add(t)
    return True

def enumerate_codes(closed,k):
    return tuple(sorted(sum(1<<v for v in t) for t in combinations(range(16),k)
                        if is_code(sum(1<<v for v in t),closed)))

def move_graph(codes,A,model):
    good=set(codes)
    edges=set()
    for C in codes:
        for i in range(16):
            if not (C>>i)&1:continue
            options=(A[i] if model=='slide' else 65535)&~C
            while options:
                bit=options&-options
                options-=bit
                D=(C^(1<<i))|bit
                if D in good and C<D: edges.add((C,D))
    return tuple(sorted(edges))

def components(codes,edges):
    neighbors={s:[] for s in codes}
    for a,b in edges:
        neighbors[a].append(b);neighbors[b].append(a)
    remaining=set(codes)
    comps=[]
    while remaining:
        a=min(remaining);remaining.remove(a);q=[a]
        for u in q:
            for v in neighbors[u]:
                if v in remaining:remaining.remove(v);q.append(v)
        comps.append(tuple(sorted(q)))
    return neighbors,tuple(comps)

def distances_ecc(neighbors,codes):
    ecc=[]
    for a in codes:
        dist={a:0};queue=deque([a])
        while queue:
            v=queue.popleft()
            for w in neighbors[v]:
                if w not in dist:dist[w]=dist[v]+1;queue.append(w)
        assert len(dist)==len(codes)
        ecc.append(max(dist.values()))
    return min(ecc),max(ecc),Counter(ecc)

def verify(kind,k,want,slide_edges,jump_edges):
    A=adjacency(kind)
    closed=[A[i]|1<<i for i in range(16)]
    # Every smaller code can be extended to a (k-1)-set, since identification
    # is monotone under adding vertices. It suffices to rule out size k-1.
    assert not enumerate_codes(closed,k-1)
    codes=enumerate_codes(closed,k)
    assert len(codes)==want
    print(f'{kind}: minimum={k}, minimum_codes={len(codes)}, subminimum=0')
    for model,edge_expected in (('slide',slide_edges),('jump',jump_edges)):
        E=move_graph(codes,A,model)
        assert len(E)==edge_expected,(kind,model,len(E))
        nbr,comps=components(codes,E)
        degrees=Counter(map(len,nbr.values()))
        sizes=Counter(map(len,comps))
        if kind=='S':
            if model=='slide':
                assert sizes=={1:96} and degrees=={0:96}
            else:
                assert sizes=={6:16} and degrees=={2:96}
                assert all(len(comp)==6 and sum(len(nbr[v]) for v in comp)==12 for comp in comps)
        else:
            assert sizes=={2208:1}
            rad,diam,ecc=distances_ecc(nbr,codes)
            assert (rad,diam)==(6,6) and ecc=={6:2208},(rad,diam,ecc)
            if model=='slide':assert degrees=={12:1344,16:864},degrees
        print(f'{kind} {model}: edges={len(E)}, component_sizes={dict(sorted(sizes.items()))}, degrees={dict(sorted(degrees.items()))}')
    return codes,move_graph(codes,A,'slide'),move_graph(codes,A,'jump')

def main():
    s=verify('S',5,96,0,96)
    r=verify('R',6,2208,14976,28800)
    if '--certificate' in sys.argv:
        # Lexicographically sorted canonical finite certificate, 0-based bit coordinates.
        with open('states.txt','w',encoding='utf-8',newline='\n') as f:
            for label,pack in (('S',s),('R',r)):
                for C in pack[0]:f.write(f'{label} {C:04x}\n')
        with open('edges.txt','w',encoding='utf-8',newline='\n') as f:
            for label,pack in (('S',s),('R',r)):
                for model,edges in (('T',pack[1]),('J',pack[2])):
                    for x,y in edges:f.write(f'{label}{model} {x:04x} {y:04x}\n')
        print('Wrote states.txt and edges.txt')
    print('PASS: all assertions and exhaustive distance checks')
if __name__=='__main__':main()

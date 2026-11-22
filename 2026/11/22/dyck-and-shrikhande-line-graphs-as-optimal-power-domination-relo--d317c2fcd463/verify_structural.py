#!/usr/bin/env python3
"""Set-based algebraic check of the orbit proof and 32-vertex cubic graph."""
import json
from itertools import combinations
from collections import deque,Counter
from pathlib import Path
G={(x,y) for x in range(4) for y in range(4)}
D={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
C={(1,2),(3,2),(2,1),(2,3),(1,3),(3,1)}
Q={(2,0),(0,2),(2,2)}
add=lambda x,y:((x[0]+y[0])%4,(x[1]+y[1])%4)
neg=lambda x:((-x[0])%4,(-x[1])%4)
sub=lambda x,y:add(x,neg(y))
nbr=lambda x:{add(x,s) for s in D}

def closure(seed):
    seen=set(seed)
    for u in seed:seen|=nbr(u)
    while 1:
        new=set(seen)
        for x in seen:
            y=nbr(x)-seen
            if len(y)==1:new|=y
        if seen==new:return seen
        seen=new

def reps():
    table=[]
    for diff in ((1,0),(0,2),(1,2)):
        seed={(0,0),diff}
        x=set(seed)
        for u in seed:x|=nbr(u)
        table.append((diff,len(x),len(closure(seed))))
    assert table==[((1,0),10,10),((0,2),12,12),((1,2),12,16)]
    R=lambda p:(p[0],(p[0]-p[1])%4)
    F=lambda p:(p[1],p[0])
    assert {R(d) for d in D}==D=={F(d) for d in D}
    for start,need in ((1,0),6),((0,2),3),((1,2),6):
        pass
    for rep,expected in (((1,0),D),((0,2),Q),((1,2),C)):
        seen={rep};todo=[rep]
        while todo:
            x=todo.pop()
            for v in (R(x),F(x)):
                if v not in seen:seen.add(v);todo.append(v)
        assert seen==expected
    return table

def main():
    print('orbit_representatives',reps())
    assert len(closure({(0,0)}))==7
    Opt={frozenset((u,v)) for u,v in combinations(sorted(G),2) if sub(v,u) in C}
    assert len(Opt)==48
    assert all(closure(s)==G for s in Opt)
    # Local triangles are defined without bit masks or a graph library.
    T={}
    for u in sorted(G):
        W=sorted(add(u,d) for d in C)
        triangles=[]
        for triple in combinations(W,3):
            if all(sub(x,y) in D for x,y in combinations(triple,2)):
                triangles.append(frozenset(triple))
        assert len(triangles)==2 and not triangles[0]&triangles[1]
        T[u]=triangles
    H={frozenset(((u,i),(v,j))) for u,v in combinations(sorted(G),2) if frozenset((u,v)) in Opt for i in range(2) for j in range(2) if v in T[u][i] and u in T[v][j]}
    assert len(H)==48
    H_ad={(u,i):set() for u in G for i in range(2)}
    for pair in H:
        a,b=tuple(pair);H_ad[a].add(b);H_ad[b].add(a)
    assert len(H_ad)==32 and set(map(len,H_ad.values()))=={3}
    # Reproduce line graph directly from cubic incidence and compare with sensor slides.
    L={frozenset(e):set() for e in H}
    for i,e in enumerate(H):
        for f in H:
            if e!=f and e&f:L[frozenset(e)].add(frozenset(f))
    assert set(map(len,L.values()))=={4}
    forward={frozenset((u,v)): next(e for e in H if any(x==(u,i) for x in e for i in range(2)) and any(x==(v,j) for x in e for j in range(2))) for u,v in combinations(sorted(G),2) if frozenset((u,v)) in Opt}
    for a in Opt:
        for b in Opt:
            if a==b:continue
            move=(len(a&b)==1 and next(iter(a-b)) in nbr(next(iter(b-a))))
            assert move == (forward[b] in L[forward[a]])
    # Distances of the line graph, without using the first verifier's bit-mask implementation.
    hist=Counter()
    for start in L:
        dist={start:0};q=deque([start])
        while q:
            x=q.popleft()
            for y in L[x]:
                if y not in dist:dist[y]=dist[x]+1;q.append(y)
        assert len(dist)==48 and max(dist.values())==5
        for d in dist.values():
            if d:hist[d]+=1
    assert {d:v//2 for d,v in hist.items()}=={1:96,2:192,3:336,4:384,5:120}
    # Identify H by its LCF graph after applying an explicit bijection.
    mapping=json.loads((Path(__file__).parent/'dyck_isomorphism.json').read_text(encoding='utf-8'))
    f={((r['u']//4,r['u']%4),r['face_index']):r['dyck_index'] for r in mapping}
    assert len(f)==32
    E={frozenset((f[x] for x in edge)) for edge in H}
    K={frozenset((i,(i+1)%32)) for i in range(32)}
    K|={frozenset((i,(i+[-13,5,-5,13][i%4])%32)) for i in range(32)}
    assert len(E)==48 and E==K
    print('independent_set_based_result',{'optimal_pairs':48,'cubic_vertices':32,'cubic_edges':48,'line_graph_states':48,'line_graph_edges':96,'line_graph_diameter':5,'dyck_explicit_isomorphism':True})
if __name__=='__main__':main()

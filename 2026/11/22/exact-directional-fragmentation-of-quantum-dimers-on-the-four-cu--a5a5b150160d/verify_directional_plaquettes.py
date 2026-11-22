#!/usr/bin/env python3
"""Exact finite certificate for anisotropic Q4 square-dimer resonance connectivity.
No network or non-standard dependencies; run with python3 verify_directional_plaquettes.py.
"""
import json
from itertools import combinations, permutations
from collections import Counter, defaultdict

N=16
COORDS=list(combinations(range(4),2))
edges=sorted((u,v) for u in range(N) for v in range(u+1,N) if (u^v).bit_count()==1)
eid={e:i for i,e in enumerate(edges)}
neighbors={u:[v for v in range(N) if (u^v).bit_count()==1] for u in range(N)}
assert len(edges)==32 and len(COORDS)==6

def enumerator_1():
    def rec(rest,mask):
        if not rest:
            yield mask
            return
        u=(rest&-rest).bit_length()-1
        for v in neighbors[u]:
            if (rest>>v)&1:
                a,b=sorted((u,v))
                yield from rec(rest^(1<<u)^(1<<v),mask|(1<<eid[a,b]))
    return sorted(rec((1<<N)-1,0))

def enumerator_2():
    even=[u for u in range(N) if u.bit_count()%2==0]
    odd=[u for u in range(N) if u.bit_count()%2==1]
    assert len(even)==len(odd)==8
    out=[]
    def rec(i,occupied,selection):
        if i==8:
            mask=0
            for a,b in selection:
                mask|=1<<eid[tuple(sorted((a,b)))]
            out.append(mask)
            return
        u=even[7-i]
        for j,v in enumerate(odd):
            if not ((occupied>>j)&1) and (u^v).bit_count()==1:
                selection.append((u,v))
                rec(i+1,occupied|(1<<j),selection)
                selection.pop()
    rec(0,0,[])
    return sorted(out)

A=enumerator_1(); B=enumerator_2()
assert A==B and len(A)==272 and len(set(A))==272
index={a:i for i,a in enumerate(A)}
faces=[]
for c,(j,k) in enumerate(COORDS):
    for x in range(16):
        if x&(1<<j) or x&(1<<k):continue
        vj=x^(1<<j); vk=x^(1<<k); w=vj^(1<<k)
        pair1=(1<<eid[tuple(sorted((x,vj)))])|(1<<eid[tuple(sorted((vk,w)))])
        pair2=(1<<eid[tuple(sorted((x,vk)))])|(1<<eid[tuple(sorted((vj,w)))])
        faces.append((c,pair1,pair2))
assert len(faces)==24 and Counter(t for t,*_ in faces)=={i:4 for i in range(6)}

# Two independent neighbor constructions: bit-mask pair flip and symmetric-difference.
adjacency=[[] for a in A]
for i,a in enumerate(A):
    for typ,pa,pb in faces:
        if a&pa==pa and not a&pb:
            b=a^pa^pb
        elif a&pb==pb and not a&pa:
            b=a^pa^pb
        else:
            continue
        assert b in index
        adjacency[i].append((index[b],typ))
assert sum(map(len,adjacency))==1536
for i,ns in enumerate(adjacency):
    assert len(ns)==len(set(ns))
    assert all(any(k==i and ty==t for k,ty in adjacency[j]) for j,t in ns)

# Traversal based on neighbor lists.
def signature_bfs(selected):
    seen=set(); sizes=[]
    for x in range(len(A)):
        if x in seen:continue
        todo=[x];seen.add(x); size=0
        while todo:
            u=todo.pop();size+=1
            for v,ty in adjacency[u]:
                if selected>>ty&1 and v not in seen:
                    seen.add(v);todo.append(v)
        sizes.append(size)
    return tuple(sorted(sizes,reverse=True))

# Separate DSU: recompute every face switch using edge-set operations, no adjacency table.
def signature_dsu(selected):
    parent=list(range(len(B))); size=[1]*len(B)
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(x,y):
        x=find(x);y=find(y)
        if x!=y:
            parent[y]=x;size[x]+=size[y]
    loc={tuple(e for e in edges if m>>eid[e]&1):i for i,m in enumerate(B)}
    for c,pa,pb in faces:
        if not(selected>>c&1):continue
        ea={edges[e] for e in range(32) if pa>>e&1}
        eb={edges[e] for e in range(32) if pb>>e&1}
        for i,m in enumerate(B):
            chosen={edges[e] for e in range(32) if m>>e&1}
            if ea.issubset(chosen):
                nextstate=(chosen-ea)|eb
                j=loc[tuple(sorted(nextstate))]
                union(i,j)
    out=Counter(find(i) for i in range(len(B)))
    return tuple(sorted(out.values(),reverse=True))

def degrees(selected):
    return tuple(sorted((sum(1 for i,j in COORDS if selected>>COORDS.index((i,j))&1 and (i==v or j==v)) for v in range(4)),reverse=True))

# In Q4, the 11 unlabeled simple graphs on coordinate axes have distinct degree sequences.
expect={
    (0,0,0,0):(1,{1:272}),
    (1,1,0,0):(6,{1:144,2:16,4:20,16:1}),
    (1,1,1,1):(3,{1:16,2:32,4:40,16:2}),
    (2,1,1,0):(12,{1:79,2:16,4:12,7:4,9:4,49:1}),
    (2,2,2,0):(4,{1:59,4:6,9:12,81:1}),
    (2,2,1,1):(12,{1:14,2:16,4:12,12:8,82:1}),
    (3,1,1,1):(4,{1:32,2:24,7:12,108:1}),
    (2,2,2,2):(3,{1:12,32:4,132:1}),
    (3,2,2,1):(12,{1:12,2:8,4:2,12:8,140:1}),
    (3,3,2,2):(6,{1:10,32:2,198:1}),
    (3,3,3,3):(1,{1:8,264:1}),
}
assert sum(x[0] for x in expect.values())==64
records=[]; classes=defaultdict(list)
for selected in range(64):
    b=signature_bfs(selected)
    d=signature_dsu(selected)
    assert b==d, (selected,b,d)
    deg=degrees(selected)
    assert deg in expect, deg
    assert Counter(b)==expect[deg][1]
    classes[deg].append(selected)
    records.append(dict(mask=selected,enabled_pairs=[list(COORDS[i]) for i in range(6) if selected>>i&1],degree_sequence=list(deg),components=len(b),size_multiplicities={str(k):v for k,v in sorted(Counter(b).items(),reverse=True)}))
assert len(classes)==11
for deg,ids in classes.items():
    assert len(ids)==expect[deg][0]
assert signature_bfs(63)==(264,)+(1,)*8
assert all(signature_bfs(63^(1<<i))==(198,32,32)+(1,)*10 for i in range(6))
print('VERIFY_OK matchings=272 faces=24 labeled_repertoires=64 symmetry_types=11 all_full_6_only=TRUE')
if __name__=='__main__':
    print('Class tables as (sorted coordinate-axis degrees, repertoires, component spectrum):')
    for deg,ids in sorted(classes.items(),key=lambda z:(z[0][0]+z[0][1]+z[0][2]+z[0][3],z[0])):
        print(deg,len(ids),dict(sorted(Counter(signature_bfs(ids[0])).items(),reverse=True)))

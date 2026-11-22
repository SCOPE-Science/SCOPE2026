#!/usr/bin/env python3
"""Independent finite-field and incidence checks of the structural ingredients."""
from collections import deque
from itertools import combinations

def mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return r

def plane(q):
    if q==3:
        points=[(a,b) for a in range(3) for b in range(3)]
        add=lambda a,b:(a+b)%3
        mm=lambda a,b:(a*b)%3
    elif q==4:
        points=[(a,b) for a in range(4) for b in range(4)]
        add=lambda a,b:a^b
        mm=mul
    else:raise ValueError(q)
    classes=[]
    classes.append([{i for i,(x,y) in enumerate(points) if x==c} for c in range(q)])
    for m in range(q):
        classes.append([{i for i,(x,y) in enumerate(points) if y==add(mm(m,x),c)} for c in range(q)])
    assert all(sorted(len(l) for l in direction)==[q]*q for direction in classes)
    lines=[frozenset(l) for direction in classes for l in direction]
    assert len(lines)==q*(q+1)
    return points,lines

def check(q):
    pts,lines=plane(q)
    p=len(pts); L=len(lines);n=p+L
    assert p==q*q and L==q*(q+1)
    assert len(set(lines))==L
    for a,b in combinations(range(p),2):assert sum(a in li and b in li for li in lines)==1
    for i,j in combinations(range(L),2):
        assert len(lines[i]&lines[j])==(0 if i//q==j//q else 1)
    dist=[[99]*n for _ in range(n)]
    adj=[set() for _ in range(n)]
    for i,l in enumerate(lines):
        for x in l:adj[x].add(p+i);adj[p+i].add(x)
    for root in range(n):
        dist[root][root]=0;todo=deque([root])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if dist[root][w]==99:
                    dist[root][w]=dist[root][v]+1;todo.append(w)
    assert max(map(max,dist))==4
    def packing_label(v):
        if v<p:return 1
        j=v-p
        if j//q==0:return 2
        if j//q==1:return 3
        return 4+j-2*q
    coloring=[packing_label(v) for v in range(n)]
    assert max(coloring)==q*q-q+3
    for i,j in combinations(range(n),2):
        if coloring[i]==coloring[j]:assert dist[i][j]>coloring[i]
    # All nonempty point selections, independent line additions maximized.
    full=(1<<p)-1; equality=[]
    for mask in range(1,1<<p):
        permitted=[j for j,s in enumerate(lines) if all(mask>>v&1==0 for v in s)]
        assert mask.bit_count()+len(permitted)<=p
        if mask.bit_count()+len(permitted)==p:
            equality.append((mask,len(permitted)))
    assert len(equality)==p+1
    assert sum(mask.bit_count()==1 for mask,_ in equality)==p
    assert sum(mask==full for mask,_ in equality)==1
    # Every complement-of-a-pencil incidence graph is connected and q-regular.
    for removed in range(p):
        activeL=[j for j,s in enumerate(lines) if removed not in s]
        remaining=set(v for v in range(n) if v!=removed and (v<p or v-p in activeL))
        assert len(activeL)==p-1
        assert all(len(adj[v]&remaining)==q for v in remaining)
        seen={min(remaining)};stack=list(seen)
        while stack:
            for nb in adj[stack.pop()]&remaining:
                if nb not in seen:seen.add(nb);stack.append(nb)
        assert seen==remaining
    print(f'order {q}: {n} vertices, diameter 4, palette {max(coloring)}, {len(equality)} equality independent sets involving points; all tests passed')

if __name__=='__main__':
    for q in (3,4):check(q)

#!/usr/bin/env python3
"""Complete finite simplicial Morse certificate for the 8-, 9-cycle square punctures.
No external dependencies. Graph vertices are residues 0,...,n-1; 0 is deleted.
"""
from itertools import combinations
from collections import deque

def complex_faces(n, punctured=True):
    vertices=tuple(range(1,n)) if punctured else tuple(range(n))
    faces={frozenset()}
    for v in vertices:
        neighbors=tuple(w for w in vertices if w!=v and min((v-w)%n,(w-v)%n)<=2)
        for k in range(1,len(neighbors)+1):
            for s in combinations(neighbors,k):
                faces.add(frozenset(s))
    return faces

def greedy_matching(faces, n):
    all_faces=faces-{frozenset()}
    live=set(all_faces)
    matching=[]
    for pivot in range(1,n):
        pairs=[]
        for low in sorted(live,key=lambda s:(len(s),tuple(sorted(s)))):
            high=low|{pivot}
            if pivot not in low and high in live:
                pairs.append((low,high))
        for low,high in pairs:
            if low in live and high in live:
                live.remove(low);live.remove(high)
                matching.append((low,high))
    return all_faces,matching,live

def check_hasse_acyclic(all_faces,matching):
    up=set(matching)
    indeg={f:0 for f in all_faces}
    outgoing={f:[] for f in all_faces}
    for high in all_faces:
        for v in high:
            low=high-{v}
            if not low: continue
            src,dst=(low,high) if (low,high) in up else (high,low)
            outgoing[src].append(dst)
            indeg[dst]+=1
    todo=deque(x for x,d in indeg.items() if d==0)
    count=0
    while todo:
        x=todo.popleft();count+=1
        for y in outgoing[x]:
            indeg[y]-=1
            if indeg[y]==0:todo.append(y)
    return count==len(all_faces)

def verify(n, expected):
    faces=complex_faces(n)
    all_faces, matching, critical=greedy_matching(faces,n)
    assert len(all_faces)==2*len(matching)+len(critical)
    assert len(set(sum(([a,b] for a,b in matching),[])))==2*len(matching)
    assert check_hasse_acyclic(all_faces,matching)
    got=sorted(tuple(sorted(x)) for x in critical)
    assert got==sorted(expected), (n,got)
    return len(all_faces),len(matching),got

if __name__=='__main__':
    for n,crit in [(8,[(1,),(2,3)]),
                   (9,[(1,),(2,3),(2,6),(4,8)])]:
        nfaces,npairs,got=verify(n,crit)
        print('PASS',n,'nonempty_faces',nfaces,'matched_pairs',npairs,'critical_faces',got)
    print('These finite tests certify the two stated cases, not an infinite family.')

#!/usr/bin/env python3
"""Reconstruct bidirected friendship multipath complexes and the fiberwise Morse matching.
Uses no nonstandard packages.  Run `python verify_friendship.py`.
"""
from collections import defaultdict, Counter, deque
from itertools import combinations


def arcs_for(m):
    arcs=[]
    for i in range(m):
        a,b=2*i+1,2*i+2
        arcs.extend([(a,b),(b,a),(0,a),(0,b),(a,0),(b,0)])
    return arcs


def valid_subset(arcs,face):
    outgoing={};incoming={}
    for j,(s,t) in enumerate(arcs):
        if not face>>j&1:continue
        if s in outgoing or t in incoming:return False
        outgoing[s]=t; incoming[t]=s
    for start in outgoing:
        seen=set();v=start
        while v in outgoing:
            if v in seen:return False
            seen.add(v);v=outgoing[v]
    return True


def all_faces(m):
    arcs=arcs_for(m)
    faces={0}; frontier=[(0,0)]
    while frontier:
        face,last=frontier.pop()
        for j in range(last,len(arcs)):
            cand=face|1<<j
            if valid_subset(arcs,cand):
                assert cand not in faces
                faces.add(cand);frontier.append((cand,j+1))
    return arcs,faces


def face_groups(m,faces):
    hubs=sum((1<<(6*i+j) for i in range(m) for j in (2,3,4,5)))
    groups=defaultdict(set)
    for f in faces:
        if f:groups[f&hubs].add(f)
    return groups


def match_fibers(m,faces):
    arcs=arcs_for(m);groups=face_groups(m,faces)
    up={};down={};critical=set()
    for h,group in groups.items():
        remaining=set(group)
        hubs=[i for i in range(len(arcs)) if h>>i&1]
        if not hubs:
            pivots=[6*i for i in range(m)]
        elif len(hubs)==2 and hubs[0]//6==hubs[1]//6:
            pivots=[6*i for i in range(m) if i!=hubs[0]//6]
        else:
            b=hubs[0]//6
            # Map any hub arrow to the one permitted peripheral orientation.
            j=hubs[0]%6
            pivots=[6*b+(0 if j in (2,5) else 1)]
        for p in pivots:
            bit=1<<p
            pairs=[(x,x|bit) for x in remaining if not x&bit and x|bit in remaining]
            for x,y in pairs:
                assert x in remaining and y in remaining
                remaining.remove(x);remaining.remove(y);up[x]=y;down[y]=x
        critical.update(remaining)
    return up,down,critical


def acyclic(m,faces,up):
    # Directed Hasse graph: downward unless the cover is a matched pair.
    indeg={x:0 for x in faces if x}
    edges=defaultdict(list)
    for x in indeg:
        for j in range(6*m):
            if x>>j&1:
                y=x^(1<<j)
                if not y:continue
                if up.get(y)==x:lower,higher=y,x
                else:lower,higher=x,y
                edges[lower].append(higher)
                indeg[higher]+=1
    todo=deque(k for k,v in indeg.items() if v==0)
    visited=0
    while todo:
        x=todo.popleft();visited+=1
        for y in edges[x]:
            indeg[y]-=1
            if indeg[y]==0:todo.append(y)
    assert visited==len(indeg),(m,len(indeg),visited)
    return sum(map(len,edges.values()))


def retraction(m,faces):
    target_bit=(0,1,0,1,1,0)
    for f in faces:
        image=0
        for i in range(6*m):
            if f>>i&1:
                image|=1<<(6*(i//6)+target_bit[i%6])
        assert image in faces
        for branch in range(m):
            assert not ((image>>(6*branch)&1) and (image>>(6*branch+1)&1))
        if all(f&sum(1<<(6*k+j) for k in range(m) for j in (2,3,4,5))==0 for _ in [0]):
            assert image==f


def mod2_betti(m,faces):
    bydim=defaultdict(list)
    for f in faces:
        if f:bydim[f.bit_count()-1].append(f)
    ranks={}
    for d,upper in bydim.items():
        if d==0:continue
        lower=bydim[d-1];ids={f:i for i,f in enumerate(lower)}
        basis={};rank=0
        for face in upper:
            v=0
            for j in range(6*m):
                if face>>j&1:v^=1<<ids[face^(1<<j)]
            while v:
                pivot=v.bit_length()-1
                if pivot in basis:v^=basis[pivot]
                else:basis[pivot]=v;rank+=1;break
        ranks[d]=rank
    return {d:len(c)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d,c in bydim.items() if len(c)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)}


def test(m,full=True):
    arcs,faces=all_faces(m)
    up,down,crit=match_fibers(m,faces)
    assert len(up)==len(down) and 2*len(up)+len(crit)==len(faces)-1
    counts=Counter(f.bit_count()-1 for f in crit)
    assert counts==({0:2,1:2} if m==1 else {0:1,m-1:1,m:2*m}), (m,counts)
    retraction(m,faces)
    incidences=acyclic(m,faces,up)
    betti=mod2_betti(m,faces) if m<=4 else None
    if betti is not None:assert betti==({0:1,1:2} if m==1 else {m-1:1,m:2*m}), (m,betti)
    print('m=%d arcs=%d faces=%d matches=%d critical=%s Hasse=%d mod2=%s'%(m,len(arcs),len(faces),len(up),dict(sorted(counts.items())),incidences,betti),flush=True)

if __name__=='__main__':
    for n in range(1,7):test(n)
    print('ALL_VERIFY_OK')

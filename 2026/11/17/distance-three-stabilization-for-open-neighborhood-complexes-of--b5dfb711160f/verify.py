#!/usr/bin/env python3
"""Independent finite computations for two-vertex punctures of Boolean cubes."""
from itertools import combinations
from math import comb
from collections import deque
import hashlib

def build(n, distance, parity):
    deleted={0,(1<<distance)-1}
    faces=set()
    for center in range(1<<n):
        if center in deleted: continue
        vertices=sorted(center^(1<<i) for i in range(n)
                        if center^(1<<i) not in deleted and
                        ((center^(1<<i)).bit_count()%2)==parity)
        for size in range(1,len(vertices)+1):
            for face in combinations(vertices,size): faces.add(face)
    return faces

def gf2_rank(columns):
    pivots={}
    for x in columns:
        while x:
            bit=x.bit_length()-1
            if bit not in pivots:
                pivots[bit]=x
                break
            x^=pivots[bit]
    return len(pivots)

def rank_and_euler(faces):
    counts={k:0 for k in range(1,10)}
    for face in faces: counts[len(face)]+=1
    verts=sorted(x[0] for x in faces if len(x)==1)
    edges=sorted(face for face in faces if len(face)==2)
    triangles=sorted(face for face in faces if len(face)==3)
    E={e:i for i,e in enumerate(edges)}
    columns=[]
    for a,b,c in triangles:
        columns.append((1<<E[(a,b)])^(1<<E[(a,c)])^(1<<E[(b,c)]))
    r2=gf2_rank(columns)
    adj={v:set() for v in verts}
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    unseen=set(verts);components=0
    while unseen:
        components+=1
        start=unseen.pop();todo=[start]
        while todo:
            v=todo.pop()
            for u in adj[v]&unseen:unseen.remove(u);todo.append(u)
    h1=len(edges)-len(verts)+components-r2
    chi=sum((-1)**(k-1)*v for k,v in counts.items())
    # The proved collapse-to-2D lemma implies beta_2=chi-components+beta_1.
    b2=chi-components+h1
    return (components-1,h1,b2),sum(counts.values())

def predicted(n,d):
    if n==3:return (0,1,0) if d==3 else (0,0,0)
    mu=(2**(n-3))*(n*n-5*n+8)-1
    if d==1:penalty=comb(n-2,2)
    elif d==2:penalty=comb(n-1,2)-1
    else:penalty=comb(n-1,2)
    return (0,0,mu-comb(n-1,2)-penalty)

def main():
    cases=0;face_total=0
    for n in range(3,8):
        for d in range(1,n+1):
            target=predicted(n,d)
            for p in (0,1):
                faces=build(n,d,p)
                actual,fcount=rank_and_euler(faces)
                assert actual==target,(n,d,p,actual,target)
                cases+=1;face_total+=fcount
                print('PASS n=%d d=%d parity=%d betti=%s faces=%d'%(n,d,p,actual,fcount))
    # The exceptional distance-three boundary triangle is filled by seven
    # triangles in any dimension at least four (use the fourth coordinate).
    for n in range(4,8):
        faces=build(n,3,1)
        a,b,c,h=1,2,4,8
        x=a|b|h; y=a|c|h; z=b|c|h
        disk=[(a,b,x),(b,c,z),(a,c,y),(a,x,y),
              (b,x,z),(c,y,z),(x,y,z)]
        for f in disk:
            assert tuple(sorted(f)) in faces, (n,f)
        boundary={}
        for tri in disk:
            for e in combinations(sorted(tri),2):
                boundary[e]=boundary.get(e,0)^1
        assert {e for e,v in boundary.items() if v}=={(a,b),(a,c),(b,c)}
    print('LOCAL_FILLING_PASS n=4..7')
    print('ALL_PASS cases=%d total_faces=%d'%(cases,face_total))

if __name__=='__main__': main()

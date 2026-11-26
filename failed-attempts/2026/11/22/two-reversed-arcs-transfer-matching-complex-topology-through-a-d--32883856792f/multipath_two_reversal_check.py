#!/usr/bin/env python3
"""Standalone finite checks for the two-reversal multipath theorem.
No external packages. All graph labels are internal to this test.
"""
from itertools import product
from random import Random

def faces_directed(m,n,base):
    # Reverse the two disjoint distinguished edges (0,0),(1,1).
    arcs=[(i,m+j) if (i,j) not in ((0,0),(1,1)) else (m+j,i) for i,j in sorted(base)]
    accepted={0}
    for mask in range(1,1<<len(arcs)):
        incoming=[0]*(m+n); outgoing=[0]*(m+n)
        nxt={}; ok=True
        for k,(a,b) in enumerate(arcs):
            if mask>>k&1:
                incoming[b]+=1;outgoing[a]+=1
                if incoming[b]>1 or outgoing[a]>1:ok=False;break
                nxt[a]=b
        if not ok:continue
        for start in nxt:
            seen=set();x=start
            while x in nxt:
                if x in seen:ok=False;break
                seen.add(x);x=nxt[x]
            if not ok:break
        if ok:accepted.add(mask)
    return arcs,accepted

def faces_formula(m,n,base,arcs):
    labels={a:i for i,a in enumerate(arcs)}
    r1=labels[(m,0)];r2=labels[(m+1,1)]
    xs=labels.get((0,m+1)); ys=labels.get((1,m))
    fwd=[(k,(a,b)) for k,(a,b) in enumerate(arcs) if k not in (r1,r2)]
    matches=[]
    for subset in range(1<<len(fwd)):
        used=set();mask=0;good=True
        for j,(k,(a,b)) in enumerate(fwd):
            if subset>>j&1:
                if a in used or b in used:good=False;break
                used.update((a,b));mask|=1<<k
        if good:matches.append(mask)
    out=set()
    for mask in matches:
        for extra in (0,1<<r1,1<<r2):out.add(mask|extra)
        if xs is None or ys is None or not ((mask>>xs&1) and (mask>>ys&1)):
            out.add(mask|(1<<r1)|(1<<r2))
    return out

def matching_faces(vertices,edges):
    edges=list(edges); faces={0}
    for mask in range(1,1<<len(edges)):
        used=set();good=True
        for k,(u,v) in enumerate(edges):
            if mask>>k&1:
                if (0,u) in used or (1,v) in used:good=False;break
                used.update(((0,u),(1,v)))
        if good:faces.add(mask)
    return faces

def f2_rank(columns):
    piv={}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p not in piv:piv[p]=c;break
            c^=piv[p]
    return len(piv)

def reduced_betti(faces,edge_count):
    bydim={-1:[0]}
    for face in faces-{0}:
        bydim.setdefault(face.bit_count()-1,[]).append(face)
    ranks={}
    for d,ds in bydim.items():
        if d<0:continue
        under=bydim.get(d-1,[])
        indices={a:j for j,a in enumerate(under)}
        cols=[]
        for x in ds:
            boundary=0
            for i in range(edge_count):
                if (x>>i)&1:boundary ^= 1<<indices[x^(1<<i)]
            cols.append(boundary)
        ranks[d]=f2_rank(cols)
    return {d:len(items)-ranks.get(d,0)-ranks.get(d+1,0)
            for d,items in bydim.items() if len(items)-ranks.get(d,0)-ranks.get(d+1,0)}

def run(m,n,base):
    base=set(base)
    assert (0,0) in base and (1,1) in base
    arcs,real=faces_directed(m,n,base)
    formula=faces_formula(m,n,base,arcs)
    assert real==formula,(m,n,base,real^formula)
    leftover=[(i-2,j-2) for (i,j) in base if i>=2 and j>=2]
    R=matching_faces((m-2,n-2),leftover)
    beta=reduced_betti(R,len(leftover))
    predicted={k+3:v for k,v in beta.items()} if (0,1) in base and (1,0) in base else {}
    measured=reduced_betti(real,len(arcs))
    assert measured==predicted,(m,n,base,measured,predicted)
    return measured

def main():
    ncases=0; nontrivial=0; examples={}
    for m,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4)]:
        remaining=[(i,j) for i in range(m) for j in range(n) if (i,j) not in ((0,0),(1,1))]
        for mask in range(1<<len(remaining)):
            base={(0,0),(1,1)}|{e for k,e in enumerate(remaining) if (mask>>k)&1}
            beta=run(m,n,base);ncases+=1
            if beta:nontrivial+=1
        print('all graphs',m,n,'checked',1<<len(remaining))
    rng=Random(20261120)
    for m,n in [(4,4),(4,5),(5,4)]:
        remaining=[(i,j) for i in range(m) for j in range(n) if (i,j) not in ((0,0),(1,1))]
        for _ in range(15):
            base={(0,0),(1,1)}|{e for e in remaining if rng.randrange(2)}
            run(m,n,base);ncases+=1
        print('random graphs',m,n,'checked 15')
    for m,n in [(2,2),(3,4),(4,4),(4,5)]:
        ex=run(m,n,product(range(m),range(n)))
        examples[f'{m}x{n}']=ex
    print('PASS cases',ncases+4,'nontrivial',nontrivial,'complete-bipartite examples',examples)
if __name__=='__main__':main()

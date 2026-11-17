#!/usr/bin/env python3
"""Standalone finite verification for the sparse-reversal polygon theorem.
Checks graph-level definition, face factorization, and acyclic matching with
critical relative cells; no scientific or operational provenance embedded.
"""
from collections import Counter
from itertools import combinations

def valid_directed(face, arcs, n):
    out={}; inc={}
    for idx in face:
        u,v=arcs[idx]
        if u in out or v in inc: return False
        out[u]=v;inc[v]=u
    for start in out:
        x=start;seen=set()
        while x in out:
            if x in seen: return False
            seen.add(x);x=out[x]
    return True

def field_homology(faces, p):
    levels={}
    for f in faces:
        if f:levels.setdefault(len(f)-1,[]).append(tuple(sorted(f)))
    for items in levels.values():items.sort()
    ranks={}
    for d in range(1,max(levels)+1):
        rows={f:i for i,f in enumerate(levels.get(d-1,[]))}
        pivots={}
        for f in levels.get(d,[]):
            col={rows[f[:i]+f[i+1:]]:(1 if i%2==0 else p-1) for i in range(len(f))}
            while col:
                v=max(col)
                if v not in pivots:
                    a=pow(col[v],-1,p)
                    pivots[v]={i:(val*a)%p for i,val in col.items()}
                    break
                fac=col[v]
                for i,val in pivots[v].items():
                    t=(col.get(i,0)-fac*val)%p
                    if t:col[i]=t
                    else:col.pop(i,None)
        ranks[d]=len(pivots)
    betti={d:len(v)-ranks.get(d,0)-ranks.get(d+1,0) for d,v in levels.items()}
    betti[0]-=1
    return {d:b for d,b in betti.items() if b}

def test(k):
    n=3*k
    F=[(i,(i+1)%n) for i in range(n)]
    rr=[((3*i+1)%n,3*i%n) for i in range(k)]
    arcs=F+rr
    faces=set()
    for mask in range(1<<(n+k)):
        face=frozenset(j for j in range(n+k) if mask>>j&1)
        if valid_directed(face,arcs,n): faces.add(face)
    blocks=[]
    for i in range(k):
        j=3*i;blocks.append({(j-1)%n,j,(j+1)%n})
    assert set.union(*blocks)==set(range(n))
    assert sum(len(x) for x in blocks)==n
    expected=set()
    for mask in range(1<<(n+k)):
        f=frozenset(j for j in range(n+k) if mask>>j&1)
        if len(f.intersection(range(n)))==n:continue
        if all(not ((n+i) in f and bool(f&blocks[i])) for i in range(k)):
            expected.add(f)
    assert faces==expected, (len(faces),len(expected))
    chosen={min(b) for b in blocks}
    extras=set(range(n))-chosen
    Y={f for f in faces if not (f&extras)}
    paired={}; critical=[]
    for f in faces:
        present=[i for i,b in enumerate(blocks) if f & (b-{min(b)})]
        if not present:continue
        i=present[0];v=min(blocks[i])
        g=f^frozenset({v})
        if g in faces:
            paired[f]=g
        else:critical.append(f)
    assert all(paired.get(g)==f for f,g in paired.items())
    assert len(critical)==1 and critical[0]==frozenset(set(range(n))-{min(blocks[0])})
    assert sum(1 for f in faces if f not in paired)==len(Y)+1
    # Gradient graph directed: unpaired cover downward, matched cover upward.
    # Check acyclicity with topological sorting, including the empty face.
    from collections import defaultdict, deque
    edges=defaultdict(list);indeg={f:0 for f in faces}
    for f in faces:
        for v in f:
            g=f-{v}
            if paired.get(g)==f:lo,hi=g,f
            else:lo,hi=f,g
            edges[lo].append(hi);indeg[hi]+=1
    Q=deque([f for f,d in indeg.items() if d==0]);visited=0
    while Q:
        f=Q.popleft();visited+=1
        for g in edges[f]:
            indeg[g]-=1
            if indeg[g]==0:Q.append(g)
    assert visited==len(faces),(k,len(faces),visited)
    # Inclusion of full directed cycle's sphere and retraction onto cross-polytope sphere.
    for f in faces:
        retract=frozenset(min(blocks[i]) if v<n else v for i in range(k) for v in f&blocks[i])|frozenset(v for v in f if v>=n)
        assert retract in Y
    fvec=Counter(len(f)-1 for f in faces if f)
    reduced_euler=sum((-1)**i*c for i,c in fvec.items())-1
    predicted=(-1)**(k-1)+(-1)**(n-2)
    assert reduced_euler==predicted
    for p in ((2,3) if k<=3 else (2,)):
        betti=field_homology(faces,p)
        assert betti=={k-1:1,n-2:1}, (k,p,betti)
    print('PASS k=%d n=%d faces=%d relative_critical_dim=%d reduced_Euler=%d prime_checks=%s'%(k,n,len(faces),n-2,reduced_euler,((2,3) if k<=3 else (2,))))

if __name__=='__main__':
    for k in (2,3,4):test(k)

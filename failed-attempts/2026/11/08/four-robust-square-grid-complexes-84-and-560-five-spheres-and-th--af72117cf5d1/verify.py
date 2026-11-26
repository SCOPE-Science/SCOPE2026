#!/usr/bin/env python3
"""Exhaustive finite verification of four-robust square-grid complexes.
No external libraries. Use Python 3.10 or later: python3 verify_robust_k4.py.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from math import comb

TRANSFORMS=('id','r90','r180','r270','horizontal','vertical','diagonal','antidiagonal')

def transform(n,r,c,t):
    if t=='id': return r,c
    if t=='r90': return c,n-1-r
    if t=='r180': return n-1-r,n-1-c
    if t=='r270': return n-1-c,r
    if t=='horizontal': return n-1-r,c
    if t=='vertical': return r,n-1-c
    if t=='diagonal': return c,r
    if t=='antidiagonal': return n-1-c,n-1-r
    raise ValueError(t)

def sign_of_permutation(seq):
    return -1 if sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])%2 else 1

def faces_of_robust_grid(n):
    N=n*n
    adj=[0]*N
    for r in range(n):
        for c in range(n):
            u=r*n+c
            for dr,dc in ((1,0),(0,1)):
                if r+dr<n and c+dc<n:
                    v=(r+dr)*n+c+dc
                    adj[u]|=1<<v
                    adj[v]|=1<<u
    @lru_cache(maxsize=None)
    def alpha(mask):
        if mask==0:return 0
        bit=mask&-mask; v=bit.bit_length()-1; rest=mask^bit
        return max(alpha(rest),1+alpha(rest&~adj[v]))
    faces=set()
    for size in range(7):
        for w in combinations(range(N),size):
            m=sum(1<<v for v in w)
            if alpha(m)<4:faces.add(m)
    assert 0 in faces and all(x.bit_count()<=6 for x in faces)
    # Independent implementation: a face contains no independent four-set.
    independent4=set()
    for q in combinations(range(N),4):
        m=sum(1<<v for v in q)
        if all(not(adj[u]>>v&1) for u,v in combinations(q,2)):
            independent4.add(m)
    for size in range(4,7):
        for q in combinations(range(N),size):
            m=sum(1<<v for v in q)
            bad=any(sum(1<<v for v in t) in independent4 for t in combinations(q,4))
            assert (m in faces)==(not bad)
    # In a bipartite graph, any set with >=7 vertices contains four same-color vertices.
    assert len(faces)=={4:4812,5:27598}[n]
    return faces

def morse_certificate(faces,n):
    N=n*n
    unmatched=set(faces);unmatched.remove(0)
    pairs={}
    for v in range(N):
        bit=1<<v
        for a in sorted(unmatched):
            b=a|bit
            if not a&bit and b in unmatched:
                unmatched.remove(a);unmatched.remove(b)
                pairs[b]=a
    crit=Counter(x.bit_count()-1 for x in unmatched)
    target=comb((n-1)**2,3)
    assert crit=={0:1,5:target},(n,crit)
    indeg={a:0 for a in faces if a}
    adj_dir=defaultdict(list)
    edges=0
    for b in indeg:
        rem=b
        while rem:
            bit=rem&-rem;rem^=bit
            a=b^bit
            if not a: continue
            if pairs.get(b)==a:
                adj_dir[a].append(b);indeg[b]+=1
            else:
                adj_dir[b].append(a);indeg[a]+=1
            edges+=1
    Q=deque(a for a,d in indeg.items() if d==0)
    visited=0
    while Q:
        a=Q.popleft();visited+=1
        for b in adj_dir[a]:
            indeg[b]-=1
            if indeg[b]==0:Q.append(b)
    assert visited==len(indeg),(visited,len(indeg))
    assert len(pairs)*2+len(unmatched)==len(faces)-1
    return len(pairs),len(unmatched),edges,visited

def group_characters(faces,n):
    for t in TRANSFORMS:
        perm=[(lambda a:a[0]*n+a[1])(transform(n,v//n,v%n,t)) for v in range(n*n)]
        lef=-1  # Empty-simplex term in reduced Lefschetz number.
        for m in faces:
            if not m:continue
            verts=[v for v in range(n*n) if m>>v&1]
            images=[perm[v] for v in verts]
            if sum(1<<v for v in images)!=m:continue
            lef+=(-1 if len(verts)%2==0 else 1)*sign_of_permutation(images)
        trace=-lef   # Only reduced H_5, so Lefschetz = -trace.
        cells=list(range((n-1)**2))
        pc={q:(lambda a:a[0]*(n-1)+a[1])(transform(n-1,q//(n-1),q%(n-1),t)) for q in cells}
        fixed=sum(all(pc[v] in triple for v in triple) for triple in combinations(cells,3))
        orientation_sign=1 if t in TRANSFORMS[:4] else -1
        expected=orientation_sign*fixed
        assert trace==expected,(n,t,trace,expected)
        print('character',n,t,'H5_trace',trace,'signed_triple_trace',expected)

for n in (4,5):
    F=faces_of_robust_grid(n)
    pairs,critical,hasse,visited=morse_certificate(F,n)
    print('morse',n,'nonempty_faces',len(F)-1,'pairs',pairs,'critical_cells',critical,
          'critical_H5',comb((n-1)**2,3),'hasse_incidences',hasse,'acyclic_vertices',visited)
    group_characters(F,n)
print('ALL_VERIFY_OK: n=4,5; 16 characters; exhaustive acyclic Morse matching and independent face test')

#!/usr/bin/env python3
"""Reproduce intrinsic radius-3 Cech homotopy and relative one-edge deletion using exact combinatorics."""
from collections import defaultdict, Counter, deque
from itertools import combinations

ORDER=list(range(14))

def build(fault):
    edges={tuple(sorted((j,7+i))) for i in range(7) for j in (i,(i+1)%7,(i+3)%7)}
    if fault:edges.remove((0,7))
    adj=[set() for _ in range(14)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    ds=[]
    for a in range(14):
        dist=[99]*14;dist[a]=0; queue=deque([a])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if dist[w]>dist[v]+1:dist[w]=dist[v]+1;queue.append(w)
        ds.append(dist)
    facets=[tuple(c for c in range(14) if min(ds[c][u],ds[c][v])<=1) for u,v in sorted(edges)]
    faces=set()
    for f in facets:
        for j in range(1,len(f)+1):faces.update(combinations(f,j))
    # Independently reconstruct all shortest paths by Floyd--Warshall.
    fw=[[0 if i==j else (1 if tuple(sorted((i,j))) in edges else 99) for j in range(14)] for i in range(14)]
    for k in range(14):
        for i in range(14):
            for j in range(14):fw[i][j]=min(fw[i][j],fw[i][k]+fw[k][j])
    assert fw==ds
    return edges,ds,facets,faces

def vertex_matching(faces,order=ORDER):
    remain=set(faces);pairs=[]
    for v in order:
        for s in sorted(list(remain),key=lambda x:(len(x),x)):
            if v in s or s not in remain:continue
            t=tuple(sorted(s+(v,)))
            if t in remain:
                assert len(t)==len(s)+1 and s in remain
                remain.remove(s);remain.remove(t);pairs.append((s,t))
    assert 2*len(pairs)+len(remain)==len(faces)
    return pairs,remain

def check_acyclic(all_faces,pairs):
    # For a relative acyclic matching use the relative non-A face poset.
    matched={(a,b) for a,b in pairs}
    sset=set(all_faces)
    indeg={f:0 for f in sset};directions=defaultdict(list);nedges=0
    for b in sset:
        for a in combinations(b,len(b)-1):
            if a not in sset:continue
            # Reverse a->b if matched, otherwise b->a.
            u,v=(a,b) if (a,b) in matched else (b,a)
            directions[u].append(v);indeg[v]+=1;nedges+=1
    q=deque(x for x in indeg if not indeg[x]);count=0
    while q:
        a=q.popleft();count+=1
        for b in directions[a]:
            indeg[b]-=1
            if indeg[b]==0:q.append(b)
    assert count==len(sset),('cycle',len(sset)-count)
    return nedges

def rank(cols):
    piv={}
    for a in cols:
        while a:
            k=a.bit_length()-1
            if k in piv:a ^= piv[k]
            else:piv[k]=a;break
    return len(piv)

def binary_homology(faces):
    fs={k:sorted(f for f in faces if len(f)==k+1) for k in range(6)}
    br={0:0}
    for k in range(1,6):
        m={f:i for i,f in enumerate(fs[k-1])}
        cols=[]
        for f in fs[k]:
            b=0
            for a in combinations(f,len(f)-1):b^=1<<m[a]
            cols.append(b)
        br[k]=rank(cols)
    hom={k:len(fs[k])-br[k]-br.get(k+1,0) for k in range(6)};hom[0]-=1
    return {k:len(v) for k,v in fs.items()},br,hom

if __name__=='__main__':
    intact=build(False);fault=build(True)
    assert len(intact[0])==21 and len(fault[0])==20
    # Explicit incidence-preserving generators prove all twenty-one edges form one orbit.
    def mult(v):return (2*v)%7 if v<7 else 7+(2*(v-7)+6)%7
    def translate(v):return (v+1)%7 if v<7 else 7+((v-7+1)%7)
    for perm in (mult,translate):
        assert {tuple(sorted((perm(u),perm(v)))) for u,v in intact[0]}==intact[0]
    orbit=set();u,v=(0,7)
    for k in range(3):
        a,b=u,v
        for j in range(7):
            orbit.add(tuple(sorted((a,b))))
            a,b=translate(a),translate(b)
        u,v=mult(u),mult(v)
    assert orbit==intact[0]
    assert all(len(a)==3 for a in [set(v for u,v in intact[0] if u==x)|set(u for u,v in intact[0] if v==x) for x in range(14)])
    assert fault[3].issubset(intact[3])
    f,intf=fault[3],intact[3]
    pf,cf=vertex_matching(f); pi,ci=vertex_matching(intf)
    assert Counter(map(lambda s:len(s)-1,cf))=={0:1,2:37}
    assert Counter(map(lambda s:len(s)-1,ci))=={0:1,2:48}
    e_f=check_acyclic(f,pf);e_i=check_acyclic(intf,pi)
    rel=intf-f
    pr,cr=vertex_matching(rel)
    assert Counter(map(lambda s:len(s)-1,cr))=={2:11}
    e_r=check_acyclic(rel,pr)
    assert check_acyclic(intf,pr)==e_i  # extends to the full pair, no cyclic gradient path through the base
    ff,rf,hf=binary_homology(f);fi,ri,hi=binary_homology(intf)
    assert (ff,fi)==({0:14,1:86,2:262,3:236,4:100,5:16},{0:14,1:91,2:308,3:287,4:126,5:21})
    assert hf=={0:0,1:0,2:37,3:0,4:0,5:0}
    assert hi=={0:0,1:0,2:48,3:0,4:0,5:0}
    print('INTACT',len(intf),'faces',len(pi),'pairs',len(ci),'critical',e_i,'Hasse edges',fi,ri,hi)
    print('FAULT',len(f),'faces',len(pf),'pairs',len(cf),'critical',e_f,'Hasse edges',ff,rf,hf)
    print('RELATIVE',len(rel),'faces',len(pr),'pairs',len(cr),'critical',e_r,'Hasse edges')
    print('VERIFY_OK')

#!/usr/bin/env python3
"""Independent characteristic-polynomial check by matchings on labelled trees.
Only the Python standard library is required. Polynomials are bitmasks over F_2.
"""
from itertools import product
from collections import defaultdict

def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        a<<=1;b>>=1
    return out

def edges_from_prufer(code, n):
    deg=[1]*n
    for z in code:deg[z]+=1
    ed=[]
    for v in code:
        leaf=next(k for k in range(n) if deg[k]==1)
        ed.append((leaf,v));deg[leaf]-=1;deg[v]-=1
    a,b=[k for k in range(n) if deg[k]==1]
    ed.append((a,b))
    return ed

def tree_poly(edges,n):
    # Matching polynomial in char 2: sum_M x^(n-2|M|).
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    def walk(v,p):
        children=[walk(w,v) for w in adj[v] if w!=p]
        P=2
        for q,_ in children:P=mul(P,q)
        for i,(_,q_del) in enumerate(children):
            t=q_del
            for j,(q,_) in enumerate(children):
                if j!=i:t=mul(t,q)
            P^=t
        R=1
        for q,_ in children:R=mul(R,q)
        return P,R
    return walk(0,-1)[0]

def distance(edges,n,u,v):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    q=[u];dist={u:0}
    for x in q:
        for y in adj[x]:
            if y not in dist:dist[y]=dist[x]+1;q.append(y)
    return dist[v]

counts={}
for n in (4,6,8):
    total=0
    for code in product(range(n),repeat=n-2):
        num=[0]*n
        for c in code:num[c]+=1
        ev=[i for i,x in enumerate(num) if x%2==1]  # deg=1+count
        if len(ev)!=2:continue
        ed=edges_from_prufer(code,n)
        d=distance(ed,n,*ev)
        m=d+1
        assert n>=2*m
        q=(1<<(m+1))-1
        predicted=mul(q,q)<<(n-2*m)
        actual=tree_poly(ed,n)
        assert predicted==actual,(n,code,d,predicted,actual)
        total+=1
    counts[n]=total
print('MATCHING_CHECK_OK',counts)

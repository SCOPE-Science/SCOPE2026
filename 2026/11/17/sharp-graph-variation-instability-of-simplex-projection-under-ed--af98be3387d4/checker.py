#!/usr/bin/env python3
"""Exact-rational diagnostics for simplex projection and edge variation."""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def edges_for(n, emask):
    all_edges=list(combinations(range(n),2))
    return [e for j,e in enumerate(all_edges) if emask>>j &1]

def connected(n,edges):
    neighbors=[[] for _ in range(n)]
    for u,v in edges: neighbors[u].append(v);neighbors[v].append(u)
    seen={0};stack=[0]
    while stack:
        u=stack.pop()
        for v in neighbors[u]:
            if v not in seen:seen.add(v);stack.append(v)
    return len(seen)==n

def value_for(n, edges, active, cut):
    k=active.bit_count(); a=(active&cut).bit_count();b=k-a
    H=[b if (active>>i &1) and (cut>>i &1) else (-a if (active>>i &1) else 0) for i in range(n)]
    num=sum(abs(H[u]-H[v]) for u,v in edges)
    c=sum(((cut>>u)^(cut>>v))&1 for u,v in edges)
    return F(num, k*c) if c else F(0)

def closed(n):
    if n%2: return 1+F(n*n-1,16)
    if n%4==0: return 1+F(n*n,16)
    return 1+F(n*n-4,16)

def project_simplex(x,r=F(1)):
    z=sorted(x,reverse=True)
    for k in range(len(x),0,-1):
        threshold=(sum(z[:k])-r)/k
        if z[k-1]>threshold and (k==len(x) or z[k]<=threshold):
            out=[max(F(0),v-threshold) for v in x]
            assert sum(out)==r
            return out
    raise AssertionError('threshold missing')

def tv(x,edges):return sum(abs(x[u]-x[v]) for u,v in edges)

def witness(n):
    vals=[(F((k*k)//4,k)*(n-k),k) for k in range(2,n+1)]
    target,k=max(vals,key=lambda a:a[0])
    a=k//2;b=k-a
    # First clique S has a active plus n-k inactive vertices; second clique is b active.
    s=n-b;edges=list(combinations(range(s),2))+list(combinations(range(s,n),2))+[(0,s)]
    A=set(range(a))|set(range(s,n))
    y=[F(1,k) if i in A else F(-1) for i in range(n)]
    h=[F(1) if i<s else F(0) for i in range(n)]
    eps=F(1,10*n)
    p=project_simplex(y);q=project_simplex([y[i]+eps*h[i] for i in range(n)])
    den=tv([eps*t for t in h],edges)
    got=tv([q[i]-p[i] for i in range(n)],edges)/den
    assert got==closed(n),(n,got,closed(n))
    return got, k, a,b

count=0
for n in range(2,6):
    ne=n*(n-1)//2
    graphcount=0;triples=0;observed=F(0)
    for mask in range(1<<ne):
        edges=edges_for(n,mask)
        if not connected(n,edges):continue
        graphcount+=1
        for A in range(1,1<<n):
            for S in range(1,(1<<n)-1):
                v=value_for(n,edges,A,S)
                assert v<=closed(n),(n,edges,A,S,v,closed(n))
                observed=max(observed,v)
                triples+=1
    assert observed==closed(n),(n,observed,closed(n))
    print('ALL_CONNECTED_LABELED_GRAPHS_AND_SUPPORT_CUTS_PASSED',n,graphcount,triples,'sharp',observed)
    count+=triples
rnd=Random(8111)
trials=0
for n in range(6,12):
    for _ in range(30):
        edges=[(i,i+1) for i in range(n-1)]
        for u,v in combinations(range(n),2):
            if (u,v) not in edges and rnd.randrange(3)==0:edges.append((u,v))
        for _ in range(250):
            A=rnd.randrange(1,1<<n); S=rnd.randrange(1,(1<<n)-1)
            value=value_for(n,edges,A,S)
            assert value<=closed(n)
            trials+=1
print('RANDOM_CONNECTED_GRAPH_ACTIVE_CUT_RATIONAL_BOUNDS_PASSED',trials)
def q_clique_witness(n,q):
    assert n>=4*q
    values=[(F((k*k)//4,k)*(n-k), k) for k in range(2,n+1) if k//2>=q]
    f,k=max(values,key=lambda pair: pair[0])
    assert 1+f/q==1+(closed(n)-1)/q
    a=k//2;b=k-a
    inactive=n-k;u=inactive//2;v=inactive-u
    left=a+u;right=b+v
    assert min(left,right)>=q+1
    # active positions: first a on left, first b on right
    A=set(range(a))|set(range(left,left+b))
    edges=list(combinations(range(left),2))+list(combinations(range(left,n),2))
    edges+=list(zip(range(q),range(left,left+q)))
    S=sum(1<<i for i in range(left));Amask=sum(1<<i for i in A)
    value=value_for(n,edges,Amask,S)
    assert value==1+(closed(n)-1)/q,(n,q,value)
    # independent exact nonlinear projection pair
    x=[F(1,k) if i in A else F(-1) for i in range(n)]
    y=[x[i]+F(1,10*n)*(i<left) for i in range(n)]
    Px=project_simplex(x);Py=project_simplex(y)
    ratio=tv([Py[i]-Px[i] for i in range(n)],edges)/tv([y[i]-x[i] for i in range(n)],edges)
    assert ratio==value
    # exact edge-connectivity verification for small order only
    if n<=13:
        mincut=min(sum(((cut>>x)^(cut>>y))&1 for x,y in edges) for cut in range(1,(1<<n)-1))
        assert mincut==q,(n,q,mincut)
    return ratio

qc=0
for q in range(1,6):
    for n in range(4*q,4*q+9):
        q_clique_witness(n,q)
        qc+=1
print('EXACT_EDGE_CONNECTIVITY_SHARPNESS_WITNESSES_PASSED',qc)
for n in range(2,61):
    ans,k,a,b=witness(n)
    print('EXACT_ATTAINING_BRIDGED_CLIQUES',n,str(ans),k,a,b)
print('ALL_GRAPH_SIMPLEX_VARIATION_CHECKS_PASSED',count+trials+59)

#!/usr/bin/env python3
"""Exact finite checks for the vacancy-overlap kernel of partial triple systems.
Requires Python 3 standard library only. The proof for arbitrary size is in RESULT.md.
"""
from itertools import combinations
from math import gcd
from collections import Counter


def ext_gcd(a,b):
    if b == 0: return (abs(a), 1 if a>0 else -1, 0)
    g,x,y=ext_gcd(b,a%b)
    return g,y,x-(a//b)*y


def lattice_basis(vectors,n):
    """Unimodular column operations yield a Z-basis of the column lattice."""
    if not vectors: return []
    a=[[v[i] for v in vectors] for i in range(n)]
    m=len(vectors); k=0
    for i in range(n):
        candidates=[j for j in range(k,m) if a[i][j]!=0]
        if not candidates:continue
        j=candidates[0]
        for row in a:row[k],row[j]=row[j],row[k]
        for j in range(k+1,m):
            x,y=a[i][k],a[i][j]
            if y==0:continue
            g,u,v=ext_gcd(x,y)
            for row in a:
                oldk,oldj=row[k],row[j]
                row[k]=u*oldk+v*oldj
                row[j]=(-y//g)*oldk+(x//g)*oldj
        if a[i][k]<0:
            for row in a:row[k]=-row[k]
        assert all(a[i][j]==0 for j in range(k+1,m))
        k+=1
        if k==m:break
    assert all(a[i][j]==0 for i in range(n) for j in range(k,m))
    return [[a[i][j] for i in range(n)] for j in range(k)]


def det(a):
    n=len(a)
    if n==0:return 1
    b=[list(row) for row in a]
    sign=1;prev=1
    for k in range(n-1):
        if b[k][k]==0:
            for j in range(k+1,n):
                if b[j][k]:b[k],b[j]=b[j],b[k];sign=-sign;break
            else:return 0
        piv=b[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=b[i][j]*piv-b[i][k]*b[k][j]
                assert num%prev==0
                b[i][j]=num//prev
            b[i][k]=0
        prev=piv
    return sign*b[-1][-1]


def smith_by_minors(a):
    n=len(a);dprev=1;res=[]
    for k in range(1,n+1):
        dk=0
        for rows in combinations(range(n),k):
            for cols in combinations(range(n),k):
                dk=gcd(dk,abs(det([[a[i][j] for j in cols] for i in rows])))
                if dk==dprev:break
            if dk==dprev:break
        if dk==0:break
        assert dk%dprev==0
        res.append(dk//dprev);dprev=dk
    return res


def matchings(n,edges):
    edges=list(edges)
    def go(i,used,chosen):
        if i==len(edges):yield tuple(chosen);return
        yield from go(i+1,used,chosen)
        x,y=edges[i]
        if not ((1<<x|1<<y)&used):yield from go(i+1,used|(1<<x)|(1<<y),chosen+[edges[i]])
    return list(go(0,0,[]))


def smith_for_leave(n,edges):
    vectors=[[1]*n]+[[int(j in e) for j in range(n)] for e in edges]
    b=lattice_basis(vectors,n)
    G=[[sum(x*y for x,y in zip(v,w)) for w in b] for v in b]
    return smith_by_minors(G)


def connected(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    seen={0};todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    return len(seen)==n,adj


def prediction(n,edges):
    ok,adj=connected(n,edges)
    if not ok:return None
    color={0:0};todo=[0];bip=True
    while todo:
        x=todo.pop()
        for y in adj[x]:
            if y not in color:color[y]=1-color[x];todo.append(y)
            elif color[y]==color[x]:bip=False
    if bip:
        p=sum(v==0 for v in color.values());s=abs(n-2*p)
        if s==0:return [1]*(n-2)+[n]
        if n==1:return [1]
        g=gcd(n,s)
        return [1]*(n-2)+[g,s*s//g]
    return [1]*n if n%2 else [1]*(n-2)+[2,2]


def partial_systems(n):
    ts=list(combinations(range(n),3))
    pairs=list(combinations(range(n),2))
    pairids={p:i for i,p in enumerate(pairs)}
    ms=[sum(1<<pairids[e] for e in combinations(t,2)) for t in ts]
    def go(k,used,sel):
        if k==len(ts):yield tuple(sel);return
        yield from go(k+1,used,sel)
        if not (used&ms[k]):yield from go(k+1,used|ms[k],sel+[ts[k]])
    return go(0,0,[])


def direct_check(n,edges):
    ms=matchings(n,edges)
    F=[[int(i not in {z for e in m for z in e}) for i in range(n)] for m in ms]
    C=[[sum(x*y for x,y in zip(u,v)) for v in F] for u in F]
    for i,m in enumerate(ms):
        for j,m2 in enumerate(ms):
            common=sum(all(v not in e for e in m) and all(v not in e for e in m2) for v in range(n))
            assert C[i][j]==common
    if len(ms)<=10:
        B=lattice_basis(F,n)
        G=[[sum(x*y for x,y in zip(v,w)) for w in B] for v in B]
        assert smith_by_minors(C)==smith_by_minors(G)
    return len(ms)


def run():
    graph_tests=0
    for n in range(1,6):
        es=list(combinations(range(n),2))
        for mask in range(1<<len(es)):
            E=[e for i,e in enumerate(es) if mask>>i&1]
            pred=prediction(n,E)
            if pred is None:continue
            assert smith_for_leave(n,E)==pred,(n,E,pred,smith_for_leave(n,E))
            graph_tests+=1
    # Independent exact enumeration of all small partial designs.
    system_tests=0; groups=Counter()
    for n in range(1,7):
        for S in partial_systems(n):
            covered={e for t in S for e in combinations(t,2)}
            E=[e for e in combinations(range(n),2) if e not in covered]
            if n<=4:direct_check(n,E)
            actual=smith_for_leave(n,E)
            expected=prediction(n,E)
            if expected is not None:assert actual==expected
            groups[n]+=1;system_tests+=1
    # Nontrivial balanced connected leave: two disjoint old triples.
    E=[(x,y) for x in range(3) for y in range(3,6)]
    assert len(matchings(6,E))==34
    assert smith_for_leave(6,E)==[1,1,1,1,6]
    # Leave a star by adjoining one unused point to a Fano plane.
    E=[(0,y) for y in range(1,8)]
    assert smith_for_leave(8,E)==[1]*6+[2,18]
    # Directly check all vacancy-overlap counts on key examples.
    direct_check(4,list(combinations(range(4),2)))
    direct_check(6,[(0,i) for i in range(1,6)])
    print('GRAPH_CHECKS',graph_tests)
    print('PARTIAL_DESIGN_CHECKS',system_tests,dict(groups))
    print('TWO_TRIPLES_SNF','1,1,1,1,6')
    print('FANO_PLUS_ISOLATE_SNF','1,1,1,1,1,1,2,18')
    print('VERIFY_OK')

if __name__=='__main__':run()

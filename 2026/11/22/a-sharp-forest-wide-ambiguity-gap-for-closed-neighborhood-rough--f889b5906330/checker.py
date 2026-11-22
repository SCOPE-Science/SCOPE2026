#!/usr/bin/env python3
"""Independent finite tests for the tree rough-observation edge-cover formula.
No external libraries; Python 3.10+.
"""
from collections import Counter
from itertools import combinations, product
from random import Random


def components(n, edges):
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i].append(j); adj[j].append(i)
    comps=[]; seen=set()
    for i in range(n):
        if i in seen: continue
        todo=[i];seen.add(i); comp=[]
        while todo:
            u=todo.pop(); comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v);todo.append(v)
        comps.append(comp)
    return comps


def forest(n, edges):
    # Since connected components of a forest have |V|-1 edges.
    return len(edges)==n-len(components(n,edges))


def brute(n, edges):
    neigh=[1<<u for u in range(n)]
    for u,v in edges:
        neigh[u]|=1<<v;neigh[v]|=1<<u
    out=Counter()
    for x in range(1<<n):
        A=0;Z=0
        for u in range(n):
            if x&neigh[u]==neigh[u]:A|=1<<u
            if x&neigh[u]==0:Z|=1<<u
        out[A,Z]+=1
    return out


def parity_between(n, edges, u, v, F):
    adj=[[] for _ in range(n)]
    for i,(a,b) in enumerate(edges):
        adj[a].append((b,i));adj[b].append((a,i))
    stack=[(u,-1,0)]
    while stack:
        x,prev,par=stack.pop()
        if x==v:return par
        for y,i in adj[x]:
            if y!=prev:stack.append((y,x,par^((F>>i)&1)))
    raise AssertionError('no path in component')


def formula(n,edges,A,Z):
    mask=(1<<n)-1
    if A&Z:return 0
    W=A|Z; B=mask^W
    comps=components(n,edges)
    free=sum(not any(W>>v&1 for v in comp) for comp in comps)
    valid=0
    for F in range(1<<len(edges)):
        cover=0;wrong=False
        for i,(u,v) in enumerate(edges):
            if F>>i&1:
                if (W>>u&1) or (W>>v&1):wrong=True;break
                cover|=(1<<u)|(1<<v)
        if wrong or cover!=B:continue
        for comp in comps:
            marked=[v for v in comp if W>>v&1]
            if not marked:continue
            root=marked[0]
            for v in marked[1:]:
                if (bool(A>>root&1)^bool(A>>v&1))!=bool(parity_between(n,edges,root,v,F)):
                    wrong=True;break
            if wrong:break
        if not wrong:valid+=1
    return (1<<free)*valid


def central_and_gap(n,edges,out):
    c=out[0,0]
    # Here output labels A=Z=0 is the central pair.
    assert c>0, ('no central',n,edges)
    comps=components(n,edges)
    for (A,Z),f in out.items():
        s=sum(any((A|Z)>>v&1 for v in comp) for comp in comps)
        assert f*(1<<s)<=c,(n,edges,A,Z,f,c,s)
    edgecover=sum(all(any(((F>>i)&1) and (u==vtx or v==vtx) for i,(u,v) in enumerate(edges)) for vtx in range(n)) for F in range(1<<len(edges)))
    assert c==(1<<len(comps))*edgecover,(n,edges,c,edgecover)


def verify(n,edges):
    out=brute(n,edges)
    central_and_gap(n,edges,out)
    for labels in product(range(3),repeat=n):
        A=sum(1<<i for i,x in enumerate(labels) if x==1)
        Z=sum(1<<i for i,x in enumerate(labels) if x==2)
        pred=formula(n,edges,A,Z)
        assert pred==out[A,Z],('fiber mismatch',n,edges,A,Z,pred,out[A,Z])
    return len(out)


def main():
    graphs=0;fiberlabels=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for g in range(1<<len(pairs)):
            E=[e for i,e in enumerate(pairs) if g>>i&1]
            if forest(n,E) and all(any(u in e for e in E) for u in range(n)):
                fiberlabels+=3**n
                verify(n,E);graphs+=1
    rng=Random(651108)
    for n in (6,7):
        # Extra random spanning trees with intentionally varied branching.
        for trial in range(24):
            E=[]
            for v in range(1,n):E.append((rng.randrange(v),v))
            rng.shuffle(E)
            fiberlabels+=3**n
            verify(n,E);graphs+=1
    print(f'VERIFY_OK graphs={graphs} label_tests={fiberlabels}')

if __name__=='__main__':main()

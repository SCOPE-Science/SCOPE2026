#!/usr/bin/env python3
"""Independent finite checks for adjacent-swap geometry of one-pass pop-stack sortable permutations.
The mathematical proof is in RESULT.md; this finite checker is not used as an infinite proof.
"""
from itertools import permutations, combinations
from collections import Counter, deque
from math import prod


def fibonacci(k):
    a,b=0,1
    for _ in range(k): a,b=b,a+b
    return a


def compositions(n):
    if n==0:
        yield ()
        return
    for mask in range(1 << (n-1)):
        lengths=[]; last=0
        for p in range(1,n):
            if mask & (1 << (p-1)):
                lengths.append(p-last);last=p
        lengths.append(n-last)
        yield tuple(lengths)


def layered(comp):
    out=[];m=0
    for x in comp:
        out.extend(range(m+x,m,-1));m+=x
    return tuple(out)


def popstack(p):
    ans=[];a=0
    while a<len(p):
        b=a+1
        while b<len(p) and p[b-1]>p[b]:b+=1
        ans.extend(reversed(p[a:b]));a=b
    return tuple(ans)


def graph(n):
    comps=list(compositions(n)); labels={layered(c):c for c in comps}
    vertices=set(labels)
    adjacency={p:set() for p in vertices}
    for p in vertices:
        for j in range(n-1):
            q=list(p);q[j],q[j+1]=q[j+1],q[j];q=tuple(q)
            if q in vertices:adjacency[p].add(q)
    return labels,adjacency


def gap_signature(comp):
    """Alternating sequence: ordinary interval lengths, frozen interval lengths."""
    gaps=[]; frozen=[]; current=0
    for x in comp:
        if x>=3:
            gaps.append(current);frozen.append(x);current=0
        else:current+=x
    gaps.append(current)
    return tuple(gaps),tuple(frozen)


def bits(comp):
    """For each non-frozen interval: dimer start bits, length gap-1."""
    arr=[];cur=[]
    for x in comp+(3,):
        if x>=3:
            arr.append(tuple(cur));cur=[]
        else:
            if x==1:cur.extend([0])
            else:cur.extend([1,0])
    # The bits above are indexed by unit positions in each gap,
    # with 2-blocks marked by 1 at their starts; remove final entry.
    return tuple(tuple(z[:-1]) for z in arr)


def expected_components(n):
    c=Counter()
    for comp in compositions(n):c[gap_signature(comp)]+=1
    return c


def actual_components(adjacency,labels):
    todo=set(adjacency); groups=[]
    while todo:
        p=todo.pop();stack=[p];group={p}
        while stack:
            q=stack.pop()
            for r in adjacency[q]:
                if r in todo:
                    todo.remove(r);group.add(r);stack.append(r)
        groups.append(group)
    return groups


def pairwise_distance_check(group,adjacency,labels):
    for source in group:
        ds={source:0};queue=deque([source])
        while queue:
            p=queue.popleft()
            for q in adjacency[p]:
                if q not in ds:ds[q]=ds[p]+1;queue.append(q)
        assert set(ds)==group
        for target,d in ds.items():
            aa=bits(labels[source]);bb=bits(labels[target])
            assert len(aa)==len(bb)
            ham=sum(x!=y for a,b in zip(aa,bb) for x,y in zip(a,b))
            assert d==ham,(source,target,d,ham)


def comp_count_recurrence(N):
    # (1 - 2z + z^2 - z^3) C(z) = 1-z
    c=[0]*(N+1)
    for n in range(N+1):
        c[n]=(1 if n==0 else -1 if n==1 else 0)
        if n>=1:c[n]+=2*c[n-1]
        if n>=2:c[n]-=c[n-2]
        if n>=3:c[n]+=c[n-3]
    return c


def isolated_count_recurrence(N):
    # (1-z-z^3-z^4) I(z)=1-z^2
    a=[0]*(N+1)
    for n in range(N+1):
        a[n]=(1 if n==0 else -1 if n==2 else 0)
        for k in (1,3,4):
            if n>=k:a[n]+=a[n-k]
    return a


def main():
    rec_c=comp_count_recurrence(120)
    rec_i=isolated_count_recurrence(120)
    for n in range(0,13):
        labels,adj=graph(n)
        assert len(labels)==(1<<(max(n-1,0)))
        if n<=8:
            legit=set(permutations(range(1,n+1))) if n else {()}
            expected={p for p in legit if popstack(p)==tuple(range(1,n+1))}
            assert expected==set(labels),(n,len(expected),len(labels))
        for p,ns in adj.items():
            assert all(p in adj[q] for q in ns)
            c=labels[p]
            expected_degree=sum(a==2 for a in c)+sum(c[i]==c[i+1]==1 for i in range(len(c)-1))
            assert len(ns)==expected_degree,(n,p,c,expected_degree,len(ns))
        components=actual_components(adj,labels)
        group_signatures=[]
        for group in components:
            signatures={gap_signature(labels[p]) for p in group}
            assert len(signatures)==1,(n,signatures)
            sig=next(iter(signatures));group_signatures.append(sig)
            gaps,_=sig
            assert len(group)==prod(fibonacci(l+1) for l in gaps)
            assert all(len(bits(labels[p])[j])==max(0,l-1) for p in group for j,l in enumerate(gaps))
            if n<=8:pairwise_distance_check(group,adj,labels)
        assert len(group_signatures)==len(set(group_signatures))
        assert len(components)==rec_c[n]
        assert sum(len(g)==1 for g in components)==rec_i[n]
        edges=sum(len(v) for v in adj.values())//2
        expected_edges=(n+1)*(2**(n-4)) if n>=4 else (2 if n==3 else 1 if n==2 else 0)
        assert edges==expected_edges,(n,edges,expected_edges)
        if n>=2:
            big=max(components,key=len)
            assert len(big)==fibonacci(n+1)
            assert sum(len(g)==len(big) for g in components)==1
        print(f'n={n:2} vertices={len(labels):4} edges={edges:4} components={len(components):3} isolates={sum(len(g)==1 for g in components):3} largest={max(map(len,components)):3}')
    print('PASS: exhaustive algorithmic classification, geodesics through n=8; induced graph and enumerators through n=12; independent pop-stack enumeration through n=8')

if __name__=='__main__':main()

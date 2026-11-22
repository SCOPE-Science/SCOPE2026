"""Exact rim-and-chord enumeration of maximum induced matchings.

Independent of check_twisted.py: edges are 2n-cycle and antipodal chords,
and exhaustive search uses edge-conflict bitmasks and branch-and-bound.
Run python3 verify_rim.py [maximum_n] (default 12).
"""
from collections import Counter
import sys

def check(n):
    assert n>=4
    N=2*n
    E=sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)}|
             {(i,i+n) for i in range(n)})
    A=[set() for _ in range(N)]
    for u,v in E:A[u].add(v);A[v].add(u)
    blocked=[]
    for i,(u,v) in enumerate(E):
        mask=0
        for j,(a,b) in enumerate(E):
            if i==j or {u,v}&{a,b} or a in A[u] or b in A[u] or a in A[v] or b in A[v]:
                mask|=1<<j
        blocked.append(mask)
    best=0;sol=[]
    def rec(candidates, chosen, size):
        nonlocal best,sol
        if not candidates:
            if size>best:best=size;sol=[chosen]
            elif size==best:sol.append(chosen)
            return
        if size+candidates.bit_count()<best:return
        vertex=(candidates&-candidates).bit_length()-1
        rec(candidates & ~blocked[vertex],chosen|(1<<vertex),size+1)
        rec(candidates & ~(1<<vertex),chosen,size)
    rec((1<<len(E))-1,0,0)
    assert best==n//2,(n,best)
    expect=n*n if n%2 else (6 if n%4==2 else 2)
    assert len(sol)==expect,(n,len(sol),expect)
    opt=set(sol);deg=Counter();adj={v:set() for v in sol}
    for x in sol:
        for edge in range(len(E)):
            if x>>edge&1:
                reduced=x^(1<<edge)
                for replacement in range(len(E)):
                    if not(reduced>>replacement&1):
                        y=reduced|(1<<replacement)
                        if y!=x and y in opt:adj[x].add(y)
        deg[len(adj[x])]+=1
    remaining=set(sol);comp=[]
    while remaining:
        start=remaining.pop();q=[start];count=1
        while q:
            x=q.pop()
            for y in adj[x]:
                if y in remaining:
                    remaining.remove(y);q.append(y);count+=1
        comp.append(count)
    if n%2:
        assert comp==[n*n] and deg==Counter({4:n*(n-3),5:2*n,6:n}),(n,comp,deg)
        assert sum(map(len,adj.values()))//2==2*n*(n+1)
    else:
        assert len(comp)==expect and all(k==1 for k in comp) and deg==Counter({0:expect})
    return (n,best,len(sol),sorted(deg.items()),sorted(comp))

if __name__=='__main__':
    top=int(sys.argv[1]) if len(sys.argv)>1 else 12
    for n in range(4,top+1):
        print(check(n),flush=True)

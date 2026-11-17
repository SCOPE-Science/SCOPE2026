#!/usr/bin/env python3
"""Exact finite transition certificate for short time returns of elementary Rule 110.
All arithmetic is Python integer arithmetic; no third-party packages.
"""
from collections import defaultdict
import json

RULE = 110

def loc(a,b,c):
    return (RULE >> (4*a+2*b+c)) & 1

def edges(t):
    """An edge is a (2t+1)-word whose t-fold local update is its center."""
    k=2*t
    result=[]
    for word in range(1<<(k+1)):
        b=[(word >> (k-i)) & 1 for i in range(k+1)]
        v=b[:]
        for _ in range(t):
            v=[loc(v[i],v[i+1],v[i+2]) for i in range(len(v)-2)]
        if v[0]==b[t]:
            result.append((word>>1,word&((1<<k)-1)))
    return result

def components(vcount, pairs):
    adj=[[] for _ in range(vcount)]
    for a,b in pairs: adj[a].append(b)
    index=[-1]*vcount; low=[0]*vcount; stack=[]; in_stack=[False]*vcount
    out=[]; next_index=0
    def visit(v):
        nonlocal next_index
        index[v]=low[v]=next_index;next_index+=1
        stack.append(v);in_stack[v]=True
        for w in adj[v]:
            if index[w]<0:
                visit(w);low[v]=min(low[v],low[w])
            elif in_stack[w]:low[v]=min(low[v],index[w])
        if low[v]==index[v]:
            comp=[]
            while True:
                w=stack.pop();in_stack[w]=False;comp.append(w)
                if w==v:break
            out.append(comp)
    import sys
    sys.setrecursionlimit(12000)
    for v in range(vcount):
        if index[v]<0:visit(v)
    return out

def mul(x,y):
    z=[0]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    return z

def determinant_from_traces(vertices,pairs):
    n=len(vertices); d={v:i for i,v in enumerate(vertices)}
    adj=[[] for _ in range(n)]
    for a,b in pairs:
        if a in d and b in d:adj[d[a]].append(d[b])
    traces=[0]*(n+1)
    for start in range(n):
        dp=[0]*n;dp[start]=1
        for t in range(1,n+1):
            ndp=[0]*n
            for v,weight in enumerate(dp):
                if weight:
                    for w in adj[v]:ndp[w]+=weight
            dp=ndp;traces[t]+=dp[start]
    coeff=[1]
    for k in range(1,n+1):
        total=sum(coeff[k-i]*traces[i] for i in range(1,k+1))
        assert total%k==0,(k,total)
        coeff.append(-total//k)
    return coeff, traces

expected={
  1:[1,-1],
  2:mul([1,-1],[1,0,0,0,-1]),
  3:mul([1,-1],[1]+[0]*8+[-1]),
  4:mul([1,-1],[1,0,0,0,-1]),
  5:mul(mul([1,-1],[1]+[0]*4+[-2]),mul([1]+[0]*4+[1]+[0]*4+[-1],[1]+[0]*4+[1]+[0]*4+[-1]))
}
output=[]
for t in range(1,6):
    k=2*t;pairs=edges(t);vcount=1<<k
    comps=components(vcount,pairs)
    cycles=[]
    for comp in comps:
        c=set(comp)
        if len(comp)>1 or any(a==b and a in c for a,b in pairs):cycles.append(sorted(comp))
    expected_big={1:[],2:[4],3:[9],4:[4],5:[64]}
    assert sorted(len(comp) for comp in cycles if len(comp)>1)==expected_big[t]
    assert sum(len(comp)==1 for comp in cycles)==1
    assert any(comp==[0] for comp in cycles)
    full=[1]
    for comp in cycles:
        det,trace=determinant_from_traces(comp,pairs)
        full=mul(full,det)
    while len(full)>1 and full[-1]==0:full.pop()
    assert full==expected[t],(t,full,expected[t])
    output.append({'time_iterate':t,'vertices':vcount,'edges':len(pairs),
       'cyclic_component_sizes':sorted(map(len,cycles)),
       'determinant_coefficients_degree':len(full)-1,
       'determinant_nonzero_coefficients':{str(i):a for i,a in enumerate(full) if a},
       'largest_component_edges':max(sum(a in set(c) and b in set(c) for a,b in pairs) for c in cycles)})
print(json.dumps({'rule':110,'certificate':'PASS', 'proof_steps':output},sort_keys=True,indent=2))

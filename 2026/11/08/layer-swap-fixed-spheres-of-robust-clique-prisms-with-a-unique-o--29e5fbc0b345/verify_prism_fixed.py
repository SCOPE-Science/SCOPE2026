#!/usr/bin/env python3
"""Exhaustive small-case verification of fixed-layer robust clique prism theorem."""
from itertools import combinations
from math import comb

def connected_bipartite(G,sub):
    sub=set(sub); color={}
    for start in sub:
        if start in color: continue
        color[start]=0; stack=[start]
        while stack:
            v=stack.pop()
            for w in G[v] & sub:
                if w in color:
                    if color[w]==color[v]: return False
                else:
                    color[w]=1-color[v]; stack.append(w)
    return True

def max_bipartite_suborder(G,S):
    for n in range(len(S),-1,-1):
        for t in combinations(S,n):
            if connected_bipartite(G,t): return n
    assert False

def graph(n,edges):
    G=[set() for _ in range(n)]
    for u,v in edges: G[u].add(v);G[v].add(u)
    return G

def boundary_rank_mod2(columns):
    piv={}
    for col in columns:
        v=col
        while v:
            p=v.bit_length()-1
            if p in piv: v^=piv[p]
            else: piv[p]=v;break
    return len(piv)

def betti(F):
    # F is list of faces as frozensets; empty included. For reduced homology.
    L=[sorted([tuple(sorted(f)) for f in F if len(f)==j]) for j in range(max(map(len,F))+1)]
    ranks={}
    for j in range(1,len(L)):
        ix={v:i for i,v in enumerate(L[j-1])}
        ranks[j]=boundary_rank_mod2([sum(1<<ix[f[:z]+f[z+1:]] for z in range(len(f))) for f in L[j]])
    ranks[0]=0
    return {j-1:len(L[j])-ranks.get(j,0)-ranks.get(j+1,0) for j in range(len(L)) if len(L[j])-ranks.get(j,0)-ranks.get(j+1,0)}

def direct_prism_alpha(G,S):
    vv=[(v,l) for v in S for l in range(2)]
    adj=[]
    for i,(v,l) in enumerate(vv):
        adj.append(sum((1<<j) for j,(w,ll) in enumerate(vv) if i!=j and ((v==w and l!=ll) or (l==ll and w in G[v]))))
    best=0
    for mask in range(1<<len(vv)):
        if mask.bit_count()<=best: continue
        if any((mask>>i)&1 and adj[i]&mask for i in range(len(vv))): continue
        best=mask.bit_count()
    return best

def examine(n,edges,odd_cycle):
    G=graph(n,edges); checked=0
    for k in range(2,n+2):
        F=[]
        for mask in range(1<<n):
            S=[i for i in range(n) if (mask>>i)&1]
            alpha=max_bipartite_suborder(G,S)
            pred=len(S)-(int(bool(odd_cycle) and set(odd_cycle)<=set(S)))
            assert alpha==pred,(n,edges,k,S,alpha,pred)
            if k==2:
                assert direct_prism_alpha(G,S)==alpha,(n,edges,S,alpha)
            if alpha<k:F.append(frozenset(S))
        expected= (n>k and comb(n-1,k-1) or (n==k and 1 or 0))
        if odd_cycle and k<=n and k>=len(odd_cycle):expected-=comb(n-len(odd_cycle),k-len(odd_cycle))
        B=betti(F)
        if k<=n:
            assert B==({k-2:expected} if expected else {}),(n,k,edges,B,expected)
        else: assert B=={},(n,k,B)
        checked+=1
    return checked

def cycle(n):return [(j,(j+1)%n) for j in range(n)]

cases=[(3,cycle(3),[0,1,2]),(4,cycle(4),[]),(5,cycle(5),[0,1,2,3,4]),(6,cycle(6),[]),
       (7,cycle(7),list(range(7))),(6,cycle(3)+[(2,3),(3,4),(3,5)],[0,1,2]),
       (7,cycle(3)+[(2,3),(3,4),(4,5),(5,6)],[0,1,2]),
       (7,cycle(5)+[(1,5),(5,6)],list(range(5))),
       (7,[(i,i+1) for i in range(6)],[])]
count=0
for n,ed,odd in cases:
    count+=examine(n,ed,odd)
    print('PASS',n,'edges',len(ed),'odd_cycle',len(odd),'k_cases',n)
print('ALL_PRISM_FIXED_CHECKS_OK',len(cases),'graph_cases',count,'k_values')

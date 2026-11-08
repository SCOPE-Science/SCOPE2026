#!/usr/bin/env python3
"""Exact small-graph census for isolated-vertex/tree-component covariance in G(n,m)."""
from itertools import combinations
from fractions import Fraction
from math import comb

def ratio(a,b,t):
    return Fraction(comb(a,t),comb(b,t)) if 0 <= t <= a <= b else Fraction(0)

def predicted(n,k,m):
    M=comb(n,2); A=comb(n-1,2)
    Q=comb(n-k,2); B=comb(n-k-1,2)
    r=m-k+1
    if not (0 <= r <= Q):return None
    return (n-k)*ratio(B,Q,r)-n*ratio(A,M,m)

def counts(n,edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    isols=sum(not ns for ns in adj)
    seen=set(); trees=[0]*(n+1)
    for root in range(n):
        if root in seen:continue
        todo=[root];seen.add(root);verts=[]
        while todo:
            x=todo.pop();verts.append(x)
            for y in adj[x]:
                if y not in seen:seen.add(y);todo.append(y)
        k=len(verts)
        if k>=2 and sum(len(adj[v]) for v in verts)==2*(k-1):trees[k]+=1
    return isols,trees

tests=0
for n in range(3,7):
    edges=list(combinations(range(n),2));M=len(edges)
    for m in range(M+1):
        s_iso=0;s_tree=[0]*(n+1);s_mix=[0]*(n+1);total=0
        for subset in combinations(edges,m):
            I,T=counts(n,subset);s_iso+=I;total+=1
            for k in range(2,n):s_tree[k]+=T[k];s_mix[k]+=I*T[k]
        for k in range(2,n):
            if s_tree[k]:
                empirical=Fraction(s_mix[k],total)-Fraction(s_iso*s_tree[k],total*total)
                expected=Fraction(s_tree[k],total)*predicted(n,k,m)
                assert empirical==expected,(n,k,m,empirical,expected)
                tests+=1
    print('census',n,'graphs',2**M)
for n in range(4,35):
    for k in range(2,n):
        M=comb(n,2);Q=comb(n-k,2);A=comb(n-1,2);B=comb(n-k-1,2)
        prev=None;signs=[]
        for m in range(k-1,k+Q):
            delta=predicted(n,k,m)
            sg=(delta>0)-(delta<0)
            signs.append(sg)
            if m<k-1+B and m<A:
                r=m-k+1
                D=(Q-r)*(A-m)-(B-r)*(M-m)
                assert 2*D==(n-k-1)*(k*(n-3)+2)+2*k*(m-k+1), (n,k,m,D)
                tests+=1
        assert signs==sorted(signs,reverse=True),(n,k,signs)
        tests+=1
print('CHECK_OK',tests)

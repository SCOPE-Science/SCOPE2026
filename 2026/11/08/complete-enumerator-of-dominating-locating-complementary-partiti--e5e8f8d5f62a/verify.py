#!/usr/bin/env python3
"""Checks locating-dominating/dominating ordered complementary pairs on clique coronas."""
from collections import Counter
from itertools import combinations
from math import comb

def make_adj(n, r, edges):
    # vertex i*(r+1) is core hub, next r are private clique vertices.
    k=n*(r+1); a=[0]*k
    for i in range(n):
        z=[i*(r+1)+j for j in range(r+1)]
        for v,w in combinations(z,2):
            a[v]|=1<<w;a[w]|=1<<v
    for i,j in edges:
        u=i*(r+1);v=j*(r+1)
        a[u]|=1<<v;a[v]|=1<<u
    return a

def direct_counts(n,r,edges):
    adj=make_adj(n,r,edges); N=len(adj); full=(1<<N)-1; out=Counter()
    for S in range(1<<N):
        T=full^S
        # T dominates S. S locates and dominates T.
        if any(not (adj[v]&T) for v in range(N) if S>>v&1):continue
        sig=[]; good=True
        for v in range(N):
            if T>>v&1:
                ne=adj[v]&S
                if not ne or ne in sig:
                    good=False;break
                sig.append(ne)
        if good:out[S.bit_count()]+=1
    return out

def formula_counts(n,r,edges):
    adj=[0]*n
    for i,j in edges:adj[i]|=1<<j;adj[j]|=1<<i
    out=Counter()
    for A in range(1<<n):
        c=sum(1 for i in range(n) if not (A>>i&1) and adj[i]&A)
        a=A.bit_count()
        for j in range(c+1):out[r*n-j]+=comb(c,j)*r**(a+j)
    return out

def gamma(n,edges):
    adj=[0]*n
    for i,j in edges:adj[i]|=1<<j;adj[j]|=1<<i
    for s in range(n+1):
        for pts in combinations(range(n),s):
            A=sum(1<<i for i in pts)
            if all((A>>i&1) or adj[i]&A for i in range(n)):
                return s
    raise AssertionError

def check_one(n,r,edges):
    p=formula_counts(n,r,edges)
    d=direct_counts(n,r,edges)
    assert p==d,(n,r,edges,p,d)
    assert min(p)==(r-1)*n+gamma(n,edges),(n,r,edges,p)
    return sum(p.values())

def main():
    cnt=0
    for n in range(1,5):
      pairs=list(combinations(range(n),2))
      for r in ([2,3] if n<=3 else [2]):
        for mask in range(1<<len(pairs)):
          edges=[e for j,e in enumerate(pairs) if mask>>j&1]
          check_one(n,r,edges);cnt+=1
      print('ALL_LABELLED_HOSTS_OK',n,cnt)
    # Larger host profiles with independent formula checks and direct counts.
    for n,r,edges in [(4,3,[(0,1),(1,2),(2,3)]),(4,3,list(combinations(range(4),2))),(5,2,[(i,i+1) for i in range(4)]),(5,2,[(i,(i+1)%5) for i in range(5)])]:
      check_one(n,r,edges)
      print('ADDITIONAL_HOST_OK',n,r,len(edges))
    print('CHECKS_OK',cnt+4)

if __name__=='__main__': main()

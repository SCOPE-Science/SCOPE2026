#!/usr/bin/env python3
"""Exact finite search for edge-multiset resolving sets of open ladders.
The BFS distance model is independent of the coordinate formulas in the proof.
Run with Python 3.10+; no external packages.
"""
from collections import deque
from itertools import combinations


def graph(n):
    vs=list(range(2*n))
    edges=[(2*i,2*i+1) for i in range(n)]
    edges += [(2*i+j,2*i+2+j) for i in range(n-1) for j in (0,1)]
    adj=[[] for _ in vs]
    for x,y in edges: adj[x].append(y);adj[y].append(x)
    ds=[]
    for root in vs:
        d=[-1]*(2*n);d[root]=0;qu=deque([root])
        while qu:
            x=qu.popleft()
            for y in adj[x]:
                if d[y]<0:d[y]=d[x]+1;qu.append(y)
        assert all(x>=0 for x in d)
        ds.append(d)
    return edges,ds

def resolved(edges,ds,vertices):
    sigs={}
    for edge in edges:
        sig=tuple(sorted(min(ds[v][edge[0]],ds[v][edge[1]]) for v in vertices))
        if sig in sigs:return False
        sigs[sig]=edge
    return True

def counts(n,maxk):
    edges,ds=graph(n)
    ans=[]
    for k in range(2*n+1):
        if k>maxk:break
        count=sum(resolved(edges,ds,S) for S in combinations(range(2*n),k))
        ans.append(count)
    return ans

def main():
    expected={2:[0]*5,3:[0]*7,4:[0]*9,
              5:[0,0,0,0,4],6:[0,0,0,0,20],7:[0,0,0,4],8:[0,0,0,0,80]}
    for n,ref in expected.items():
        result=counts(n,len(ref)-1)
        assert result==ref,(n,result,ref)
        print('n=',n,'counts=',result,sep='')
    for n in range(7,151):
        if n==8:continue
        edges,ds=graph(n)
        j=2 if n%2 else 3
        assert resolved(edges,ds,(0,2*j,2*(n-1))),n
    print('BFS_EXACT_AND_FAMILY_WITNESS_OK')
if __name__=='__main__':main()

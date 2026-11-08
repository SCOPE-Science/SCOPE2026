"""Exact independent checks for cherry count and distance-profile covariance in uniform labelled trees."""
from fractions import Fraction as F
from itertools import product
from collections import deque
from math import comb

def P(n,k):
    if not 1<=k<n: return F(0)
    prod=1
    for j in range(k-1):prod*=n-2-j
    return F((k+1)*prod,n**k)

def expected_sizebiased(n,k):
    if k==1: return F(n-1)
    return F((n-2)*(n-3),2)*P(n-2,k)+2*(n-3)*P(n-2,k-1)+int(k==2)

def exact_delta(n,k):
    return expected_sizebiased(n,k)-F(n*(n-1),2)*P(n,k)

def prufer_edges(code,n):
    deg=[1]*n
    for u in code: deg[u]+=1
    edges=[]
    for u in code:
        v=next(i for i in range(n) if deg[i]==1)
        edges.append((v,u));deg[v]-=1;deg[u]-=1
    a,b=[i for i in range(n) if deg[i]==1]
    edges.append((a,b))
    return edges

def moments(n):
    totalsC=0
    totalsM=[0]*n
    totalsCM=[0]*n
    count=0
    for code in product(range(n),repeat=n-2):
        edges=prufer_edges(code,n)
        adj=[[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b);adj[b].append(a)
        # independent direct interpretation of all sibling leaf pairs
        cherries=sum(comb(sum(len(adj[x])==1 for x in adj[v]),2) for v in range(n))
        shell=[0]*n
        for root in range(n):
            ds=[-1]*n;ds[root]=0;queue=deque([root])
            while queue:
                x=queue.popleft()
                for y in adj[x]:
                    if ds[y]<0: ds[y]=ds[x]+1;queue.append(y)
            for j in range(root+1,n):shell[ds[j]]+=1
        totalsC+=cherries
        for k in range(1,n):totalsM[k]+=shell[k];totalsCM[k]+=cherries*shell[k]
        count+=1
    assert count==n**(n-2)
    E_C=F(totalsC,count)
    for k in range(1,n):
        got=F(totalsCM[k],count)-E_C*F(totalsM[k],count)
        expected=E_C*exact_delta(n,k)
        assert got==expected,(n,k,got,expected)
    assert all(exact_delta(n,k)>0 for k in [2])
    assert all(exact_delta(n,k)<0 for k in range(3,n)) if n<=7 else True
    return count

def tests():
    total=0
    for n in range(4,8):total+=moments(n)
    # test positivity to negativity exactly at all finite sizes; not an infinite proof
    for n in range(4,201):
        signs=[(exact_delta(n,k)>0)-(exact_delta(n,k)<0) for k in range(2,n)]
        assert signs[0]==1 and signs[-1]==-1
        assert all(signs[i]>=signs[i+1] for i in range(len(signs)-1))
        assert sum(exact_delta(n,k) for k in range(1,n))==0
        assert sum(k*exact_delta(n,k) for k in range(1,n))<0
    print('PASS: exact exhaustive Prüfer code trees 4..7, total',total, '; 197 exact shell-sign identities and distance total checks')
if __name__=='__main__':tests()

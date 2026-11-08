"""Independent integer dynamic program and Pell addition checks.
No external packages required; all-tree test sizes are finite.
"""
import heapq
from itertools import product
from random import Random

def from_prufer(n,word):
    deg=[1]*n
    for v in word:deg[v]+=1
    q=[v for v in range(n) if deg[v]==1];heapq.heapify(q)
    adj=[[] for _ in range(n)]
    for x in word:
        y=heapq.heappop(q);adj[x].append(y);adj[y].append(x)
        deg[x]-=1;deg[y]-=1
        if deg[x]==1:heapq.heappush(q,x)
    u=heapq.heappop(q);v=heapq.heappop(q)
    adj[u].append(v);adj[v].append(u)
    return adj

def canonical(adj):
    n=len(adj);d=list(map(len,adj));q=[i for i,v in enumerate(d) if v<=1];remaining=n
    while remaining>2:
        remaining-=len(q);nq=[]
        for u in q:
            for v in adj[u]:
                d[v]-=1
                if d[v]==1:nq.append(v)
        q=nq
    def encode(x,p):return '('+''.join(sorted(encode(y,x) for y in adj[x] if y!=p))+')'
    return min(encode(x,-1) for x in q)

def rootpair(adj,u,p=-1):
    a,S=0,1
    for v in adj[u]:
        if v==p:continue
        x,y=rootpair(adj,v,u)
        a=a*(x+y)+S*y
        S*=x+y
    return a,a+S

def pell(k):
    x,y=0,1
    for _ in range(k):x,y=y,x+2*y
    return x

if __name__=='__main__':
    processed=0
    for n in range(2,9):
        seen=set();vals=[]
        for word in product(range(n),repeat=n-2):
            adj=from_prufer(n,word);key=canonical(adj)
            if key in seen:continue
            seen.add(key)
            count=2*rootpair(adj,0)[0]
            assert 2*(n-1)<=count<=2*pell(n-1)
            if n>=4:
                assert (count==2*(n-1))==(max(map(len,adj))==n-1)
                assert (count==2*pell(n-1))==(sorted(map(len,adj))==[1,1]+[2]*(n-2))
            vals.append(count);processed+=1
        print('ALL_TREE_DP',n,len(vals),min(vals),max(vals))
    rng=Random(19203)
    for n in range(9,31):
        for _ in range(100):
            adj=from_prufer(n,[rng.randrange(n) for i in range(n-2)])
            cnt=2*rootpair(adj,0)[0]
            assert 2*(n-1)<=cnt<=2*pell(n-1)
            processed+=1
    for m in range(1,100):
        for n in range(1,100):
            pm,pn=pell(m),pell(n)
            sm=pm+pell(m-1);sn=pn+pell(n-1)
            assert pm*sn+pn*sm==pell(m+n)
            assert pell(m+n-1)+pell(m+n)==sm*sn+2*pm*pn
    print('TREE_DP_OK',processed)

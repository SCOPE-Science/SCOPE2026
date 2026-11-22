from collections import deque
from itertools import product

def words(n,k):
    if n==0: return [()]
    return [(v,)+s for v in range(k) for s in words(n-1,k)] + [(k,k)+s for s in words(n-2,k)] if n>=2 else [(v,) for v in range(k)]

def features(x,k):
    n=len(x);h=list(x);ds=[0]*(n-1);i=0
    while i<n:
        if x[i]==k:
            assert i<n-1 and x[i+1]==k
            ds[i]=1;h[i]=h[i+1]=k-1;i+=2
        else:i+=1
    return h,ds

def embedding(x,k):
    n=len(x);p=k-1; assert p%2==1
    h,ds=features(x,k)
    cs=list(range(1,(p+1)//2+1));ns=list(range((p+1)//2+1,p+1))
    out=[]
    for i in range(n):
        for j in range(p):
            if j%2==0:out.append(int(h[i]<cs[j//2]))
            else:out.append(int(h[i]>=ns[j//2]))
        if i+1<n:out.append(ds[i])
    assert len(out)==k*n-1
    assert all(not(out[i] and out[i+1]) for i in range(len(out)-1)), (x,out)
    return tuple(out)

def adj(x,k,ws):
    n=len(x); res=set()
    for i,a in enumerate(x):
        if a<k:
            for b in (a-1,a+1):
                if 0<=b<k:
                    y=x[:i]+(b,)+x[i+1:]
                    if y in ws:res.add(y)
    for i in range(n-1):
        if x[i:i+2]==(k-1,k-1): res.add(x[:i]+(k,k)+x[i+2:])
        if x[i:i+2]==(k,k):
            y=x[:i]+(k-1,k-1)+x[i+2:]
            if y in ws:res.add(y)
    return res

def verify(n,k):
    xs=words(n,k);s=set(xs); assert len(s)==len(xs)
    enc={x:embedding(x,k) for x in xs};assert len(set(enc.values()))==len(xs)
    edge= {x:adj(x,k,s) for x in xs}
    for x in xs:
        for y in edge[x]:
            assert x in edge[y]
            assert sum(a!=b for a,b in zip(enc[x],enc[y]))==1
    for x in xs:
        dist={x:0};q=deque([x]);
        while q:
            u=q.popleft()
            for v in edge[u]:
                if v not in dist:dist[v]=dist[u]+1;q.append(v)
        assert len(dist)==len(xs)
        for y in xs:
            d=sum(a!=b for a,b in zip(enc[x],enc[y])); assert d==dist[y], (n,k,x,y,d,dist[y])
    # witness each axis
    ds = [set() for _ in range(k*n-1)]
    for x in xs:
        for y in edge[x]:
            e=[i for i,(a,b) in enumerate(zip(enc[x],enc[y])) if a!=b]; assert len(e)==1
            ds[e[0]].add(tuple(sorted((x,y))))
    assert all(ds)
    return n,k,len(xs),sum(map(len,edge.values()))//2,k*n-1

if __name__=='__main__':
    for k,nmax in [(2,6),(4,4),(6,3),(8,2)]:
        for n in range(1,nmax+1):print('PASS',*verify(n,k),flush=True)

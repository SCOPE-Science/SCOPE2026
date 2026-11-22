"""Direct bit-mask enumeration of power domination and optimal slides."""
from itertools import combinations
from collections import Counter, deque

def build(n):
    adj=[0]*(n+n*(n-1)//2); labels=[]
    for a in range(n):
        for b in range(a+1,n):
            e=n+len(labels); labels.append((a,b))
            adj[e]|=1<<a|1<<b
            adj[a]|=1<<e;adj[b]|=1<<e
    return adj,labels

def power(adj,s):
    obs=s; full=(1<<len(adj))-1
    for i in range(len(adj)):
        if s>>i&1:obs|=adj[i]
    while True:
        after=obs
        for i,nei in enumerate(adj):
            if obs>>i&1:
                v=nei&~obs
                if v and v&(v-1)==0:after|=v
        if after==obs:return obs==full
        obs=after

def expected(n,labels):
    out=set(); full=(1<<n)-1
    for a,b in combinations(range(n),2):out.add(full^(1<<a|1<<b))
    for a,b,c in combinations(range(n),3):
        original=full^(1<<a|1<<b|1<<c)
        for e in ((a,b),(a,c),(b,c)):
            out.add(original|(1<<(n+labels.index(e))))
    return out

def run(n):
    adj,labels=build(n)
    valid=set()
    for k in range(n-1):
        for tup in combinations(range(len(adj)),k):
            mask=sum(1<<i for i in tup)
            if power(adj,mask):valid.add(mask)
        if valid:break
    predicted=expected(n,labels)
    assert k==n-2,(n,k)
    assert valid==predicted,(n,len(valid),len(predicted),len(valid^predicted))
    edges=set(); neigh={v:set() for v in valid}
    for x in valid:
        for a in range(len(adj)):
            if x>>a&1:
                for b in range(len(adj)):
                    if adj[a]>>b&1 and not (x>>b&1):
                        y=(x^(1<<a))|(1<<b)
                        if y in valid:
                            neigh[x].add(y);edges.add(tuple(sorted((x,y))))
    assert len(edges)==2*(n-2)*((n*(n-1))//2)
    assert Counter(map(len,neigh.values()))==Counter({2:((n*(n-1))//2)*(n-2),2*(n-2):(n*(n-1))//2}) if n>3 else set(map(len,neigh.values()))=={2}
    eccentricities=[]
    for s in valid:
        dist={s:0}; q=deque([s])
        while q:
            u=q.popleft()
            for v in neigh[u]:
                if v not in dist:dist[v]=dist[u]+1;q.append(v)
        assert len(dist)==len(valid)
        eccentricities.append(max(dist.values()))
    assert max(eccentricities)==min(n,6)
    print(f'n={n} gamma={k} sets={len(valid)} slides={len(edges)} diameter={max(eccentricities)} ecc={dict(Counter(eccentricities))}')

if __name__=='__main__':
    for n in range(3,8):run(n)

from collections import deque, Counter
from itertools import combinations

def partitions(n, maxpart=None):
    if maxpart is None or maxpart>n: maxpart=n
    if n==0:
        yield ()
        return
    for first in range(maxpart,0,-1):
        for rest in partitions(n-first, first):
            yield (first,)+rest

def build(parts):
    labels=[]
    for i,a in enumerate(parts): labels += [i]*a
    n=len(labels); adj=[set() for _ in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if labels[u]!=labels[v]: adj[u].add(v); adj[v].add(u)
    return adj, labels

def dist(adj, s, blocked=frozenset()):
    if s in blocked: return [10**9]*len(adj)
    d=[10**9]*len(adj); d[s]=0; q=deque([s])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v in blocked or d[v]<10**9: continue
            d[v]=d[u]+1; q.append(v)
    return d

def total_visible(adj, X):
    n=len(adj); X=set(X)
    base=[dist(adj,u) for u in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            blocked=X-{u,v}
            if dist(adj,u,blocked)[v] != base[u][v]:
                return False
    return True

def formula_coeffs(parts):
    n=sum(parts); q=sum(a>=2 for a in parts)
    # coefficients indexed by |X| from direct complement inclusion-exclusion formula
    # (1+x)^n - sum_i x^(n-a_i)(1+x)^a_i + (q-1)x^n for q>=1
    from math import comb
    c=[comb(n,k) for k in range(n+1)]
    if q:
        for a in parts:
            if a>=2:
                shift=n-a
                for j in range(a+1): c[shift+j]-=comb(a,j)
        c[n]+=q-1
    return c

def expected_maximal(parts):
    n=sum(parts); non=[(i,a) for i,a in enumerate(parts) if a>=2]; s=sum(a==1 for a in parts)
    q=len(non)
    if q==0: return n,1
    if q==1: return n-1,s
    count=s+sum(a*b for (_,a),(_,b) in combinations(non,2))
    return n-2,count

def check(parts):
    adj,labels=build(parts); n=len(labels)
    tv=[]; coeff=[0]*(n+1)
    for mask in range(1<<n):
        X=[i for i in range(n) if mask>>i&1]
        ok=total_visible(adj,X)
        if ok:
            tv.append(mask); coeff[len(X)]+=1
    assert coeff==formula_coeffs(parts),(parts,coeff,formula_coeffs(parts))
    maximal=[]
    S=set(tv)
    for mask in tv:
        if all((mask|(1<<v)) not in S for v in range(n) if not (mask>>v&1)):
            maximal.append(mask)
    low,count=expected_maximal(parts)
    assert min(m.bit_count() for m in maximal)==low,(parts,[m.bit_count() for m in maximal],low)
    assert len(maximal)==count,(parts,len(maximal),count)

checked=0
for n in range(2,10):
    for parts in partitions(n):
        if len(parts)<2: continue
        check(parts); checked+=1
print('VERIFY_OK')
print(f'checked {checked} complete multipartite isomorphism types of orders 2..9')
print('verified the full total-visibility polynomial, maximal-set count, and lower total mutual-visibility formula')
print('the all-orders theorem rests on the accompanying structural proof')

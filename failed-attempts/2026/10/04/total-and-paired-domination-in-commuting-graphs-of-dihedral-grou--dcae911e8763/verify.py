#!/usr/bin/env python3
from itertools import combinations

def mul(x,y,n):
    a,b=x; c,d=y
    return ((a + (-1 if b else 1)*c) % n, (b+d) % 2)

def commute(x,y,n):
    return mul(x,y,n)==mul(y,x,n)

def graph(n):
    G=[(a,b) for a in range(n) for b in (0,1)]
    Z=[x for x in G if all(commute(x,y,n) for y in G)]
    V=[x for x in G if x not in Z]
    adj=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if commute(x,V[j],n):
                adj[i].add(j); adj[j].add(i)
    return G,Z,V,adj

def components(adj):
    seen=set(); comps=[]
    for v in range(len(adj)):
        if v in seen: continue
        stack=[v]; seen.add(v); C=[]
        while stack:
            u=stack.pop(); C.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        comps.append(C)
    return comps

def total_dom(S,adj):
    S=set(S)
    return all(adj[v] & S for v in range(len(adj)))

def pm(S,adj):
    S=set(S)
    if not S: return True
    if len(S)%2: return False
    v=next(iter(S))
    for u in list(adj[v] & S):
        if pm(S-{v,u},adj):
            return True
    return False

def minima(adj):
    if any(len(N)==0 for N in adj):
        return None,None
    N=len(adj)
    gt=gp=None
    for k in range(2,N+1):
        if gt is None:
            for S in combinations(range(N),k):
                if total_dom(S,adj):
                    gt=k; break
        if gp is None and k%2==0:
            for S in combinations(range(N),k):
                if total_dom(S,adj) and pm(S,adj):
                    gp=k; break
        if gt is not None and gp is not None:
            return gt,gp
    return gt,gp

rows=[]
for n in range(3,11):
    G,Z,V,adj=graph(n)
    comps=components(adj)
    gt,gp=minima(adj)
    if n%2:
        assert len(Z)==1
        assert sorted(len(c) for c in comps)==[1]*n+[n-1]
        assert gt is None and gp is None
    else:
        assert len(Z)==2
        assert sorted(len(c) for c in comps)==[2]*(n//2)+[n-2]
        assert gt==n+2 and gp==n+2
    rows.append((n,len(V),len(Z),sorted(len(c) for c in comps),gt,gp))

print('VERIFY_OK')
for row in rows:
    print('n=%d vertices=%d center=%d components=%s gamma_t=%s gamma_pr=%s' % row)

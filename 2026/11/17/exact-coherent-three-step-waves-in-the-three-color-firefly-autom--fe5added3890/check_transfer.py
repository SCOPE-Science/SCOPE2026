#!/usr/bin/env python3
"""Exact transfer certificate for the three-color inhibitory oscillator on a cycle."""
from itertools import product
from collections import defaultdict

def local(a,b,c):
    return b if b == 2 and (a == 1 or c == 1) else (b+1)%3

def third(w):
    one = [local(w[j-1],w[j],w[j+1]) for j in range(1,6)]
    two = [local(one[j-1],one[j],one[j+1]) for j in range(1,4)]
    return local(*two)

# Ordered words give canonical vertices and exact directed adjacency.
V=list(product(range(3),repeat=6)); idx={v:i for i,v in enumerate(V)}
adj=[[] for _ in V]
for w in product(range(3),repeat=7):
    if third(w) == w[4]:
        adj[idx[w[:6]]].append(idx[w[1:]])
assert all(len(set(v)) == len(v) for v in adj)
# Standard Tarjan SCC algorithm, excluding singleton components without a loop.
clock=0; st=[]; stackset=set(); indices={}; low={}; components=[]
def visit(v):
    global clock
    indices[v]=low[v]=clock;clock+=1;st.append(v);stackset.add(v)
    for w in adj[v]:
        if w not in indices:
            visit(w);low[v]=min(low[v],low[w])
        elif w in stackset:low[v]=min(low[v],indices[w])
    if low[v]==indices[v]:
        c=[]
        while True:
            w=st.pop();stackset.remove(w);c.append(w)
            if w==v:break
        components.append(c)
for v in range(len(V)):
    if v not in indices:visit(v)
active=[c for c in components if len(c)>1 or (len(c)==1 and c[0] in adj[c[0]])]
assert len(active)==1,[(len(c),c[:3]) for c in active]
vertices=sorted(active[0]); I={x:i for i,x in enumerate(vertices)}
E=[(I[v],I[w]) for v in vertices for w in adj[v] if w in I];N=len(vertices)
assert N==65 and len(E)==118,(N,len(E))
assert any(i==j for i,j in E), "The cyclic component must be aperiodic"
# Trace A^k via 65 independent exact walk-count recurrences.
tr=[0]* (N+1)
for source in range(N):
    counts=[0]*N;counts[source]=1
    for k in range(1,N+1):
        other=[0]*N
        for i,j in E:other[j]+=counts[i]
        counts=other;tr[k]+=counts[source]
# Newton identities: char polynomial = lambda^N + c1 lambda^(N-1)+ ...
c=[1]
for k in range(1,N+1):
    a=sum(c[j]*tr[k-j] for j in range(k))
    assert a%k==0,(k,a)
    c.append(-a//k)
assert c == [1,-3,3,-1,-1]+[0]*(N-4),[(i,z) for i,z in enumerate(c) if z]
# Exact traces from characteristic polynomial, covering every finite ring.
a=[0,3,3,3,7]
for n in range(5,31):a.append(3*a[n-1]-3*a[n-2]+a[n-3]+a[n-4])
for n in range(1,31):
    # Verify the trace-power identity using recurrence after the initial 4.
    if n<=N: assert tr[n]==a[n],(n,tr[n],a[n])
print('allowed 7-windows:', sum(map(len,adj)))
print('unique cyclic SCC: vertices=65 arcs=118')
print('charpoly: lambda^61 (lambda^4 - 3 lambda^3 + 3 lambda^2 - lambda - 1)')
print('power sums n=1..12:', a[1:13])
print('exact characteristic certificate: PASS (65 Newton identities)')

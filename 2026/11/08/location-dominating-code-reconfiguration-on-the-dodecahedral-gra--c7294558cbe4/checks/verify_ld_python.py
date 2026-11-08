"""Complete standard-library enumeration of optimum locating-dominating sets of GP(10,2).

Run: python3 checks/verify_ld_python.py
"""
from itertools import combinations
from collections import Counter,deque

N=20
edges=set()
for i in range(10):
    for a,b in ((i,(i+1)%10),(i,i+10),(i+10,(i+2)%10+10)):
        edges.add(tuple(sorted((a,b))))
assert len(edges)==30
adj=[0]*N
for a,b in edges:adj[a]|=1<<b; adj[b]|=1<<a
ball=[adj[u]|(1<<u) for u in range(N)]

def locating_dominating(s):
    signals=[s&ball[v] for v in range(N) if not(s>>v&1)]
    return all(signals) and len(set(signals))==N-s.bit_count()

assert all(adj[i].bit_count()==3 for i in range(N))
minimum=[]
for k in range(1,8):
    good=[]
    for subset in combinations(range(N),k):
        mask=sum(1<<u for u in subset)
        if locating_dominating(mask):good.append(mask)
    if k<7:assert not good, (k,len(good))
    else:minimum=good
assert len(minimum)==220,len(minimum)
state_index={x:i for i,x in enumerate(minimum)}
assert len(state_index)==220
J=[set() for _ in minimum]
S=[set() for _ in minimum]
for i,s in enumerate(minimum):
    occupied=[u for u in range(N) if s>>u&1]
    free=[v for v in range(N) if not(s>>v&1)]
    for u in occupied:
        for v in free:
            t=s^(1<<u)^(1<<v)
            j=state_index.get(t)
            if j is None:continue
            J[i].add(j)
            if adj[u]>>v&1:S[i].add(j)
assert J==S
assert sum(map(len,J))==1140
assert Counter(map(len,J))=={4:120,6:40,7:60}
assert all(i in J[j] for j,L in enumerate(J) for i in L)

def dist(start):
    d=[-1]*len(J);d[start]=0
    q=deque([start])
    while q:
        v=q.popleft()
        for w in J[v]:
            if d[w]<0:d[w]=d[v]+1;q.append(w)
    return d
E=[]
for i in range(len(J)):
    ds=dist(i)
    assert all(x>=0 for x in ds)
    E.append(max(ds))
assert min(E)==8 and max(E)==9
print('PYTHON_LD_PASS gamma_LD=7 optimal_states=220 legal_edges=570')
print('PYTHON_LD_PASS TJ_equals_TS=yes degree_profile=4:120,6:40,7:60 connected=yes radius=8 diameter=9')

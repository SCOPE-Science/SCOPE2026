"""Exhaustive direct state-graph check for inclusive-neighborhood minority dynamics.
No external dependencies. Each discrete step chooses one vertex uniformly and updates its value.
"""
from collections import deque

def update(state, v, m):
    n=2*m+1
    bits=[(state>>j)&1 for j in range(n)]
    neighbors=list(range(1,n)) if v==0 else [0, 1+2*((v-1)//2)+(1-(v-1)%2)]
    same=sum(bits[w]==bits[v] for w in neighbors)
    if 2*same>=len(neighbors):
        return state^(1<<v)
    return state

def energy(state,m):
    b=[(state>>j)&1 for j in range(2*m+1)]
    return sum(int(b[0]==b[2*i+1])+int(b[0]==b[2*i+2])+int(b[2*i+1]==b[2*i+2]) for i in range(m))

def tarjan(adj):
    sz=len(adj); ids=[-1]*sz; low=[0]*sz; stack=[]; on=[False]*sz; comps=[]; tick=0
    def dfs(v):
        nonlocal tick
        ids[v]=low[v]=tick;tick+=1;stack.append(v);on[v]=True
        for w in adj[v]:
            if ids[w]<0: dfs(w);low[v]=min(low[v],low[w])
            elif on[w]: low[v]=min(low[v],ids[w])
        if low[v]==ids[v]:
            comp=[]
            while True:
                w=stack.pop();on[w]=False;comp.append(w)
                if w==v: break
            comps.append(comp)
    for v in range(sz):
        if ids[v]<0:dfs(v)
    return comps

for m in range(1,5):
    n=2*m+1; sz=1<<n
    adj=[set(update(s,v,m) for v in range(n)) for s in range(sz)]
    comp=tarjan(adj)
    closed=[]
    for c in comp:
        S=set(c)
        if all(adj[s]<=S for s in c): closed.append(S)
    ground={s for s in range(sz) if energy(s,m)==m}
    assert len(ground)==2*3**m
    assert len(closed)==1 and closed[0]==ground,(m,len(closed),[len(c) for c in closed])
    assert all(any(update(s,v,m)!=s for v in range(n)) for s in ground)
    # independently count hub-flippable ground states
    hubflip=sum(update(s,0,m)!=s for s in ground)
    assert hubflip==2**(m+1)
    for s in ground:
        for v in range(n):
            t=update(s,v,m)
            assert energy(t,m)==m
            if t!=s: assert update(t,v,m)==s
    print(f'm={m} states={sz} closed_components={len(closed)} recurrent={len(ground)} hub_flippable={hubflip} hub_flip_stationary={hubflip}/{n*len(ground)}')
print('SCC CHECK PASS')

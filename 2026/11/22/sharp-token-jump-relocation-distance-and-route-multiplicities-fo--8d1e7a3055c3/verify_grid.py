"""Independent finite check using actual augmented grid graph and separator subsets.
Run: python verify_grid.py
"""
from itertools import combinations
from collections import deque


def evaluate(n):
    # Three horizontal rows, n columns. s and t attach to all first/last-column sites.
    sites = 3*n
    s, t = sites, sites+1
    adj = [set() for _ in range(sites+2)]
    def vertex(i,j): return i*n+j
    for i in range(3):
        for j in range(n):
            u=vertex(i,j)
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                a,b=i+di,j+dj
                if 0<=a<3 and 0<=b<n: adj[u].add(vertex(a,b))
            if j==0: adj[u].add(s);adj[s].add(u)
            if j==n-1: adj[u].add(t);adj[t].add(u)
    def is_cut(mask):
        seen={s};todo=[s]
        for u in todo:
            for v in adj[u]:
                if v<sites and (mask>>v)&1: continue
                if v not in seen:seen.add(v);todo.append(v)
        return t not in seen
    states=[]
    for triple in combinations(range(sites),3):
        mask=sum(1<<i for i in triple)
        if is_cut(mask): states.append(mask)
    by={v:i for i,v in enumerate(states)}
    expected={sum(1<<vertex(i,x[i]) for i in range(3)) for x in __import__('itertools').product(range(n),repeat=3)
              if abs(x[0]-x[1])<=1 and abs(x[1]-x[2])<=1}
    assert set(states)==expected,(n,len(states),len(expected))
    graph=[[] for _ in states]
    for i,a in enumerate(states):
        for j,b in enumerate(states):
            if i==j: continue
            if (a^b).bit_count()==2:graph[i].append(j)  # TJ, not TS
    left=sum(1<<vertex(i,0) for i in range(3));right=sum(1<<vertex(i,n-1) for i in range(3))
    dist={by[left]:0};count={by[left]:1};todo=deque([by[left]])
    while todo:
        u=todo.popleft()
        for v in graph[u]:
            if v not in dist:dist[v]=dist[u]+1;count[v]=0;todo.append(v)
            if dist[v]==dist[u]+1:count[v]+=count[u]
    L=n-1
    predicted_dist=0 if L==0 else (3*L+1)//2+1
    predicted_count=1 if L==0 else 6 if L==1 else 2**(L//2) if L%2==0 else 2**((L+3)//2)
    assert len(dist)==len(states)
    assert dist[by[right]]==predicted_dist
    assert count[by[right]]==predicted_count
    return n,len(states),sum(map(len,graph))//2,dist[by[right]],count[by[right]]

if __name__=='__main__':
    for n in range(1,8):print(*evaluate(n))
    print('PASS: independent full augmented-grid separator search n=1..7')

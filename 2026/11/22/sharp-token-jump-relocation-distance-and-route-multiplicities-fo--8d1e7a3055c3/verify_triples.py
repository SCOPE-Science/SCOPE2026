"""Independent abstract-coordinate graph BFS and shortest-route counts.
Run: python verify_triples.py
"""
from itertools import product
from collections import deque

def compute(L):
    vertices=[z for z in product(range(L+1),repeat=3) if abs(z[0]-z[1])<=1 and abs(z[1]-z[2])<=1]
    lookup={z:i for i,z in enumerate(vertices)}
    neighbors=[]
    for x in vertices:
        neigh=[]
        for j in range(3):
            for v in range(L+1):
                if v==x[j]:continue
                y=list(x);y[j]=v;y=tuple(y)
                if y in lookup:neigh.append(lookup[y])
        neighbors.append(neigh)
    assert len(vertices)==1 if L==0 else len(vertices)==9*L-1
    if L>=1:assert sum(map(len,neighbors))//2==23*L-11
    src=lookup[(0,0,0)];dst=lookup[(L,L,L)]
    dist=[-1]*len(vertices);ways=[0]*len(vertices)
    dist[src]=0;ways[src]=1;todo=deque([src])
    while todo:
        i=todo.popleft()
        for j in neighbors[i]:
            if dist[j]==-1:dist[j]=dist[i]+1;todo.append(j)
            if dist[j]==dist[i]+1:ways[j]+=ways[i]
    assert all(d>=0 for d in dist)
    expect=0 if L==0 else (3*L+1)//2+1
    routes=1 if L==0 else 6 if L==1 else 2**(L//2) if L%2==0 else 2**((L+3)//2)
    assert (dist[dst],ways[dst])==(expect,routes)
    return L,len(vertices),dist[dst],ways[dst]

if __name__=='__main__':
    for L in range(31):
        print(*compute(L))
    print('PASS: abstract-coordinate BFS and counts L=0..30')

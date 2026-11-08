"""Independent exhaustive bitmask test of clique-corona zero forcing minima and their reconfiguration graphs."""
from itertools import combinations
from collections import deque
from math import comb

def build(n, edges, r=0):
    N=n*(r+1)
    adj=[0]*N
    def edge(a,b):
        adj[a]|=1<<b;adj[b]|=1<<a
    for u,v in edges:edge(u,v)
    if r:
        for v in range(n):
            verts=[v]+[n+r*v+j for j in range(r)]
            for a,b in combinations(verts,2):edge(a,b)
    return adj

def forces(adj, state):
    n=len(adj); target=(1<<n)-1
    while 1:
        nxt=state
        for u in range(n):
            if state>>u&1:
                whites=adj[u] & ~state
                if whites and whites&(whites-1)==0:nxt|=whites
        if nxt==state:return state==target
        state=nxt

def minima(adj):
    N=len(adj)
    for k in range(N+1):
        found=[]
        for cs in combinations(range(N),k):
            s=sum(1<<c for c in cs)
            if forces(adj,s):found.append(s)
        if found:return k,set(found)

def exchange(states):
    st=list(sorted(states));edges=set()
    for i,x in enumerate(st):
        for j in range(i):
            if (x^st[j]).bit_count()==2:edges.add((st[j],x))
    visited=set(); sizes=[]
    near={x:set() for x in st}
    for a,b in edges:near[a].add(b);near[b].add(a)
    for a in st:
        if a not in visited:
            todo=[a];visited.add(a);cnt=0
            while todo:
                u=todo.pop();cnt+=1
                for v in near[u]-visited:visited.add(v);todo.append(v)
            sizes.append(cnt)
    return len(edges),sorted(sizes)

def run(n,edges,r):
    z,bases=minima(build(n,edges))
    k,solutions=minima(build(n,edges,r))
    E,components=exchange(solutions)
    e0,com0=exchange(bases)
    q=r**(n-z)*(r+1)**z
    e_formula=len(bases)*q*(z*r+(n-z)*(r-1))//2 + e0*(4*r**(n-z+1)*(r+1)**(z-1))
    assert k==n*(r-1)+z,(k,n,z,r)
    assert len(solutions)==len(bases)*q,(len(solutions),len(bases),q)
    assert E==e_formula,(E,e_formula)
    assert components==sorted(t*q for t in com0),(components,com0,q)
    print(f'{n=} {r=} {edges=} base_Z={z} base_min={len(bases)} base_edges={e0} corona_Z={k} corona_min={len(solutions)} corona_edges={E} components={components} PASS')

if __name__=='__main__':
    run(2,[(0,1)],2)
    run(2,[(0,1)],3)
    run(3,[(0,1),(1,2)],2)
    run(3,[(0,1),(1,2),(0,2)],2)
    run(4,[(0,1),(1,2),(2,3)],2)
    run(4,[(0,1),(0,2),(0,3)],2)
    run(4,[(0,1),(1,2),(2,3),(3,0)],2)
    print('verify_a all checks passed')

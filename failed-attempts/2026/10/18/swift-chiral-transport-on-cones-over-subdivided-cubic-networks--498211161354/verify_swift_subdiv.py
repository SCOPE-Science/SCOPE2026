#!/usr/bin/env python3
"""Finite exact checks and independent Taylor evolution for chiral subdivision cones.

No finite check proves the all-graph classification; the proof uses local
three-phase rigidity and graph bipartiteness.
"""
import cmath
import collections
import itertools
import math


def examples():
    return {
        'K4': (4, list(itertools.combinations(range(4), 2)), False),
        'K3,3': (6, [(u, v + 3) for u in range(3) for v in range(3)], True),
        'cube Q3': (8, [(u, u ^ (1 << b)) for u in range(8)
                        for b in range(3) if u < (u ^ (1 << b))], True),
        'triangular prism': (6, [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),
                                  (0,3),(1,4),(2,5)], False),
        'Petersen': (10, [(i, (i+1)%5) for i in range(5)]
                      + [(i, i+5) for i in range(5)]
                      + [(i+5, 5+(i+2)%5) for i in range(5)], False),
    }


def bipartition(n, edges):
    neighbors = [[] for _ in range(n)]
    for a,b in edges:
        neighbors[a].append(b); neighbors[b].append(a)
    color = [None]*n
    for source in range(n):
        if color[source] is not None: continue
        color[source] = 0
        q = collections.deque([source])
        while q:
            u = q.popleft()
            for v in neighbors[u]:
                if color[v] is None:
                    color[v] = 1-color[u]; q.append(v)
                elif color[v] == color[u]: return None
    return color


def edge_colorings(n, edges):
    incident = [[] for _ in range(n)]
    for j,(u,v) in enumerate(edges):
        incident[u].append(j); incident[v].append(j)
    assert all(len(row)==3 for row in incident)
    a = [-1]*len(edges)
    solutions = []
    def dfs(j):
        if j == len(edges):
            solutions.append(tuple(a)); return
        u,v = edges[j]
        for c in range(3):
            if (all(a[t]!=c for t in incident[u] if t!=j)
                and all(a[t]!=c for t in incident[v] if t!=j)):
                a[j]=c; dfs(j+1)
        a[j]=-1
    dfs(0)
    return solutions

# Exact algebraic integer arithmetic: a + b*omega with omega^2+omega+1=0.
PHASES = [(1,0),(0,1),(-1,-1)]
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0], -x[1])
def conjugate(x): return (x[0]-x[1], -x[1])
def check_phase_rows(n,edges,part,cols):
    sums = [(0,0) for _ in range(n+len(edges))]
    rows = []
    for j,(u,v) in enumerate(edges):
        a = PHASES[cols[j]]
        zu = a if part[u]==0 else neg(a)
        zv = a if part[v]==0 else neg(a)
        sums[u]=add(sums[u],zu)
        sums[v]=add(sums[v],zv)
        sums[n+j]=add(sums[n+j],add(conjugate(zu),conjugate(zv)))
        rows.append((u,v,zu,zv))
    assert all(a==(0,0) for a in sums), (sums,rows)
    return rows


def evolve_cone(n, edges, rows):
    N=n+len(edges)
    adj=[[] for _ in range(N+1)]
    # Apex is 0, original vertices are 1..n, midpoints are n+1..n+m.
    for v in range(1,N+1):
        adj[0].append((v,1.0+0j));adj[v].append((0,1.0+0j))
    def complexval(ab): return ab[0]+ab[1]*cmath.exp(2j*math.pi/3)
    for j,(u,v,zu,zv) in enumerate(rows):
        w=1+n+j
        for x,z in [(1+u,complexval(zu)),(1+v,complexval(zv))]:
            adj[x].append((w,z)); adj[w].append((x,z.conjugate()))
    t=math.pi/(2*math.sqrt(N))
    factor=-1j*t
    term=[0j]*(N+1);term[0]=1.0
    total=term[:]
    for k in range(1,90):
        nxt=[0j]*(N+1)
        for u in range(N+1):
            for v,z in adj[u]:nxt[u]+=z*term[v]
        term=[factor*z/k for z in nxt]
        total=[a+b for a,b in zip(total,term)]
    err=max([abs(abs(total[0])**2)] + [abs(abs(z)**2-1/N) for z in total[1:]])
    assert err<2e-12, (N,err)
    return err


def walk_moment_identity(n,edges):
    N=n+len(edges)
    adj=[[] for _ in range(N+1)]
    for v in range(1,N+1):
        adj[0].append(v);adj[v].append(0)
    for j,(u,v) in enumerate(edges):
        w=n+j+1
        for x in (u+1,v+1):adj[x].append(w);adj[w].append(x)
    x=[0]*(N+1);x[0]=1
    for _ in range(4):
        x=[sum(x[v] for v in adj[u]) for u in range(N+1)]
    degrees=[len(adj[v])-1 for v in range(1,N+1)]
    return x[0] == N*N+sum(d*d for d in degrees)


def main():
    counts={};max_error=0.0;phase_profiles=0
    for name,(n,E,is_bip) in examples().items():
        assert len(E)==3*n//2
        part=bipartition(n,E)
        assert (part is not None)==is_bip, name
        assert walk_moment_identity(n,E)
        if is_bip:
            sols=edge_colorings(n,E)
            assert len(sols)>0 and len(sols)%3==0
            for sol in sols:
                rows=check_phase_rows(n,E,part,sol)
                phase_profiles+=1
            max_error=max(max_error,evolve_cone(n,E,rows))
            counts[name]=len(sols)
    assert counts=={'K3,3':12,'cube Q3':24},counts
    print('VERIFY_OK examples=5 exact_phase_profiles=%d K33_colorings=12 cube_colorings=24 ' 
          'component_counts=4,8 fourth_moment_checks=5 max_taylor_error=%.3e' % (phase_profiles,max_error))

if __name__=='__main__':main()

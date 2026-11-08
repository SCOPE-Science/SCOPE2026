#!/usr/bin/env python3
"""Exact rooted-tree percolation moment and small-tree cutoff checker.
Uses only Python's standard library; no external graph catalog, tables or floating-point tests.
"""
from itertools import product, combinations
from collections import defaultdict, deque
from math import comb
import heapq


def prufer_edges(sequence, n):
    if n == 2:
        return ((0, 1),)
    degree = [1] * n
    for x in sequence: degree[x] += 1
    leaves = [i for i, d in enumerate(degree) if d == 1]
    heapq.heapify(leaves)
    out = []
    for x in sequence:
        u = heapq.heappop(leaves)
        out.append(tuple(sorted((u, x))))
        degree[u] -= 1
        degree[x] -= 1
        if degree[x] == 1:
            heapq.heappush(leaves, x)
    u, v = [i for i, d in enumerate(degree) if d == 1]
    out.append(tuple(sorted((u, v))))
    return tuple(sorted(out))


def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    return adj


def canonical(n, edges, marked=()):
    adj=adjacency(n,edges)
    deg=[len(x) for x in adj]
    leaves=[i for i in range(n) if deg[i]<=1]
    remaining=n
    while remaining>2:
        remaining-=len(leaves)
        new=[]
        for u in leaves:
            for v in adj[u]:
                deg[v]-=1
                if deg[v]==1:new.append(v)
            deg[u]=0
        leaves=new
    centers=leaves
    marks=set(marked)
    def code(u,parent):
        kids=sorted(code(v,u) for v in adj[u] if v!=parent)
        return ('1' if u in marks else '0') + '(' + ''.join(kids) + ')'
    if len(centers)==1: return code(centers[0],-1)
    a,b=centers
    c1,c2=code(a,b),code(b,a)
    return 'E('+''.join(sorted((c1,c2)))+')'


def distances(n, edges):
    adj=adjacency(n,edges)
    dist=[]
    for s in range(n):
        d=[-1]*n;d[s]=0; Q=deque([s])
        while Q:
            u=Q.popleft()
            for v in adj[u]:
                if d[v]<0:d[v]=d[u]+1; Q.append(v)
        assert min(d)>=0
        dist.append(d)
    return dist


def convolution(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def variance_poly(n, ds, s):
    first=[0]*n;second=[0]*n
    for u in range(n):first[ds[s][u]]+=1
    for u in range(n):
        for v in range(n):
            z=(ds[s][u]+ds[s][v]+ds[u][v])//2
            assert 2*z==ds[s][u]+ds[s][v]+ds[u][v]
            second[z]+=1
    first_sq=convolution(first,first)
    out=[0]*(2*n-1)
    for i,x in enumerate(second):out[i]+=x
    for i,x in enumerate(first_sq):out[i]-=x
    return tuple(out)


def signed_poly(c):
    while c and c[-1]==0:c.pop()
    return c


def divide_p_one_minus_p(H):
    H=signed_poly(list(H))
    if not H:return []
    assert H[0]==0 and sum(H)==0
    g=H[1:]
    q=[]
    for x in g[:-1]:q.append(x+(q[-1] if q else 0))
    assert g[-1]==-q[-1]
    return signed_poly(q)


def mobius(q):
    if not q:return []
    d=len(q)-1
    return [sum(q[k]*comb(d-k,j-k) for k in range(j+1)) for j in range(d+1)]


def variations(arr):
    a=[v>0 for v in arr if v]
    return sum(a[i]!=a[i-1] for i in range(1,len(a)))


def evalpoly(co,x_num,x_den=1):
    d=len(co)-1
    return sum(c*x_num**j*x_den**(d-j) for j,c in enumerate(co))


def percolation_moments(n,edges,s):
    # Separate enumeration by edge masks, followed by exact binomial expansion.
    m=len(edges)
    mean=[0]*(m+1);mom2=[0]*(m+1)
    for mask in range(1<<m):
        chosen=[edges[k] for k in range(m) if (mask>>k)&1]
        adj=adjacency(n,chosen)
        found={s};queue=deque([s])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if v not in found:found.add(v);queue.append(v)
        k=len(found);a=bin(mask).count("1");b=m-a
        for j in range(b+1):
            coeff=comb(b,j)*(-1)**j
            mean[a+j]+=k*coeff
            mom2[a+j]+=k*k*coeff
    v=convolution(mean,mean)
    for i,x in enumerate(mom2):v[i]-=x
    return tuple(-x for x in v)


def main():
    types=[];interesting=[]
    for n in range(2,8):
        unique={}
        seqs=product(range(n), repeat=max(0,n-2))
        for seq in seqs:
            e=prufer_edges(seq,n)
            key=canonical(n,e)
            if key not in unique:unique[key]=e
        types.append(len(unique))
        counts=defaultdict(int);total=0
        for edges in unique.values():
            D=distances(n,edges)
            V=[variance_poly(n,D,s) for s in range(n)]
            for s,t in combinations(range(n),2):
                H=[x-y for x,y in zip(V[s],V[t])]
                if not any(H):continue
                total+=1
                q=divide_p_one_minus_p(H)
                v=variations(mobius(q));counts[v]+=1
                assert v <= (2 if n==7 else 1), (n,edges,s,t,q,v)
                if v==2:
                    # Two distinct roots in (0,1) by IVT, Descartes upper bound.
                    signs=[evalpoly(q,0),evalpoly(q,1,2),evalpoly(q,1)]
                    assert signs[0]*signs[1]<0 and signs[1]*signs[2]<0
                    interesting.append((canonical(n,edges,(s,t)),edges,s,t,q,signs))
        print('n',n,'isomorphism types',len(unique),'nonzero unordered seed pairs',total,'Descartes bounds',dict(sorted(counts.items())))
    assert types==[1,1,2,3,6,11]
    assert len(interesting)==3
    assert len(set(z[0] for z in interesting))==2
    print('SEVEN_VERTEX_PAIR_ORBITS',len(set(z[0] for z in interesting)))
    for key,edges,s,t,q,signs in interesting:
        print('TWO_CROSSING',edges,'seeds',s,t,'q ascending',q,'q signs numerator at 0,1/2,1',signs)
    witness=((0,1),(0,4),(1,2),(1,3),(4,5),(4,6))
    D=distances(7,witness)
    V0=variance_poly(7,D,0);V1=variance_poly(7,D,1)
    assert V0==percolation_moments(7,witness,0)
    assert V1==percolation_moments(7,witness,1)
    q=divide_p_one_minus_p([a-b for a,b in zip(V0,V1)])
    assert q==[-1,9,-3,-8,-4],q
    print('WITNESS_Q',q,'P0',V0,'P1',V1,'INDEPENDENT_MASK_CHECK','PASS')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()

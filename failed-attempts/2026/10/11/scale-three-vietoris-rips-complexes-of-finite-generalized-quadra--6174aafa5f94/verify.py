#!/usr/bin/env python3
from itertools import product, combinations
from collections import deque
from math import comb

def inv(a,p): return pow(a,-1,p)

def norm(v,p):
    for x in v:
        if x%p:
            z=inv(x%p,p)
            return tuple((z*y)%p for y in v)
    raise ValueError

def add(u,v,p): return tuple((a+b)%p for a,b in zip(u,v))
def smul(a,u,p): return tuple((a*x)%p for x in u)
def omega(u,v,p):
    # u0 v1-u1 v0 + u2 v3-u3 v2
    return (u[0]*v[1]-u[1]*v[0]+u[2]*v[3]-u[3]*v[2])%p

def W3(q):
    assert q in (2,3), 'verifier intentionally checks prime q=2,3 only'
    pts=sorted({norm(v,q) for v in product(range(q), repeat=4) if any(v)})
    pindex={v:i for i,v in enumerate(pts)}
    lines=set()
    for a,b in combinations(pts,2):
        if omega(a,b,q)!=0: continue
        span={norm(add(smul(x,a,q),smul(y,b,q),q),q) for x in range(q) for y in range(q) if x or y}
        if len(span)==q+1: lines.add(tuple(sorted(pindex[x] for x in span)))
    lines=sorted(lines)
    return pts,lines

def check(q):
    pts,lines=W3(q); np=len(pts); nl=len(lines)
    expected=(q+1)*(q*q+1)
    assert np==nl==expected,(q,np,nl,expected)
    through=[[] for _ in range(np)]
    for j,L in enumerate(lines):
        assert len(L)==q+1
        for x in L: through[x].append(j)
    assert all(len(z)==q+1 for z in through)
    # Levi graph and all-pairs distances
    N=np+nl; A=[set() for _ in range(N)]
    for j,L in enumerate(lines):
        for x in L:
            A[x].add(np+j); A[np+j].add(x)
    d=[]
    for s in range(N):
        ds=[99]*N; ds[s]=0; Q=deque([s])
        while Q:
            u=Q.popleft()
            for v in A[u]:
                if ds[v]==99: ds[v]=ds[u]+1; Q.append(v)
        d.append(ds)
    assert max(map(max,d))==4
    # cross distances are 1 or 3; same-type distances are 0,2,4
    assert all(d[p][np+l] in (1,3) for p in range(np) for l in range(nl))
    assert all(d[a][b] in (0,2,4) for a in range(np) for b in range(np))
    assert all(d[np+a][np+b] in (0,2,4) for a in range(nl) for b in range(nl))
    # Point factor K_P: every clique of size >=2 lies in a unique line.
    # It suffices to check every collinear pair lies on exactly one line, and every triangle clique lies on one line.
    pair_lines={}
    for j,L in enumerate(lines):
        for a,b in combinations(L,2): pair_lines.setdefault((a,b),[]).append(j)
    assert all(len(v)==1 for v in pair_lines.values())
    col=lambda a,b: tuple(sorted((a,b))) in pair_lines
    for tri in combinations(range(np),3):
        if all(col(a,b) for a,b in combinations(tri,2)):
            common=set(through[tri[0]]) & set(through[tri[1]]) & set(through[tri[2]])
            assert len(common)==1
    # f-vector of one clique factor, using uniqueness of positive-dimensional faces by line.
    f=[np] + [nl*comb(q+1,k) for k in range(2,q+2)]
    chi=sum(((-1)**i)*x for i,x in enumerate(f))
    m=q**4
    assert chi==1-m,(q,f,chi,m)
    # Levi cycle rank and predicted scale-3 join reduced Euler characteristic.
    E=np*(q+1); beta=E-(np+nl)+1
    assert beta==m
    red_join=-(chi-1)*(chi-1)
    assert red_join==-(q**8)
    return dict(q=q,points=np,lines=nl,incidences=E,factor_f_vector=f,factor_euler=chi,levi_cycle_rank=beta,predicted_s3_spheres=q**8,reduced_euler_scale3=red_join)

if __name__=='__main__':
    for q in (2,3): print(check(q))
    print('VERIFY_OK')

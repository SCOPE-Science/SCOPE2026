#!/usr/bin/env python3
"""Exact small-case checks for vertex- versus volume-uniform second moments
of ordinary (unit-generator) graphical zonotopes of cactus graphs.
No network, symbolic libraries, or nonstandard packages are required.
"""
from fractions import Fraction as Q
from itertools import product
from math import prod


def cyc_edges(v):
    return [(v[i],v[(i+1)%len(v)]) for i in range(len(v))]


def make(n, blocks):
    # A block is either ('edge', [u,v]) or ('cycle', [v0,...,v_{k-1}]).
    E=[]; btypes=[]
    for kind,verts in blocks:
        if kind == 'edge':
            assert len(verts)==2
            es=[tuple(verts)]
        else:
            assert kind=='cycle' and len(verts)>=3
            es=cyc_edges(verts)
        for u,v in es:
            assert u!=v
            assert tuple(sorted((u,v))) not in [tuple(sorted(e)) for e in E]
            E.append((u,v))
        btypes.append((kind,es))
    assert len(set(u for e in E for u in e))==n
    return E,btypes


def acyclic(n, edges, signs):
    indeg=[0]*n; adj=[[] for _ in range(n)]
    for (u,v),s in zip(edges,signs):
        a,b=(u,v) if s==1 else (v,u)
        indeg[b]+=1; adj[a].append(b)
    todo=[j for j in range(n) if indeg[j]==0]
    p=0
    while p<len(todo):
        j=todo[p];p+=1
        for k in adj[j]:
            indeg[k]-=1
            if not indeg[k]:todo.append(k)
    return p==n


def outer(b):
    return [[u*v for v in b] for u in b]


def accumulate(A,B,factor=1):
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j]+=factor*B[i][j]


def incidence(n,edge):
    u,v=edge;b=[0]*n;b[u]=1;b[v]=-1;return b


def vertex_cov(n,edges):
    xs=[]
    for signs in product((-1,1),repeat=len(edges)):
        if not acyclic(n,edges,signs):continue
        x=[0]*n
        for (u,v),s in zip(edges,signs):
            x[u]+=s; x[v]-=s
        xs.append(tuple(x))
    assert xs and len(xs)==len(set(xs)), 'distinct acyclic orientations must map to distinct vertices'
    N=len(xs)
    means=[Q(sum(x[i] for x in xs),2*N) for i in range(n)]
    assert all(m==0 for m in means)
    C=[[sum(Q(x[i]*x[j],4*N) for x in xs) for j in range(n)] for i in range(n)]
    return C,N


def volume_tiles_cov(n,block_edges):
    # Independent construction: a cycle zonotope is tiled by k images of
    # [0,1]^(k-1), one for each omitted edge. Each has equal intrinsic volume.
    # A bridge gives a single centered unit interval.
    C=[[Q(0) for j in range(n)] for i in range(n)]
    for kind,es in block_edges:
        bs=[incidence(n,e) for e in es]
        if kind=='edge':
            accumulate(C,outer(bs[0]),Q(1,12))
        else:
            k=len(es)
            block=[[Q(0) for j in range(n)] for i in range(n)]
            for omit in range(k):
                # Conditional covariance + conditional mean outer product:
                # x = sum_(i != omit) U_i b_i, U_i independently Uniform[0,1].
                # E[x|omit] = -b_omit/2 (since sum all b_i=0).
                cond=[[Q(0) for j in range(n)] for i in range(n)]
                for i in range(k):
                    if i!=omit:accumulate(cond,outer(bs[i]),Q(1,12))
                accumulate(cond,outer(bs[omit]),Q(1,4))
                accumulate(block,cond,Q(1,k))
            accumulate(C,block)
    return C


def coefficients(n,blocks):
    Cv=[[Q(0) for j in range(n)] for i in range(n)]
    Cz=[[Q(0) for j in range(n)] for i in range(n)]
    count=1; products=[Q(1),Q(1)]
    for kind,es in blocks:
        k=len(es)
        if kind=='edge':
            wv=Q(1,4); wz=Q(1,12); count*=2
            tv=wv;tz=wz
        else:
            wv=Q(2**(k-1),4*(2**(k-1)-1)); wz=Q(k+2,12*k)
            count*=2**k-2
            tv=k*wv**(k-1);tz=k*wz**(k-1)
        products[0]*=tv;products[1]*=tz
        for e in es:
            a=outer(incidence(n,e))
            accumulate(Cv,a,wv)
            accumulate(Cz,a,wz)
    return Cv,Cz,count,products


def det(A):
    M=[list(map(Q,row)) for row in A];n=len(M);val=Q(1)
    for i in range(n):
        p=next((r for r in range(i,n) if M[r][i]),None)
        if p is None:return Q(0)
        if p!=i:M[i],M[p]=M[p],M[i];val=-val
        v=M[i][i];val*=v
        for j in range(i+1,n):
            q=M[j][i]/v
            for k in range(i,n):M[j][k]-=q*M[i][k]
    return val


def run():
    cases=[
        (2,[('edge',[0,1])]),
        (3,[('cycle',[0,1,2])]),
        (4,[('cycle',[0,1,2,3])]),
        (5,[('cycle',[0,1,2,3,4])]),
        (6,[('cycle',[0,1,2,3,4,5])]),
        (4,[('edge',[0,1]),('edge',[1,2]),('edge',[2,3])]),
        (5,[('cycle',[0,1,2]),('edge',[2,3]),('edge',[3,4])]),
        (5,[('cycle',[0,1,2]),('cycle',[2,3,4])]),
        (6,[('cycle',[0,1,2,3]),('cycle',[3,4,5])]),
        (8,[('cycle',[0,1,2,3]),('cycle',[3,4,5,6,7])]),
        (7,[('cycle',[0,1,2,3,4]),('edge',[4,5]),('edge',[5,6])]),
        (8,[('cycle',[0,1,2,3]),('cycle',[3,4,5]),('edge',[5,6]),('edge',[6,7])]),
        (9,[('cycle',[0,1,2]),('cycle',[2,3,4,5]),('cycle',[5,6,7,8])]),
    ]
    entries=0; total=0
    for n,blocks in cases:
        edges,bs=make(n,blocks)
        actual,number=vertex_cov(n,edges)
        tile=volume_tiles_cov(n,bs)
        Cv,Cz,expected,ptau=coefficients(n,bs)
        assert number==expected
        assert actual==Cv, ('vertex',n,blocks)
        assert tile==Cz, ('volume',n,blocks)
        assert det([row[:-1] for row in Cv[:-1]])==ptau[0],('vertex cofactor',n)
        assert det([row[:-1] for row in Cz[:-1]])==ptau[1],('volume cofactor',n)
        entries+=2*n*n;total+=number
    # Exact finite check only: the proof handles every cycle length.
    assert Q(3*4,4+2)*Q(8,7)==Q(16,7)
    assert Q(3*5,5+2)*Q(16,15)==Q(16,7)
    for l in range(3,151):
        R=Q(3*l,l+2)*Q(2**(l-1),2**(l-1)-1)
        assert Q(16,7)<=R<3
    # Boundary test: a noncactus graph can have nonzero covariance at nonedges.
    edges=[(u,v) for u in (0,1) for v in (2,3,4)]  # K_{2,3}
    outside,outside_n=vertex_cov(5,edges)
    assert outside_n==46 and outside[0][1]==Q(-3,92)
    print('CACTUS_VERTEX_VOLUME_COVARIANCE_CHECKS_PASSED',
          'profiles='+str(len(cases)), 'vertices='+str(total),
          'matrix_entries='+str(entries),'cycle_lengths=148')

if __name__=='__main__':run()

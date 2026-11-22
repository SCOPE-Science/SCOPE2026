"""Exact-rational tests for a fixed-end sweep of persistent up-Laplacians.
All stages are generated as genuine face-closed simplicial filtrations.
Run: python checker.py
"""
import random
import itertools
from collections import defaultdict
from sympy import Matrix, eye, zeros


def boundary(bases0, bases1):
    pos={f:i for i,f in enumerate(bases0)}
    b=zeros(len(bases0),len(bases1))
    for j,sigma in enumerate(bases1):
        for k in range(len(sigma)):
            face=sigma[:k]+sigma[k+1:]
            b[pos[face],j]+=(-1)**k
    return b


def reduction(B):
    R=B.copy(); V=eye(B.cols)
    low={}
    for j in range(B.cols):
        while True:
            rows=[i for i in range(B.rows) if R[i,j]!=0]
            if not rows: break
            p=rows[-1]
            if p not in low:
                low[p]=j; break
            i=low[p]; fac=R[p,j]/R[p,i]
            for r in range(B.rows): R[r,j]-=fac*R[r,i]
            for r in range(B.cols): V[r,j]-=fac*V[r,i]
    assert B*V==R
    pivots=[max([i for i in range(B.rows) if R[i,j]!=0],default=None) for j in range(B.cols)]
    assert len(set(p for p in pivots if p is not None))==sum(p is not None for p in pivots)
    return V,pivots


def direct_projected_lap(B,birth0,birth1,s,t):
    rows=[i for i,u in enumerate(birth0) if u<=s]
    cols=[j for j,u in enumerate(birth1) if u<=t]
    if not rows or not cols: return zeros(len(rows))
    B_sub=B.extract(list(range(B.rows)),cols)
    outside=[i for i in range(B.rows) if i not in rows]
    M=B_sub.extract(outside,list(range(len(cols))))
    ker=M.nullspace() if outside else [eye(len(cols))[:,i] for i in range(len(cols))]
    if not ker:return zeros(len(rows))
    X=Matrix.hstack(*ker)
    P=X*(X.T*X).inv()*X.T
    return B_sub.extract(rows,list(range(len(cols))))*P*B_sub.extract(rows,list(range(len(cols)))).T


def sweep_check(B,birth0,birth1):
    m=B.cols;n=B.rows
    if not m:return 0
    V,pivots=reduction(B)
    start=[0 if p is None else birth0[p] for p in pivots]
    assert all(start[j]<=birth1[j] for j in range(m))
    cnt=0
    for t in sorted(set(birth1)):
        basis=[]; P=zeros(n)
        for s in sorted({start[j] for j in range(m) if birth1[j]<=t}):
            for j in range(m):
                if birth1[j]>t or start[j]!=s:continue
                v=V[:,j]
                for w in basis:
                    v-=w*(w.T*v)[0]/(w.T*w)[0]
                assert v.dot(v)!=0
                u=B*v
                assert all(u[i]==0 for i in range(n) if birth0[i]>s)
                P+=u*u.T/(v.T*v)[0]
                basis.append(v)
            rows=[i for i,u in enumerate(birth0) if u<=s]
            test=P.extract(rows,rows)
            exact=direct_projected_lap(B,birth0,birth1,s,t)
            assert test==exact, (t,s,B, start, birth0,birth1,test,exact)
            cnt+=1
    # Full exhaustive pair verification, including off-grid pairs where spectra are padded or unchanged.
    for t in sorted(set(birth0+birth1)):
        for s in sorted(set([0]+birth0+birth1)):
            if s>t:continue
            eligible=[j for j in range(m) if birth1[j]<=t and start[j]<=s]
            if not eligible: p=zeros(n)
            else:
                X=V[:,eligible]; p=B*X*(X.T*X).inv()*X.T*B.T
            rows=[i for i,u in enumerate(birth0) if u<=s]
            assert p.extract(rows,rows)==direct_projected_lap(B,birth0,birth1,s,t)
    return cnt


def tests(seed=718, samples=120):
    rng=random.Random(seed)
    totals={0:0,1:0}; cases={0:0,1:0}
    for rep in range(samples):
        n=rng.randint(3,6)
        vertices=[(i,) for i in range(n)]
        times={v:rng.randint(0,2) for v in vertices}
        edges=[]
        for edge in itertools.combinations(range(n),2):
            if rng.random()<.75:
                edges.append(edge)
                times[edge]=max(times[(edge[0],)],times[(edge[1],)],rng.randint(2,5))
        edge_set=set(edges)
        triangles=[]
        for tri in itertools.combinations(range(n),3):
            faces=list(itertools.combinations(tri,2))
            if set(faces).issubset(edge_set) and rng.random()<.55:
                triangles.append(tri)
                times[tri]=max(*(times[e] for e in faces),rng.randint(3,8))
        for q,lower,upper in [(0,vertices,edges),(1,edges,triangles)]:
            if not lower or not upper:continue
            lo=sorted(lower,key=lambda x:(times[x],x)); hi=sorted(upper,key=lambda x:(times[x],x))
            B=boundary(lo,hi)
            c=sweep_check(B,[times[x] for x in lo],[times[x] for x in hi]); cases[q]+=1;totals[q]+=c
    print('PASS exact rational: seed',seed,'sampled filtrations',samples,'checks',totals,'cases',cases)

if __name__=='__main__':tests()

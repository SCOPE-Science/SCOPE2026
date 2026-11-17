"""Exact checks of two-cluster finite metric Lipschitz polar vertices.
Only Python standard library is used; all linear algebra is exact rational.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter


def tree_edges_from_prufer(seq, n):
    deg=[1]*n
    for v in seq: deg[v]+=1
    edges=[]
    for v in seq:
        u=next(i for i in range(n) if deg[i]==1)
        edges.append((u,v));deg[u]-=1;deg[v]-=1
    a,b=[i for i in range(n) if deg[i]==1]
    edges.append((a,b))
    return edges


def raw_vertices(p,q,s,t):
    n=p+q
    d=[[F(0) if i==j else (s if i<p and j<p else t if i>=p and j>=p else F(1)) for j in range(n)] for i in range(n)]
    out=set()
    for pr in product(range(n),repeat=n-2):
        edges=tree_edges_from_prufer(pr,n)
        adj=[[] for _ in range(n)]
        for e,(u,v) in enumerate(edges):
            adj[u].append((v,e,1));adj[v].append((u,e,-1))
        for signs in product((-1,1),repeat=n-1):
            vals=[None]*n;vals[0]=F(0); stack=[0]
            while stack:
                u=stack.pop()
                for v,e,sgn in adj[u]:
                    if vals[v] is None:
                        vals[v]=vals[u]+sgn*signs[e]*d[u][v];stack.append(v)
            if all(abs(vals[i]-vals[j])<=d[i][j] for i in range(n) for j in range(i+1,n)):
                out.add(tuple(vals))
    return out


def theory_vertices(p,q,s,t):
    n=p+q; out=set()
    for xa in product((F(0),s),repeat=p):
        if F(0) not in xa: continue
        for yb in product((F(1), F(1)-t), repeat=q):
            if F(1) not in yb: continue
            arr=xa+yb
            for sg in (1,-1):
                vv=[sg*(a-arr[0]) for a in arr]
                out.add(tuple(vv))
    return out


def centered_norm2(z):
    n=len(z)
    return sum(v*v for v in z)-sum(z)**2/n


def predicted(p,q,t):
    n=p+q
    vals=[F(p*q,n)+t*(t-F(2*p,n))*y-(t*t/n)*y*y for y in range(q)]
    maxv=max(vals);ys=[y for y,v in enumerate(vals) if v==maxv]
    from math import comb
    num=2*sum(comb(q,y) for y in ys)
    rank=q if any(y>=1 for y in ys) else 1
    return maxv,ys,num,rank


def rank_dense(vecs):
    # Exact Gaussian elimination over rationals
    M=[list(r) for r in vecs]
    if not M:return 0
    rows=len(M);cols=len(M[0]);r=0
    for c in range(cols):
        pivot=next((z for z in range(r,rows) if M[z][c]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]; fac=M[r][c]
        M[r]=[v/fac for v in M[r]]
        for z in range(r+1,rows):
            if M[z][c]:
                mult=M[z][c];M[z]=[a-mult*b for a,b in zip(M[z],M[r])]
        r+=1
        if r==rows:break
    return r


def run_one(p,q,s,t,independent=True):
    s=F(s);t=F(t); assert p>=2 and p<=q and 0<s<1 and 0<t<1
    tv=theory_vertices(p,q,s,t)
    if independent:
        rv=raw_vertices(p,q,s,t)
        assert rv==tv,(p,q,s,t,len(rv),len(tv),len(rv-tv),len(tv-rv))
    norm=max(centered_norm2(z) for z in tv)
    contacts=[z for z in tv if centered_norm2(z)==norm]
    pv,ys,ct,rr=predicted(p,q,t)
    assert norm==pv,(p,q,s,t,norm,pv)
    assert len(contacts)==ct,(p,q,s,t,len(contacts),ct)
    centered=[tuple(x-sum(z)/len(z) for x in z) for z in contacts]
    rank=rank_dense(centered)
    assert rank==rr,(p,q,s,t,rank,rr)
    return (p,q,str(s),str(t),len(tv),len(contacts),rank)

if __name__=='__main__':
    cases=[(2,2,'2/5','3/4'),(2,3,'1/3','9/10'),(2,4,'3/5','2/3'),(2,4,'9/10','4/5'),(2,4,'1/6','9/10'),(3,3,'4/7','5/6'),(2,4,'4/5','4/5')]
    for p,q,s,t in cases:
        print('EXACT_SPANNING_TREE_VERTEX_AND_CONTACT_RANK_PASS',run_one(p,q,s,t),flush=True)
    for p in range(2,8):
        for q in range(p,22):
            for a in (F(1,23),F(2,5),F(18,25),F(49,50)):
                for b in (F(1,17),F(1,3),F(4,5),F(99,100)):
                    # independently exhaust the integer potential count pairs
                    n=p+q
                    qs=[(F(q)+a*a*x-(2*b-b*b)*y-(F(q)+a*x-b*y)**2/n,x,y) for x in range(p) for y in range(q)]
                    win=max(z[0] for z in qs)
                    val,ys,ct,r=predicted(p,q,b)
                    assert win==val and all(x==0 for v,x,y in qs if v==win),(p,q,a,b)
    print('ALL_TWO_CLUSTER_SCREENING_AND_PHASE_CHECKS_PASS',flush=True)

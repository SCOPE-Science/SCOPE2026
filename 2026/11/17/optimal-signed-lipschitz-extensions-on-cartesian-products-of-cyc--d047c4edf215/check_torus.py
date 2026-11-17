"""Finite LP corroboration of cycle-product extension formula.
Usage: python check_torus.py
Requires numpy and scipy. The theorem is proved analytically in RESULT.md.
"""
from itertools import product
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog


def test_cycle_product(lengths):
    vs=list(product(*(range(n) for n in lengths)))
    ids={v:i for i,v in enumerate(vs)}
    N=len(vs)
    dims=len(lengths)
    diam=sum(n//2 for n in lengths)
    c=sum((Fraction((n*n)//4,n) for n in lengths),Fraction())
    def d(u,v):
        return sum(min(abs(u[i]-v[i]), lengths[i]-abs(u[i]-v[i])) for i in range(dims))
    distances=np.array([[d(u,v) for v in vs] for u in vs], dtype=int)
    for u in vs:
        assert sum(distances[ids[u]])==N*c
    edges=set()
    for v in vs:
        for j,n in enumerate(lengths):
            q=list(v);q[j]=(q[j]+1)%n
            a,b=ids[v],ids[tuple(q)]
            edges.add(tuple(sorted((a,b))))
    A=[]
    for a,b in edges:
        row=np.zeros(N);row[a]=1;row[b]=-1
        A += [row,-row]
    A=np.array(A)
    bounds=[(0,0)]+[(None,None)]*(N-1)
    def KR(w,v):
        signed=np.array(w,dtype=float)*-1
        signed[ids[v]]+=1
        res=linprog(-signed,A_ub=A,b_ub=np.ones(len(A)),bounds=bounds,method='highs')
        if not res.success:raise AssertionError(res.message)
        return -res.fun
    uniform=np.ones(N)/N
    base=vs[0]
    opposite=tuple(n//2 for n in lengths)
    wpair=np.zeros(N)
    for v in vs:
        # For each odd factor retain all coordinates uniformly; even factors correlate by a global sign.
        factors=[i for i,n in enumerate(lengths) if n%2]
        even=[i for i,n in enumerate(lengths) if n%2==0]
        if all(v[i] in (0,opposite[i]) for i in even) and (not even or len({v[i]!=0 for i in even})==1):
            wpair[ids[v]] = 1
    wpair=wpair/sum(wpair)
    independent=np.array([np.prod([1/n if n%2 else (0.5 if v[i] in (0,n//2) else 0) for i,n in enumerate(lengths)]) for v in vs])
    for name,w in [('uniform',uniform),('correlated',wpair),('independent',independent)]:
        assert abs(sum(w)-1)<1e-9
        for j,n in enumerate(lengths):
            marginal=np.array([sum(w[ids[v]] for v in vs if v[j]==a) for a in range(n)])
            if n%2:
                assert np.allclose(marginal,np.ones(n)/n)
            else:
                assert np.allclose(marginal[:n//2], marginal[n//2:])
        assert np.allclose(distances@w,float(c))
        sample=vs if N<=30 else [vs[0],vs[N//2],vs[-1]]
        for v in sample:
            assert abs(KR(w,v)-float(c))<1e-7,(lengths,name,v)
    dr=np.zeros(N);dr[ids[base]]=1
    assert abs(KR(dr,opposite)-diam)<1e-7
    # A tiny signed perturbation of a critical optimizer has strictly larger free norm.
    if all(wpair>0):
        # A four-cell signed-zero checkerboard perturbation leaves each marginal unchanged.
        u=vs[0]; p=list(u);p[0]=1; q=list(u);q[1]=1; pq=list(u);pq[0]=1;pq[1]=1
        wpair[ids[u]]+=1/N; wpair[ids[tuple(pq)]]+=1/N
        wpair[ids[tuple(p)]]-=1/N; wpair[ids[tuple(q)]]-=1/N
        assert min(wpair)==0
    b=next(v for v in vs if abs(wpair[ids[v]])<1e-12)
    signed=wpair.copy();signed[ids[base]]+=.01;signed[ids[b]]-=.01
    assert signed[ids[b]]<0
    assert max(KR(signed,v) for v in (vs if N<=30 else [opposite,vs[-1]])) > float(c)+1e-7
    codim=sum(n-1 if n%2 else n//2 for n in lengths)
    rows=[]
    for j,n in enumerate(lengths):
        if n%2:
            for a in range(n-1):
                row=[int(v[j]==a)-int(v[j]==n-1) for v in vs]
                rows.append(row)
        else:
            for a in range(n//2):
                row=[int(v[j]==a)-int(v[j]==a+n//2) for v in vs]
                rows.append(row)
    rank=np.linalg.matrix_rank(np.array(rows+[np.ones(N)]))
    assert rank==codim+1,(lengths,rank,codim)
    print('CHECK_PASS',lengths,'vertices',N,'c',c,'diameter',diam,'critical_face_dimension',N-1-codim,'rank',rank)

for sizes in [(3,3),(3,4),(4,4),(4,5),(4,6),(5,5),(5,6),(3,4,4)]:
    test_cycle_product(sizes)
print('CYCLE_PRODUCT_SIGNED_OPTIMALITY_LP_CHECKS_PASS')

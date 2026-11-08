"""Exact simplex-integration check for complete-bipartite polar covariance."""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
import numpy as np
from scipy.spatial import HalfspaceIntersection, ConvexHull
from sympy import Matrix


def verify(p,q):
    n=p+q; d=n-1
    # Gauge the final vertex of the q-class to zero.
    inequalities=[]
    for i in range(p):
        for j in range(q):
            v=np.zeros(d)
            v[i]=1
            if j<q-1: v[p+j]=-1
            inequalities.extend([np.r_[v,-1.0],np.r_[-v,-1.0]])
    raw=HalfspaceIntersection(np.array(inequalities),np.zeros(d)).intersections
    verts=set()
    for row in raw:
        point=tuple(int(round(x)) for x in row)
        assert max(abs(x-y) for x,y in zip(row,point)) < 1e-7
        assert all(np.dot(h[:-1],row)+h[-1]<1e-7 for h in inequalities)
        verts.add(point)
    vlist=sorted(verts)
    hull=ConvexHull(np.array(vlist,dtype=float), qhull_options='Qx')
    det_sum=0
    mom=[[F(0) for _ in range(n)] for _ in range(n)]
    first=[F(0) for _ in range(n)]
    for simplex in hull.simplices:
        col=[vlist[i] for i in simplex]
        weight=abs(int(Matrix(col).det()))
        if weight==0: continue  # Degenerate Qhull simplices contribute zero volume.
        det_sum+=weight
        projected=[]
        for x in col:
            vec=[F(j) for j in x[:p]]+[F(j) for j in x[p:]]+[F(0)]
            mu=sum(vec,F(0))/n
            projected.append([t-mu for t in vec])
        S=[sum((r[k] for r in projected),F(0)) for k in range(n)]
        for k in range(n): first[k]+=weight*S[k]
        for i in range(n):
            for j in range(n):
                mom[i][j]+=weight*(S[i]*S[j]+sum((r[i]*r[j] for r in projected),F(0)))
    assert all(t==0 for t in first), (p,q,first)  # Mean is zero.
    mom=[[t/(det_sum*(d+1)*(d+2)) for t in row] for row in mom]
    lp=F((p+1)*(p+2),3*n*(n+1))
    lq=F((q+1)*(q+2),3*n*(n+1))
    lb=F(p*q+2,3*n*(n+1))
    for i in range(n):
        for j in range(n):
            # O(p) and O(q) contrast projectors, plus the between-block projector.
            v=F(0)
            if i<p and j<p:
                v+=lp*(F(int(i==j))-F(1,p)) + lb*F(q,p*n)
            elif i>=p and j>=p:
                v+=lq*(F(int(i==j))-F(1,q)) + lb*F(p,q*n)
            else:
                v-=lb*F(1,n)
            assert mom[i][j]==v,(p,q,i,j,mom[i][j],v)
    expected=F(2**d*factorial(p)*factorial(q),factorial(n-1))
    assert F(det_sum,factorial(d)) == expected,(p,q,det_sum,expected)
    return (len(vlist),len(hull.simplices),n*n)

if __name__=='__main__':
    cases=[(2,2),(2,3),(3,2),(2,4),(4,2),(3,3)]
    out=[verify(p,q) for p,q in cases]
    print('BICLIQUE_POLAR_EXACT_MOMENTS_PASSED', 'profiles='+str(len(cases)), 'vertices='+str(sum(a for a,b,c in out)), 'simplices='+str(sum(b for a,b,c in out)), 'entries='+str(sum(c for a,b,c in out)))

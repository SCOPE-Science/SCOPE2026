#!/usr/bin/env python3
"""Independent finite checks for the Catalan matroid Euclidean separation theorem.
Run: python check_catalan_distance.py
Requirements: numpy, scipy. These computations supplement the proof.
"""
from itertools import combinations
from math import comb, floor
import numpy as np
from scipy.optimize import minimize


def distance_to_catalan(x):
    x = np.asarray(x, dtype=float)
    n = len(x) // 2
    m = 2*n-2
    z = x[1:-1]
    # Intrinsic coordinates: first and last are fixed to 1 and 0.
    A = np.array([[1.]* (2*k) + [0.] * (m-2*k) for k in range(1,n-1)])
    constraints = [{'type':'eq', 'fun':lambda t:t.sum()-(n-1),
                    'jac':lambda t:np.ones(m)}]
    if A.size:
        b = np.arange(1,n-1, dtype=float)
        constraints.append({'type':'ineq','fun':lambda t:A@t-b,'jac':lambda t:A})
    out=minimize(lambda t:np.dot(t-z,t-z), np.full(m, .5),
                 jac=lambda t:2*(t-z),method='SLSQP',
                 bounds=[(0,1)]*m, constraints=constraints,
                 options={'ftol':1e-11,'maxiter':160})
    if not out.success:
        raise RuntimeError((n,x.tolist(),out.message))
    return float((1-x[0])**2+x[-1]**2+np.sum((out.x-z)**2)),np.r_[1.,out.x,0.]


def cube_projection(x):
    n=len(x)//2
    y=np.array(x,dtype=float)
    y[0]=1.;y[-1]=0.
    for j in range(n-1):
        i=1+2*j
        delta=(x[i]+x[i+1]-1.)/2.
        y[i:i+2]=x[i:i+2]-delta
    return y


def expected_maximizers(n):
    if n % 2:
        return {tuple([0]*n+[1]*n)}
    x=[0]*n+[1]*n
    y=x.copy()
    y[n-1],y[n]=1,0
    return {tuple(x),tuple(y)}


def dyck_vertices(n):
    for inds in combinations(range(2*n),n):
        x=[int(i in inds) for i in range(2*n)]
        if all(2*sum(x[:j])>=j for j in range(1,2*n+1)):
            yield np.array(x,dtype=float)


def check():
    num_qp=0;num_dyck=0
    for n in range(2,7):
        R2=(n+3)//2
        candidates=set()
        dycks=list(dyck_vertices(n))
        assert len(dycks)==comb(2*n,n)//(n+1)
        num_dyck+=len(dycks)
        for inds in combinations(range(2*n),n):
            x=np.zeros(2*n); x[list(inds)]=1.
            q,y=distance_to_catalan(x)
            num_qp+=1
            if q>R2+1e-7:raise AssertionError(('upper',n,inds,q,R2))
            if abs(q-R2)<1e-7:
                candidates.add(tuple(x.astype(int)))
        if candidates != expected_maximizers(n):
            raise AssertionError(('wrong maximizers',n,candidates,expected_maximizers(n)))
        # Exact normal certificate on each farthest vertex against every Dyck vertex.
        for xt in candidates:
            x=np.array(xt,dtype=float)
            y=cube_projection(x)
            residual=x-y
            assert abs(np.dot(residual,residual)-R2)<1e-10
            assert all(np.dot(residual,z-y)<1e-10 for z in dycks)
            q,z=distance_to_catalan(x)
            assert np.linalg.norm(z-y)<1e-6
        if n%2==0:
            x1,x2=map(lambda t:np.asarray(t,dtype=float),sorted(candidates))
            w=x1-cube_projection(x1)
            assert np.linalg.norm(w-(x2-cube_projection(x2)))<1e-10
            for t in [0.13,0.5,0.79]:
                p=t*x1+(1-t)*x2
                d,y=distance_to_catalan(p)
                assert abs(d-R2)<1e-7
        print(f'pass n={n} hypersimplex_vertices={comb(2*n,n)} dyck_vertices={len(dycks)} deepest_vertices={len(candidates)} squared_distance={R2}')
    # Higher ranks: exact normal certificates for the claimed deepest points, no exhaustive check.
    for n in range(7,41):
        for xt in expected_maximizers(n):
            x=np.asarray(xt,dtype=float)
            y=cube_projection(x)
            w=x-y
            assert abs(np.dot(w,w)-(n+3)//2)<1e-10
            pairs=w[1:-1].reshape(-1,2)
            assert np.allclose(pairs[:,0],pairs[:,1])
            assert np.all(np.diff(pairs[:,0]) >= -1e-10)
    print(f'CATALAN_HAUSDORFF_PASS exhaustive_ranks=2..6 QP={num_qp} dyck_vertices={num_dyck} exact_certificates_ranks=2..40')

if __name__=='__main__':
    check()

"""Finite cross-checks for uniform-volume covariance of K_{2,q} graphical zonotopes.

Requires numpy and scipy; independent vertex triangulation for q=2,3,4 and
Monte Carlo sampling of exact coordinate fibers for q=5,8,15.
"""
import itertools
import math
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull


def prediction(q):
    n = q + 2
    c = np.zeros((n, q))
    for j in range(q):
        c[0, j] = c[1, j] = 0.5
        c[2 + j, j] = -1
    d = np.zeros(n)
    d[0], d[1] = 1, -1
    a = (2*q-1)/(6*q)
    b = q*(q+1)/48
    return a*c@c.T+b*np.outer(d,d), q*2**(q-1)*math.sqrt(q+2)


def finite_hull_check(q):
    n=q+2
    edges = [(i, 2+j) for i in range(2) for j in range(q)]
    B=np.zeros((n,2*q))
    for i,(v,w) in enumerate(edges):
        B[v,i]=1
        B[w,i]=-1
    U=null_space(np.ones((1,n)))
    corners=np.array([B@np.array(z)/2 for z in itertools.product((-1.,1.), repeat=2*q)])
    verts=np.unique(np.round(corners@U, 10), axis=0)
    hull=ConvexHull(verts)
    D=n-1
    V=0.
    M=np.zeros((D,D))
    for simplex in hull.simplices:
        vs=verts[simplex]
        vol=abs(np.linalg.det(vs))/math.factorial(D)
        V+=vol
        M+=vol*(vs.T@vs+np.outer(vs.sum(axis=0),vs.sum(axis=0)))/((D+1)*(D+2))
    M/=V
    expected, expected_volume=prediction(q)
    eV=abs(V/expected_volume-1)
    eM=np.max(np.abs(M-U.T@expected@U))
    assert eV<1e-8, (q,eV)
    assert eM<1e-8, (q,eM)
    return len(verts),len(hull.simplices),eV,eM


def fiber_sample_check(q,draws=600000):
    rng=np.random.default_rng(7521+q)
    accepted=[]
    total=0
    while total<draws//3:
        t=rng.uniform(-1,1,(100000,q))
        width=(q-np.sum(np.abs(t),axis=1))
        mask=rng.uniform(size=100000)*q<=width
        take=t[mask]
        if take.size:
            accepted.append(take)
            total+=len(take)
    t=np.concatenate(accepted)[:draws//3]
    W=q-np.abs(t).sum(axis=1)
    s=(rng.random(len(t))-.5)*W
    exp_a=(2*q-1)/(6*q)
    exp_b=q*(q+1)/48
    ea=np.mean(t**2,axis=0)
    eb=np.mean(s**2)
    # Two-sigma sampling tolerances, deliberately loose finite diagnostics.
    assert np.max(np.abs(ea-exp_a))<0.012, (q,ea,exp_a)
    assert abs(eb-exp_b)<0.08, (q,eb,exp_b)
    assert np.max(np.abs(t.mean(axis=0)))<0.011
    return len(t),float(np.max(np.abs(ea-exp_a))),float(abs(eb-exp_b))


def main():
    for q in (2,3,4):
        print('hull',q,*finite_hull_check(q))
    for q in (5,8,15):
        print('fiber',q,*fiber_sample_check(q))
    print('K2Q_VOLUME_COVARIANCE_CHECKS_PASSED')

if __name__=='__main__':
    main()

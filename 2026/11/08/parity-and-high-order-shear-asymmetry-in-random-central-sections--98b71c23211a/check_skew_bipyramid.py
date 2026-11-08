#!/usr/bin/env python3
"""Independent numeric checks for section-count laws of vertex-aligned skew bipyramids.

Requires numpy and scipy. Deterministic seed, no network or external files.
"""
import math
from collections import Counter
import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull


def exact_law(n, lam):
    if n % 2 == 0:
        return {n + 2: 1.0}
    q = (n - 1)//2
    kappa = lam / math.hypot(1., lam)
    F = lambda t: math.asin(kappa * math.sin(t))
    ts = [(j+0.5)*math.pi/n for j in range(q+1)]
    H = F(ts[0]) + sum((-1)**j * (F(ts[j])-F(ts[j-1])) for j in range(1, q+1))
    diff = 2*(-1)**q * H / math.pi
    x = math.atan(lam)/math.pi
    return {n+1: x + diff/2, n+2: 1-2*x, n+3: x-diff/2}


def quadrature_law(n, lam):
    if n % 2 == 0:
        return {n+2: 1.0}
    q = (n-1)//2
    def f(t):
        return lam*math.cos(t)/math.sqrt(1+(lam*math.cos(t))**2)
    vals = {n+1:0., n+3:0.}
    for j in range(-q, q+1):
        prob = quad(f, (j-0.5)*math.pi/n, (j+0.5)*math.pi/n, epsabs=1e-13)[0]/math.pi
        vals[n+1 if (-1)**(q+j)>0 else n+3] += prob
    vals[n+2] = 1-vals[n+1]-vals[n+3]
    return vals


def sample_law(n, lam, sample_count=85000):
    # Crucially, keep the apices' lateral projection strictly INSIDE the base.
    s = 0.2
    h = s/lam
    phi = 2*math.pi*np.arange(n)/n
    vertices = np.array([[math.cos(x),math.sin(x),0] for x in phi] + [[s,0,h],[s,0,-h]])
    hull = ConvexHull(vertices)
    # Derive edges from the 3D convex hull, not the asserted bipyramid graph.
    edges = {tuple(sorted((int(i),int(j)))) for face in hull.simplices
             for i,j in ((face[0],face[1]),(face[1],face[2]),(face[2],face[0]))}
    assert len(edges) == 3*n
    rng = np.random.default_rng(1431 + n*9 + round(100*lam))
    normals = rng.standard_normal((sample_count,3))
    normals /= np.linalg.norm(normals,axis=1)[:,None]
    signs = normals @ vertices.T > 0
    counts = np.zeros(sample_count,dtype=np.int32)
    for i,j in edges:
        counts += signs[:,i] != signs[:,j]
    return {int(x):int(y) for x,y in zip(*np.unique(counts,return_counts=True))}


def main():
    for n in (3,4,5,6,7,9):
        for lam in (0.3,1.4,4.):
            a, b = exact_law(n,lam), quadrature_law(n,lam)
            assert a.keys() == b.keys()
            for k in a:
                assert abs(a[k]-b[k])<3e-13,(n,lam,k,a[k],b[k])
            samples = sample_law(n,lam)
            assert samples.keys()==a.keys(),(n,lam,samples,a)
            for k in a:
                observed = samples[k]/sum(samples.values())
                sigma = math.sqrt(a[k]*(1-a[k])/sum(samples.values()))
                assert abs(observed-a[k]) < 6*sigma+0.002,(n,lam,k,observed,a[k])
    # Check the normalization and high-order rare-event bias with high precision.
    import mpmath as mp
    mp.mp.dps=70
    for n in (3,5,7,9):
        q=(n-1)//2
        lam=mp.mpf('0.01')
        k=lam/mp.sqrt(1+lam*lam)
        F=lambda t:mp.asin(k*mp.sin(t))
        t=lambda j:mp.pi*(j+mp.mpf('0.5'))/n
        H=F(t(0))+sum((-1)**j*(F(t(j))-F(t(j-1))) for j in range(1,q+1))
        D=2*(-1)**q*H/mp.pi
        predicted=2*mp.binomial(2*q,q)*lam**n/(mp.pi*16**q)
        assert 0 < D and abs(D/predicted-1)<0.01,(n,D,predicted)
    print('SKEW_BIPYRAMID_FULL_LAW_OK 18 configurations x 85000 directions')
    print('SKEW_BIPYRAMID_QUADRATURE_OK')
    print('SKEW_BIPYRAMID_HIGH_ORDER_ASYMMETRY_OK n=3,5,7,9')

if __name__=='__main__':
    main()

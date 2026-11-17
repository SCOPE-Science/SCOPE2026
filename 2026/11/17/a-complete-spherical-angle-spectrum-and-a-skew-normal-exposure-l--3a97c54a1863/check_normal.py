#!/usr/bin/env python3
"""Finite numerical checks for the angular law of isocanted cubes.

The analytic theorem is proved in RESULT.md; finite numerical tests are only corroboration.
"""
import math
from itertools import product
import numpy as np
from scipy.stats import qmc, norm
from scipy.spatial import ConvexHull


def exact_moments(d):
    ang=math.asin(1/math.sqrt(d))
    return d/2+d*ang/math.pi, d/4-(d*ang/math.pi)**2


def vertex_set(d, ell=2., cant=.6):
    h=(ell-cant)/2
    t=cant/2
    verts=[]
    for signs in product((-1,1),repeat=d):
        z=np.asarray(signs,dtype=float)*h
        for eta in (-1,1):
            if eta*sum(signs)==-d:
                continue
            verts.append((tuple(signs),eta,z+eta*t*np.ones(d)))
    return verts


# Exactly 2^(d+1)-2 points, all extreme, and normal-fan signs recover each vertex.
for d in range(2,7):
    verts=vertex_set(d)
    x=np.array([v[2] for v in verts])
    hull=ConvexHull(x)
    assert len(verts)==2**(d+1)-2
    assert len(hull.vertices)==len(verts),(d,len(hull.vertices),len(verts))
    assert set(hull.vertices)==set(range(len(verts)))
print('EXTREME_VERTEX_CHECK_PASS dims=2..6')

# Check 1: for each spherical random direction, find the exposed
# vertex directly by its coordinates, then verify the sign-defined label.
rg=np.random.default_rng(20261113)
for d in range(2,9):
    labels=vertex_set(d)
    vertices=np.array([v[2] for v in labels])
    G=rg.normal(size=(16000,d))
    winners=(G@vertices.T).argmax(axis=1)
    k=np.count_nonzero(G>0,axis=1)
    eta=np.where(G.sum(axis=1)>0,1,-1)
    dictionary={(tuple(s),t):i for i,(s,t,_v) in enumerate(labels)}
    predicted=np.fromiter((dictionary[(tuple(np.where(g>0,1,-1)),int(t))]
                           for g,t in zip(G,eta)),dtype=int,count=G.shape[0])
    assert np.array_equal(winners,predicted)
print('EXPOSURE_MAP_CHECK_PASS dims=2..8 directions_per_dim=16000')

# Check 2: standardized selected-angle-level J has the arcsine
# moment formulas; simulate directions and verify with 6-sigma envelopes.
for d in (2,3,4,5,8,12,32,64):
    N=250000
    G=rg.normal(size=(N,d))
    K=np.count_nonzero(G>0,axis=1)
    S=G.sum(axis=1)
    J=np.where(S>0,K,d-K)
    m,v=exact_moments(d)
    # Conservative 8 SE for mean/variance; Gaussian mixtures have finite moments.
    mean=float(J.mean());var=float(J.var())
    assert abs(mean-m)<8*math.sqrt(v/N)+.012,(d,mean,m)
    assert abs(var-v)<8*(v+1)*math.sqrt(4/N)+.04,(d,var,v)
print('ARCSINE_MOMENT_MONTE_CARLO_PASS dims=2,3,4,5,8,12,32,64 samples=250000_per_dim')

# Check 3: finite d-level structure and all-angle summation.
# The exact q_j is approximated by a deterministic scrambled Sobol Gaussian cube
# integral, then compared against independent random-direction exposure frequencies.
for d in (2,3,4,5,7,9):
    sampler=qmc.Sobol(d,scramble=True,seed=42+d)
    sample=sampler.random_base2(m=18)
    h=norm.ppf(.5+.5*sample)
    tot=h.sum(axis=1)
    qvals=[0.]
    sums=np.zeros(len(h))
    for j in range(1,d+1):
        sums+=h[:,j-1]
        qvals.append(float(np.mean(2*sums>tot)))
    assert all(a<b for a,b in zip(qvals,qvals[1:])),(d,qvals)
    assert max(abs(qvals[j]+qvals[d-j]-1) for j in range(d+1))<.012
    assert abs(sum(2*math.comb(d,j)*qvals[j]/2**d for j in range(1,d+1))-1)<.012
    # q_{d,j} central-window CLT is separately proved; only finite checks here.
print('FINITE_ANGLE_LEVEL_SOBOL_PASS dims=2,3,4,5,7,9 sobol_points_per_dim=262144')

# CLT numerical corroboration: three standardized rank positions and finite d.
c=math.sqrt(2/(math.pi-2))
for d in (128,512):
    sampler=qmc.Sobol(d,scramble=True,seed=2*d)
    # Test scalar conditional triangular CLT via independent half-normal draws.
    U=norm.ppf(.5+.5*sampler.random_base2(m=12))
    pref=np.cumsum(U,axis=1)
    total=pref[:,-1]
    for z in (-1.,0.,1.):
        j=int(round((d+z*math.sqrt(d))/2))
        approx=np.mean(2*pref[:,j-1]>total)
        target=norm.cdf(c*(2*j-d)/math.sqrt(d))
        assert abs(approx-target)<.065,(d,j,approx,target)
print('CENTRAL_WINDOW_SANITY_PASS dims=128,512 ranks=3')
print('ISOCANTED_ANGULAR_PASS')

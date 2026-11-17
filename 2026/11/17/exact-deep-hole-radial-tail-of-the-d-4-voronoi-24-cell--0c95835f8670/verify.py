#!/usr/bin/env python3
"""Reproducible computational checks for the D4 Voronoi deep-hole tail formula."""
from fractions import Fraction as F
from math import comb, factorial, sqrt
import itertools
import numpy as np
from numpy.polynomial.legendre import leggauss

def cube_A_moment(m):
    out=F(0)
    for j0 in range(m+1):
      for j1 in range(m-j0+1):
       for j2 in range(m-j0-j1+1):
        j3=m-j0-j1-j2
        out+=F(factorial(m),factorial(j0)*factorial(j1)*factorial(j2)*factorial(j3)*(2*j1+1)*(2*j2+1)*(2*j3+1))
    return out

def ccoef(m):
    # coeff in P / ((3/2)*eps**4)
    return F(4*comb(2*m+4,m), (2*m+4)*4**m)*cube_A_moment(m)

assert [ccoef(k) for k in range(4)]==[F(1), F(2), F(56,15), F(152,21)]

def tail_integral(eps,n=24):
    nodes,w=leggauss(n)
    a=1+nodes[:,None,None]**2 + nodes[None,:,None]**2 + nodes[None,None,:]**2
    t=eps/(1+np.sqrt(1-a*eps))
    return 3*np.einsum('i,j,k,ijk->',w,w,w,t**4)

# Orthogonal triality transformation preserves the 24 vertices.
verts=[]
for i in range(4):
 for s in [-1,1]:
  v=[0.0]*4;v[i]=float(s);verts.append(tuple(v))
for signs in itertools.product([-0.5,0.5],repeat=4):verts.append(signs)
assert len(set(verts))==24
H=np.array([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
assert np.array_equal(H@H.T,np.eye(4))
for v in verts: assert tuple(H@np.array(v)) in verts
for v,w in itertools.combinations(verts,2):assert sum(x*y for x,y in zip(v,w))<=.5+1e-12

rng=np.random.default_rng(271828)
n=1200000
# uniform sampling of Voronoi P, by half-volume central cubes and spikes
mask=rng.random(n)<.5
coords=rng.random((n,4))*.5
spike_idx=np.flatnonzero(~mask)
k=len(spike_idx)
t=.5*rng.random(k)**.25
coords[spike_idx,:]=rng.random((k,4))*t[:,None]
chosen=rng.integers(0,4,size=k)
coords[spike_idx,chosen]=1-t
norm2=(coords**2).sum(axis=1)
for i in range(4):
 for j in range(i+1,4):assert np.max(coords[:,i]+coords[:,j])<=1+1e-12
assert np.max(norm2)<=1+1e-12
print('series coefficients:',[str(ccoef(j)) for j in range(4)])
for e in [.12,.17,.20,.24]:
    exact=tail_integral(e)
    observed=np.mean(norm2>1-e)
    stdev=np.sqrt(exact*(1-exact)/n)
    assert abs(exact-observed)<6*stdev+1e-5,(e,exact,observed,stdev)
    first=1.5*e**4 +3*e**5 +5.6*e**6 +(76/7)*e**7
    print(f'eps={e:.2f}: exact integral {exact:.11f}; sampling {observed:.11f}; truncated expansion {first:.11f}; SE {stdev:.8f}')
# area of the central [0,.5]^4 cube plus four spikes (positive orthant)
assert F(1,16)+4*F(1,64)==F(1,8)
assert 16*F(1,8)==2
print('all checks PASSED')

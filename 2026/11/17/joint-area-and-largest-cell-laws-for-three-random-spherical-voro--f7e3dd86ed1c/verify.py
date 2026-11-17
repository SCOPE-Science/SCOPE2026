"""Independent numerical checks for a three-site spherical Voronoi area-vector theorem.

Run: python verify.py. Dependencies: NumPy, SciPy.
The checks are finite diagnostics, not a proof of the exact identities.
"""
import numpy as np
from scipy.integrate import dblquad, quad

PI = np.pi
rng = np.random.default_rng(20261111)

def area_max_cdf(m):
    if m <= 4*PI/3: return 0.0
    if m >= 2*PI: return 1.0
    return ((1.5*m-2*PI)*np.cos(m) - (np.sin(2*m)+np.sin(m))/2)/PI

def angle_pdf(a,b):
    return 8/(3*PI)*np.sin(a)*np.sin(b)*np.sin(a+b)

normalization, _ = dblquad(lambda b,a: angle_pdf(a,b),0,PI,lambda a:0,lambda a:PI-a,epsabs=1e-10)
assert abs(normalization-1) < 1e-9, normalization
mean, _ = quad(lambda m: 1-area_max_cdf(m),4*PI/3,2*PI,epsabs=1e-10)
assert abs(4*PI/3+mean -(2*PI-27/(8*PI)))<1e-10

# The independent sampling step uses normalized Gaussian directions; the area
# calculation uses physical Euclidean angles rather than the sine-product law.
n = 350_000
p = rng.normal(size=(n,3,3))
p /= np.linalg.norm(p,axis=-1,keepdims=True)
angle = np.empty((n,3))
for i in range(3):
    u = p[:,(i+1)%3,:]-p[:,i,:]
    v = p[:,(i+2)%3,:]-p[:,i,:]
    z = np.einsum('ij,ij->i',u,v)/(np.linalg.norm(u,axis=1)*np.linalg.norm(v,axis=1))
    angle[:,i] = np.arccos(np.clip(z,-1,1))
assert np.max(np.abs(angle.sum(axis=1)-PI))<1e-7
areas = 2*(PI-angle)
assert np.max(np.abs(areas.sum(axis=1)-4*PI)) <1e-7
mx=areas.max(axis=1)
for m in [1.4*PI,1.5*PI,1.65*PI,1.8*PI]:
    obs=np.mean(mx<=m); exp=area_max_cdf(m)
    assert abs(obs-exp)<0.006, (m,obs,exp)
assert abs(mx.mean() - (2*PI-27/(8*PI)))<0.012
assert abs(np.mean(np.max(angle,axis=1)<PI/2)-0.5)<0.006

# Two-dimensional test of density in an interior rectangle.
a0,a1=0.3,0.9
b0,b1=0.4,1.1
expected, _=dblquad(lambda b,a:angle_pdf(a,b),a0,a1,lambda a:b0,lambda a:b1,epsabs=1e-10)
observed=np.mean((angle[:,0]>a0)&(angle[:,0]<a1)&(angle[:,1]>b0)&(angle[:,1]<b1))
assert abs(observed-expected)<0.004, (observed,expected)

# Direct membership integration of lune areas without angle formula.
for k in range(6):
    xyz=rng.normal(size=(85000,3)); xyz /= np.linalg.norm(xyz,axis=1,keepdims=True)
    sites=p[k]
    dot=xyz@sites.T
    empirical=4*PI*np.bincount(np.argmax(dot,axis=1),minlength=3)/len(xyz)
    assert np.max(np.abs(empirical-areas[k]))<0.085, (k,empirical,areas[k])
print('THREE_SITE_JOINT_AREA_CHECKS_OK', n, 'mean',float(mx.mean()), 'rectangle_probability',float(observed))

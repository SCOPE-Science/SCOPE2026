"""Standalone checks for local angular-anisotropy laws of three-dimensional unit zonotopes.

Requires numpy and scipy. These are finite checks, not proofs of infinite-dimensional claims.
"""
import math
import numpy as np
from scipy.special import eval_legendre, roots_legendre

rng = np.random.default_rng(731909)
P2 = lambda z: (3.0 * z*z - 1.0)/2.0
mu = math.pi/8
A1 = math.pi/64

def a(m):
    return (math.pi/4) * math.exp(2*math.lgamma(2*m+1)-4*math.lgamma(m+1)-m*math.log(16)) / ((2*m-1)*(2*m+2))

def unit_draw(n, eps=0):
    if eps == 0:
        x = rng.normal(size=(n,3))
        return x / np.linalg.norm(x,axis=1)[:,None]
    out=[]
    while sum(len(arr) for arr in out) < n:
        k = int((n-sum(len(arr) for arr in out))*2.2)+10
        xyz = rng.normal(size=(k,3)); xyz /= np.linalg.norm(xyz,axis=1)[:,None]
        # 1 + eps P2(z) is between 0 and 1+max(eps,-eps/2) for eps in [-1,2]
        bound=1+max(eps,-eps/2)
        accepted=xyz[rng.uniform(size=k)*bound <= (1+eps*P2(xyz[:,2]))]
        out.append(accepted)
    return np.concatenate(out,axis=0)[:n]

# Verified polynomial eigenfunctions: Legendre eigenvalues on S^2.
t,wt = roots_legendre(320)
for m in range(1,13):
    value=np.sum(wt*np.sqrt(1-t*t)*eval_legendre(2*m,t))/4
    assert abs(value+a(m)) < 8e-9,(m,value,a(m))
for ell in range(1,12,2):
    value=np.sum(wt*np.sqrt(1-t*t)*eval_legendre(ell,t))/4
    assert abs(value)<3e-14
assert abs(a(1)-A1)<1e-15
assert abs(sum((4*m+1)*a(m) for m in range(1,5000)) -mu)<6e-5
assert abs(sum((4*m+1)*a(m)**2 for m in range(1,100)) -(1/6-math.pi**2/64))<1e-10

# Check the degree-two conditional operator T_g on polar/equatorial test points.
q,wq=roots_legendre(160)
phi=np.arange(320)*2*math.pi/320
for z in [1., 0.75, 0.22, 0., -0.8]:
    u=np.array([math.sqrt(max(0,1-z*z)),0,z])
    cosuv=u[0]*np.sqrt(1-q[:,None]**2)*np.cos(phi[None,:])+u[2]*q[:,None]
    kval=0.5*np.sqrt(np.maximum(0,1-cosuv**2))-mu
    # normalized sphere integral: d sigma = dq dphi/(4pi)
    integ=np.sum((wq[:,None]/2)*(1/320)*kval*P2(q[:,None]))
    assert abs(integ + A1*P2(z))<1e-5,(z,integ,-A1*P2(z))

# Sampling-density moment and finite sample volume on 3 vectors.
for eps in [-0.7,-0.2,0,0.2,0.7]:
    x=unit_draw(65000,eps)
    assert abs(np.mean(P2(x[:,2]))-eps/5)<0.008,(eps,np.mean(P2(x[:,2])))
for n in [3,4,5,6]:
    x=unit_draw(n,0.3)
    geom=0.
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                geom+=abs(np.linalg.det(np.stack((x[i],x[j],x[k]))))
    # Directly compare triple volumes with scalar triple-products.
    fast=sum(abs(np.dot(x[i],np.cross(x[j],x[k]))) for i in range(n) for j in range(i+1,n) for k in range(j+1,n))
    assert abs(geom-fast)<1e-12

# Sharp critical and supercritical variance and support constants.
base=1/12 - math.pi**2/128
assert base>0
for c in [-5,-2,0,3,7]:
    var=base + (A1**2*c*c/5)
    assert var>=base
    upper=math.pi/16 + A1*c*c/10
    assert upper>=math.pi/16
    nc=c*c/5
    means=np.array([rng.noncentral_chisquare(5,nc) for _ in range(2500)])
    assert abs(np.mean(means)-(5+nc))<0.7
assert abs(A1**2/5-math.pi**2/20480)<1e-16
print('ALL_ANGULAR_ANISOTROPY_ZONOTOPE_CHECKS_PASSED')

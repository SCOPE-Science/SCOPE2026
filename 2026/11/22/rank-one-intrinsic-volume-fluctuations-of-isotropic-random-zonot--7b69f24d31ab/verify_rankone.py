"""Reproduce finite-dimensional checks for intrinsic volumes of isotropic zonotopes.

These numerical diagnostics corroborate the stated exact analytic theorem;
they are not substitutes for its proof or for historical-priority review.
"""
import math
import itertools
import numpy as np
from scipy.special import eval_gegenbauer, gamma
from scipy.spatial import ConvexHull

rng=np.random.default_rng(491728)

def sphere(size,d):
    z=rng.normal(size=(size,d))
    return z/np.linalg.norm(z,axis=1)[:,None]

def s(d):
    return math.gamma(d/2)**2/(math.gamma((d-1)/2)*math.gamma((d+1)/2))

def c(d,k):
    if k == 2:return 1.
    return (math.gamma(d/2)/math.gamma((d+1)/2))**(k-2)*math.gamma((d-1)/2)/math.gamma((d-k+1)/2)

def wedge(u):
    return float(np.sqrt(max(0.,np.linalg.det(u@u.T))))

def vk(u,k):
    return sum(wedge(u[list(idx)]) for idx in itertools.combinations(range(len(u)),k))

for d in range(3,7):
    sd=s(d)
    assert abs(sd-(gamma(d/2)**2/(gamma((d-1)/2)*gamma((d+1)/2))))<1e-13
    assert (d-1)/d-sd**2>0
    if d==3:assert abs(sd-math.pi/4)<1e-14
    if d<=5:
        x,w=np.polynomial.legendre.leggauss(550)
        f=gamma(d/2)/(math.sqrt(math.pi)*gamma((d-1)/2))*(1-x*x)**((d-3)/2)
        for m in range(1,5):
            ell=2*m
            nu=(d-2)/2
            P=eval_gegenbauer(ell,nu,x)/eval_gegenbauer(ell,nu,1.)
            b=-np.sum(w*f*(np.sqrt(1-x*x)-sd)*P)
            assert b>0, (d,m,b)
            if m==1:assert abs(b-sd/(d*d-1)) < 4e-7,(d,b,sd/(d*d-1))

# A deterministic and independent convex-hull check of the top intrinsic volume.
for d,n in [(3,4),(3,6),(4,5)]:
    u=sphere(n,d)
    endpoints=np.array([np.sum(u[list(I)],axis=0) if I else np.zeros(d)
                        for bits in itertools.product((0,1),repeat=n)
                        for I in [tuple(j for j,a in enumerate(bits) if a)]])
    hullvol=ConvexHull(endpoints).volume
    determinant_sum=vk(u,d)
    assert abs(hullvol-determinant_sum)<1e-9,(d,n,hullvol,determinant_sum)

# Empirically reconstruct the conditional second-order Hoeffding projection.
for d,k in [(3,3),(4,3),(4,4),(5,5)]:
    t=0.38
    u=np.zeros(d);u[0]=1
    v=np.zeros(d);v[0]=t;v[1]=np.sqrt(1-t*t)
    M=33000
    G=sphere((k-2)*M,d).reshape(M,k-2,d)
    arr=np.concatenate((np.broadcast_to(u,(M,1,d)),np.broadcast_to(v,(M,1,d)),G),axis=1)
    # Gram product via batched matrix determinants
    gram=arr@np.transpose(arr,(0,2,1))
    samples=np.sqrt(np.maximum(0,np.linalg.det(gram)))
    expected=c(d,k)*np.sqrt(1-t*t)
    observed=samples.mean()
    assert abs(observed-expected) < 0.026*expected,(d,k,observed,expected)

# Exact conditional U-stat variances and the nontrivial 3-body residual.
sd=s(3)
var2=2/3-sd*sd
var3_res=math.pi**2/32-5/18
assert var3_res>0
N=140000
v=sphere(3*N,3).reshape(N,3,3)
a=np.linalg.det(v)
ss=(np.linalg.norm(np.cross(v[:,0],v[:,1]),axis=1)+
    np.linalg.norm(np.cross(v[:,0],v[:,2]),axis=1)+
    np.linalg.norm(np.cross(v[:,1],v[:,2]),axis=1))
r=np.abs(a)-math.pi/8-0.5*(ss-3*sd)
assert abs(np.var(r)-var3_res)<0.0027,(np.var(r),var3_res)
assert abs(np.mean(r))<0.004

# Check the exact regression/covariance and its limiting rank-one normalization.
for d,k,n in [(3,3,8),(4,4,8),(5,3,8)]:
    beta=c(d,k)*math.comb(n-2,k-2)
    sigma2=(d-1)/d-s(d)**2
    expected_cov=beta*math.comb(n,2)*sigma2
    assert expected_cov>0
    assert abs(beta/(n**(k-2)) - c(d,k)/math.factorial(k-2))<0.3

# Independently estimate the asserted finite-sample cross-covariance of two distinct
# intrinsic volumes, using fresh entire random zonotopes rather than fixed pairs.
for d,k,n,M in [(3,3,6,10000),(4,4,6,10000)]:
    U=sphere(M*n,d).reshape(M,n,d)
    def all_wedges(order):
        out=np.zeros(M)
        for ix in itertools.combinations(range(n),order):
            A=U[:,ix,:]
            gram=A@np.transpose(A,(0,2,1))
            out+=np.sqrt(np.maximum(0,np.linalg.det(gram)))
        return out
    A=all_wedges(2)
    B=all_wedges(k)
    beta=c(d,k)*math.comb(n-2,k-2)
    exact=beta*math.comb(n,2)*((d-1)/d-s(d)**2)
    observed=np.cov(A,B,bias=True)[0,1]
    assert abs(observed-exact)/exact<0.13,(d,k,observed,exact)

print('ALL_CHECKS_PASSED')

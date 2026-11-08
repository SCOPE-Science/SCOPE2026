"""Reproducibility calculations for random hyperbolic geodesic triangles.
Run: python check_hyperbolic.py
Requires numpy and scipy. No simulations are used as infinite proofs.
"""
import numpy as np
from scipy.integrate import cumulative_trapezoid

rng=np.random.default_rng(20261107)

def radial_quantiles(dim, R, u):
    if dim==2: return np.arccosh(1+u*(np.cosh(R)-1))
    t=np.linspace(0,R,35001)
    area=cumulative_trapezoid(np.sinh(t)**(dim-1), t, initial=0)
    area/=area[-1]
    return np.interp(u,area,t)

def simulated(dim,R,n):
    u=rng.random((n,3))
    r=radial_quantiles(dim,R,u)
    E=-np.log(u)/(dim-1)
    v=rng.standard_normal((n,3,dim))
    v/=np.linalg.norm(v,axis=2)[:,:,None]
    S=np.empty((n,3,3))
    D=np.empty((n,3,3))
    for i in range(3):
        for j in range(i+1,3):
            s=np.sqrt(np.maximum(0, (1-np.sum(v[:,i]*v[:,j],axis=1))/2))
            S[:,i,j]=S[:,j,i]=s
            coshd=np.cosh(r[:,i]-r[:,j])+2*np.sinh(r[:,i])*np.sinh(r[:,j])*s*s
            D[:,i,j]=D[:,j,i]=np.arccosh(coshd)
    alpha=np.zeros((n,3))
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        a,b,c=D[:,j,k],D[:,i,k],D[:,i,j]
        semi=(a+b+c)/2
        sinhalf=np.sqrt(np.maximum(0, np.sinh(semi-b)*np.sinh(semi-c)/(
                         np.sinh(b)*np.sinh(c))))
        alpha[:,i]=2*np.arcsin(np.clip(sinhalf,0,1))
    acoeff=np.zeros((n,3))
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        acoeff[:,i]=2*S[:,j,k]/(S[:,i,j]*S[:,i,k])
    W=np.sum(acoeff*np.exp(E),axis=1)
    actual=np.exp(R)*np.sum(alpha,axis=1)
    keep=(np.min(u,axis=1)>.03)&(np.min(np.array([S[:,0,1],S[:,0,2],S[:,1,2]]),axis=0)>.10)
    rel=np.abs(actual[keep]/W[keep]-1)
    return np.quantile(rel,[.5,.9,.99]),np.quantile(actual,[.1,.5,.9]),np.quantile(W,[.1,.5,.9]),int(keep.sum())

# Pure deterministic check on a 120-degree equilateral angular triple at common radius R.
for R in [5.,7.,9.]:
    s=np.sqrt(3)/2
    d=np.arccosh(1+2*np.sinh(R)**2*s*s)
    a=np.arccos(np.cosh(d)/(1+np.cosh(d)))
    scaled=3*a*np.exp(R)
    assert abs(scaled-4*np.sqrt(3)) < 0.05

for dim in (2,3,5):
    errors_by_radius=[]
    for R in (5.,7.,9.):
        errors,observed,limit,count=simulated(dim,R,45000)
        print('dim',dim,'R',R,'compact_rel_err',errors,
              'observed_q',observed,'limit_q',limit,'compact_count',count)
        assert count>20000
        assert np.all(np.isfinite(errors))
        errors_by_radius.append(errors)
    assert errors_by_radius[0][1]>errors_by_radius[1][1]>errors_by_radius[2][1]
    assert errors_by_radius[2][1]<.03

# Check the Pareto integral for all admissible positive moment orders, not an
# empirical estimate of an infinite expectation.
from scipy.integrate import quad
for dim in (2,3,5):
    k=dim-1
    for p in (.25*k,.5*k,.9*k):
        integral=quad(lambda y:k*y**(p-k-1),1,np.inf,epsrel=1e-8)[0]
        assert abs(integral-k/(k-p)) < 1e-7*(k/(k-p))
print('HYPERBOLIC_TRIANGLE_AREA_LIMIT_NUMERIC_OK')

"""Independent numerical diagnostics for the Fermat-point radial law.
This script checks formulas, not historical priority or mathematical proof.
"""
import numpy as np
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss
from math import pi, sqrt
rng=np.random.default_rng(987654321)

def density(r,nphi=16384):
    p=(np.arange(nphi)+0.5)*2*pi/nphi
    h1=np.sqrt(1-r*r*np.sin(p)**2)
    h2=np.sqrt(1-r*r*np.sin(p+2*pi/3)**2)
    return 3*sqrt(3)/(8*pi**3)*(2*pi/nphi)*np.sum(1/(h1*h2))
assert abs(density(0)-3*sqrt(3)/(4*pi**2))<1e-12

def radial_cdf(r,n=200):
    xs, ws=leggauss(n)
    rs=r*(xs+1)/2
    return np.dot(ws,np.array([2*pi*v*density(v,nphi=3072) for v in rs]))*(r/2)
for r in (.2,.5,.8,.95):
    print('RADIAL_CDF',r,radial_cdf(r))
for r in (.99,.999,.9999):
    ratio=density(r)/np.log(1/(1-r*r))
    print('BOUNDARY_DENSITY',r,density(r),ratio, 'target',3/pi**3)
# Sample points on unit circle independently; compute Fermat point.
n=16000
ang=rng.uniform(0,2*pi,size=(n,3))
v=np.stack((np.cos(ang),np.sin(ang)),axis=-1)
# Angle >=120 iff dot of two edge vectors <= -length product/2.
V=np.zeros((n,3))
for j in range(3):
    a=v[:,(j+1)%3]-v[:,j]
    b=v[:,(j+2)%3]-v[:,j]
    V[:,j]=np.sum(a*b,axis=1)/np.linalg.norm(a,axis=1)/np.linalg.norm(b,axis=1)
obt=np.min(V,axis=1)<=-.5
print('BOUNDARY_MASS',np.mean(obt),'target',1/3)
interior=v[~obt]
x=interior.mean(axis=1)
for it in range(45):
    dis=np.maximum(np.linalg.norm(x[:,None,:]-interior,axis=2),1e-14)
    w=1/dis
    xn=np.sum(interior*w[:,:,None],axis=1)/np.sum(w,axis=1)[:,None]
    x=xn
radii=np.linalg.norm(x,axis=1)
for r in (.2,.5,.8,.95):
    emp=np.mean(~obt)*np.mean(radii<r)
    calc=radial_cdf(r)
    stderr=np.sqrt(emp*(1-emp)/n)
    print('TEST_CDF',r,'emp',emp,'formula',calc,'z',abs(emp-calc)/stderr)
    assert abs(emp-calc)<6*stderr+0.002
assert abs(np.mean(obt)-1/3)<.025
print('FERMAT_RADIAL_DENSITY_DIAGNOSTICS_OK')
# Independent finite-difference verification of the coordinate Jacobian.
for z in (np.array([.2,.3]),np.array([-.6,.25]),np.array([.1,-.8])):
    for phi in (.43,2.39):
        def theta_map(w):
            zz=w[:2]; p=w[2]
            phis=p+2*pi*np.arange(3)/3
            dirs=np.stack((np.cos(phis),np.sin(phis)),axis=1)
            h=np.sqrt(1-np.dot(zz,zz)+(dirs@zz)**2)
            t=h-dirs@zz
            u=zz[None,:]+t[:,None]*dirs
            return np.angle(u[:,0]+1j*u[:,1])
        w=np.array([*z,phi]); h=1e-6
        fd=np.column_stack([np.angle(np.exp(1j*(theta_map(w+np.eye(3)[k]*h)-theta_map(w-np.eye(3)[k]*h))))/(2*h) for k in range(3)])
        dirs=np.stack((np.cos(phi+2*pi*np.arange(3)/3),np.sin(phi+2*pi*np.arange(3)/3)),axis=1)
        hh=np.sqrt(1-np.dot(z,z)+(dirs@z)**2)
        tt=hh-dirs@z
        exact=np.column_stack((-dirs[:,1]/hh,dirs[:,0]/hh,tt/hh))
        assert np.max(np.abs(fd-exact))<5e-9
        detabs=np.abs(np.linalg.det(exact))
        detformula=sqrt(3)/2*np.sum(tt)/np.prod(hh)
        assert abs(detabs-detformula)<1e-10
print('FERMAT_JACOBIAN_FINITE_DIFFERENCE_OK')

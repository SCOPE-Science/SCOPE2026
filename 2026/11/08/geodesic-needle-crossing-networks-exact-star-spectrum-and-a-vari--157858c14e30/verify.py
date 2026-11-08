"""Independent numerical checks for spherical geodesic arc crossings.

Usage: python verify.py. Requires NumPy. Analytic proof is in RESULT.md;
Monte Carlo provides independent corroboration only.
"""
import math
from math import pi
import numpy as np


def random_sphere(rng, shape):
    a=rng.normal(size=(*shape,3))
    return a/np.linalg.norm(a,axis=-1,keepdims=True)


def arcs(rng, repetitions, n, fixed=False):
    m=random_sphere(rng,(repetitions,n))
    t=random_sphere(rng,(repetitions,n))
    t=t-(t*m).sum(-1,keepdims=True)*m
    t=t/np.linalg.norm(t,axis=-1,keepdims=True)
    if fixed:
        length=np.full((repetitions,n),pi/2)
    else:
        # For independent area-uniform endpoints on S^2, cos(length) is uniform.
        length=np.arccos(rng.uniform(-1,1,size=(repetitions,n)))
    a=np.cos(length[...,None]/2)*m-np.sin(length[...,None]/2)*t
    b=np.cos(length[...,None]/2)*m+np.sin(length[...,None]/2)*t
    normal=np.cross(a,b);normal/=np.linalg.norm(normal,axis=-1,keepdims=True)
    return a,b,normal,length


def is_on_arc(a,b,q,length):
    d1=np.arccos(np.clip((a*q).sum(-1),-1,1))
    d2=np.arccos(np.clip((b*q).sum(-1),-1,1))
    return np.abs(d1+d2-length)<1e-6


def crossing_matrix(a,b,normal,length):
    repetitions,n,_=a.shape
    degrees=np.zeros((repetitions,n),dtype=int)
    total=np.zeros(repetitions,dtype=int)
    for i in range(n):
        for j in range(i+1,n):
            q=np.cross(normal[:,i],normal[:,j])
            q/=np.linalg.norm(q,axis=-1,keepdims=True)
            present=(is_on_arc(a[:,i],b[:,i],q,length[:,i])&
                     is_on_arc(a[:,j],b[:,j],q,length[:,j])) | (is_on_arc(a[:,i],b[:,i],-q,length[:,i])&
                     is_on_arc(a[:,j],b[:,j],-q,length[:,j]))
            total+=present;degrees[:,i]+=present;degrees[:,j]+=present
    return degrees,total


def main():
    rng=np.random.default_rng(2026110701)
    n=10
    trials=20000
    p=1/8
    gamma=(pi*pi-8)/(64*pi*pi)
    for fixed in (False,True):
        a,b,normal,length=arcs(rng,trials,n,fixed)
        degree,crossings=crossing_matrix(a,b,normal,length)
        mu=n*(n-1)*p/2
        vv=n*(n-1)*p*(1-p)/2
        if not fixed:
            vv+=n*(n-1)*(n-2)*gamma
        measured_mean=float(np.mean(crossings))
        measured_var=float(np.var(crossings))
        print('fixed',fixed,'mean',measured_mean,'theory_mean',mu,'variance',measured_var,'theory_variance',vv)
        assert abs(measured_mean-mu)<0.15
        assert abs(measured_var-vv)<0.65
        # Degree conditional on length: g(l)=l/(4*pi) for uniform endpoints;
        # at length pi/2 for fixed arcs it is exactly 1/8.
        g=length[:,0]/(4*pi) if not fixed else np.full(trials,p)
        mean_sq=np.mean((degree[:,0]-(n-1)*g)**2)
        predicted=np.mean((n-1)*g*(1-g))
        print('conditional_degree_squared_error',mean_sq,'binomial_prediction',predicted)
        assert abs(mean_sq-predicted)<0.1
    # Explicit moment recurrence and sine-law normalization checks.
    I=[2,pi]
    for r in range(2,16):
        I.append(pi**r-r*(r-1)*I[r-2])
    assert abs(I[1]/(2*4*pi)-1/8)<1e-14
    assert abs(I[2]/(2*(4*pi)**2)-(p*p+gamma))<1e-14
    from numpy.polynomial.legendre import leggauss
    x,w=leggauss(160)
    z=(x+1)/8
    mass=np.sum(w*2*pi*np.sin(4*pi*z))/8
    assert abs(mass-1)<1e-12
    print('SPHERICAL_GEODESIC_NEEDLE_CROSSING_NETWORK_OK',trials,n)

if __name__=='__main__':main()

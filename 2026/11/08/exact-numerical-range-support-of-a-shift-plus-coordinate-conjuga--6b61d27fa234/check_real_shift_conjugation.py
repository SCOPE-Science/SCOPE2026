#!/usr/bin/env python3
"""Finite-dimensional diagnostics for the numerical-range support of S+aC."""
import math
import numpy as np

def predicted(alpha,theta):
    c=abs(math.cos(theta)); s=abs(math.sin(theta))
    if s*s<=alpha*c:
        return alpha+c
    return math.sqrt(alpha*alpha+s*s)/s

def finite_support(alpha,theta,n):
    # x=u+i*v; <(S+alpha*C)x,x> is linear in first variable.
    R=np.zeros((2*n,2*n))
    c,s=math.cos(theta),math.sin(theta)
    R[:n,:n]+=alpha*c*np.eye(n)
    R[n:,n:]-=alpha*c*np.eye(n)
    R[:n,n:]-=alpha*s*np.eye(n)
    R[n:,:n]-=alpha*s*np.eye(n)
    for j in range(n-1):
        R[j,j+1]+=c/2; R[j+1,j]+=c/2
        R[n+j,n+j+1]+=c/2; R[n+j+1,n+j]+=c/2
        # Im<Sx,x>= sum(v_j u_{j+1}-u_j v_{j+1})
        R[n+j,j+1]+=s/2; R[j+1,n+j]+=s/2
        R[j,n+j+1]-=s/2; R[n+j+1,j]-=s/2
    return np.linalg.eigvalsh(R)[-1]

def direct(alpha,theta,x):
    z=np.vdot(x[1:],x[:-1])+alpha*np.sum(np.conj(x)**2)
    return (np.exp(-1j*theta)*z).real

def run():
    rng=np.random.default_rng(401224)
    N=0
    for alpha in [0.07,0.3,0.9,1.7,3.5]:
        for theta in [0.0,0.13,0.7,1.12,math.pi/2,2.14,math.pi]:
            n=48
            z=finite_support(alpha,theta,n)
            h=predicted(alpha,theta)
            assert z <=h+1e-10,(alpha,theta,z,h)
            # Large blocks approximate support, but a few approach it slowly.
            assert h-z<0.045,(alpha,theta,z,h)
            N+=2
    for n in [2,3,5,9]:
        for _ in range(80):
            alpha=rng.uniform(0,2)
            theta=rng.uniform(-math.pi,math.pi)
            x=rng.normal(size=n)+1j*rng.normal(size=n)
            x=x/np.linalg.norm(x)
            z=direct(alpha,theta,x)
            # Test the real matrix representation by reconstructing quadratic form.
            c,s=math.cos(theta),math.sin(theta)
            u=x.real;v=x.imag
            z2=alpha*c*(u@u-v@v)-2*alpha*s*(u@v)
            z2+=c*(u[1:]@u[:-1]+v[1:]@v[:-1])
            z2+=s*(v[:-1]@u[1:]-u[:-1]@v[1:])
            assert abs(z-z2)<1e-10,(z,z2)
            N+=1
    print('PASS:',N,'support/realification diagnostics')
if __name__=='__main__':run()

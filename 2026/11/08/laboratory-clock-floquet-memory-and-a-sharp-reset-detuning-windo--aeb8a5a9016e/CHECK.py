#!/usr/bin/env python3
"""Finite diagnostics for the lab-clock, Poisson-reset, Floquet localization result.
Run: python CHECK.py. Requires NumPy and SciPy. Analytical proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import jv, jn_zeros, roots_laguerre

Z0=float(jn_zeros(0,1)[0]); N=38
NONS=np.concatenate((np.arange(-N,0),np.arange(1,N+1)))

def q(t,z):
    t=np.asarray(t)
    return np.sum((jv(NONS,z)/(1j*NONS))[:,None]
                  *(np.exp(1j*NONS[:,None]*np.ravel(t)[None,:])-1),axis=0).reshape(t.shape)

def constants(z):
    c=-np.sum(jv(NONS,z)/(1j*NONS))
    V=np.sum(np.abs(jv(NONS,z)/(1j*NONS))**2)
    return c,V

def exact_m2(rho,z,theta,grid=2500):
    """Exact age average, after conditional geometric block integration (omega=Delta=1)."""
    psi=np.linspace(0,2*math.pi,grid+1)
    p=math.exp(-2*math.pi*rho)
    em=p/(1-p); em2=p*(1+p)/(1-p)**2
    B=q(theta,z)-q(theta-psi,z)
    b0=float(jv(0,z))
    expr=(b0*b0)*((2*math.pi)**2*em2+4*math.pi*em*psi+psi**2)
    expr+=2*b0*(2*math.pi*em+psi)*B.real+np.abs(B)**2
    density=rho*np.exp(-rho*psi)/(1-p)
    return float(np.trapezoid(expr*density,psi)/2)

def direct_m2(rho,z,theta,grid=50001):
    """Direct renewal-age integral with exponentially small truncation error."""
    x=np.linspace(0,25,grid)
    B=(jv(0,z)*x/rho)+q(theta,z)-q(theta-x/rho,z)
    return float(np.trapezoid(np.exp(-x)*np.abs(B)**2,x)/2)

def asymptotic_m2(xi,theta):
    c,V=constants(Z0)
    v=-float(jv(1,Z0))*xi
    A=q(theta,Z0)-c
    return float((2*v*v+2*v*A.real+abs(A)**2+V)/2)

def limit_probability(xi,theta,n):
    lag,w=roots_laguerre(120)
    ang=np.arange(512)*2*math.pi/512
    amplitudes=((-jv(1,Z0)*xi*lag)[:,None]
                +q(theta,Z0)-q(ang,Z0)[None,:])
    probs=jv(n,np.abs(amplitudes))**2
    return float(np.sum(w[:,None]*probs)/len(ang))

def exact_probability(rho,xi,theta,n,grid=40001):
    z=Z0+xi*rho
    x=np.linspace(0,25,grid)
    amplitudes=(jv(0,z)*x/rho+q(theta,z)-q(theta-x/rho,z))
    return float(np.trapezoid(np.exp(-x)*jv(n,np.abs(amplitudes))**2,x))

count=0

def check(cond,msg):
    global count
    if not cond: raise AssertionError(msg)
    count+=1

if __name__=='__main__':
    check(abs(jv(0,Z0))<1e-14,'root')
    check(abs(jv(1,Z0))>.5,'root simple')
    for z in [0.,0.6,Z0,3.1]:
        c,V=constants(z)
        check(abs(c.real)<1e-13,'mean real')
        check(V>=0,'Fourier variance')
        for theta in [0.,.4,math.pi/2,2.,math.pi,5.,2*math.pi]:
            Q=q(theta,z)
            direct=quad(lambda t: math.cos(z*math.sin(t))-jv(0,z),0,theta,epsabs=1e-11)[0]
            direct+=1j*quad(lambda t: math.sin(z*math.sin(t)),0,theta,epsabs=1e-11)[0]
            check(abs(Q-direct)<1e-11,'q antiderivative')
        check(abs(q(2*math.pi,z))<1e-11,'periodic q')
    for rho in [.4,.2,.1,.06]:
        for xi,theta in [(0.,0.),(0.,math.pi/2),(1.,.45)]:
            z=Z0+rho*xi
            v1=exact_m2(rho,z,theta)
            v2=direct_m2(rho,z,theta)
            check(abs(v1-v2)<.0008,f'exact geometric/direct age disagreement rho={rho}: {v1} vs {v2}')
    for xi,theta in [(0.,0.),(0.,math.pi/2),(1.,.45),(-1.,.45)]:
        target=asymptotic_m2(xi,theta)
        errors=[]
        for rho in [.1,.05,.025,.0125]:
            errors.append(abs(exact_m2(rho,Z0+xi*rho,theta)-target))
        check(errors[-1]<errors[0]*.50+1e-9,f'asymptotic convergence {xi,theta}: {errors}')
        check(errors[-1]<.09,f'final asymptotic accuracy {xi,theta}: {errors}')
    c,V=constants(Z0)
    check(abs(V-.6415807323994268)<1e-12,'Fourier micro-motion constant')
    check(abs(c.imag-1.1776917331968324)<1e-12,'mean imaginary micromotion')
    check(abs(asymptotic_m2(0,0)-1.0142692754197924)<1e-12,'resonant phase 0')
    check(abs(asymptotic_m2(0,math.pi/2)-.3207903661997134)<1e-9,'resonant phase pi/2')
    check(abs(0.5*(2*V)-V)<1e-12,'phase average')
    for xi,theta in [(0.,0.),(0.,math.pi/2),(1.,.4)]:
        for n in [0,1,2,3,4]:
            l=limit_probability(xi,theta,n)
            p=exact_probability(.016,xi,theta,n)
            check(abs(l-p)<.025, f'probability crossover {xi,theta,n}: {l} {p}')
    for xi,theta in [(0.,0.),(1.,.4)]:
        probs=np.array([limit_probability(xi,theta,n) for n in range(-30,31)])
        check(abs(np.sum(probs)-1)<5e-5,'probability normalization')
        check(abs(np.sum(np.arange(-30,31)**2*probs)-asymptotic_m2(xi,theta))<5e-5,'moment normalization')
    print(f'PASS {count} independent finite diagnostic assertions')
    print('first J0 zero',Z0,'J0 derivative',-jv(1,Z0),'V',V)
    print('resonant variance phase 0',asymptotic_m2(0,0))
    print('resonant variance phase pi/2',asymptotic_m2(0,math.pi/2))
    print('resonant phase-averaged variance',V)

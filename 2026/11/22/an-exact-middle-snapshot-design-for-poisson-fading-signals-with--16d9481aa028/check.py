#!/usr/bin/env python3
"""Reproducible diagnostics for the three-snapshot Poisson exponential design."""
import math
import random

COUNT=0

def verify(condition, message='diagnostic failed'):
    global COUNT
    COUNT+=1
    if not condition:
        raise AssertionError(message)

def aux(q,z):
    c=q/math.expm1(q)
    h=z-c*math.expm1(z)
    hp=1-c*math.exp(z)
    return h,hp

def score(q,rho,z):
    h,hp=aux(q,z)
    return 2*hp/h-2+1/(1+rho*math.exp(z))

def solve(q,rho):
    lo=q*1e-8
    hi=q*(1-1e-8)
    verify(score(q,rho,lo)>0 and score(q,rho,hi)<0)
    for _ in range(90):
        md=(lo+hi)/2
        if score(q,rho,md)>0: lo=md
        else: hi=md
    return (lo+hi)/2

def reduced(q,rho,z):
    h,_=aux(q,z)
    return math.exp(-2*z)*h*h/(math.exp(-z)+rho)

def det3(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])

def direct_det(q,rho,z,theta,lam):
    times=[0,z/lam,q/lam]
    js=[[math.exp(-lam*t),-theta*t*math.exp(-lam*t),1] for t in times]
    mus=[theta*(math.exp(-lam*t)+rho) for t in times]
    dj=det3(js)
    return dj*dj/math.prod(mus)

def closed_det(q,rho,z,theta,lam):
    return (1-math.exp(-q))**2/(theta*lam*lam*(1+rho)*(math.exp(-q)+rho))*reduced(q,rho,z)

rng=random.Random(83046)
for j in range(300):
    q=rng.uniform(.5,10)
    rho=math.exp(rng.uniform(-3,3))
    theta=math.exp(rng.uniform(-2,2))
    lam=math.exp(rng.uniform(-2,2))
    z=q*rng.uniform(.1,.9)
    exact=closed_det(q,rho,z,theta,lam)
    verify(abs(direct_det(q,rho,z,theta,lam)/exact-1)<1e-9,'Fisher determinant identity')
    zstar=solve(q,rho)
    verify(0<zstar<q,'interior maximum')
    verify(abs(score(q,rho,zstar))<1e-7,'stationarity')
    benchmark=reduced(q,rho,zstar)
    for k in range(1,20):
        zk=q*k/20
        verify(reduced(q,rho,zk)<=benchmark*(1+1e-10),'global grid dominance')
    # Increasing background must bring design earlier.
    verify(solve(q,rho*.8)>zstar>solve(q,rho*1.2),'strict background monotonicity')

# Gaussian-homoscedastic limit at large background, and no-background Poisson limit.
for q in [.5,1,3,4,8,12]:
    zp=solve(q,1e-7)
    zlow=solve(q,1)
    zhigh=solve(q,1e7)
    verify(zp>zlow>zhigh)
    h,hp=aux(q,zhigh)
    verify(abs(hp/h-1)<1e-5)
    h,hp=aux(q,zp)
    verify(abs(hp/h-.5)<1e-5)

for rho in [.1,1,10]:
    for q in [.01,.02,.04]:
        observed=solve(q,rho)/q
        pred=.5-q*(1+4*rho)/(48*(1+rho))
        verify(abs(observed-pred)<.1*q*q,'small-horizon coefficient')
    for q in [30,50]:
        z=solve(q,rho)
        verify(1<z<2)
        verify(abs(2/z-2+1/(1+rho*math.exp(z)))<1e-8)

q=4;rho=1
zstar=solve(q,rho)
ratio=reduced(q,rho,zstar)/reduced(q,rho,2)
verify(abs(zstar-1.043396317665199)<1e-12)
verify(abs(ratio-2.013109816346372)<1e-10)
print('PASS',COUNT,'deterministic checks')
print('example optimal time',format(zstar,'.15f'),'information determinant ratio',format(ratio,'.15f'))

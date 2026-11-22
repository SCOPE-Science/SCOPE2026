"""Numerical cross-checks for a two-observation damped-rotation information design.
Run with Python 3 standard library: python verify.py
The printed tests do not replace the analytic uniqueness proof.
"""
import math
import random

PI=math.pi

def information_eigenvalue(r,z):
    q=math.exp(-2*r*z)
    S=math.sin(z)**2
    D=math.hypot(1-q,2*math.sqrt(q)*math.cos(z))
    return 2*q*S/(1+q+D)

def stationarity(r,z):
    q=math.exp(-2*r*z)
    L=information_eigenvalue(r,z)
    return math.cos(z)/math.sin(z)*(1+q/(1-L))-r

def optimal_phase(r):
    lo=1e-12
    hi=PI/2-1e-12
    assert stationarity(r,lo)>0 and stationarity(r,hi)<0
    for k in range(85):
        mid=(lo+hi)*0.5
        if stationarity(r,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)*0.5

def gram_min_direct(a,b,t1,t2):
    # Outer products of measurement rows; constant observation noise normalized to 1.
    u=(math.exp(-a*t1)*math.cos(b*t1),-math.exp(-a*t1)*math.sin(b*t1))
    v=(math.exp(-a*t2)*math.cos(b*t2),-math.exp(-a*t2)*math.sin(b*t2))
    M11=u[0]*u[0]+v[0]*v[0]
    M22=u[1]*u[1]+v[1]*v[1]
    M12=u[0]*u[1]+v[0]*v[1]
    d=math.hypot(M11-M22,2*M12)
    return 2*(M11*M22-M12*M12)/(M11+M22+d)

rng=random.Random(20261116)
checks=0
for _ in range(17000):
    a=10**rng.uniform(-1,1)
    b=10**rng.uniform(-1,1)
    t1=rng.random()*2
    t2=t1+rng.random()*3
    calculated=gram_min_direct(a,b,t1,t2)
    expected=math.exp(-2*a*t1)*information_eigenvalue(a/b,b*(t2-t1))
    assert abs(calculated-expected)<5e-13*(1+abs(expected)),(a,b,t1,t2,calculated,expected)
    checks+=1
for r in [0.0001,0.001,0.01,0.1,0.5,1,2,5,10,100]:
    z=optimal_phase(r)
    d=math.atan(1/r)
    assert 0<d<z<PI/2
    assert abs(stationarity(r,z))<5e-8
    for j in range(1000):
        trial=rng.random()*20
        assert information_eigenvalue(r,trial)<=information_eigenvalue(r,z)+2e-14
        checks+=1
    for horizon in (0.1,0.5,1,2,5,20):
        t=min(z,horizon)
        best=information_eigenvalue(r,t)
        for _ in range(200):
            first=rng.random()*horizon
            second=first+rng.random()*(horizon-first)
            L=math.exp(-2*r*first)*information_eigenvalue(r,second-first)
            assert L<=best+5e-14,(r,horizon,first,second,L,best)
            checks+=1
# Anchor examples and asymptotic checks.
z1=optimal_phase(1)
assert abs(z1-0.8730697652040061)<2e-12
assert abs(information_eigenvalue(1,z1)-0.09488968133484221)<1e-12
r=1.e-4
assert abs((PI/2-optimal_phase(r))/(PI*r*r)-1)<3e-4
r=100.
c0=1.108857552878572
assert abs(r*optimal_phase(r)-c0)<4e-5
print(f'PASS: {checks} direct-matrix, finite-horizon and phase comparisons')
print('r=1 phase=',format(z1,'.15f'))
print('r=1 information=',format(information_eigenvalue(1,z1),'.15f'))
print('large-damping scaled phase=',format(r*optimal_phase(r),'.15f'))
print('All finite tests are supplementary to the analytic proof.')

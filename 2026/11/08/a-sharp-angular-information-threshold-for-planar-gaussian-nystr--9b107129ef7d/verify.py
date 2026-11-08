#!/usr/bin/env python3
"""Independent executable checks for a planar rank-one Gaussian Nyström risk identity.

Uses exact SymPy algebra and deterministic angular quadrature. Numeric tests are
sanity checks for the analytic circle integral, not a replacement for its proof.
"""
import math
import random
import sympy as sp
from scipy.integrate import quad
import numpy as np

assertions=0

def check(condition, note):
    global assertions
    assert bool(condition), note
    assertions += 1

def risk(A,K):
    D=math.sqrt(np.linalg.det(A)*np.linalg.det(K))
    return (D*np.trace(A)+np.linalg.det(A)*np.trace(K))/(np.trace(A@K)+2*D)

def angle_average(A,K):
    L=np.linalg.cholesky(K)
    def fn(t):
        z=np.array([math.cos(t),math.sin(t)])
        g=L@z
        return np.linalg.det(A)*np.dot(g,g)/np.dot(g,A@g)
    return quad(fn,0,2*math.pi,epsabs=2e-10,epsrel=2e-10,limit=300)[0]/(2*math.pi)

def orientation_risk(a,b,r,theta):
    A=np.diag([a,b])
    c,s=math.cos(theta),math.sin(theta)
    R=np.array([[c,-s],[s,c]])
    K=R@np.diag([r,1.])@R.T
    return risk(A,K)

# The algebraic form via the two-dimensional Gaussian ratio identity.
for a,b,c,d,e,f in [
    (3,1,2,1,1,0), (5,2,4,2,1,1), (7,3,9,5,2,1),
    (11,3,13,8,4,2), (6,2,6,4,0,1), (7,1,3,2,2,0),
]:
    A=sp.Matrix([[a,sp.Rational(e,5)],[sp.Rational(e,5),b]])
    K=sp.Matrix([[c,sp.Rational(f,4)],[sp.Rational(f,4),d]])
    check(A.det()>0 and K.det()>0,'SPD inputs')
    delta=sp.sqrt(A.det()*K.det())
    lhs=sp.simplify(A.det()*sp.trace((A+delta*K.inv()).inv()))
    rhs=(delta*sp.trace(A)+A.det()*sp.trace(K))/(sp.trace(A*K)+2*delta)
    check(sp.simplify(lhs-rhs)==0,'trace identity exact')

# Check the angular identity against full-circle numerical integration.
for q in range(45):
    rng=np.random.default_rng(1201+q)
    X=rng.normal(size=(2,2));Y=rng.normal(size=(2,2))
    A=X@X.T+np.eye(2)*(.1+q/30)
    K=Y@Y.T+np.eye(2)*(.12+q/40)
    closed=risk(A,K)
    numerical=angle_average(A,K)
    check(abs(numerical-closed)<3e-9*(1+closed),f'angle integral #{q}')

# All-direction optimality, explicit extrema and robust-isotropy benchmark.
for a,b,r in [(4.,1.,9.),(9.,1.,100.),(7.,2.,5.),(3.,1.,2.),(22.,7.,6.)]:
    t=math.sqrt(a*r/b)
    lo=(b*t+a)/(t+1)
    u=math.sqrt(a/(b*r))
    hi=(b*u+a)/(u+1)
    check(abs(orientation_risk(a,b,r,0)-lo)<1e-10,'aligned minimum')
    check(abs(orientation_risk(a,b,r,math.pi/2)-hi)<1e-10,'antialigned maximum')
    check(lo<math.sqrt(a*b)<hi,'isotropic bracket')
    for j in range(1,80):
        th=(math.pi/2)*j/80
        v=orientation_risk(a,b,r,th)
        check(lo<v<hi,'sharp orientation interval')

# Verify leading two-scale sensitivity on a sequence with theta ~ r^{-1/4}.
a,b=4.,1.
for r in [10**4,10**6,10**8]:
    th=.8*r**(-.25)
    exact=orientation_risk(a,b,r,th)-b
    predicted=(a-b)*math.sqrt(b/(a*r)) + b*(a-b)/a * th**2
    check(abs(exact/predicted-1) < 8*r**(-.25),'joint asymptotic')

# Angular-information threshold: optimum is at isotropy or singular covariance.
for a,b in [(4.,1.),(9.,2.),(1.25,1.),(10.,1.)]:
    critical=math.atan((a/b)**.25)
    for theta in [0,math.pi/8,math.pi/4,critical-.005,critical,critical+.005,math.pi/3,math.pi/2]:
        alpha=a*math.cos(theta)**2+b*math.sin(theta)**2
        target=min(math.sqrt(a*b),a*b/alpha)
        for ratio in [1,1.01,2,8,100,1e4]:
            got=orientation_risk(a,b,ratio,theta)
            check(got>=target-2e-10,'angular minimax lower bound')
            if abs(theta-critical)<1e-8 and ratio>1:
                check(got>target+1e-10,'critical angle strict finite-anisotropy penalty')
        if theta<critical-1e-7:
            check(a*b/alpha<math.sqrt(a*b),'concentration regime')
        if theta>critical+1e-7:
            check(a*b/alpha>math.sqrt(a*b),'isotropic regime')

check(abs(orientation_risk(4,1,9,0)-10/7)<1e-12,'exact aligned example')
check(abs(orientation_risk(4,1,9,math.pi/2)-14/5)<1e-12,'exact anti example')
print(f'PASS: {assertions} assertions; exact algebra, full-circle quadrature, sharp eigen-alignment, isotropic minimax, two-scale limit.')

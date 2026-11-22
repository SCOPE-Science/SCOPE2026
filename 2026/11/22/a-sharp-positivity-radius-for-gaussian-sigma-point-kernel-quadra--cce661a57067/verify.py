"""Reproduce Gaussian kernel quadrature symmetry reduction and positivity crossover.
Requirements: Python 3.10+, numpy (for independent full Gram solve).
"""
import math
import numpy as np

checks=0

def check(test, message):
    global checks
    checks += 1
    assert bool(test), message

def formula(d, ell, tau, a):
    u=ell*ell/(ell*ell+tau*tau)
    s=math.exp(-a*a/(2*ell*ell))
    q0=u**(d/2)
    w1=q0*(s**u-s)/(1-s*s)**2
    w0=q0-2*d*s*w1
    return w0,w1

def fullsolve(d, ell, tau, a):
    pts=np.zeros((2*d+1,d))
    for j in range(d):
        pts[2*j+1,j]=a
        pts[2*j+2,j]=-a
    D=pts[:,None,:]-pts[None,:,:]
    K=np.exp(-np.sum(D**2,axis=2)/(2*ell**2))
    q=(ell*ell/(ell*ell+tau*tau))**(d/2)*np.exp(-np.sum(pts**2,axis=1)/(2*(ell**2+tau**2)))
    return np.linalg.solve(K,q)

def F(s,u):
    return 2*s*(s**u-s)/(1-s*s)**2

def crossing(d,u):
    lo=0.0
    hi=1.0
    for _ in range(180):
        mid=(lo+hi)/2
        if F(mid,u)<1/d:
            lo=mid
        else:
            hi=mid
    return (hi+lo)/2

for d in range(2,12):
    for ell in (0.5,1.,2.,4.):
        for tau in (0.25,1.,2.):
            for a in (0.7,1.9,3.5):
                w0,w1=formula(d,ell,tau,a)
                wp=fullsolve(d,ell,tau,a)
                check(abs(wp[0]-w0)<2e-8*(1+abs(w0)),(d,ell,tau,a,'center',wp[0],w0))
                check(np.allclose(wp[1:],w1,atol=2e-8,rtol=2e-8),(d,ell,tau,a,'outer'))
                check(w1>0,(d,ell,tau,a,'outer positive'))

for u in (0.01,0.1,0.5,0.9,0.999):
    for d in (2,3,5,10,50,200,1000):
        root=crossing(d,u)
        check(0<root<1,'root range')
        check(abs(d*F(root,u)-1)<1e-9,'root equation')
        check(d*F(root*.85,u)<1,'safe larger radius')
        check(d*F(1-(1-root)*.85,u)>1,'unsafe smaller radius')
        check(root>0,'all outer weights')
        if d>=200 and u<=.5:
            pred=(1/(2*d))**(1/(1+u))
            check(abs(math.log(root/pred))<.13,('asymptotic',d,u,root,pred))

for u in (0.02,.18,.45,.77,.96):
    old=0.0
    for i in range(1,500):
        s=i/500
        val=F(s,u)
        check(val>old,('monotonicity',u,s,val,old))
        old=val

for d in (2,4,8):
    a=3.7; tau=1.15
    for ell in (20,50,100):
        w0,w1=formula(d,ell,tau,a)
        check(abs(w0-(1-d*tau*tau/a**2))<.02,'flat center')
        check(abs(w1-tau*tau/(2*a*a))<.02,'flat outer')

print('PASS',checks,'assertions')

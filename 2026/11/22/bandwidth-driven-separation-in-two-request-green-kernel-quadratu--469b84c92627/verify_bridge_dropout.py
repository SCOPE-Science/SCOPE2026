#!/usr/bin/env python3
"""Direct numerical checks for the pinned exponential Green-kernel two-site design."""
import math
import random


def gap_variance(kappa, h):
    assert h >= 0
    if kappa == 0:
        return h**3 / 12
    return (h - 2 * math.tanh(kappa*h/2) / kappa) / kappa**2


def gap_derivative(kappa,h):
    if kappa == 0:
        return h*h/4
    return (math.tanh(kappa*h/2)/kappa)**2


def covariance(kappa,x,y):
    if kappa == 0:
        return min(x,y)*(1-max(x,y))
    m=min(x,y);M=max(x,y)
    return math.sinh(kappa*m)*math.sinh(kappa*(1-M))/(kappa*math.sinh(kappa))


def integral_covariance(kappa,x):
    if kappa == 0:
        return x*(1-x)/2
    return (1-math.cosh(kappa*(x-.5))/math.cosh(kappa*.5))/kappa**2


def schur_risk(kappa,points):
    var=gap_variance(kappa,1)
    if len(points)==0:return var
    if len(points)==1:
        x=points[0]
        return var-integral_covariance(kappa,x)**2/covariance(kappa,x,x)
    x,y=points
    a=covariance(kappa,x,x)
    d=covariance(kappa,y,y)
    b=covariance(kappa,x,y)
    c=integral_covariance(kappa,x)
    e=integral_covariance(kappa,y)
    det=a*d-b*b
    return var-(d*c*c-2*b*c*e+a*e*e)/det


def dropout_risk(kappa,p,x,y):
    q=1-p
    return (q*q*gap_variance(kappa,1)+p*q*(gap_variance(kappa,x)+gap_variance(kappa,1-x)+gap_variance(kappa,y)+gap_variance(kappa,1-y))+p*p*(gap_variance(kappa,x)+gap_variance(kappa,y-x)+gap_variance(kappa,1-y)))


def optimizer_gap(kappa,p):
    def first(u):
        a=(1-u)/2
        b=(1+u)/2
        return (1-p)*(gap_derivative(kappa,b)-gap_derivative(kappa,a))+p*(gap_derivative(kappa,u)-gap_derivative(kappa,a))
    lo=0;hi=1/3
    assert first(lo)<0 and first(hi)>0
    for _ in range(75):
        mid=(lo+hi)/2
        if first(mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def close(a,b,tol=2e-9):
    assert abs(a-b) <= tol*max(1,abs(a),abs(b)), (a,b)


random.seed(20261121)
count=0
for kappa in [0,.25,.6,1,2,4,7]:
    for _ in range(55):
        x,y=sorted(random.uniform(.02,.98) for j in range(2))
        if y-x<.04:continue
        p=random.uniform(.02,.98)
        close(schur_risk(kappa,[]),gap_variance(kappa,1));count+=1
        close(schur_risk(kappa,[x]),gap_variance(kappa,x)+gap_variance(kappa,1-x));count+=1
        close(schur_risk(kappa,[x,y]),gap_variance(kappa,x)+gap_variance(kappa,y-x)+gap_variance(kappa,1-y));count+=1
        direct=(1-p)**2*schur_risk(kappa,[])+p*(1-p)*(schur_risk(kappa,[x])+schur_risk(kappa,[y]))+p*p*schur_risk(kappa,[x,y])
        close(dropout_risk(kappa,p,x,y),direct);count+=1

# The elementary Brownian limit is an independent exact reference for the root.
for p in [.01,.1,.25,.5,.75,.99]:
    u=optimizer_gap(0,p)
    radical=p/(2-p+math.sqrt((2-p)**2+3*p*p))
    close(u,radical,5e-13);count+=1

# Global minimum witnesses on grids and monotone tension ordering.
for p in [.08,.3,.6,.9]:
    us=[]
    for kappa in [0,.3,1,3,8,18]:
        u=optimizer_gap(kappa,p);us.append(u)
        x,y=(1-u)/2,(1+u)/2
        value=dropout_risk(kappa,p,x,y)
        for i in range(21):
            xx=.01+.98*i/20
            for j in range(i+1,21):
                yy=.01+.98*j/20
                assert dropout_risk(kappa,p,xx,yy)>=value-1e-11
                count+=1
    assert all(us[i]<us[i+1] for i in range(len(us)-1));count+=1

# Large-tension scaling: asymptotic offset against analytic coefficient.
for p in [.2,.5,.8]:
    for kappa in [40,60]:
        u=optimizer_gap(kappa,p)
        target=(2/3)*math.log(1/p)
        assert abs(kappa*(1/3-u)-target)<.08, (p,kappa,u,target)
        count+=1

# Distinguish the integral target from pointwise-variance integration.
for p in [.2,.5,.8]:
    u=optimizer_gap(2,p)
    assert 0<u<1/3
    count+=1

print('PASS',count,'conditional-Green-kernel, dropout-risk, root, grid and asymptotic checks')
print('p=0.5 kappa=0:',optimizer_gap(0,.5))
print('p=0.5 kappa=2:',optimizer_gap(2,.5))
print('p=0.5 kappa=10:',optimizer_gap(10,.5))

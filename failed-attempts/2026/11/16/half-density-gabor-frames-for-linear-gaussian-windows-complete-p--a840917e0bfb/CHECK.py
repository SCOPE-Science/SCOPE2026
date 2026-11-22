#!/usr/bin/env python3
"""Finite numerical consistency tests for the half-density polynomial-Gaussian Zak model."""
import math
import cmath

PI=math.pi

def f_p(x,w,beta=PI,n=18):
    fs=0j; ps=0j
    for k in range(-n,n+1):
        t=x-k
        v=math.exp(-beta*t*t)*cmath.exp(2j*PI*k*w)
        fs+=v; ps+=t*v
    return fs,ps

def score(x,w,c,beta=PI):
    f,p=f_p(x,w,beta)
    h,q=f_p(x+.5,w,beta)
    return abs(p-c*f)**2+abs(q-c*h)**2

def theta(u,beta=PI,n=18):
    v=0j; d=0j
    for k in range(-n,n+1):
        t=cmath.exp(-beta*k*k+2*beta*k*u)
        v+=t; d+=2*beta*k*t
    return v,d

checked=0
for beta in (.8,PI,4.2):
    t,d=theta(.5+1j*PI/(2*beta),beta)
    assert abs(t)<1e-10
    checked+=1
    for u in (.13+.09j, .29-.19j):
        t,d=theta(u,beta)
        rt,rd=theta(u+1,beta)
        factor=cmath.exp(beta+2*beta*u)
        assert abs(rt-factor*t)<1e-9*(1+abs(rt))
        assert abs(rd-factor*(d+2*beta*t))<1e-8*(1+abs(rd))
        checked+=2
        iv,idv=theta(u+1j*PI/beta,beta)
        assert abs(iv-t)<1e-9*(1+abs(t))
        checked+=1
    for x in (0,.1,.27,.49):
        for w in (0,.2,.47):
            ff,pp=f_p(x,w,beta)
            th,thp=theta(x+1j*PI*w/beta,beta)
            assert abs(ff-math.exp(-beta*x*x)*th)<2e-10
            assert abs(pp-math.exp(-beta*x*x)*(x*th-thp/(2*beta)))<2e-10
            checked+=2
            assert abs(score(x,w,.2+.1j,beta)-score((x+.5)%1,w,.2+.1j,beta))<2e-10
            checked+=1
for c in (0j,.1+.2j,-.1-.2j,.3j,.07):
    assert abs(score(0,0,c)-abs(c)**2*(f_p(0,0)[0].real**2+f_p(.5,0)[0].real**2))<1e-12
    checked+=1
    for x,w in ((.06,.27),(.24,.3),(.37,.66),(.09,.78)):
        assert abs(score(x,w,c)-score((-x)%(.5),(-w)%1,-c))<1e-9
        checked+=1
E0=sum(math.exp(-PI*k*k) for k in range(-16,17))
Eh=sum(math.exp(-PI*(k-.5)**2) for k in range(-16,17))
M0=sum(k*k*math.exp(-PI*k*k) for k in range(-16,17))
Mh=sum((k-.5)**2*math.exp(-PI*(k-.5)**2) for k in range(-16,17))
f=(E0,Eh)
u=(E0-2*PI*M0,Eh-2*PI*Mh)
v=(-2*PI*M0,-2*PI*Mh)
delta=f[0]*u[1]-f[1]*u[0]
cr=delta**2/sum(x*x for x in u)
ci=delta**2/sum(x*x for x in v)
assert abs(cr-1.9999160962706483)<1e-12
assert abs(ci-.48815123519380465)<1e-12
checked+=2
# Construct first-order minimizer in both perturbation directions and verify its leading coefficient.
for e in (.0001,.0002,.0004):
    for c, direction, C in ((e,u,cr),(1j*e,v,ci)):
        base=e*(sum(f[j]*direction[j] for j in range(2))/sum(direction[j]**2 for j in range(2)))
        x,w=(base,0) if c.imag==0 else (0,base)
        val=score(x,w,c)
        assert abs(val/e**2-C)<.003
        checked+=1
print(f'PASS: {checked} finite numerical assertions; CR={cr:.15f}, CI={ci:.15f}; analytically proved infinite claims not dependent on this checker')

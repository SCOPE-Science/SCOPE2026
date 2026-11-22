#!/usr/bin/env python3
"""Independent finite checks for a two-spectral residual-difference iteration.

Uses only the Python standard library; finite tests do not certify asymptotic claims.
"""
from fractions import Fraction as F
import math

checks=0
for a,b in [(F(2),F(1)),(F(3),F(2)),(F(5),F(1)),(F(7),F(3))]:
    kappa=a/b
    for x,y in [(F(1),F(1)),(F(2),F(3)),(F(-1),F(4)),(F(3),F(-2)),(F(7),F(1))]:
        r=[x,y]
        e0=(x/y)**2
        e=[e0]
        alphas=[]
        for j in range(6):
            if j==0:
                alpha=(r[0]**2+r[1]**2)/(a*r[0]**2+b*r[1]**2)
            else:
                d=[r[i]-prev[i] for i in range(2)]
                alpha=(d[0]**2+d[1]**2)/(a*d[0]**2+b*d[1]**2)
                alpha_derived=(a*a*old[0]**2+b*b*old[1]**2)/(a**3*old[0]**2+b**3*old[1]**2)
                assert alpha==alpha_derived
                checks+=1
            alphas.append(alpha)
            prev=r[:]
            r=[(1-alpha*a)*r[0], (1-alpha*b)*r[1]]
            e.append((r[0]/r[1])**2)
            if j==0:
                assert e[1]==1/e[0]
                checks+=1
            else:
                assert e[j+1] == e[j]/(kappa**4 * e[j-1]**2)
                assert kappa**2*e[j+1] == (kappa**2*e[j])/(kappa**2*e[j-1])**2
                checks+=2
            old=prev
        assert all(alpha>0 for alpha in alphas)
        checks+=1

R=math.sqrt(2.0)
theta=math.acos(1/(2*R))
def H(phase,terms=110):
    p=q=0.0
    for m in range(2,terms+2):
        v=math.cos(phase-m*theta)/R**m
        p+=max(v,0);q+=max(-v,0)
    return min(p,q)

def logs_of_components(a,b,x,y,n):
    kap=a/b; init=(x/y)**2;L=math.log(kap)
    phi0=2*L+math.log(init);phi1=2*L-math.log(init)
    z0=phi0;z1=phi1
    C=math.hypot(phi0,(2*phi1-phi0)/math.sqrt(7))
    delta=math.atan2((2*phi1-phi0)/math.sqrt(7),phi0)
    u=math.log(abs(x));v=math.log(abs(y))
    lam0=(init+1)/(a*init+b)
    high=-(kap-1)/(kap*init+1)
    low=(kap-1)*init/(kap*init+1)
    u+=math.log(abs(high));v+=math.log(abs(low))
    for j in range(n-1):
        z= C*R**j*math.cos(j*theta-delta)
        # log(1+kap*exp(z)) without overflow
        w=z+L
        logden=max(0,w)+math.log1p(math.exp(-abs(w)))
        u+=math.log(kap-1)-logden
        v+=math.log(kap-1)+z-logden
    return u,v,C,delta,phi0,phi1

for a,b,x,y in [(2,1,1,1),(3,1,2,3),(4,3,10,1),(7,5,3,17),(2,1,1,math.sqrt(math.sqrt(2)))]:
    L=math.log(a/b)
    for n in [24,30,36,40,48]:
        u,v,C,delta,z0,z1=logs_of_components(a,b,x,y,n)
        assert C>=2*L-1e-10
        profile=-max(u,v)/R**n
        target=C*H(n*theta-delta)
        assert abs(profile-target) < 8*(1+C+L)*n/R**n
        checks+=2
        assert abs(z1-(z0/2+C*math.sqrt(7)/2*math.sin(delta))) <1e-9
        checks+=1
assert H(.2)>0 and H(.5)>0
checks+=2
print('VERIFY_OK',checks,'finite exact-rational and independent scaled-log checks')

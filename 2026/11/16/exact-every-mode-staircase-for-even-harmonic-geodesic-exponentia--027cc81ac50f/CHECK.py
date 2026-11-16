#!/usr/bin/env python3
"""Independent finite checks for the second-harmonic geodesic covariance formula.
No nonstandard dependencies; finite samples do not establish infinite assertions.
"""
import math
from fractions import Fraction


def ratio(t, n):
    return ((t + (n-2)**2) * (t + (n+2)**2)
            / ((t+n*n)*(t+n*n+4)))


def crossing(n):
    b = 2*n*n + 2*n + 25
    c = -3*n**4 - 6*n**3 + 5*n*n + 8*n + 20
    return (-b + math.sqrt(b*b-20*c))/10


def coeff(a, n):
    return a*(1-(-1)**n*math.exp(-math.pi*a))/(math.pi*(a*a+n*n))


def simpson(a,b,n,panels=4096):
    h=math.pi/panels
    z=0.0
    for j in range(panels+1):
        th=h*j
        w=1 if j in (0,panels) else (4 if j%2 else 2)
        z+=w*math.exp(-a*th)*(1+b*math.cos(2*th))*math.cos(n*th)
    return z*h/(3*math.pi)


def run():
    checks=0
    for a in (0.15,0.3,1.0,1.8,3.0,5.0):
        t=a*a
        nstar=math.sqrt((t+4+4*math.sqrt((t+1)*(t+4)))/3)
        candidates=(math.floor(nstar),math.ceil(nstar))
        rho=min(ratio(t,n) for n in candidates)
        assert abs(rho-min(ratio(t,n) for n in range(2,300)))<1.e-12
        checks+=1
        for n in range(0,30):
            r=ratio(t,n)
            c=coeff(a,n)
            cnm=coeff(a,abs(n-2))
            cnp=coeff(a,n+2)
            assert abs(2*c/(cnm+cnp)-r)<1.e-10
            checks+=1
            if n<=15:
                d=c-.5*rho*(cnm+cnp)
                assert d>=-1e-13
                assert abs(simpson(a,-rho,n)-d)<3e-8
                checks+=2
    prev=0.0
    for n in range(2,100):
        t=crossing(n)
        assert t>prev
        assert abs(ratio(t,n)-ratio(t,n+1))<2e-12
        assert abs(min(ratio(t,k) for k in range(2,200))-ratio(t,n))<2e-12
        assert min(range(2,200),key=lambda k:ratio(max(1e-10,t-1e-5),k))==n
        assert min(range(2,200),key=lambda k:ratio(t+1e-5,k))==n+1
        checks+=5
        prev=t
    for n in range(2,70):
        t=Fraction(n,3)+Fraction(1,7)
        rn=lambda j: (t+(j-2)**2)*(t+(j+2)**2)/((t+j*j)*(t+j*j+4))
        assert rn(n) == 1 + 4*(t+4-3*n*n)/((t+n*n)*(t+n*n+4))
        p = 5*t*t + (2*n*n+2*n+25)*t - 3*n**4-6*n**3+5*n*n+8*n+20
        delta = 4*(2*n+1)*p / ((t+n*n)*(t+n*n+4)*(t+(n+1)**2)*(t+(n+1)**2+4))
        assert rn(n)-rn(n+1) == delta
        checks+=2
    print('passed',checks,'finite exact/arithmetic/integral/boundary checks')

if __name__=='__main__':
    run()

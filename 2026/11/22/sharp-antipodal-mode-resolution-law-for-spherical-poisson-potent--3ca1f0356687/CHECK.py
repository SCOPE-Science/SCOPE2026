"""Independent arithmetic diagnostics for two-antipodal spherical Poisson potentials.
Run: python3 CHECK.py. The analytic theorem is proved in RESULT.md.
"""
import math
import random

checks = 0

def check(test, msg):
    global checks
    assert test, msg
    checks += 1


def terms(d, r):
    a = 1.0 + r*r
    b = 2.0*r
    c = 1.0-r*r
    k = (d+2.0)/2.0
    gamma = d/2.0
    A = a+b
    B = a-b
    return a,b,c,gamma,k,A,B


def threshold(d, r):
    return math.tanh((d+2)*math.atanh(r))


def U(d, r, p, x):
    a,b,c,g,k,A,B=terms(d,r)
    return c*(p/(a-b*x)**g+(1-p)/(a+b*x)**g)


def dU(d,r,p,x):
    a,b,c,g,k,A,B=terms(d,r)
    return c*g*b*(p/(a-b*x)**k-(1-p)/(a+b*x)**k)


def x_valley(d,r,p):
    a,b,c,g,k,A,B=terms(d,r)
    t=(p/(1-p))**(1/k)
    return (a/b)*(1-t)/(1+t)


def U_valley(d,r,p):
    a,b,c,g,k,A,B=terms(d,r)
    t=(p/(1-p))**(1/k)
    return c*(1+t)**k/((2*a)**g*(1+t**k))


def cusp_coefficients(d,r):
    a,b,c,g,k,A,B=terms(d,r)
    H=(A**k+B**k)**2*A*B/(2*k*b*(A+B)*(A*B)**k)
    C=c*g*(A**k+B**k)**3*A*B/(8*k*(A+B)*(A*B)**(2*k))
    return H,C


random.seed(20261118)
for d in [2,3,4,5,8,12]:
    for r in [.04,.10,.18,.30,.45]:
        a,b,c,g,k,A,B=terms(d,r)
        qcrit=threshold(d,r)
        check(abs(qcrit-(A**k-B**k)/(A**k+B**k))<2e-13,(d,r,'threshold'))
        for frac in [.01,.12,.50,.80,.99]:
            q=qcrit*frac
            p=(1+q)/2
            x0=x_valley(d,r,p)
            check(-1<x0<1,(d,r,p,'inside'))
            check(abs(dU(d,r,p,x0))<1e-9,(d,r,p,'stationary'))
            check(abs(U(d,r,p,x0)-U_valley(d,r,p))<1e-9,(d,r,p,'closed min'))
            check(U(d,r,p,x0) < U(d,r,p,-1),(d,r,p,'weak peak'))
            check(U(d,r,p,x0) < U(d,r,p,1),(d,r,p,'strong peak'))
            for z in [-.999,-.2,0,.2,.999]:
                if z<x0-1e-7:check(dU(d,r,p,z)<0,(d,r,p,z,'left gradient'))
                if z>x0+1e-7:check(dU(d,r,p,z)>0,(d,r,p,z,'right gradient'))
        if qcrit<.999:
            for frac in [.25,.75]:
                q=qcrit+(1-qcrit)*frac
                p=(1+q)/2
                for x in [-1,-.7,-.2,0,.3,.85,1]:
                    check(dU(d,r,p,x)>0,(d,r,p,x,'single mode'))
        # Local angular displacement and secondary peak contrast agree with the coefficients.
        if qcrit<.98:
            delta=min(1e-6, (1-qcrit)*1e-3)
            p=(1+qcrit-delta)/2
            x0=x_valley(d,r,p)
            H,C=cusp_coefficients(d,r)
            check(abs((x0+1)/delta/H-1)<.001,(d,r,'H coefficient'))
            check(abs((U(d,r,p,-1)-U(d,r,p,x0))/delta**2/C-1)<.02,(d,r,'C coefficient'))
for d in [2,3,5,10,20]:
    for q in [.05,.2,.5,.8]:
        r=math.tanh(math.atanh(q)/(d+2))
        check(abs(threshold(d,r)-q)<2e-14,(d,q,'resolution radius'))
print('PASS',checks,'arithmetic diagnostics')

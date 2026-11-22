#!/usr/bin/env python3
"""Exact rational and numerical checks for the two-invariant correction theorem.
No external dependencies. These checks supplement the written proof.
"""
from fractions import Fraction as F
import math


def gram_step(m, r, rho, t):
    """Raw two-invariant Gram solve for u=e1, p=(m,r,0), v=(m,t,0)."""
    m,r,rho,t=map(F,(m,r,rho,t))
    g11=F(1); g12=m; g22=m*m+(r+t)**2/F(4)
    det=g11*g22-g12*g12
    assert det != 0
    b2=(rho*rho-r*r)/2
    lam2=b2/det
    lam1=-g12*lam2
    return (m+lam1+lam2*m, r+lam2*(r+t)/2), det


def closed(r,rho,k):
    r,rho=F(r),F(rho)
    a=(r-rho)/(r+rho)
    return rho*(1+a**(k+1))/(1-a**(k+1))


def count(r,rho,eps):
    # Ground truth from the separate parity inequalities, no slow iteration.
    alpha=(rho-r)/(rho+r)
    def threshold(parity):
        lim=eps/(2-eps) if parity==0 else eps/(2+eps)
        n=parity
        while alpha**(n+1)>lim:
            n+=2
        return n
    return min(threshold(0), threshold(1))


def rational_checks():
    tests=0
    for m in (-3,0,2):
        for r,rho in [(1,2),(2,1),(3,5),(5,3),(7,7)]:
            t=F(r)
            for k in range(16):
                assert t==closed(r,rho,k)
                y,det=gram_step(m,r,rho,t)
                assert det>0 and y[0]==m
                t=y[1]
                assert t>0
                tests+=4
            if r!=rho:
                for sign in (1,-1):
                    z,det=gram_step(m,r,rho,sign*F(rho))
                    assert det>0 and z==(F(m),sign*F(rho))
                    tests+=2
            else:
                assert gram_step(m,r,rho,F(rho))[0]==(F(m),F(rho))
        # Check rank collapse and sphere multiplicity when r=0.
        for rho in (1,2,5):
            p=(F(m),F(0),F(0))
            g12=F(m); g22=F(m)*F(m)
            assert g22-g12*g12==0
            # For v=(m,rho,0) or (m,0,rho), raw Gram is full rank and output=v.
            for axis in (1,2):
                v=[F(m),F(0),F(0)];v[axis]=F(rho)
                g2=[F(m),(v[1])/2,(v[2])/2]
                det=sum(x*x for x in g2)-F(m)*F(m)
                lam2=(F(rho)**2/2)/det
                lam1=-F(m)*lam2
                z=[p[j]+lam1*(j==0)+lam2*g2[j] for j in range(3)]
                assert z==v
                tests+=2
    return tests


def asymptotic_checks():
    tests=0
    eps=0.1
    L=math.log((2-eps)/eps)
    errors=[]
    for r in (0.01,0.005,0.001,0.0002):
        N=count(r,1.0,eps)
        alpha=(1-r)/(1+r)
        for n in range(max(0,N-2),N):
            t=(1+(-alpha)**(n+1))/(1-(-alpha)**(n+1))
            assert abs(t-1)>eps* (1-1e-12)
        t=(1+(-alpha)**(N+1))/(1-(-alpha)**(N+1))
        assert abs(t-1)<=eps*(1+1e-12)
        errors.append((r,N,2*r*N,L))
        tests+=3
    assert abs(errors[-1][2]-L)<0.008
    return tests,errors


def oscillator_checks():
    # e1 is the conserved mass, (e2,e3) is a rotating two-dimensional plane.
    # Three consecutive explicit vector-field evaluations yield R(hJ)=I+hJ+h^2J^2+h^3J^3.
    tests=0
    for h in (0.0,0.5,0.9,0.999,1.0,1.001,1.1,2.0):
        # y=(m,a,b); skew J y=(0,-b,a).
        m,a,b=2.0,3.0,4.0
        def vf(x):return (0.0,-x[2],x[1])
        def add(x,z,k):return tuple(x[i]+k*z[i] for i in range(3))
        k1=vf((m,a,b));k2=vf(add((m,a,b),k1,h));k3=vf(add((m,a,b),k2,h))
        p=add((m,a,b),k3,h)
        expected=(m,(1-h*h)*(a-h*b),(1-h*h)*(b+h*a))
        assert all(abs(x-y)<1e-12 for x,y in zip(p,expected))
        ratio=math.hypot(p[1],p[2])/math.hypot(a,b)
        assert abs(ratio-abs(1-h*h)*math.sqrt(1+h*h))<1e-12
        tests+=2
    return tests


if __name__=='__main__':
    a=rational_checks();b,v=asymptotic_checks();c=oscillator_checks()
    print('PASS: exact rational Gram/Picard checks:',a)
    print('PASS: sharp stopping-law numerical checks:',b)
    for rr,n,scaled,target in v:
        print('  r=',rr,'N=',n,'2*r*N=',round(scaled,9),'target=',round(target,9))
    print('PASS: oscillator predictor checks:',c)

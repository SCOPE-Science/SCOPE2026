#!/usr/bin/env python3
"""Reproduce algebraic and numerical checks for a cubic Hamiltonian center.
Python 3 standard library only; numerical tests corroborate, not prove, limits.
"""
from fractions import Fraction as F
from math import sqrt, asinh, atanh

def check_hamiltonian():
    for a, k in [(F(0), F(1)), (F(1,2), F(1)), (F(-3,5), F(2))]:
        for x,y in [(F(0),F(3,4)),(F(2,3),F(-5,2)),(F(-3,2),F(7,5))]:
            p=1+2*a*x+k*x*x
            vx=x-a*x*x+k*x*x*x
            h_x=(a+k*x)*y*y+vx
            h_y=p*y
            xdot=p*y
            ydot=-x+a*(x*x-y*y)-k*x*(x*x+y*y)
            assert h_y==xdot and h_x==-ydot

def root(a,k,E,s):
    def v(r):return r*r/2-s*a*r**3/3+k*r**4/4
    hi=1.
    while v(hi)<E: hi*=2.
    lo=0.
    for _ in range(90):
        mid=(lo+hi)/2
        if v(mid)>E:hi=mid
        else:lo=mid
    return (lo+hi)/2

def adaptive_simpson(f,left,right,eps=2e-10,max_depth=26):
    def sim(a,b,fa,fm,fb):return (b-a)*(fa+4*fm+fb)/6
    a,b=left,right; m=(a+b)/2
    fa,fm,fb=f(a),f(m),f(b); orig=sim(a,b,fa,fm,fb)
    def recurse(a,b,fa,fm,fb,orig,eps,depth):
        m=(a+b)/2; l=(a+m)/2; r=(m+b)/2
        fl,fr=f(l),f(r)
        il=sim(a,m,fa,fl,fm); ir=sim(m,b,fm,fr,fb)
        if depth==0 or abs(il+ir-orig)<=15*eps:
            return il+ir+(il+ir-orig)/15
        return recurse(a,m,fa,fl,fm,il,eps/2,depth-1)+recurse(m,b,fm,fr,fb,ir,eps/2,depth-1)
    return recurse(a,b,fa,fm,fb,orig,eps,max_depth)

def half_period(a,k,E,s):
    r=root(a,k,E,s)
    def f(t):
        u=1-t*t
        g=(r*r/2)*(1+u)-s*a*r**3/3*(1+u+u*u)+k*r**4/4*(1+u)*(1+u*u)
        p=1+2*s*a*r*u+k*r*r*u*u
        return 2*r*sqrt(2)/sqrt(p*g)
    return adaptive_simpson(f,0.,1.,eps=3e-11)

def primitive(a,k,r,s):
    d=sqrt(k-a*a)
    return (asinh((k*r+s*a)/d)-asinh(s*a/d))/sqrt(k)

def check_mass_potential_factorization():
    # Rational hyperbolic data with exp(t)=q>1, S=sinh(t), h=cosh(t)-1.
    for q in (F(2), F(3), F(5), F(10)):
        S=(q-1/q)/2
        h=(q+1/q)/2-1
        assert S*S==h*(h+2)
        for beta in (F(-3,4), F(-1,2), F(0), F(1,2), F(3,4)):
            up=S+beta*h
            um=S-beta*h
            vp=up*up/2-beta*up**3/3+up**4/4
            vm=um*um/2+beta*um**3/3+um**4/4
            rhs=(2*beta*S*h/F(3))*(3*h*h+5*h+1+3*beta*beta*h*(h-1))
            assert vp-vm==rhs,(q,beta,vp-vm,rhs)
            bracket=3*h*h+5*h+1+3*beta*beta*h*(h-1)
            assert bracket>0

def check_asymptotics():
    a,k=.5,1.
    predicted=-2*sqrt(2/k)*atanh(a/sqrt(k))
    errors=[]
    for E in (1e3,1e5,1e7):
        rp=root(a,k,E,+1); rm=root(a,k,E,-1)
        Fdiff=primitive(a,k,rp,+1)-primitive(a,k,rm,-1)
        assert abs(Fdiff+2/sqrt(k)*atanh(a/sqrt(k)))<1.5/(E**.25)
        d=(half_period(a,k,E,+1)-half_period(a,k,E,-1))*sqrt(E)
        errors.append(abs(d-predicted))
    assert errors[0]>errors[1]>errors[2],(errors,predicted)
    assert errors[2]<.02,(errors,predicted)
    assert abs(half_period(0.,k,100.,+1)-half_period(0.,k,100.,-1))<1e-12
    # The inverse identity is exact algebra, checked at two parameter values.
    for a,k in ((.5,1.),(-.3,2.)):
        L=1/sqrt(2*k)
        B=-2*sqrt(2/k)*atanh(a/sqrt(k))
        kr=1/(2*L*L)
        ar=sqrt(kr)*__import__('math').tanh(-B*sqrt(kr)/(2*sqrt(2)))
        assert abs(k-kr)<1e-12 and abs(a-ar)<1e-12

if __name__=='__main__':
    check_hamiltonian();check_mass_potential_factorization();check_asymptotics()
    print('SIGNED_CUBIC_CENTER_RESIDENCE_INVERSE_OK')

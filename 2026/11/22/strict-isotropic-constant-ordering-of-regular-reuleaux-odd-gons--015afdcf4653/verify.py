#!/usr/bin/env python3
"""Standalone rational certificate for monotonicity of normalized Reuleaux inertia.
The analytic tangent tail bound and the geometric Green identity are proved in RESULT.md.
Only Python standard library is required.
"""
from fractions import Fraction as F
from math import pi, tan, cos, sin, isclose


def add(*args):
    out = [F(0)] * max(map(len,args))
    for a in args:
        for i,v in enumerate(a):out[i]+=v
    return out


def scale(a,k):return [k*v for v in a]


def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out


def sh(a,n):return [F(0)]*n+a


def tangent_coeffs(M):
    # tan(b)/b = sum_k a[k]*b^(2k), from d tan(b)/db=1+tan^2(b).
    a=[F(1)]
    for k in range(1,M+1):
        a.append(sum((a[i]*a[k-1-i] for i in range(k)),F(0))/F(2*k+1))
    return a




def derivative_identity():
    # Exact polynomial identity for the derivative, without a symbolic-algebra dependency.
    def pa(*terms):
        r={}
        for i,j,c in terms:r[(i,j)]=r.get((i,j),F(0))+F(c)
        return {k:v for k,v in r.items() if v}
    def padd(*ps):
        d={}
        for p in ps:
            for k,v in p.items():d[k]=d.get(k,F(0))+v
        return {k:v for k,v in d.items() if v}
    def pm(a,b):
        d={}
        for (i,j),v in a.items():
            for (k,l),w in b.items():d[(i+k,j+l)]=d.get((i+k,j+l),F(0))+v*w
        return {k:v for k,v in d.items() if v}
    def sc(a,c):return {k:v*c for k,v in a.items() if v*c}
    one=pa((0,0,1));b=pa((1,0,1));t=pa((0,1,1));t2=pm(t,t)
    D=padd(sc(b,2),sc(t,-1))
    B=pa((1,0,12),(1,2,4),(0,1,-11),(0,3,-1))
    Bb=pa((0,0,12),(0,2,4))
    Bt=pa((1,1,8),(0,0,-11),(0,2,-3))
    Nd=padd(pm(padd(B,pm(b,padd(Bb,pm(Bt,padd(one,t2))))),D),sc(pm(pm(b,B),padd(one,sc(t2,-1))),-2))
    Ne=pa((3,3,16),(3,1,16),(2,4,-6),(2,2,-4),(2,0,2),(1,5,1),(1,3,-16),(1,1,-13),(0,4,1),(0,2,11))
    assert Nd==Ne, (Nd,Ne)
    return True

def derivative_certificate():
    M=8
    x=tangent_coeffs(M)
    assert x[:5]==[F(1),F(1,3),F(2,15),F(17,315),F(62,2835)]
    assert all(a<=F(1,2)**k for k,a in enumerate(x))
    x2=mul(x,x);x3=mul(x2,x);x4=mul(x3,x);x5=mul(x4,x)
    # For b>0, z=b*b, x=tan(b)/b,
    # N/b^2=P(z,x), N=(2b-tan b)^3*(d/db)[b*B/(2b-tan b)^2]
    P=add([F(2)],scale(x,-13),scale(x2,11),
          sh(add(scale(x,16),scale(x2,-4),scale(x3,-16),x4),1),
          sh(add(scale(x3,16),scale(x4,-6),x5),2))
    assert len(P)==43 and P[0]==P[1]==0
    assert P[2:7]==[F(64,45),F(128,105),F(2944,4725),F(3968,18711),F(364864,14189175)]
    neg_tail=sum((-c)*F(1,3)**(k-2) for k,c in enumerate(P) if k>=7 and c<0)
    assert neg_tail<F(1,1000), ('negative_tail',neg_tail)
    # tan b/b-T_8(b^2) <= C*(b^2)^9 for 0<b<=pi/6,
    # via a[k]<=2^(-k) from the tangent ODE, z<1/3.
    C=F(3,1280)
    assert 90*C/F(3)**7 <F(1,100)
    # |dP/dx|<90 for z<=1/3 and 1<=x<=7/6.
    X=F(7,6);Z=F(1,3)
    deriv_bound=(13+22*X)+Z*(16+8*X+48*X**2+4*X**3)+Z**2*(48*X**2+24*X**3+5*X**4)
    assert deriv_bound<90, deriv_bound
    # Therefore P(z,tan(sqrt z)/sqrt z)/z^2 >64/45-1/1000-1/100>0.
    margin=F(64,45)-F(1,1000)-F(1,100)
    assert margin>F(7,5)
    return neg_tail, C,deriv_bound,margin


def direct_reconstruction():
    # Boundary formula for radius one, n arcs, normal (-cos u,-sin u).
    from math import sqrt
    for n in [3,5,7,9,11,17,31,51]:
        b=pi/(2*n);R=1/(2*cos(b));u=tan(b)
        A=(pi-n*u)/2
        I=(2*pi*(3+u*u)-n*u*(11+u*u))/16
        # integral of circle-arc flux for area and second radial moment
        # Composite midpoint quadrature is supplementary, not a proof.
        N=4096
        step=2*b/N
        Ar=0.0;Mr=0.0
        for k in range(N):
            angle=-b+(k+.5)*step
            c=cos(angle)
            f=1-R*c
            Ar+=f
            Mr+=(R*R+1-2*R*c)*f
        Ar*=n*step/2
        Mr*=n*step/4
        assert abs(Ar-A)<2e-8 and abs(Mr-I)<2e-8,(n,Ar,A,Mr,I)
        Lsq=I/(2*A*A)
        if n>=5:assert Lsq>1/(4*pi)
    for n in range(3,99,2):
        def Lsq(n):
            b=pi/(2*n); u=tan(b)
            A=(pi-n*u)/2;I=(2*pi*(3+u*u)-n*u*(11+u*u))/16
            return I/(2*A*A)
        assert Lsq(n)>Lsq(n+2),n
    return True

if __name__=='__main__':
    derivative_identity()
    vals=derivative_certificate()
    direct_reconstruction()
    print('PASS: exact rational positivity certificate, tangent-series recurrence and integral regression')
    print('negative-tail upper bound:',str(vals[0]))
    print('tangent-tail constant:',str(vals[1]))
    print('derivative upper bound:',str(vals[2]))
    print('certified normalized derivative positivity margin >',str(vals[3]))

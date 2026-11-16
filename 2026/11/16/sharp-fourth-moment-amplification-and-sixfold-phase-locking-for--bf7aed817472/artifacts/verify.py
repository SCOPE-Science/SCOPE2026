#!/usr/bin/env python3
"""Standalone verification for the sharp four-character sixth-cycle Fourier fourth moment.
Science and reproducibility only. Standard-library Python."""
from fractions import Fraction
from random import Random
from math import cos, sin, pi, sqrt
from cmath import exp


def fraction_fourth(v):
    a,b,c,d = map(Fraction,v)
    r0 = a*a+b*b+c*c+d*d
    r1 = a*b+b*c+c*d
    r2 = a*c+b*d
    r3 = 2*a*d
    via_autocorrelation = r0*r0+2*r1*r1+2*r2*r2+r3*r3
    coeff = [Fraction(0) for _ in range(6)]
    for i,x in enumerate((a,b,c,d)):
        for j,y in enumerate((a,b,c,d)):
            coeff[(i+j)%6] += x*y
    return via_autocorrelation, sum(x*x for x in coeff)


def quartic(v):
    E = sum(abs(z)**2 for z in v)
    R = [sum(v[(j+k)%6]*v[j].conjugate() for j in range(6)) for k in range(6)] if False else None
    r1 = v[1]*v[0].conjugate()+v[2]*v[1].conjugate()+v[3]*v[2].conjugate()
    r2 = v[2]*v[0].conjugate()+v[3]*v[1].conjugate()
    r3 = v[3]*v[0].conjugate()+v[0]*v[3].conjugate()
    via_corr = E*E + 2*(abs(r1)**2+abs(r2)**2)+abs(r3)**2
    values=[sum(z*exp(2j*pi*j*k/6) for j,z in enumerate(v)) for k in range(6)]
    via_dft=sum(abs(x)**4 for x in values)/6
    return via_corr, via_dft


def F(t):
    return (3*t**4+4*t**3+12*t*t+4)/(2*(1+t*t)**2)


def poly(t):
    return t**3+3*t*t-3*t-2


def run():
    a=Fraction(1145102,1000000);b=Fraction(1145103,1000000)
    assert poly(a)<0<poly(b)
    lo,hi=float(a),float(b)
    for _ in range(65):
        mid=(lo+hi)/2
        if poly(mid)>0:hi=mid
        else:lo=mid
    rho=(lo+hi)/2
    C=F(rho)
    assert abs(rho-1.1451026912004224)<2e-14
    assert abs(C-2.892164358578031)<2e-13
    rng=Random(641019)
    nfrac=0
    for i in range(1600):
        v=[Fraction(rng.randint(-13,13),rng.randint(1,17)) for _ in range(4)]
        x,y=fraction_fourth(v)
        assert x==y,(v,x,y)
        nfrac+=1
    nineq=0
    for _ in range(6000):
        a,b,c,d=[rng.randint(0,100) for _ in range(4)]
        A=a*a+d*d; B=b*b+c*c
        assert (a*b+c*d)**2<=A*B
        assert (a*c+b*d)**2<=A*B
        assert 2*b*c<=B and 2*a*d<=A
        nineq+=1
    ncomplex=0
    for _ in range(4600):
        v=[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for _ in range(4)]
        e=sum(abs(z)**2 for z in v)
        actual,dft=quartic(v)
        assert abs(actual-dft)<1e-7*max(1.0,dft)
        assert actual<=C*e*e+1e-8*max(1.0,e*e)
        ncomplex+=1
    for k in range(6):
        eta=exp(2j*pi*k/6)
        v=[1,rho*eta,rho*eta**2,eta**3]
        actual,dft=quartic(v)
        E=sum(abs(z)**2 for z in v)
        assert abs(actual/E**2-C)<3e-13
        assert abs(dft/E**2-C)<3e-13
    print('VERIFY_OK', 'rational_convolution', nfrac, 'rational_amplitude',nineq,'complex_DFT',ncomplex,'sharp_phases',6,'rho',format(rho,'.16f'),'C',format(C,'.16f'))

if __name__=='__main__':run()

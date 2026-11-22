#!/usr/bin/env python3
"""Independent exact-rational checks of a circular boxcar averaging error law."""
from fractions import Fraction as F
from math import pi, sqrt, sin, cos


def arc_overlap(d, x, a):
    # Exact overlap length of the forward window with the periodic indicator [0,d).
    return sum((max(F(0), min(x+a, k+d)-max(x, F(k))) for k in (0, 1, 2)), F(0))


def exact_error(a,d):
    cuts={F(0),F(1),d}
    for k in (0,1,2):
        for x in (F(k),F(k)+d,F(k)-a,F(k)+d-a):
            if 0<x<1: cuts.add(x)
    pts=sorted(cuts)
    out=F(0)
    for left,right in zip(pts,pts[1:]):
        f=F(1) if (left+right)/2<d else F(0)
        # Endpoint values of the continuous boxcar average, f constant on this interval.
        yl=f-arc_overlap(d,left,a)/a
        yr=f-arc_overlap(d,right,a)/a
        out+=(right-left)*(yl*yl+yl*yr+yr*yr)/3
    return out


def formula(a,d):
    d=min(d,1-d)
    p=min(a,d)
    i1=d*p*p/F(2)-p*p*p/F(3)
    e=max(F(0),a+d-1)
    i2=e*e*(2*a+1-d)/6
    return d-2*(i1+i2)/(a*a)


def sharp(a):
    return a/6 if a<=F(1,2) else (-8*a**3+12*a*a-1)/(48*a*a)


def run():
    n=0
    # Exhaustive exact-rational two-dimensional test for a,b on a grid, including regime boundaries.
    for den in (3,5,8,13,21,34):
        for na in range(1,den+1):
            a=F(na,den)
            for nd in range(1,den):
                d=F(nd,den)
                actual=exact_error(a,d)
                expected=formula(a,d)
                assert actual==expected,('residual',a,d,actual,expected)
                assert expected<=4*sharp(a),('upper bound',a,d,expected,sharp(a))
                n+=2
    # At small windows any arc between a and 1-a attains the plateau.
    for den in (5,11,37,97):
        for na in range(1,(den//2)+1):
            a=F(na,den)
            for nd in range(na,den-na+1):
                assert formula(a,F(nd,den))==4*sharp(a)
                n+=1
    # At longer windows the semicircle is optimal; verify sampled strict inequality.
    for den in (7,17,61):
        for na in range(den//2+1,den+1):
            a=F(na,den)
            assert formula(a,F(1,2))==4*sharp(a)
            n+=1
            for nd in range(1,den//2+1):
                d=F(nd,den)
                assert formula(a,d)<4*sharp(a)
                n+=1
    # Selected Fourier reconstruction with an independently defined multiplier.
    for a,d in [(0.1,0.35),(0.3,0.49),(0.5,0.5),(0.7,0.5),(0.92,0.25)]:
        s=0.0
        for k in range(1,40001):
            w=2*pi*k
            re=sin(w*a)/(w*a)
            im=(1-cos(w*a))/(w*a)
            filt=(1-re)**2+im*im
            s+=2*(sin(pi*k*d)/(pi*k))**2*filt
        assert abs(s-float(formula(F(str(a)),F(str(d)))))<1.6e-5
        n+=1
    from sympy import symbols, simplify, diff
    x=symbols('x',positive=True)
    q= (-8*x**3+12*x*x-1)/(48*x*x)
    assert simplify(diff(q,x)-(1-4*x**3)/(24*x**3))==0
    n+=1
    print('PASS:',n,'exact-rational, symbolic and independent Fourier checks')
    print('C squared maximum:',(1-4**(-1/3))/4,'at bandwidth',4**(-1/3))
    print('C squared 0.5:',float(sharp(F(1,2))),'1:',float(sharp(F(1,1))))

if __name__=='__main__':run()

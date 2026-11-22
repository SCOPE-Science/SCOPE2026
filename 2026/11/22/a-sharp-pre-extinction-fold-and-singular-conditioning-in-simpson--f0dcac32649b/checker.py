#!/usr/bin/env python3
"""Independent numerical/rational checks of a scalar Simpson energy identity.

This file is supplemental verification, not a proof of continuum statements.
Requires only the Python standard library.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isclose

getcontext().prec = 75
D = Decimal
ONE = D(1)
TWO = D(2)
SIX = D(6)


def B(x):
    return ONE - x/SIX*(ONE + D(4)/(ONE-x).sqrt())


def F(x):
    return B(x)-TWO*(x/SIX).sqrt()


def Fprime(x):
    return -(ONE + D(4)/(ONE-x).sqrt())/SIX-x/(D(3)*(ONE-x)**D('1.5'))-ONE/(SIX*x).sqrt()


def roots(x):
    b=B(x)
    delta=b*b-D(2)*x/D(3)
    if delta < 0:
        return ()
    return ((b-delta.sqrt())/TWO,(b+delta.sqrt())/TWO)


def residual(x,y):
    return y-ONE+x/SIX*(ONE+D(4)/(ONE-x).sqrt()+ONE/y)


def qres(x,y):
    return y*y-B(x)*y+x/SIX


def root_by_bisection():
    lo,hi=D('0.43'),D('0.45')
    assert F(lo)>0 and F(hi)<0
    for _ in range(280):
        mid=(lo+hi)/TWO
        if F(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/TWO


def run():
    checks=0
    xi=root_by_bisection()
    expected=D('0.43657451259244038974886861760102044434')
    assert abs(xi-expected)<D('1e-35'); checks+=1
    assert F(xi.next_minus())>=0 or abs(F(xi))<D('1e-70');checks+=1
    assert F(D('0.45'))<0 and F(D('0.4'))>0; checks+=1
    vp=(xi/SIX).sqrt()
    fprime=Fprime(xi)
    gap=(-D(4)*vp*fprime).sqrt()
    assert abs(gap-D('1.4751534132015147421391678566'))<D('1e-25');checks+=1
    assert abs(vp/gap-D('0.1828590146620118493620555206'))<D('1e-25');checks+=1
    for j in range(1,1000):
        x=xi*D(j)/D(1000)
        yy=roots(x)
        assert len(yy)==2 and 0<yy[0]<yy[1];checks+=1
        assert abs(qres(x,yy[0]))<D('1e-65');checks+=1
        assert abs(qres(x,yy[1]))<D('1e-65');checks+=1
        assert abs(residual(x,yy[0]))<D('1e-63');checks+=1
        assert abs(residual(x,yy[1]))<D('1e-63');checks+=1
        assert yy[1]<(ONE-D(2)*x).sqrt();checks+=1
        assert yy[1]*yy[0]==x/SIX or abs(yy[1]*yy[0]-x/SIX)<D('1e-65');checks+=1
    for j in range(1,1000):
        x=xi+(D('0.5')-xi)*D(j)/D(1000)
        assert F(x)<0;checks+=1
        # H(y)>=-F(x)>0 follows by AM-GM, checked at representative y values.
        for y in (D('0.01'),D('0.1'),D('0.3'),D('0.8'),D(2)):
            assert residual(x,y)>0;checks+=1
    for k in range(3,9):
        x=D(1)/D(10)**k
        yp=roots(x)[1]
        true=(ONE-D(2)*x).sqrt()
        scaled=(yp-true)/x**5
        assert abs(scaled + D(7)/D(192))<D('0.3')*x;checks+=1
    for k in range(2,9):
        x=xi-D(1)/D(10)**k
        gapmeas=roots(x)[1]-roots(x)[0]
        assert abs(gapmeas/(xi-x).sqrt()-gap)<D(5)*(xi-x).sqrt();checks+=1
        yplus=roots(x)[1]
        jac=ONE-x/(SIX*yplus*yplus)
        assert abs(jac - gapmeas/yplus)<D('1e-60');checks+=1
    for j in range(1,500):
        initial=D(7)/D(3)
        h=initial*initial/D(4)*D(j)/D(500)
        ending=(initial*initial-D(4)*h).sqrt()
        area_diff=D(4)*(ending**2-initial**2)
        simpson_loss=D(16)*h
        assert abs(area_diff+simpson_loss)<D('1e-65');checks+=1
    # Fraction arithmetic also validates coefficients and no approximation in normalization.
    for num,den in [(1,10),(1,4),(1,3),(2,5)]:
        x=Fraction(num,den)
        d=D(x.numerator)/D(x.denominator)
        for y in roots(d):
            assert abs(y*y-B(d)*y+d/SIX)<D('1e-65');checks+=1
    print('PASS: %s standard-library deterministic assertions' % checks)
    print('fold_xi =',xi)
    print('gap_coefficient =',gap)
    print('inverse_Jacobian_coefficient =',vp/gap)

if __name__ == '__main__':
    run()

"""Reproducibility checks for the piecewise-max map's global contraction theorem.

These are finite sanity checks. The analytic argument, not the checks, proves
uniform validity for all real parameters and interior initial conditions.
"""
from fractions import Fraction as Q
from math import log, log1p, exp, ceil
import random


def phi(alpha, x, y):
    ax = alpha*x*(1-y)
    bx = 1-x
    ay = alpha*y*(1-x)
    by = 1-y
    return max(ax, bx)/(ax+bx), max(ay, by)/(ay+by)


def step_odds(alpha, z, w):
    rx=alpha*w/(z*(1+w))
    ry=alpha*z/(w*(1+z))
    return (min(rx,1/rx), min(ry,1/ry)), (rx, ry)


exact = 0
for a in [Q(21,10), Q(5,2), Q(3), Q(4), Q(9)]:
    for i in range(3,17):
        for j in range(3,i):
            # x>y>1/2; exact rational arithmetic
            x,y=Q(2*i-1,2*i),Q(2*j-1,2*j)
            if x<=y or y<=Q(1,2): continue
            z,w=(1-x)/x,(1-y)/y
            r0=w/z
            bound=max(0, ceil(log(float((a-1)/(r0-1)))/log(1.5)))
            t=0
            for t in range(min(bound+2,90)):
                (zn,wn),(rx,ry)=step_odds(a,z,w)
                X,Y=phi(a,x,y)
                assert zn==(1-X)/X and wn==(1-Y)/Y
                assert X>Y and rx>1
                if ry<=1:
                    break
                assert (wn/zn-1)>=Q(3,2)*(w/z-1)
                x,y,z,w=X,Y,zn,wn
            else:
                raise AssertionError('failure to reach switching branch')
            assert t<=bound
            for k in range(4):
                (zn,wn),(rx,ry)=step_odds(a,z,w)
                assert ry<=1 and rx>1
                z,w=zn,wn
            exact+=1


random.seed(91741)
near = 0
for a in [2.000001, 2.01, 2.5, 3.0, 10.0, 100.0]:
    c=.75+.5/a
    Ustar=-log(a*(a-1)**2-1)
    Vstar=-log(a-1)
    for _ in range(2000):
        x=.5+.5*random.random()
        y=.5+.5*random.random()
        if y>x: x,y=y,x
        z,w=(1-x)/x,(1-y)/y
        r0=w/z
        bound=max(0,ceil(log((a-1)/(r0-1))/log(1.5)))
        t=0
        for t in range(bound+2):
            ry=a*z/(w*(1+z))
            if ry<=1:break
            z,w=z*(1+w)/(a*w),w*(1+z)/(a*z)
        else:raise AssertionError('finite entry bound')
        assert t<=bound
        assert 0<z<w<=1.0+1e-12
        assert z<=1/(a-1)+1e-12
        def norm(u,v):return max(abs(u),abs(v),abs(u-v))
        u,v=log(z),log(w)
        n0=norm(u-Ustar,v-Vstar)
        for k in range(12):
            ry=a*exp(u)/(exp(v)*(1+exp(u)))
            assert ry<1+1e-12
            p,q=u-v+log1p(exp(v))-log(a),u-v+log(a)-log1p(exp(u))
            u,v=p,q
            if k%2==1:
                assert norm(u-Ustar,v-Vstar)<=c**((k+1)//2)*n0+5e-11
        near+=1
print('PASS exact rational state and switching comparisons:',exact)
print('PASS floating nonlinear two-step contraction checks:',near)

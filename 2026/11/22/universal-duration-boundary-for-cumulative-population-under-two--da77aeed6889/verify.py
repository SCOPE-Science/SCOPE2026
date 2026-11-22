#!/usr/bin/env python3
"""Independent deterministic checks for an equal-duration switched logistic model.

All integrated abundances use the dimensionless time z=r*t.  These
calculations are evidence for explicit formulas; they do not certify the
infinite-domain uniqueness theorem, which requires the analytic proof.
"""
import math
from fractions import Fraction

COUNT = 0


def check(condition, message):
    global COUNT
    if not condition:
        raise AssertionError(message)
    COUNT += 1


def inverse_after(y, K, h):
    return math.exp(-h)*y + (1-math.exp(-h))/K


def one_stage(y, K, h):
    return K * math.log1p((math.expm1(h))/(K*y))


def score(y, kh, kl, h, high_first):
    first, second = (kh, kl) if high_first else (kl, kh)
    return one_stage(y, first, h) + one_stage(inverse_after(y, first, h), second, h)


def inverse_path(y, kh, kl, h, z, high_first):
    first, second = (kh, kl) if high_first else (kl, kh)
    if z <= h:
        return inverse_after(y, first, z)
    return inverse_after(inverse_after(y, first, h), second, z-h)


def simpson(f, start, end, n=1200):
    step = (end-start)/n
    value = f(start)+f(end)
    for i in range(1,n):
        value += (4 if i%2 else 2)*f(start+i*step)
    return value*step/3


def first_weight(z, y, kh, kl, h):
    a = inverse_path(y, kh, kl, h, z, True)
    b = inverse_path(y, kh, kl, h, z, False)
    return 1/(a*b)


def difference_coefficient(z, h):
    u = math.exp(-h)
    if z <= h:
        return -math.expm1(-z)
    return (2-u)*math.exp(-(z-h))-1


def ratio(y, kh, kl, h):
    zstar = h + math.log(2-math.exp(-h))
    plus = simpson(lambda z: difference_coefficient(z,h)*first_weight(z,y,kh,kl,h),0,zstar,300)
    minus = simpson(lambda z: -difference_coefficient(z,h)*first_weight(z,y,kh,kl,h),zstar,2*h,300)
    return minus/plus


# Exact finite witness: E=3, K_H=2, K_L=1, y=7.
E=Fraction(3); Y=Fraction(7)
qh=Fraction(1,3)
a_end = qh*Y+(1-qh)/2
b_end = qh*Y+(1-qh)
# Stage integral = K*log((E+K*y-1)/(K*y)); compare products before log.
prod_HL = ((E+2*Y-1)/(2*Y))**2 * ((E+a_end-1)/a_end)
prod_LH = ((E+Y-1)/Y) * ((E+2*b_end-1)/(2*b_end))**2
check(prod_HL==prod_LH==Fraction(16,7),'exact equal integrated outputs')

hcrit=math.log1p(math.sqrt(2))
check(abs(hcrit-0.881373587019543)<1e-13,'universal critical duration')

# Polynomial identity for the limiting difference, checked at rational E.
for E_integer in range(2,100):
    E=Fraction(E_integer)
    A_first=(E-1)**2/2
    A_second=E**2*((2-1/E)*(E-1)-(E**2-1)/2)
    closed=-(E-1)**2*(E**2-2*E-1)/2
    check(A_first+A_second==closed,'exact limiting integral identity')

for kh,kl in ((2.,1.), (3.,0.7), (1.2,.8), (17.,2.)):
    for h in (.13,.4,.8,.8813,.881374,.98,math.log(3),1.3,2.):
        change=h+math.log(2-math.exp(-h))
        check(h<change<2*h,'crossing strictly in second stage')
        # Pointwise comparison and exact analytic difference of inverse populations.
        for y in (1e-2,.03,.1,.3,1,3,7,30,100,1000):
            for i in range(1,200):
                z=2*h*i/200
                D = (1-math.exp(-z)) if z<=h else (2-math.exp(-h))*math.exp(-(z-h))-1
                got=inverse_path(y,kh,kl,h,z,False)-inverse_path(y,kh,kl,h,z,True)
                check(abs(got-(1/kl-1/kh)*D)<=2e-12*(1+abs(got)), 'pointwise inverse difference')
                check((got>0) if z<change-1e-8 else ((got<0) if z>change+1e-8 else True), 'one sign change in time')
        # Exact stage formula versus independent quadrature of both trajectories.
        for y in (.2,3,30):
            for high_first in (True,False):
                exact=score(y,kh,kl,h,high_first)
                numeric=simpson(lambda z: 1/inverse_path(y,kh,kl,h,z,high_first),0,h,1400)+simpson(lambda z: 1/inverse_path(y,kh,kl,h,z,high_first),h,2*h,1400)
                check(abs(exact-numeric)<5e-9*(1+abs(exact)), f'integral mismatch K={kh,kl} h={h} y={y} hi={high_first}: exact={exact}, numeric={numeric}, delta={exact-numeric}')
        # Terminal abundance is larger for low first (high last).
        for y in (.1,1.,7.,100.):
            check(inverse_path(y,kh,kl,h,2*h,True)>inverse_path(y,kh,kl,h,2*h,False),'universal endpoint ordering')
        # Compare signs of integrated quantity on a grid of initial values.
        values=[]
        for y in (0.0001,.001,.01,.1,1.,3.,7.,30.,100.,1e3):
            d=score(y,kh,kl,h,True)-score(y,kh,kl,h,False)
            values.append(d)
            if h<=hcrit-1e-8:
                check(d > -2e-12,'short-time ranking')
        # As y increases, ratio of negative to positive time contributions strictly increases.
        ys=(.01,.04,.2,1.,5.,25.,100.)
        rs=[ratio(y,kh,kl,h) for y in ys]
        for r1,r2 in zip(rs,rs[1:]):
            check(r1<r2,'negative-positive weight ratio increases with inverse initial size')

# Strict numerical sign checks for an exactly described crossover.
ln3=math.log(3)
check(abs(score(7.,2.,1.,ln3,True)-math.log(16/7))<1e-13,'exact critical initial population HL')
check(abs(score(7.,2.,1.,ln3,False)-math.log(16/7))<1e-13,'exact critical initial population LH')
check(score(10.,2.,1.,ln3,True)<score(10.,2.,1.,ln3,False),'below threshold population prefers low first')
check(score(2.,2.,1.,ln3,True)>score(2.,2.,1.,ln3,False),'above threshold population prefers high first')

print('PASS:',COUNT,'deterministic assertions')
print('critical dimensionless duration:',format(hcrit,'.15f'))
print('exact tie: initial N=1/7, duration tau=log(3), high K=2, low K=1')
print('common integrated biomass:',format(math.log(16/7),'.15f'))
print('N=0.1: HL',score(10.,2.,1.,ln3,True),'LH',score(10.,2.,1.,ln3,False))
print('N=0.5: HL',score(2.,2.,1.,ln3,True),'LH',score(2.,2.,1.,ln3,False))

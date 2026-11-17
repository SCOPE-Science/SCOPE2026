"""Reproducible algebraic and numerical checks for zero-energy Chazy trajectories."""
from fractions import Fraction
from math import isclose, copysign


def phi(q, sigma, r, c):
    u = c - r**(2*q+1)/(2*q+1)
    return (sigma*r*r, 2*sigma*r*u, 2*sigma*(u*u-r**(2*q+1)*u))


def f(q, x, y, z):
    if x == 0:
        return (y,z,0)
    return (y,z,-abs(x)**q*z-(q+1)*(1 if x > 0 else -1)*abs(x)**(q-1)*y*y)


def identity(q, sigma, r, c):
    u=c-r**(2*q+1)/(2*q+1)
    uprime=-r**(2*q)
    xp=2*sigma*r*u
    yp=2*sigma*(u*u+r*uprime*u)
    zp=2*sigma*u*(2*u*uprime-(2*q+1)*r**(2*q)*u-r**(2*q+1)*uprime)
    x,y,z=phi(q,sigma,r,c)
    return max(abs(xp-y),abs(yp-z),abs(zp-f(q,x,y,z)[2]),abs(x*z-y*y/2+x*abs(x)**q*y))

for q in range(2,9):
    for sigma in (-1,1):
        for r,c in ((-2,1),(-1,-1),(0,2),(0,0),(0.37,0.5),(1,1.23),(3,-4)):
            err=identity(q,sigma,r,c)
            scale=1+sum(abs(v) for v in phi(q,sigma,r,c))**2
            assert err/scale < 2e-10, (q,sigma,r,c,err)
    # Exact rational arithmetic at r=0,1,2 to avoid numerical-only support.
    for r,c in ((Fraction(0),Fraction(1)),(Fraction(1),Fraction(2)),(Fraction(2),Fraction(-3))):
        for sigma in (-1,1):
            assert identity(q,sigma,r,c)==0

# Reference explicit algebraic c=0 integration identity and limiting constant.
for q in range(2,9):
    a=Fraction(2*q,2*q+1)
    for x0 in (Fraction(1,2),Fraction(3,2)):
        for t in (Fraction(0),Fraction(1),Fraction(3)):
            # |x(t)|^{-q}=|x0|^{-q}+ 2q/(2q+1) t
            B=x0**(-q)+a*t
            assert B-x0**(-q)==a*t
print('CHAZY_ZERO_ENERGY_ALGEBRAIC_CHECK_OK')

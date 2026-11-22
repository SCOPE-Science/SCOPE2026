"""Standalone arithmetic checks of the scalar first-update formulas.

Python 3.10+, standard library only. Finite tests complement, not replace, proof.
"""
from fractions import Fraction as Q
from math import exp, log, isclose
import random


def coefficients(k):
    return ((3*k-1)/(k-3), 4*(1-k)/(k-3), Q(1)), (
        2*k*k/(3+2*k-k*k), 4*k/(3+2*k-k*k), 2/(3+2*k-k*k))


def parts(z):
    e=exp(-z)
    return 4*e-1, 2-4*z*e, 3-2*z-4*e


def F(z,k):
    a,b,c=parts(z)
    return a+k*b+k*k*c


def recurrence(z,k):
    alpha,beta=coefficients(k)
    return -(float(alpha[1])+z*float(beta[1]))*exp(-z)/(1+z*float(beta[2]))-(float(alpha[0])+z*float(beta[0]))/(1+z*float(beta[2]))


def bisection(f,lo,hi):
    assert f(lo)*f(hi)<0
    for _ in range(120):
        mid=(lo+hi)/2
        if f(lo)*f(mid)<=0:hi=mid
        else:lo=mid
    return (lo+hi)/2


# Exact rational coefficient normalization and second-order consistency.
for i in range(101):
    k=Q(i,101)
    a,b=coefficients(k)
    assert sum(a)==0
    assert sum(b)==sum(Q(j)*a[j] for j in range(3))
    assert 2*sum(Q(j)*b[j] for j in range(3))==sum(Q(j*j)*a[j] for j in range(3))

# The first-output identity must agree with the original recurrence independently.
random.seed(271828)
for i in range(8000):
    z=10*random.random()
    k=random.random()
    d=3+2*k-k*k+2*z
    assert isclose(recurrence(z,k),F(z,k)/d,rel_tol=2e-11,abs_tol=3e-13)

# Root and vertex, both computed from the source coefficients.
def discr(z):
    a,b,c=parts(z)
    return b*b-4*a*c

zs=bisection(discr,log(4),2)
a,b,c=parts(zs)
ks=-b/(2*c)
assert 0<ks<1 and abs(F(zs,ks))<2e-12
assert abs(discr(zs))<2e-12
assert abs(zs-1.5172147403362556)<1e-12
assert abs(ks-.3668716351624039)<1e-12

# Direct sign boundaries and unique max along a dense rational parameter grid.
for j in range(1001):
    k=j/1001
    z=bisection(lambda zz:F(zz,k),0,10)
    assert z<=zs+2e-12
    assert F(z-.0001,k)>0
    assert F(z+.0001,k)<0

zc=(2-log(4))/(2*(log(4)-1))
assert .794<zc<.795
for k in [0, .2, ks, .5, zc, .8, .99]:
    z=bisection(lambda zz:F(zz,k),0,10)
    if k not in (0,zc):
        assert (z>log(4))==(k<zc)
    else:
        assert abs(z-log(4))<2e-12
print('VERIFY_OK 101 exact-rational identities; 8,000 recurrence checks; 1,001 boundaries')

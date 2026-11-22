"""Exact rational certificates and supplementary numerical checks for a two-site founding allocation theorem.
Run with Python 3 standard library: python check.py
"""
from fractions import Fraction as Q
from math import factorial, exp, isfinite


def e_interval(N=20):
    lo=sum((Q(1, factorial(k)) for k in range(N+1)), Q(0))
    hi=lo+Q(2,factorial(N+1))
    return lo,hi

ELO,EHI=e_interval()
assert EHI>ELO>2

def power(k):
    """Exact rational bounds on exp(integer k); k may be negative."""
    if k>=0: return ELO**k, EHI**k
    return EHI**k, ELO**k

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    z=[a[i]*b[j] for i in (0,1) for j in (0,1)]
    return min(z),max(z)
def c(z):return z,z

def scale(z,q):return mul(z,c(Q(q)))

checks=0

def assert_less(a,b):
    global checks
    assert a[1]<b[0],(a,b)
    checks+=1

# Q(u)=1/2[(5/u-1)e^(5+u)-(5/u+1)e^(5-u)], for u>0.
def Q_u(u):
    v=Q(u)
    return add(scale(power(5+u),(Q(5,1)/v-1)/2),
               scale(power(5-u),-(Q(5,1)/v+1)/2))

assert_less(c(Q(0)),c(Q(1)))
assert_less(c(Q(4)),c(Q(5)))
assert_less(scale(power(5),4),c(Q(799)))
assert_less(Q_u(2),c(Q(799)))
assert_less(c(Q(799)),Q_u(3))
assert_less(c(Q(799)),Q_u(4))
assert Q_u(5)==c(Q(-1))

# f(x)=[1+799(1+x)e^-x]/800, F(x)=f(x)f(10-x).
def f_of_int(x):
    return scale(add(c(Q(1)),scale(power(-x),799*(1+x))),Q(1,800))

def F_of_int(x):return mul(f_of_int(x),f_of_int(10-x))
assert_less(F_of_int(3),F_of_int(0))
assert_less(F_of_int(3),F_of_int(5))
assert_less(F_of_int(3),F_of_int(2))

# Independent numerical derivative and exact formula diagnostics, not existence proof.
q=799/800

def fnum(x):return 1-q+q*(1+x)*exp(-x)
def Fnum(x):return fnum(x)*fnum(10-x)
def numQ(u):return exp(5)*(5*__import__('math').sinh(u)/u-__import__('math').cosh(u))

def numder(x):
    y=10-x
    return Fnum(x)*(y/(1+y+(1-q)/q*exp(y)) - x/(1+x+(1-q)/q*exp(x)))

for i in range(1,250):
    x=5*i/250
    h=2e-5
    fd=(Fnum(x+h)-Fnum(x-h))/(2*h)
    assert abs(numder(x)-fd)<1e-9, (x,fd,numder(x))
    checks+=1

lo,hi=2.,3.
for _ in range(80):
    mid=(lo+hi)/2
    if numQ(mid)<799:lo=mid
    else:hi=mid
u=(lo+hi)/2
xstar=5-u
assert 2<xstar<3
assert Fnum(xstar)<Fnum(3)<min(Fnum(0),Fnum(5))
checks+=3
print(f'CERTIFIED_OK exact_rational_sign_checks=9 numerical_assertions={checks-9}')
print('Euler e rational interval width <=',float(EHI-ELO))
print('optimum x=',format(xstar,'.15f'), 'success=',format(1-Fnum(xstar),'.15f'))
print('failure one-site=',format(Fnum(0),'.15f'),'equal=',format(Fnum(5),'.15f'))

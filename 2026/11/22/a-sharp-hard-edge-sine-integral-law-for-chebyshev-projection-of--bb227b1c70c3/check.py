"""Reproducible numerical and symbolic-identity checks for Chebyshev BV projection error.

Only standard Python is required. Numerical checks corroborate rather than prove
uniform convergence, compactness, or uniqueness of the limiting maximizer.
"""
from math import pi, cos, sin, sqrt, factorial
from fractions import Fraction

# Rational alternating-series enclosures certify G(2)>4/3.
def atan_trunc(z, upper):
    # even final index = upper, odd final index = lower for 0 < z < 1.
    m = 8 if upper else 9
    return sum(((-1)**k*z**(2*k+1)/Fraction(2*k+1) for k in range(m+1)), Fraction(0))

pi_lower=16*atan_trunc(Fraction(1,5), False)-4*atan_trunc(Fraction(1,239), True)
cos2_upper=sum(((-1)**k*Fraction(2)**(2*k)/factorial(2*k) for k in range(7)),Fraction(0))
si2_upper=sum(((-1)**k*Fraction(2)**(2*k+1)/(Fraction(2*k+1)*factorial(2*k+1)) for k in range(7)),Fraction(0))
assert pi_lower > Fraction(314159,100000)
assert cos2_upper < Fraction(-416,1000)
assert si2_upper < Fraction(1606,1000)
assert 1-cos2_upper+pi_lower-2*si2_upper>Fraction(4,3)

count=0
def check(test, info=''):
    global count
    assert test, info
    count+=1

def si(z, terms=40):
    # Entire alternating Taylor series, rapidly convergent for 0 <= z <= 2.
    s=0.0
    for k in range(terms):
        s+=(-1)**k*z**(2*k+1)/((2*k+1)*factorial(2*k+1))
    return s

def bisect_root(fun,lo,hi,steps=80):
    check(fun(lo)*fun(hi)<0, 'unbracketed root')
    left_sign=1 if fun(lo)>0 else -1
    for _ in range(steps):
        mid=(lo+hi)/2
        if fun(mid)*left_sign>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

c0=bisect_root(lambda c:si(c)-pi/2,1.9,2)
Gstar=1-cos(c0)
check(1.92644<c0<1.92646)
check(1.34819<Gstar<1.34822)
check(Gstar>4/3)
check(1+1/pi<4/3)

def E2(n,theta):
    # Exact finite expression obtained from sum_{k>=1}(1-cos(2k theta))/k^2.
    return (pi*theta-theta*theta-sum((1-cos(2*k*theta))/(k*k) for k in range(1,n+1)))/(pi*pi)

def deriv(n,theta):
    return (pi-2*theta-2*sum(sin(2*k*theta)/k for k in range(1,n+1)))/(pi*pi)

# Degree zero is a median-step sharp L2 error of 1/2.
check(abs(E2(0,pi/2)-.25)<1e-13)
for n in range(0,18):
    for j in range(0,80):
        t=pi*j/160
        check(abs(E2(n,t)-E2(n,pi-t))<5e-13)
        # Compared with a directly truncated positive Parseval tail.
        M=30000
        direct=sum((1-cos(2*k*t))/(k*k) for k in range(n+1,M+1))/(pi*pi)
        check(abs(E2(n,t)-direct)<2/(pi*pi*M)+1e-10)
for n in (1,2,3,5,10,20,40,80,160,320):
    # The first stationary point is close to c0/(2n); it lies in (0, 1.3/n).
    hi=min(pi/2,1.3/n)
    root=bisect_root(lambda t:deriv(n,t),1e-12,hi)
    check(abs(deriv(n,root))<3e-11)
    if n>=20:
        check(abs(2*n*root-c0)<2/n)
        check(abs(n*E2(n,root)-Gstar/(pi*pi))<0.15/n)
    print('n=',n,' theta=',round(root,10),' n E_n^2=',round(n*E2(n,root),10))

print('c_*=',format(c0,'.14f'))
print('G_*=',format(Gstar,'.14f'))
print('lim sqrt(n) E_n=',format(sqrt(Gstar)/pi,'.14f'))
print('total successful assertions:',count)

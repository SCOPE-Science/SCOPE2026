#!/usr/bin/env python3
"""Supplementary exact-rational checks for low-degree spherical Bernstein identities.
The all-degree positivity assertions are proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from math import comb

def legendre_half(n):
    a,b=F(1),F(1,2)
    if n==0:return a
    if n==1:return b
    for k in range(1,n):
        a,b=b, ((2*k+1)*F(1,2)*b-k*a)/(k+1)
    return b

assert [legendre_half(k) for k in range(8)] == [F(1),F(1,2),-F(1,8),-F(7,16),-F(37,128),F(23,256),F(331,1024),F(457,2048)]
# Absolute Legendre bound: average of (1/4+3/4 cos^2 t)^4.
I8=sum(F(comb(4,j), 4**(4-j))*F(3,4)**j*F(comb(2*j,j),4**j) for j in range(5))
assert I8==F(10643,32768) and I8<F(1,3)
# Cubic asin coefficients: compare a_n and coefficient of A(u)^3.
a=[F(comb(2*n,n),4**n*(2*n+1)) for n in range(23)]
assert a[0]==1
rchecks=0
for n in range(1,22):
    c=sum((a[i]*a[j]*a[n-1-i-j] for i in range(n) for j in range(n-i)),F(0))
    expected=6*sum((F(1,(2*j-1)**2) for j in range(1,n+1)),F(0))
    assert c/a[n]==expected
    rchecks+=1
# At n=4 and theta=pi/2, Bernstein weights are [1,4,6,4,1]/16.
# P_6(1)=1; P_6(1/sqrt(2))=-19/128; P_6(0)=-5/16.
B4P6=(2+8*(-F(19,128))+6*(-F(5,16)))/16
assert B4P6==-F(17,256)
# Cos(pi/5)^5=(11+5 sqrt(5))/64, hence (1-3 cos^5)/4<0
assert 15**2*5>31**2
# For the circle n>=3, B_n[cos(2 theta)](pi/2)=-cos(pi/n)^n<0.
# Check exact n=3 boundary.
assert -F(1,2)**3==-F(1,8)
# Check all low Legendre odd/even bounds, then the analytic integral bound covers degrees>=8.
for m in range(8):
    p=legendre_half(m)
    if m%2==0: assert -F(1,3)<=p<=1
    else: assert -1<=p<=F(1,2)
# Identity F_even=(1+3p)/4 + 3(1-p)y^2,
# F_odd=3(1+p)y/2+(2-6p)y^3, using samples 1,p,+/-p,+/-1.
from math import comb
for p in [F(-1,2),-F(1,3),F(0),F(1,2),F(1)]:
  for odd in [False,True]:
    samples=[F(1),p,-p if odd else p,F(-1) if odd else F(1)]
    for y in [F(-1,2),F(-1,4),F(0),F(1,4),F(1,2)]:
      x=F(1,2)-y
      lhs=sum(F(comb(3,j))*x**j*(1-x)**(3-j)*samples[j] for j in range(4))
      rhs=(F(3,2)*(1+p)*y+(2-6*p)*y**3) if odd else ((1+3*p)/4+3*(1-p)*y*y)
      assert lhs==rhs
print('CHECK_OK exact_legendre_low=8 integral_bound=1 asin_cubic_ratios=%d cubic_identity_grid=50 negative_witnesses=3'%rchecks)

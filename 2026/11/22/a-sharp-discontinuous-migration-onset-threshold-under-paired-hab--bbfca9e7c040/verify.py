#!/usr/bin/env python3
"""Supplementary exact and numerical checks for a two-habitat seasonal-block theorem."""
from fractions import Fraction as F
from math import sqrt

def mul(A,B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))

def R(a,b,s,m):
    # R squared is the positive root of z^2-c*s*m*(1-m)*z-(u^2-v^2)^2=0.
    c=(a+b)**2/(a*b)
    p=c*s*m*(1-m)
    w=((1-m)**2-(s*m)**2)**2
    z=(p+sqrt(p*p+4*w))/2
    return sqrt(z)

def H(c,s,m):
    return (4-c*s)+(c*s+2*s*s-6)*m+4*(1-s*s)*m*m-(1-s*s)**2*m*m*m

def Hprime(c,s,m):
    return c*s+2*s*s-6+8*(1-s*s)*m-3*(1-s*s)**2*m*m

def minH(c,s):
    # Since H''>0 on [0,1], bisection finds its unique possible minimum.
    if Hprime(c,s,0)>=0: return H(c,s,0),0.0
    if Hprime(c,s,1)<=0: return H(c,s,1),1.0
    l,h=0.0,1.0
    for _ in range(65):
        m=(l+h)/2
        if Hprime(c,s,m)>0: h=m
        else: l=m
    m=(l+h)/2
    return H(c,s,m),m

def threshold(c):
    l,h=0.,4./c
    for _ in range(70):
        s=(l+h)/2
        if minH(c,s)[0]>0: l=s
        else: h=s
    s=(l+h)/2
    return s,minH(c,s)[1]

checks=0
# Exact matrix characteristic identity: tr(K)=(a+b)^2 s m(1-m);
# det(K)=-(ab)^2[(1-m)^2-(sm)^2]^2.
for a in [F(5,4),F(2),F(3),F(7)]:
 for b in [F(1,3),F(1)]:
  if a<=b: continue
  for s in [F(1,10),F(1,2),F(3,4),F(1)]:
   for m in [F(0),F(1,7),F(1,3),F(1,2),F(4,5),F(1)]:
    M=((1-m,s*m),(s*m,1-m)); D=((a,0),(0,b));J=((0,1),(1,0))
    V=mul(M,D);K=mul(J,mul(V,V))
    t=K[0][0]+K[1][1];det=K[0][0]*K[1][1]-K[0][1]*K[1][0]
    expected_t=(a+b)**2*s*m*(1-m)
    expected_det=-(a*b)**2*((1-m)**2-(s*m)**2)**2
    assert t==expected_t and det==expected_det
    c=(a+b)**2/(a*b)
    assert 1-t/(a*b)+det/(a*b)**2 == m*H(c,s,m)
    checks+=1
# Exact rational witness: for a=3,b=1,s=3/4,m=1/3, strictly profitable migration.
c=F(16,3)
assert H(c,F(3,4),F(1,3))==F(-721,6912)
checks+=1
# Degenerate double-root certificate (c is a realizable fitness contrast >4).
# c=180 sqrt(7)/49, s=1/sqrt(7), m=1/3.
# Their products are rational and reduce to cs=180/49 and s^2=1/7.
x=F(1,3);z=F(1,7);cs=F(180,49)
certH=(4-cs)+(cs+2*z-6)*x+4*(1-z)*x*x-(1-z)**2*x*x*x
certD=(cs+2*z-6)+8*(1-z)*x-3*(1-z)**2*x*x
assert certH==0 and certD==0
checks+=2
# Independent numeric comparisons: direct Perron root of K vs polynomial root.
for a,b in [(2.,1.),(3.,1.),(11.,1.)]:
 c=(a+b)**2/(a*b)
 s0,m0=threshold(c)
 assert 0<s0<4/c and 0<m0<1
 assert abs(H(c,s0,m0))<5e-13 and abs(Hprime(c,s0,m0))<5e-13
 for s in [max(0.00001,s0-0.04),s0,min(1.,s0+0.04),1.]:
  for j in range(1,100):
   m=j/100
   v=R(a,b,s,m)
   if s < s0-0.02: assert v<1+1e-10
   if s==s0: assert v<=1+3e-11
   assert (v>1)==(H(c,s,m)<0) or abs(v-1)<1e-12
   checks+=1
print('VERIFY_OK',checks,'test cases')
print('c=16/3 s_star=%.15f m_star=%.15f'%threshold(F(16,3)))

"""Reproducible checks for two independent Hermite-STFT disk localization channels.
Uses analytic radial densities and independent numerical quadrature (mpmath).
Finite checks corroborate, but do not replace, the all-level algebraic proof.
"""
from math import factorial, sqrt, exp
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 40

checks=0

def ck(x,msg):
 global checks
 checks+=1
 if not x: raise AssertionError(msg)

def poisson(k,s): return mp.exp(-s)*s**k/mp.factorial(k)
def q0(k,s): return mp.gammainc(k+1,0,s)/mp.factorial(k)
def q1(k,s):
 return mp.quad(lambda t: mp.exp(-t)*(t if k==0 else t**(k-1)*(k-t)**2/mp.factorial(k)), [0,s])
def e(k,s,rho): return rho*q0(k,s)+q1(k,s)
def closed(k,s,rho): return (1+rho)*q0(k,s)+(k-s)*poisson(k,s)
def gap(k,s,rho):
 return poisson(k,s)/(k+1)*((s-k)*(s-k-1)+rho*s)

rhos=[mp.mpf(0),mp.mpf('0.01'),mp.mpf('0.04'),mp.mpf('0.0625'),mp.mpf('0.15'),mp.mpf('0.5'),mp.mpf(1),mp.mpf(2)]
radii=[mp.mpf('0.07'),mp.mpf('0.31'),mp.mpf('0.83'),mp.mpf(1),mp.mpf('1.25'),mp.mpf('1.78'),mp.mpf(2),mp.mpf('2.3'),mp.mpf('3.6'),mp.mpf(4),mp.mpf('5.25'),mp.mpf('8.7')]
for rho in rhos:
 for s in radii:
  for k in range(10):
   ck(abs(e(k,s,rho)-closed(k,s,rho))<mp.mpf('1e-30'),('integral',str(rho),str(s),k))
   ck(abs(e(k,s,rho)-e(k+1,s,rho)-gap(k,s,rho))<mp.mpf('1e-30'),('gap',str(rho),str(s),k))
   if rho>0 and s!=int(s):
    if not k<s<k+1:
     ck(gap(k,s,rho)>0,('off-diagonal-inversion',str(rho),str(s),k))

# Exact polynomial certification of discriminant, threshold, crossings.
import sympy as sp
s,R,k=sp.symbols('s R k',real=True)
P=(s-k)*(s-k-1)+R*s
ck(sp.simplify(P-(s*s+(R-2*k-1)*s+k*(k+1)))==0,'quadratic')
ck(sp.simplify(sp.discriminant(P,s)-((R-1)**2-4*R*k))==0,'discriminant')
for kk in range(1,31):
 threshold=(sqrt(kk+1)-sqrt(kk))**2
 vertex=sqrt(kk*(kk+1))
 check=(vertex-kk)*(vertex-kk-1)+threshold*vertex
 ck(abs(check)<1e-11,('tangent',kk))
 ck(kk<vertex<kk+1,('interval',kk))

# For positive ratios, exactly the permitted indices can invert; boundary equality is tangency.
for numerator,denominator in [(1,2),(1,8),(1,16),(1,40),(1,100)]:
 rho=numerator/denominator
 for kk in range(1,100):
  eligible = rho<(sqrt(kk+1)-sqrt(kk))**2
  discr=(1-rho)**2-4*rho*kk
  ck(eligible == (discr>1e-10 and rho<1),('index cutoff',rho,kk))
  if eligible:
   minus=(2*kk+1-rho-sqrt(discr))/2
   plus=(2*kk+1-rho+sqrt(discr))/2
   ck(kk<minus<plus<kk+1,('roots',rho,kk))

print('All checks passed:',checks)

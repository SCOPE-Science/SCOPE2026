"""Reproduce exact two-patch functional-response identities and numerical limits.
Run with Python 3 standard library: python checker.py
All assertions here supplement, not replace, the analytic proof.
"""
from fractions import Fraction as Q
from math import sqrt, isclose

def f(x,k):
    return x/(k+x)

def direct_from_roots(a,b,k):
    x,y=a*a,b*b
    return (a*f(x,k)+b*f(y,k))/(a+b)

def closed_from_roots(a,b,k):
    m=(a*a+b*b)/2
    t=a*b
    return 1-k*(k+t)/(k*k+2*k*m+t*t)

def uniform_gap(a,b,k):
    m=(a*a+b*b)/2
    t=a*b
    return k*(m-t)*(k-t)/((k+m)*(k*k+2*k*m+t*t))

count=0
for ai in range(1,21):
 for bi in range(1,ai+1):
  for ki in range(1,20):
   a,b,k=Q(ai,7),Q(bi,11),Q(ki,13)
   if a<b:a,b=b,a
   m=(a*a+b*b)/2
   direct=direct_from_roots(a,b,k)
   exact=closed_from_roots(a,b,k)
   assert direct==exact
   count+=1
   gap=uniform_gap(a,b,k)
   assert direct-f(m,k)==gap
   count+=1
   assert (gap>0)==(a!=b and a*b<k)
   count+=1

for m in [0.1, 0.5, 1, 1.1, 2, 5, 50]:
 for k in [0.2,1,3]:
  def F(d):
   x,y=m+d,m-d
   return (sqrt(x)*f(x,k)+sqrt(y)*f(y,k))/(sqrt(x)+sqrt(y))
  vals=[F(m*i/1000) for i in range(1001)]
  if m<=k:
   assert all(vals[i+1]>vals[i]-1e-14 for i in range(1000))
  else:
   tstar=sqrt(2*k*(k+m))-k
   dstar=sqrt(m*m-tstar*tstar)
   dcross=sqrt(m*m-k*k)
   assert 0<dstar<dcross<m
   assert all(vals[i+1]<vals[i]+1e-13 for i in range(1000) if m*i/1000<dstar and m*(i+1)/1000<dstar)
   assert all(vals[i+1]>vals[i]-1e-13 for i in range(1000) if m*i/1000>dstar)
   assert abs(F(dcross)-F(0))<1e-12
  count+=1

for g in [0.05,0.25,0.5,0.75,0.95]:
 for k in [0.25,1,4]:
  for m in [1.01*g*k/(1-g), 2*g*k/(1-g), 10*g*k/(1-g)]:
   def Fg(d):
    x,y=m+d,m-d
    return (x**g*f(x,k)+y**g*f(y,k))/(x**g+y**g)
   d=1e-3*m
   assert Fg(d)<Fg(0)
   assert Fg(m)>Fg(0)
   count+=2
print('PASS',count,'assertions')

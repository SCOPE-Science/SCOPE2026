#!/usr/bin/env python3
"""Numerical and symbolic checks for the three-interval Fourier-fiber theorem.
Requires numpy and sympy. Finite samples are not an exhaustive proof.
"""
import math
import numpy as np
import sympy as s

count=0
u=s.symbols('u',real=True)
A=256*u**3*(1-u)
B=256*u**3*(1-u)*(3-4*u)**2
assert s.simplify(s.diff(A,u)-256*u*u*(3-4*u))==0;count+=1
assert s.simplify(s.diff(B,u)+256*u*u*(4*u-3)*(24*u*u-32*u+9))==0;count+=1
y0=(8-s.sqrt(10))/12
y1=(8+s.sqrt(10))/12
assert s.simplify(B.subs(u,y0)-(9748+1360*s.sqrt(10))/729)==0;count+=1
assert s.simplify(B.subs(u,y1)-(9748-1360*s.sqrt(10))/729)==0;count+=1
R=(25+5*s.sqrt(5))/2

def vals(t):
 a=64*math.sin(math.pi*t)**4*math.sin(2*math.pi*t)**2
 b=64*math.sin(math.pi*t)**2*math.sin(2*math.pi*t)**2*math.sin(3*math.pi*t)**2
 c=64*math.sin(2*math.pi*t)**4*math.sin(4*math.pi*t)**2
 return a,b,c
assert abs(vals(.25)[0]-16)<1e-12 and abs(vals(.25)[1]-16)<1e-12;count+=1
assert abs(vals(.2)[1]-float(R))<1e-12 and abs(vals(.2)[2]-float(R))<1e-12;count+=1
assert abs(vals(math.asin(math.sqrt(float(y0)))/math.pi)[1]-float(B.subs(u,y0)))<1e-12;count+=1

def cells(d):
 if d<.5: return [((0,d),(0,2,3)),((d,2*d),(0,1,3)),((2*d,1),(0,1,2))]
 if d==.5: return [((0,.5),(0,2,3)),((.5,1),(0,1,3))]
 return [((0,2*d-1),(0,2,4)),((2*d-1,d),(0,2,3)),((d,1),(0,1,3))]

def direct(k,t):
 V=np.exp(2j*np.pi*t*np.outer(k, [0,1,2]))
 return abs(np.linalg.det(V))**2

for d in [.02,.13,.49,.5,.51,.73,.98]:
 for (a,b),k in cells(d):
  assert a < b
  x=(a+b)/2
  true=tuple(i for i in range(5) if any(lo<=x+i<hi for lo,hi in [(0,1),(1+d,2+d),(2+2*d,3+2*d)]))
  assert true==k,(d,x,true,k)
  count+=1
for t in np.linspace(.001,.999,257):
 a,b,c=vals(t)
 for k,expected in [((0,1,2),a),((0,1,3),b),((0,2,3),b),((0,2,4),c)]:
  assert abs(direct(k,t)-expected)<3e-10,(k,t,direct(k,t),expected)
  count+=1
for t in np.linspace(.001,.499,2001):
 a,b,c=vals(t)
 assert min(a,b) <=16+1e-8
 assert b <= float(B.subs(u,y0))+1e-8
 assert min(b,c) <=float(R)+1e-8
 count+=3
print('THREE_INTERVAL_DETERMINANT_CHECKS_PASSED',count)

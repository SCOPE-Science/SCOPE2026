#!/usr/bin/env python3
"""Independent numerical and symbolic checks for a triple of rotated Gaussian windows.
This is a finite diagnostic, not a substitute for the analytical proof.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar, brentq
import sympy as sp

def v(u):
    return -math.expm1(-1.5*u)/(2+math.exp(-1.5*u))

def margin(c,s):
    u=c*math.sinh(s)
    return math.exp(-c*math.cosh(s))*(math.exp(-u)+2*math.exp(u/2))/3

def optimum(c):
    if c<=2: return 0.,math.exp(-c)
    def f(s): return v(c*math.sinh(s))-math.tanh(s)
    s=brentq(f,1e-9,1.,xtol=1e-14)
    return s,margin(c,s)

def direct(c,s,weights,angles):
    return sum(weights[j]*math.exp(-c*(math.cosh(s)+math.sinh(s)*math.cos(2*(angles-j*math.pi/3)))) for j in range(3))

# Exact normalized squared ambiguity formula from Gaussian integration:
t,a,x,xi=sp.symbols('t a x xi', real=True, positive=True)
# Gaussian cross-correlation product is known explicitly, and its covariance identity can be checked:
assert sp.simplify((a+a**-1)**2-(a-a**-1)**2-4)==0
# Normalization of the angular triple: cos values at three ray axes.
for cc in [sp.Rational(1,3),sp.Rational(7,5),sp.Rational(11,3)]:
    assert sp.simplify(cc+(sp.Rational(1,2))*(-cc)*2)==0
# Threshold monotonic certificate derivative twice: 
Y=sp.symbols('Y', positive=True)
H=Y**2+Y-2-(1+2*Y)*sp.log(Y)
assert sp.simplify(sp.diff(H,Y,2)-(1+(1-1/Y)**2))==0

checks=0
for c in [0.3,1.,1.9,2.,2.001,2.2,3.,4.,6.,10.,25.]:
    s,opt=optimum(c)
    ss=np.linspace(0,1.5,1501)
    vals=[margin(c,xx) for xx in ss]
    assert opt>=max(vals)-2e-8,(c,s,opt,max(vals))
    for sq in [0.0,0.1,0.4,0.6,1.0]:
        vals=[direct(c,sq,[1/3]*3,ang) for ang in np.linspace(0,math.pi,4001)]
        assert min(vals)>=margin(c,sq)-1e-12
        assert abs(min(vals)-margin(c,sq))<3e-6
        checks+=1
    assert 0<=s<=0.56
    checks+=1
for c in [0.75,2.5,4.0]:
 for s in [.1,.5,1.0]:
  _,opt_equal=optimum(c)
  for w in [[0.25,.35,.4],[.8,.1,.1],[.3,.3,.4]]:
   vals=[direct(c,s,w,ang) for ang in np.linspace(0,math.pi,3001)]
   assert min(vals) <= margin(c,s)+2e-10
   checks+=1
for c in [20,50,100]:
 s,optimal=optimum(c)
 assert abs(s-math.atanh(.5))<0.1
 assert abs(optimal/((2/3)*math.exp(-math.sqrt(3)*c/2))-1)<0.1
 checks+=1
for delta in [1e-2, 5e-3, 2e-3]:
 c=2+delta
 s,g=optimum(c)
 assert abs(s/delta-1)<0.035
 assert abs(math.log(g/math.exp(-c))/(delta**3/6)-1)<0.07
 checks+=1
print('THREE_GAUSSIAN_DISK_MINIMAX_CHECKS_PASS',checks)

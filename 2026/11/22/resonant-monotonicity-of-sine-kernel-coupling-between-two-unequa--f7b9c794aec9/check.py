"""Independent finite numerical and exact-symbolic checks of sine-kernel two-window identities.
Requires Python 3, numpy, scipy, sympy. No empirical test proves an asymptotic statement.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

assertions = 0

def check(cond, desc):
    global assertions
    if not cond:
        raise AssertionError(desc)
    assertions += 1


def bessel_free_transform(a,b,W):
    return math.sin(W*a)*math.sin(W*b)/W**2


def bessel_free_derivative(a,b,W):
    return (a*math.cos(W*a)*math.sin(W*b)+b*math.sin(W*a)*math.cos(W*b))/(2*W**2) - math.sin(W*a)*math.sin(W*b)/W**3

# Integrate the difference-of-uniforms density exactly as a one-dimensional overlap.
def overlap(s,a,b):
    return max(0.0,min(a/2,b/2+s)-max(-a/2,-b/2+s))


def j(d,a,b,W,deriv=0):
    # u in [-a/2,a/2], v in [-b/2,b/2], s=v-u
    def f(s):
        x=d+s
        if deriv==0:
            return overlap(s,a,b)*(math.sin(W*x)/(math.pi*x))**2
        return overlap(s,a,b)*(W*math.sin(2*W*x)/x**2 -(1-math.cos(2*W*x))/x**3)/math.pi**2
    # overlap piecewise linear: split at the four endpoints
    breaks=sorted({-(a+b)/2, -abs(a-b)/2, abs(a-b)/2, (a+b)/2})
    return sum(quad(f,lo,hi,epsabs=1e-13,epsrel=1e-12,limit=200)[0] for lo,hi in zip(breaks,breaks[1:]))


def approx(d,a,b,W):
    A=bessel_free_transform(a,b,W)
    return (a*b-A*math.cos(2*W*d))/(2*math.pi**2*d**2)


def deriv_approx(d,a,b,W):
    A=bessel_free_transform(a,b,W); Ap=bessel_free_derivative(a,b,W)
    return (W*A*math.sin(2*W*d)/d**2+(-a*b+(A+2*W*Ap)*math.cos(2*W*d))/d**3)/math.pi**2

# Check analytic moment identities: integral of complex exponential over intervals.
a,b,t=sp.symbols('a b t',positive=True,real=True)
B=4*sp.sin(a*t/2)*sp.sin(b*t/2)/t**2
W=sp.symbols('W',positive=True,real=True)
BD=sp.diff(B,t).subs(t,2*W)
closed=(a*sp.cos(a*W)*sp.sin(b*W)+b*sp.sin(a*W)*sp.cos(b*W))/(2*W**2)-sp.sin(a*W)*sp.sin(b*W)/W**3
check(sp.simplify(BD-closed)==0,'Fourier-moment derivative')
check(sp.simplify(B.subs(t,2*W)-sp.sin(a*W)*sp.sin(b*W)/W**2)==0,'Fourier-moment formula')

for a0,b0,w in [(1,1.7,1.3),(math.pi,0.8,1.0),(math.pi,2*math.pi,1.0),(.3,.6,2.5)]:
    for d in [12.2,28.7,67.1]:
        if d<.5*(a0+b0):continue
        exact=j(d,a0,b0,w)
        dx=j(d,a0,b0,w,1)
        diff=(j(d+1e-3,a0,b0,w)-j(d-1e-3,a0,b0,w))/2e-3
        check(abs(diff-dx)<max(3e-10,0.00015*abs(dx)),f'derivative quadrature {a0,b0,w,d}')
        check(abs(exact-approx(d,a0,b0,w))<5*(a0+b0)**2/d**3,'first asymptotic envelope')
        check(abs(dx-deriv_approx(d,a0,b0,w))<3*(a0+b0)**3/d**4,'derivative two-order envelope')

for a0,b0,w in [(1,1.7,1.3),(2,3,0.7)]:
    B0=bessel_free_transform(a0,b0,w)
    for k in range(30,40):
        d0=k*math.pi/(2*w)
        lo=d0-.22/w;hi=d0+.22/w
        z=brentq(lambda d:j(d,a0,b0,w,1),lo,hi)
        check(abs(z-d0)<10/d0,'critical point phase displacement')
        h=0.003
        dd=(j(z+h,a0,b0,w,1)-j(z-h,a0,b0,w,1))/(2*h)
        check(dd*B0*((-1)**k)>0,'alternating critical point type')

# Strongly resonant and singly resonant widths: derivative is eventually negative.
for a0,b0,w in [(math.pi,0.8,1),(math.pi,2*math.pi,1),(1.5,math.pi,1)]:
    for d in [60+k*math.pi/8 for k in range(18)]:
        check(j(d,a0,b0,w,1)<0,'eventual strict monotonicity')

print('SINE_TWO_WINDOW_CHECKS_PASS',assertions)

#!/usr/bin/env python3
"""Independent, finite checks for the specified Fourier-kernel asymptotic.
Requires SymPy and SciPy; numerical tests are not universal proofs."""
import math
import sympy as sp
from scipy.integrate import quad
x=sp.symbols('x',real=True)
f=sp.sqrt(1+sp.sin(x/2)**2)-sp.sin(x/2)-1
series=sp.series(f,x,0,5).removeO().expand()
assert sp.simplify(series.coeff(x,2)-sp.Rational(1,8))==0
assert sp.simplify(series.coeff(x,4)+sp.Rational(7,384))==0
assert sp.simplify(sp.diff(f,x,2).subs(x,0)-sp.Rational(1,4))==0
assert sp.simplify(sp.diff(f,x,4).subs(x,0)+sp.Rational(7,16))==0
fn=sp.lambdify(x,f,'math')
for n in (8,12,20,40,80):
    w=n+.5
    val=quad(lambda t:fn(t)*math.sin(w*t),0,math.pi,
             epsabs=1e-12,epsrel=1e-12,limit=240)[0]/math.pi
    approximation=-1/(4*math.pi*w**3)-7/(16*math.pi*w**5)
    assert abs(val-approximation)*w**7<1.1,(n,val,approximation)
    reflected=quad(lambda t:fn(t)*math.sin((-n-1+.5)*t),0,math.pi,
                   epsabs=1e-12,epsrel=1e-12,limit=240)[0]/math.pi
    assert abs(val+reflected)<5e-11
for j in range(5):
    t=(j+1)/20
    assert abs(fn(math.pi-t)-fn(math.pi+t))<1e-14
print('DISCRETE_HILBERT_CUBIC_CHECKS_PASSED 24')

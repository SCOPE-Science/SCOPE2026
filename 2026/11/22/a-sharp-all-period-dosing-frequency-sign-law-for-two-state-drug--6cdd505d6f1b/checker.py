"""Independent symbolic and numerical examples for a finite-cycle two-state phenotype model.
Run: python checker.py (requires sympy, numpy, scipy)."""
from fractions import Fraction as Q
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

A=sp.Matrix([[0,1],[1,-1]])
B=sp.Matrix([[1,3],[1,-3]])
H=lambda C: C-sp.trace(C)*sp.eye(2)/2
u=sp.simplify(sp.trace(H(A)*H(B))/2)
a2=sp.simplify(sp.trace(H(A)**2)/2)
b2=sp.simplify(sp.trace(H(B)**2)/2)
assert (u,a2,b2)==(sp.Integer(3),sp.Rational(5,4),sp.Integer(7))
assert sp.simplify(u*u-a2*b2)==sp.Rational(1,4)
# The exact correlation is h=6/sqrt(35)>1.
h=sp.simplify(u/sp.sqrt(a2*b2))
assert sp.simplify(h-6/sp.sqrt(35))==0
avg=(A+B)/2
sig_fast=sp.simplify(max(avg.eigenvals().keys()))
sig_slow=sp.simplify((max(A.eigenvals().keys())+max(B.eigenvals().keys()))/2)
assert sp.simplify(sig_fast-(-3+sp.sqrt(57))/4)==0
assert sp.simplify(sig_slow-(-3+sp.sqrt(5)+2*sp.sqrt(7))/4)==0
shift=sp.Rational(227,200)
assert float(sig_slow)<float(shift)<float(sig_fast)
# Exact rational-square upper/lower comparisons imply these bounds without floating point:
assert sp.Rational(754,100)**2 < 57
assert sp.Rational(2237,1000)**2 > 5 and sp.Rational(2646,1000)**2 > 7
assert sp.Rational(2237,1000)+2*sp.Rational(2646,1000) < 3+4*shift
mA=np.array(A.tolist(), dtype=float);mB=np.array(B.tolist(),dtype=float)
val0=float(sig_fast-shift)
val4=math.log(max(abs(np.linalg.eigvals(expm((mA-float(shift)*np.eye(2))*2)@expm((mB-float(shift)*np.eye(2))*2)))))/4
assert val0>0 and val4<0
# Verify the hyperbolic trace formula and strict sign for 500 deterministic test pairs.
rng=np.random.default_rng(20261120)
for it in range(500):
    X=rng.normal(size=(2,2));Y=rng.normal(size=(2,2))
    X[0,1]=math.exp(rng.uniform(-2,2));X[1,0]=math.exp(rng.uniform(-2,2))
    Y[0,1]=math.exp(rng.uniform(-2,2));Y[1,0]=math.exp(rng.uniform(-2,2))
    ph=float(rng.uniform(.1,.9));T=float(rng.uniform(.02,3))
    x=X-np.trace(X)/2*np.eye(2);y=Y-np.trace(Y)/2*np.eye(2)
    aa=math.sqrt(np.trace(x@x)/2);bb=math.sqrt(np.trace(y@y)/2)
    hh=np.trace(x@y)/(2*aa*bb)
    C=math.cosh(aa*ph*T)*math.cosh(bb*(1-ph)*T)+hh*math.sinh(aa*ph*T)*math.sinh(bb*(1-ph)*T)
    assert C>=1-1e-12
    closed=float(np.trace(ph*X+(1-ph)*Y)/2+math.acosh(max(1,C))/T)
    P=expm(X*ph*T)@expm(Y*(1-ph)*T)
    computed=math.log(max(abs(np.linalg.eigvals(P))))/T
    expected=max(np.linalg.eigvals(ph*X+(1-ph)*Y).real)
    assert abs(computed-closed)<2e-8
    if abs(hh-1)>1e-5 and abs(computed-expected)>1e-8:
        assert (computed-expected)*(1-hh)>-1e-10
print('PASS: symbolic identities, exact sign interval, T=4 reversal and 500 Floquet checks')
print('h=',float(h),'rapid-shift=',val0,'T4-shift=',val4,'slow-shift=',float(sig_slow-shift))

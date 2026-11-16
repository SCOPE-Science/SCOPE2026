#!/usr/bin/env python3
"""Finite independent diagnostics for adjacent Gaussian-Hermite BV coefficient norm."""
from math import factorial, pi, sqrt, exp
import sympy as s
import numpy as np
from scipy.special import roots_hermitenorm, eval_hermitenorm
x=s.symbols('x', real=True)
for n in range(1,13):
    p=s.hermite_prob(n-1,x)
    q=s.hermite_prob(n,x)
    # F(x)=exp(-x*x)/(2*pi) * B(x), so its derivative contains B'-2*x*B.
    B=p**2/s.factorial(n)+q**2/s.factorial(n+1)
    expected=-2*q*(p+x*q)/(s.factorial(n)*(n+1))
    assert s.expand(s.diff(B,x)-2*x*B-expected)==0, n
    roots,_=roots_hermitenorm(n)
    r=0.0 if n%2 else min(t for t in roots if t>0)
    xx=np.linspace(0, max(10.0,3*sqrt(n)), 30001)
    vals=np.exp(-xx*xx)*(eval_hermitenorm(n-1,xx)**2/factorial(n)+eval_hermitenorm(n,xx)**2/factorial(n+1))
    vr=exp(-r*r)*(float(eval_hermitenorm(n-1,r))**2/factorial(n)+float(eval_hermitenorm(n,r))**2/factorial(n+1))
    assert max(vals) <= vr*(1+1e-9), (n, max(vals),vr)
    extra=exp(-r*r)*float(eval_hermitenorm(n+1,r))**2/factorial(n+2)
    assert extra>1e-14
print('CHECK_OK exact_derivative=12 numerical_maxima=12 strict_three_block=12')

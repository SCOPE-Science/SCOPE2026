#!/usr/bin/env python3
"""Numerical diagnostics for the two-mode Jordan Fock semigroup.
The analytic argument, not this finite checker, establishes all-dimensional claims.
"""
import math
import numpy as np

checks = 0

def test(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def one_particle(a,c,z):
    return np.exp(-a*z)*np.array([[1,c*z],[0,1]],dtype=complex)

def singular_formula(a,c,z):
    t=z.real
    v=math.asinh(c*abs(z)/2)
    return math.exp(-a*t+v), math.exp(-a*t-v)

for a in [0.4,1.0,2.3]:
    for rat in [0.1,0.5,0.9,1.0]:
        c=2*a*rat
        for t in [0.0001,0.003,0.07,0.7,2.0]:
            span=math.sqrt((2*math.sinh(a*t)/c)**2 - t*t)
            for coef in [-1.3,-1.0,-.9,0,.9,1.,1.3]:
                z=complex(t,span*coef)
                svals=np.linalg.svd(one_particle(a,c,z),compute_uv=False)
                q,r=singular_formula(a,c,z)
                test(abs(svals[0]-q) < 2e-12*max(1,q),'singular-value 1')
                test(abs(svals[1]-r) < 2e-12*max(1,r),'singular-value 2')
                if abs(q-1)>2e-12:
                    test((q<1)==(abs(coef)<1.0),'boundedness-region')
                test(abs((q*r)-math.exp(-2*a*t)) < 3e-13,'determinant')
for a in [0.4, 1, 2.3]:
    for rat in [0.25,0.8,1]:
        c=2*a*rat
        for t in [0.0003,0.005,0.04,0.8]:
            q,r=singular_formula(a,c,complex(t,0))
            test(q<1 and r<1,'real semigroup strict contraction')
            for p in [0.5,1.0,2.,4.]:
                full=1/((1-q**p)*(1-r**p))
                trunc=sum(q**(p*j)*r**(p*k) for j in range(70) for k in range(70))
                test(trunc<=full*(1+1e-11),'partial positive Schatten sum')
            if t<=0.005:
                for p in [1,2]:
                    full=1/((1-q**p)*(1-r**p))
                    if rat==1:
                        approx=3/(p*p*a**4*t**4)
                    else:
                        approx=1/(p*p*(a*a-c*c/4)*t*t)
                    test(abs(full/approx-1) < .04,'short-time Schatten law')
for a in [0.6,1.4]:
    for t in [0.005,0.001,0.0002]:
        for delta in [0, t*t/5, t*t, t, math.sqrt(t)]:
            c=2*a*(1-delta)
            width=math.sqrt((2*math.sinh(a*t)/c)**2-t*t)
            model=t*math.sqrt(2*delta+a*a*t*t/3)
            test(abs(width/model-1)< 0.065,'uniform width crossover')
            q,r=singular_formula(a,c,t)
            for p in [1.0,2.0]:
                full=1/((1-q**p)*(1-r**p))
                model=1/(2*p*p*a*a*t*t*(delta+a*a*t*t/6))
                test(abs(full/model-1)<0.07,'uniform Schatten crossover')
print('JORDAN_FOCK_HORN_DIAGNOSTIC_OK',checks)

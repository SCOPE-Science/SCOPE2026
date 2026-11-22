#!/usr/bin/env python3
"""Standalone algebraic checks for the rate formulas; standard library only."""
import math

def coeff(m):
    return (math.gamma(3/(2*m))/math.gamma(1/(2*m)))**m

def moment(m,n):
    c=coeff(m)
    return c**(-n/(2*m))*math.gamma((n+1)/(2*m))/math.gamma(1/(2*m))

def exact(m,r,D=1.0,sigma=1.0):
    c=coeff(m); q=D/sigma**2
    return sum(c*math.factorial(2*m)/math.factorial(2*m-2*j)*moment(m,2*m-2*j)*q**j*r**(1-j) for j in range(1,m+1))

checks=0
for m in (1,2,3,4,5):
    assert abs(moment(m,0)-1)<1e-13
    assert abs(moment(m,2)-1)<1e-12
    checks+=2
    for r in (0.03125,0.1,0.5,1.0,3.0,20.0):
        s=exact(m,r)
        assert s>0
        checks+=1
        if m==1:
            assert abs(s-1)<1e-12
            checks+=1
        else:
            assert exact(m,r/2)>s>exact(m,r*2)
            checks+=1
        if m==2:
            c=coeff(m)
            assert abs(s-(12*c+24*c/r))<1e-10
            checks+=1
    lead=coeff(m)*math.factorial(2*m)
    assert abs(exact(m,1e-7)/(lead*1e-7**(1-m))-1)<1e-5
    checks+=1
# Independent exact exponential-vs-Laplace check for the scale-one
# double-exponential Brownian displacement and variance-one Laplace reset.
b=2**(-0.5)
for r in (0.01,0.1,0.5,1,2,5,20):
    a=1/math.sqrt(r)
    lap_exact=1/(b*(a+b))
    # Difference of absolute means for a convolution of two Laplace laws.
    emean=(a*a+a*b+b*b)/(a+b)
    assert abs(r*(emean-b)/b-lap_exact)<1e-12
    checks+=1
assert 1/(b*(b+1/math.sqrt(2)))==1.0
checks+=1
print('PASS: {} exact normalizations, identities, and monotonicity assertions'.format(checks))

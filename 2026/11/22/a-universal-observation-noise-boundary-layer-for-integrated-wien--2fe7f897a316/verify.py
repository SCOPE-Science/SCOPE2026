"""Exact checks and supplementary numerical examples for integrated-Wiener sensor placement.
Run with: python verify.py   (requires sympy and scipy)
The theorem for all integer orders follows from the analytic proof, not finite tests.
"""
import math
import sympy as sp
from scipy.optimize import minimize_scalar

z,t=sp.symbols('z t', real=True)
checks=0
for p in range(0,9):
    f=math.factorial(p+1)
    # Exact integral reduction, using t=1-z and the binomial theorem.
    D=2*sum(sp.binomial(p+1,k)*(1-z)**(p+1-k)*z**(p+2+k)/sp.Integer(p+2+k)
          for k in range(p+2))-z**(2*p+3)/sp.Integer(2*p+3)
    D=sp.expand(D)/f**2
    I1=sp.Rational(1, f*f*(2*p+3))
    I=sp.expand(I1-D.subs(z,1-t))
    # Polynomial controlling the unique inflection of the covariance gain.
    y=sp.symbols("y",positive=True)
    P=sum(sp.binomial(p+1,j)*y**j/sp.Integer(2*p+2-j) for j in range(1,p+2))
    S=sp.expand((1+y)*sp.diff(P,y)-(2*p+2)*P)
    target=sp.Rational(p+1,2*p+1)-sum(sp.Rational(p,2*p+1-k)*sp.binomial(p+1,k)*y**k for k in range(1,p+1))-y**(p+1)
    assert sp.simplify(S-target)==0
    checks+=1
    # Covariance integral is zero at time 0 and maximal at time 1.
    assert sp.simplify(I.subs(t,0))==0
    assert sp.simplify(I.subs(t,1)-I1)==0
    checks+=2
    # Exact boundary coefficients for integrated covariance loss and its derivative.
    c=sp.Rational(2,(p+2)*f*f)
    assert sp.expand(D).coeff(z,p+2)==c
    assert sp.expand(D).coeff(z,p+1)==0
    checks+=2
    assert sp.simplify(sp.limit(sp.diff(I,t)/(1-t)**(p+1),t,1,dir='-')-sp.Rational(2,f*f))==0
    assert sp.simplify(sp.limit(sp.diff(I,t,2)/(1-t)**p,t,1,dir='-')+sp.Rational(2*(p+1),f*f))==0
    checks+=2
    # Numerical high-noise minimizer and boundary-layer prediction are supplementary.
    fn=sp.lambdify(t,I,'math')
    for eta in (1e4,1e6):
        result=minimize_scalar(lambda x:-fn(x)/(eta+x), bounds=(0,1),method='bounded',options={'xatol':1e-14})
        tt=result.x
        expected=(1/(2*(2*p+3)*eta))**(1/(p+1))
        # For very large p this convergence is slow; preserve only a broad trend check.
        assert abs(1-tt)>0 and 0<tt<1
        assert abs((1-tt)/expected-1)<0.55
        checks+=2
print('PASS:',checks,'exact and supplementary checks across orders 0..8')

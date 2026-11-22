"""Numerical cross-checks for sharp integrated variation errors of Bernstein--Bezier operators.
Runs with Python 3, NumPy and SciPy. Finite computations test, but do not replace,
the proof's all-degree and all-parameter assertions.
"""
from math import sqrt, pi
from scipy.special import bdtrc, ndtr
from scipy.integrate import quad
from scipy.optimize import brentq
import numpy as np

def tail(n,k,x):
    return float(bdtrc(k-1,n,x))

def response(n,k,alpha,s):
    # k=ceil(n*s), except that s=left cell endpoint means a right limit
    a=quad(lambda x: tail(n,k,x)**alpha,0,s,epsabs=3e-12)[0]
    b=quad(lambda x: 1-tail(n,k,x)**alpha,s,1,epsabs=3e-12)[0]
    return a+b

def finite_norm(n,alpha):
    return max(response(n,k,alpha,s) for k in range(1,n+1)
               for s in ((k-1)/n,k/n))

def gaussian_q(z):
    return float(ndtr(-z))

def constant(alpha):
    return quad(lambda z: gaussian_q(z)**alpha +
                (-np.expm1(alpha*np.log1p(-gaussian_q(z)))),0,12,
                epsabs=2e-13)[0]

def derivative(alpha):
    def term(z):
        q=gaussian_q(z)
        if q == 0:return 0.
        return q**alpha*np.log(q) - (1-q)**alpha*np.log1p(-q)
    return quad(term,0,12,epsabs=2e-13)[0]

def independent_direct_step(n,k,alpha,s):
    xs=np.linspace(0,1,20001)
    j=np.array([tail(n,k,float(x)) for x in xs])**alpha
    return float(np.trapezoid(np.where(xs<s,j,1-j),xs))

for alpha in (0.7,1.,1.2,1.4,2.,3.):
    for n in (1,2,3,5,10):
        for k in range(1,n+1):
            s=(k-0.5)/n
            exact=response(n,k,alpha,s)
            direct=independent_direct_step(n,k,alpha,s)
            assert abs(exact-direct)<1.2e-4,(n,k,alpha,exact,direct)
print('STEP_RESPONSE_DIRECT_QUADRATURE_PASS: 126')

for alpha in (0.5,1.,1.4,2.,3.):
    assert abs(finite_norm(1,alpha)-max(alpha,1)/(alpha+1))<1e-11
print('DEGREE_ONE_ENDPOINT_FORMULA_PASS: 5')

c1=sqrt(2/pi)
assert abs(constant(1)-c1)<3e-12
assert abs(constant(2)-c1)<3e-12
astar=brentq(derivative,1,2,xtol=1e-13)
assert 1.40542<astar<1.40544
cstar=constant(astar)
assert .75749<cstar<.75751
assert derivative(1)<0<derivative(2)
assert all(constant(a)<c1 for a in (1.02,1.1,1.2,1.5,1.7,1.98))
assert all(constant(a)>c1 for a in (.25,.8,2.1,3,6))
print('GAUSSIAN_PARAMETER_CROSSING_PASS',format(astar,'.12f'),format(cstar,'.12f'))

for alpha in (1.,astar,2.):
    seq=[]
    for n in (16,32,64,128):
        seq.append(sqrt(n)*finite_norm(n,alpha))
    assert abs(seq[-1]-constant(alpha)/2)<0.026,(alpha,seq)
    print('FINITE_DEGREE_ASYMPTOTIC_PROFILE',format(alpha,'.6f'),seq)
print('BERNSTEIN_BEZIER_VARIATION_CHECKS_PASS')

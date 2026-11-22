"""Supplementary numerical checks for a two-mode damped projection theorem.

Run: python projection_checks.py
Requires: numpy, scipy. These are finite checks, not an infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.integrate import quad


def kernel(r, x, y):
    cx, sx = math.cos(r*x), math.sin(r*x)/r
    cy, sy = math.cos(r*y), math.sin(r*y)/r
    return 4*math.exp(-x-y)*(cx*cy-cx*sy-sx*cy+(2+r*r)*sx*sy)


def endpoint(r):
    return 8*math.exp(-math.atan(r)/r)/(math.sqrt(1+r*r)*(-math.expm1(-math.pi/r)))


def endpoint_independent(r):
    # Integrate |K_r(0,y)| between its successive exact zeros, plus a tail.
    z = math.atan(r)/r
    spacing=math.pi/r
    res = 0.
    lower=0.
    for k in range(400):
        upper=z+k*spacing
        if upper>90:
            break
        piece=quad(lambda y: abs(kernel(r,0.,y)),lower,upper,epsabs=1.e-12)[0]
        res += piece
        lower=upper
    # rigorous tail can be bounded by the 1-norm of the two coefficient terms;
    # numerical tail is independently integrated for the tested parameters.
    res += quad(lambda y: abs(kernel(r,0.,y)),lower,math.inf,epsabs=1.e-11,limit=1000)[0]
    return res


def confluent_kernel(x,y):
    return 4*math.exp(-x-y)*(1-x-y+2*x*y)


def test():
    # Elementary Gram identities checked independently by numerical integration.
    for r in (0.25,0.7,2.,5.):
        f=lambda x: np.array([math.exp(-x)*math.cos(r*x),math.exp(-x)*math.sin(r*x)/r])
        G = np.array([[quad(lambda x:f(x)[i]*f(x)[j],0,math.inf,epsabs=1.e-12)[0]
                       for j in range(2)] for i in range(2)])
        G_exact=np.array([[2+r*r,1],[1,1]],dtype=float)/(4*(1+r*r))
        G_inv=4*np.array([[1,-1],[-1,2+r*r]],dtype=float)
        assert np.max(np.abs(G-G_exact))<2.e-10
        assert np.max(np.abs(G_exact@G_inv-np.eye(2)))<2.e-13
        for x,y in ((0.2,0.8),(1.0,0.4),(0.,1.1)):
            prod=quad(lambda z:kernel(r,x,z)*kernel(r,z,y),0,math.inf,epsabs=1.e-10)[0]
            assert abs(prod-kernel(r,x,y))<2.e-9
        assert abs(endpoint_independent(r)-endpoint(r))<2.e-7, (r,endpoint_independent(r),endpoint(r))

    # Relative convergence at several fixed evaluation and integration points.
    for r in (0.001,0.005,0.01):
        for x,y in ((0.,0.),(0.,1.),(.5,.2),(1.5,1.8),(3.,4.)):
            assert abs(kernel(r,x,y)-confluent_kernel(x,y))<35*r*r

    # Exact endpoint constants approach both theorem values.
    assert abs(endpoint(.001)-8/math.e)<5.e-5
    assert abs(endpoint(100.)-8/math.pi)<1.e-3
    assert abs(endpoint(200.)-8/math.pi)<5.e-4
    assert abs(quad(lambda y:abs(confluent_kernel(0,y)),0,1)[0]+
               quad(lambda y:abs(confluent_kernel(0,y)),1,math.inf)[0]-8/math.e)<1.e-11
    print('PASS: Gram matrices, finite kernel idempotence, endpoint total variation, and limiting probes.')


if __name__=='__main__':
    test()

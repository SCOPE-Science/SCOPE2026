#!/usr/bin/env python3
"""Numerical and symbolic checks for the three-window chirality identity.

Requires Python, NumPy, SciPy and SymPy. No stochastic simulation is used as a
substitute for the analytic all-parameter proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from numpy.polynomial.legendre import leggauss
import sympy as sp

P = np.array([[0., 1., 0.], [0., 0., 1.], [1., 0., 0.]])
E = np.eye(3)
ONE = np.ones(3)
PI = ONE / 3


def generator(forward, backward):
    return forward * (P - E) + backward * (P.T - E)


def contrast(d):
    return (d[0]-d[1])*(d[1]-d[2])*(d[2]-d[0])


def kernel(forward, backward, u, v, d):
    Q = generator(forward, backward)
    A = np.diag(d)
    return float(PI @ A @ expm(Q*u) @ A @ expm(Q*v) @ A @ ONE)


def kernel_difference_exact(forward, backward, u, v, d):
    c = 1.5*(forward+backward)
    b = math.sqrt(3)*(forward-backward)/2
    return 2/(3*math.sqrt(3))*contrast(d)*math.exp(-c*(u+v))*math.sin(b*(u-v))


def time_arrow_exact(forward, backward, h, u, v, d):
    c = 1.5*(forward+backward)
    b = math.sqrt(3)*(forward-backward)/2
    lam = complex(-c, b)
    I = np.expm1(lam*h)/lam
    sinc_factor = h if abs(b) < 1.e-13 else math.sin(b*h)/b
    return (16/(3*math.sqrt(3))*contrast(d)*math.exp(-c*(u+v+h))
            * abs(I)**2 * sinc_factor * math.sin(b*(u-v)))


def integrated_triple(forward, backward, h, u, v, d, order=7):
    """Independent three-dimensional quadrature of the original Markov formula."""
    zz, ww = leggauss(order)
    zz = .5*h*(zz+1)
    ww = .5*h*ww
    Q = generator(forward, backward)
    A = np.diag(d)
    result = 0.
    for i, s in enumerate(zz):
        for j, t in enumerate(zz):
            L = PI @ A @ expm(Q*(h+u+t-s)) @ A
            for k, z in enumerate(zz):
                val = L @ expm(Q*(h+v+z-t)) @ A @ ONE
                result += ww[i]*ww[j]*ww[k]*float(val)
    return 8*result


def check(condition, msg):
    if not condition:
        raise AssertionError(msg)


def run():
    tests = 0
    # The key nonstandard three-state Fourier coefficient, computed symbolically.
    x,y,z = sp.symbols('x y z', real=True)
    ps = sp.Matrix([[0,1,0],[0,0,1],[1,0,0]])
    J = sp.ones(3,3)/3
    R = (ps-ps.T)/sp.sqrt(3)
    Eplus = (sp.eye(3)-J-sp.I*R)/2
    Eminus = (sp.eye(3)-J+sp.I*R)/2
    A = sp.diag(x,y,z)
    one = sp.ones(3,1)
    C = (one.T*A*Eplus*A*Eminus*A*one)[0]/3
    V = (x-y)*(y-z)*(z-x)
    check(sp.simplify(sp.im(sp.expand_complex(C))+V/(6*sp.sqrt(3)))==0,
          'Fourier coefficient sign or magnitude')
    tests += 1

    setups = [
        (1.,0.,[1.,2.,4.]),
        (1.,.3,[.2,2.5,6.]),
        (.3,1.,[.2,2.5,6.]),
        (2.,.6,[2.,5.,3.]),
        (.15,1.1,[.9,1.7,4.]),
        (.9,.9,[1.,2.,4.]),
        (1.,.3,[1.,1.,4.]),
        (1.,.3,[2.,4.,2.]),
    ]
    for forward, backward, d in setups:
        d = np.array(d)
        for u,v in [(0.,.1),(.1,1.),(.8,.2),(1.,2.),(2.,2.),(2.1,3.7)]:
            actual = kernel(forward,backward,u,v,d)-kernel(forward,backward,v,u,d)
            predicted = kernel_difference_exact(forward,backward,u,v,d)
            check(abs(actual-predicted)<3e-12*(1+max(abs(actual),abs(predicted))),
                  ('pointwise',forward,backward,u,v,actual,predicted))
            tests += 1

    setups_integrated = [
        (1.,0.,.2,.3,1.1,[1.,2.,4.]),
        (1.,.3,.8,.3,1.1,[1.,2.,4.]),
        (.3,1.,.8,.3,1.1,[1.,2.,4.]),
        (1.5,.5,.25,.1,.9,[.5,1.7,5.]),
        (2.,.1,.5,1.3,2.0,[2.,5.,3.]),
        (1.,.3,.15,1.0,1.0,[1.,2.,4.]),
        (1.,1.,.6,.1,.5,[1.,2.,4.]),
        (1.,.3,.6,.1,.5,[1.,1.,4.]),
    ]
    for a,b,h,u,v,d in setups_integrated:
        d = np.array(d)
        A1 = integrated_triple(a,b,h,u,v,d)
        A2 = integrated_triple(a,b,h,v,u,d)
        direct = A1-A2
        exact = time_arrow_exact(a,b,h,u,v,d)
        check(abs(direct-exact)<2e-9*(1+abs(A1)+abs(A2)),
              ('integrated',a,b,h,u,v,direct,exact))
        tests += 1

    # Exact null widths do not imply reversible hidden dynamics.
    a,bb=1.,.2
    omega = math.sqrt(3)*(a-bb)/2
    for n in range(1,5):
        h=n*math.pi/omega
        exact=time_arrow_exact(a,bb,h,.2,.7,[1.,2.,4.])
        check(abs(exact)<1e-14,('alias',n,exact))
        tests += 1
    # No alias between consecutive nodes for a non-degenerate contrast and unequal gaps.
    for frac in (.1,.4,.9,1.2,1.7):
        h=frac*math.pi/omega
        s=time_arrow_exact(a,bb,h,.2,.7,[1.,2.,4.])
        check(abs(s)>1e-15,('nonalias',frac,s))
        tests += 1
    print('PASS:',tests,'symbolic and independent matrix/quadrature checks')

if __name__=='__main__':
    run()

"""Independent finite-dimensional checks for the partial-reset coupled diffusion theorem.

Run with: python verify.py
Needs numpy and scipy; these checks do not substitute for the infinite-range proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm


def formulas(a, b, dx, dy, r, t):
    lam = a + b
    q = math.exp(-lam * t)
    d = (b*b*dx+a*a*dy)/(lam*lam)
    alpha = a/lam*(1-q)
    beta = (a+b*q)/lam
    vx = (2*d*t + 4*a*(b*dx-a*dy)/lam**3*(1-q)
          + a*a*(dx+dy)/lam**3*(1-q*q))
    vy = (2*d*t + 4*b*(a*dy-b*dx)/lam**3*(1-q)
          + b*b*(dx+dy)/lam**3*(1-q*q))
    return alpha, beta, vx, vy, d


def quadrature_variance(a, b, dx, dy, t):
    A = np.array([[-a, a], [b, -b]], float)
    D = np.diag([dx, dy])
    out = np.zeros((2,2))
    for i in range(2):
        v, err = quad(lambda s: (expm(A*s) @ D @ expm(A.T*s))[i,i],
                      0, t, epsabs=1e-11, epsrel=1e-11)
        out[i,i] = 2*v
    return out[0,0], out[1,1]


def expect_e(rate, p):
    return rate/(rate+p)


def embedded_moments(a,b,dx,dy,r):
    lam = a+b
    d = (b*b*dx + a*a*dy)/lam**2
    q1 = expect_e(r,lam)
    q2 = expect_e(r,2*lam)
    Evx = (2*d/r + 4*a*(b*dx-a*dy)/lam**3*(1-q1)
           + a*a*(dx+dy)/lam**3*(1-q2))
    Evy = (2*d/r + 4*b*(a*dy-b*dx)/lam**3*(1-q1)
           + b*b*(dx+dy)/lam**3*(1-q2))
    Ealpha2 = (a/lam)**2 * (1-2*q1+q2)
    Ebeta2 = (a*a+2*a*b*q1+b*b*q2)/lam**2
    bath_var = Evy/(1-Ebeta2)
    return Evx+Ealpha2*bath_var, bath_var


def stationary_generator_xvar(a,b,dx,dy,r):
    return 2*(dx*(b+r)+a*a*dy/b)/(r*(2*a+b+r))


cases = [(1.,1.,1.,1.,1.), (1.,1/7,1.,1/7,.2),
         (.4,3.,.4,2.,2.3), (8.,.25,1.7,.3,7.),
         (1.5,3.2,.2,6.,.07), (1.,.01,1.,.01,1.)]
for a,b,dx,dy,r in cases:
    for t in [0.01,.17,1.3,7.]:
        alpha,beta,vx,vy,d = formulas(a,b,dx,dy,r,t)
        N = quadrature_variance(a,b,dx,dy,t)
        assert abs(vx-N[0]) < 2e-9 * (1+N[0]), (vx,N[0])
        assert abs(vy-N[1]) < 2e-9 * (1+N[1]), (vy,N[1])
        assert 0<=alpha<1 and 0<beta<1
    xvar, yvar = embedded_moments(a,b,dx,dy,r)
    expected = stationary_generator_xvar(a,b,dx,dy,r)
    assert math.isclose(xvar,expected,rel_tol=1e-11,abs_tol=1e-11)
    assert yvar>0
    theta=math.sqrt(r/d)
    assert math.isclose(theta**2*d,r,rel_tol=1e-13)
    # Saddle-point minimization in the large-age Gaussian lower-bound proof.
    age_slope=1/(2*math.sqrt(r*d))
    rate=r*age_slope+1/(4*d*age_slope)
    assert math.isclose(rate,theta,rel_tol=1e-12)
    print(f'PASS a={a} b={b} Dx={dx} Dy={dy} r={r}: '
          f'Deff={d:.12g}, VarX={xvar:.12g}, VarY={yvar:.12g}, tail={theta:.12g}')

print('PASS: six parameter sets, 24 covariance quadratures, exact stationary-moment equations, tail variational constants')

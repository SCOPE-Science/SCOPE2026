"""Independent finite checks of a cubic-center occupation calculation.

Requires sympy, scipy and mpmath. These checks corroborate identities and sample
quadratures; all-amplitude and asymptotic statements require the written proof.
"""
from math import acos, cos, exp, log, pi, sin, sqrt
import sympy as sp
from scipy.integrate import quad
from mpmath import polylog, exp as mexp, j as mj, pi as mpi

v, alpha, beta = sp.symbols('v alpha beta', real=True)
Delta = 4*beta - alpha**2
p = 1 - alpha*v + beta*v**2
K = sp.log(p)/(2*beta) + alpha/(beta*sp.sqrt(Delta)) * (
    sp.atan((2*beta*v-alpha)/sp.sqrt(Delta))
    + sp.atan(alpha/sp.sqrt(Delta)))
assert sp.simplify(sp.diff(K, v)-v/p) == 0
assert sp.simplify(K.subs(v,0)) == 0

# Symmetric slice: normalize the limiting Cauchy density in angle theta.
cl = float(sp.im(sp.polylog(2, sp.exp(sp.I*sp.pi/3))).evalf(18))
cl_integral = quad(lambda t:log(2*cos(t)),0,pi/3,epsabs=1e-12)[0]
assert abs(cl - 2*cl_integral)<2e-12
constant = cl/pi
assert 0.32 < constant < 0.33

# Exact finite-amplitude distribution, transformed to the Cauchy angle theta.
# Note: the Cauchy mass outside the finite turning interval is included in TV.
for A in (3.0, 4.0, 5.0):
    B = A*A
    theta_max = acos(exp(-B/2))
    def weight(theta):
        return 1 / sqrt(1 + 2*log(cos(theta))/B)
    def integrand(phi):
        theta = theta_max*sin(phi)
        z = 1 + 2*log(cos(theta))/B
        if z <= 0: return 0.0
        return theta_max*cos(phi)/sqrt(z)
    Z = 2*quad(integrand,0,pi/2,epsabs=1e-9,limit=500)[0]
    theta_cross = acos(exp(B/2*((pi/Z)**2-1)))
    center_prob = (2/Z)*quad(weight,0,theta_cross,epsabs=1e-10)[0]
    TV = 2*theta_cross/pi - center_prob + 1 - 2*theta_max/pi
    assert TV>0
    print('A=',A,'A^2*TV=',A*A*TV)
assert abs(A*A*TV-constant)<0.07
print('CAUCHY_VELOCITY_OCCUPATION_CHECK_OK', 'limiting_constant=',constant)

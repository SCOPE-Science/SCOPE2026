"""Independent numerical diagnostics for the sharp Gamma-maxima KL theorem.

Requires Python 3.10+, scipy, numpy, and mpmath. This is a numerical
cross-check, not a substitute for the asymptotic proof in RESULT.md.
"""
import math
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.special import gammainccinv, gammaln

mp.mp.dps = 35
z2, z3 = mp.zeta(2), mp.zeta(3)
gamma = mp.euler
C = 11 * mp.pi**4 / 720 - 3 * z3**2 / mp.pi**2
dbeta = 1 - gamma - z3 / z2
dmu = (gamma**2 - 2*gamma + 2 - z2)/2 + (gamma-1)*z3/z2

def pexpect(fun):
    return mp.quad(lambda u: mp.exp(-u)*fun(-mp.log(u), u), [0, 1, mp.inf])

def s(y, u):
    return y + (u-1)*y*y/2

def t1(y, u):
    return 1-u

def t2(y, u):
    return -1+y*(1-u)

scores = [t1, t2]
F = mp.matrix([[pexpect(lambda y,u: scores[i](y,u)*scores[j](y,u))
                for j in range(2)] for i in range(2)])
b = mp.matrix([pexpect(lambda y,u: s(y,u)*t(y,u)) for t in scores])
d = mp.lu_solve(F,b)
raw = pexpect(lambda y,u:s(y,u)**2)/2
residual = pexpect(lambda y,u:(s(y,u)-d[0]*t1(y,u)-d[1]*t2(y,u))**2)/2
assert abs(residual-C) < mp.mpf('1e-25')
assert abs(d[0]-dmu) < mp.mpf('1e-25')
assert abs(d[1]-dbeta) < mp.mpf('1e-25')
assert C > 0 and raw > C
print('Gumbel score Gram determinant:', mp.nstr(mp.det(F),16))
print('unfitted KL coefficient:',mp.nstr(raw,16))
print('optimized KL coefficient:',mp.nstr(C,16))
print('location coefficient:',mp.nstr(dmu,16))
print('scale coefficient:',mp.nstr(dbeta,16))

# Exact finite-n forward KL integration uses H=-log(F(M_n)^n)~Exp(1).
# No simulation, empirical approximation, or discrete sample is involved.
def finite_gamma(shape, n):
    bn = float(gammainccinv(shape,1/n))
    log_pdf_at_b = (shape-1)*math.log(bn)-bn-gammaln(shape)
    an = math.exp(-math.log(n)-log_pdf_at_b)
    def values(h):
        h = max(h,1.e-300)
        surv=-math.expm1(-h/n)
        x=float(gammainccinv(shape,surv))
        y=(x-bn)/an
        lf=math.log(n*an)-(1-1/n)*h+(shape-1)*math.log(x)-x-gammaln(shape)
        return y,lf
    def expected(fun):
        return quad(lambda h:math.exp(-h)*fun(*values(h)),0,90,
                    epsabs=2.e-11,epsrel=2.e-10,limit=180,
                    points=[.0001,.001,.01,.1,1,10])[0]
    kl=expected(lambda y,lf:lf+y+math.exp(-y))
    mean=expected(lambda y,lf:y)
    e_log_pdf=expected(lambda y,lf:lf)
    def objective(r):
        return e_log_pdf-math.log(r)+r*mean + math.log(expected(lambda y,lf:math.exp(-r*y)))+1
    res=minimize_scalar(objective,bounds=(0.8,1.2),method='bounded',options={'xatol':1.e-11})
    assert res.success and 0 < res.fun < kl
    predicted=(shape-1)**2*float(C)/bn**4
    assert .5 < res.fun/predicted < 1.1
    print(f'shape={shape:g}, n={n}: b={bn:.7f}, KL(reference)={kl:.10g}, '
          f'KL(optimal)={res.fun:.10g}, ratio to leading prediction={res.fun/predicted:.7f}')

finite_gamma(2,1_000_000)
finite_gamma(3,1_000_000)
print('All diagnostics passed; asymptotic proof is supplied separately.')

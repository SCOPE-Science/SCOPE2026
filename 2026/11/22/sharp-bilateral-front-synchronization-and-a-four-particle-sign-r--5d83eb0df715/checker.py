"""Independent numerical checks of bilateral edge synchronization formulas.

Run: python checker.py  (requires NumPy and SciPy).
All thermodynamic limits are established analytically in RESULT.md;
finite quadrature and simulation cannot establish those limits.
"""
from math import pi, sqrt, asin, log
import numpy as np
from scipy.integrate import quad, trapezoid
from scipy.special import ndtr, ndtri

K = 1 - pi / 4
C = pi**2 / (6 * (4 - pi))

def moments(n):
    """Exact one-dimensional integral representations of max moments."""
    def pplus(t):
        q = ndtr(-t)
        return -np.expm1(n * np.log1p(-q))
    def pminus(t):
        return ndtr(-t)**n
    mu = quad(lambda t: pplus(t)-pminus(t), 0, 12,
              epsabs=2e-12, epsrel=2e-12)[0]
    e2 = quad(lambda t: 2*t*(pplus(t)+pminus(t)), 0, 12,
              epsabs=2e-12, epsrel=2e-12)[0]
    return mu, e2

def opposite_cov(n, step=0.025):
    """Hoeffding CDF covariance identity integrated on [-8,8]^2."""
    x = np.arange(-8, 8.0001, step)
    f = ndtr(x)
    p = np.maximum(f[:,None]+f[None,:]-1, 0)
    joint = np.power(p, n)
    marginal = f**n
    return float(trapezoid(trapezoid(
        joint-marginal[:,None]*marginal[None,:], x, axis=1),x))

def pearson(n,step=0.025):
    mu,second=moments(n)
    var=second-mu*mu
    c=opposite_cov(n,step)
    return (c+K*mu*mu)/(var+K*mu*mu)

def test():
    checks=0
    m3 = 3/(2*sqrt(pi))
    e23 = 1+sqrt(3)/(2*pi)
    uv3 = sqrt(3)/pi
    m4 = 3/(2*sqrt(pi))+3*asin(1/3)/(pi*sqrt(pi))
    e24 = 1+sqrt(3)/pi
    uv4 = 3/pi
    rho3 = (uv3 - pi*m3*m3/4)/(e23-pi*m3*m3/4)
    rho4 = (uv4 - pi*m4*m4/4)/(e24-pi*m4*m4/4)
    assert -1 < rho3 < 0 < rho4 < 1
    checks+=1
    for n,m,e2,uv in ((2,1/sqrt(pi),1,0),(3,m3,e23,uv3),(4,m4,e24,uv4)):
        qm,qe2=moments(n)
        assert abs(qm-m)<2e-10 and abs(qe2-e2)<2e-10
        assert abs(opposite_cov(n,0.02)-(uv-m*m))<2e-6
        checks+=2
    assert abs(pearson(2)+1/3)<1e-6
    assert abs(pearson(3)-rho3)<1e-6
    assert abs(pearson(4)-rho4)<1e-6
    checks+=3
    assert abs(C-1.9162628019520258)<1e-11
    checks+=1
    for n in (5,8,20,100,500,2000):
        rho=pearson(n)
        assert 0<rho<1
        checks+=1
    # Gaussian maximum variance has b_N^2 Var(U_N) -> pi^2/6.
    pairs=[]
    for n in (100,1000,10000,100000,1000000):
        mu,e2=moments(n)
        b=ndtri(1-1/n)
        pairs.append((n,b*b*(e2-mu*mu)))
        assert e2-mu*mu>0 and mu>0
        checks+=1
    assert pairs[-1][1]>pairs[0][1]
    assert 1.0<pairs[-1][1]<pi*pi/6
    checks+=2
    # Parameter-free stationary correlation: multiply every coordinate by
    # sqrt(2*D*A), A~Exp(rate). The two scale moments are always pi/4 apart.
    for D,r in ((0.1,0.2),(1,1),(15,0.07),(0.6,20)):
        es2=2*D/r
        es=sqrt(2*D)*sqrt(pi)/(2*sqrt(r))
        assert abs(es*es/es2-pi/4)<1e-12
        checks+=1
    print('PASS',checks,'deterministic comparisons; rho(2)=-1/3',
          'rho(3)=',rho3,'rho(4)=',rho4,'coefficient=',C)
    print('Gaussian extreme variance diagnostic (n, b_n^2 Var U_n):',pairs)

if __name__=='__main__':
    test()

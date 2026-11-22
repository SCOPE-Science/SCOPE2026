"""Independent finite consistency tests for spectral phase-asymptotic theorem.

Run: python3 check.py (requires SciPy and NumPy).
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ive


def phi(z, a, family):
    z = max(0.0, float(z))
    if family == 'mittag_leffler':
        return 1.0 / (1.0 + z**a)
    if family == 'stable':
        return math.exp(-z**a)
    if family == 'mixture':
        return 0.5 / (1.0 + z**a) + 0.5 * math.exp(-z**a)
    if family == 'exponential':
        return 1.0 / (1.0 + z)
    if family == 'constant':
        return math.exp(-z)
    raise ValueError(family)


def spectral_integral(m, n, theta, alpha, family, tau=1.0):
    """Exact finite-time survival, transformed to an O(1) quadrature scale."""
    # Laplace leading constant is 1 for every test family.
    inv_scale = (n * (tau * math.pi**2 / 2)**alpha)**(1 / (2*alpha))
    # p=y/inv_scale, with p in [0,1].
    upper = min(1.0 * inv_scale, 40.0)
    def g(y):
        p = y / inv_scale
        if p >= 1: return 0.0
        if p < 1e-9:
            A = 2.0 * m
        else:
            A = math.sin(math.pi*m*p) * math.sin(math.pi*p) / (2*math.sin(math.pi*p/2)**2)
        ell = 2 * math.sin(math.pi*p/2)**2
        z = phi(tau*ell,alpha,family)
        return A * math.exp(n*math.log(z)) * phi(theta*tau*ell,alpha,family)
    return quad(g,0,upper,epsabs=2e-13,epsrel=2e-12,limit=120)[0] / inv_scale


def reference_survival(m, u):
    return ive(0,u)+ive(m,u)+2*sum(ive(j,u) for j in range(1,m))


def tests():
    count = 0
    # Independent Bessel recurrence identity for constant clocks in physical time.
    for m in [1,2,3,5]:
        for t in [0.2,0.8,2.0,5.0,12.0,30.0]:
            got=spectral_integral(m,1,0.0,1.0,'constant',tau=t)
            want=reference_survival(m,t)
            assert abs(got-want)<2e-10,(m,t,got,want)
            count+=1
    # Fixed-block phase contrast, including heavy tails and the finite-mean boundary.
    for alpha,family in [(0.5,'mittag_leffler'),(0.5,'stable'),
                         (0.5,'mixture'),(0.7,'mittag_leffler'),
                         (0.7,'stable'),(1.0,'exponential')]:
        for m in [1,3,5]:
            for theta in [0.10,0.25,0.55,0.8]:
                n=1500
                s0=spectral_integral(m,n,0.0,alpha,family)
                st=spectral_integral(m,n,theta,alpha,family)
                nu=1/(2*alpha)
                value=n*((1+theta/n)**nu*st/s0-1)
                theory=nu*(theta-theta**alpha)
                assert abs(value-theory)<0.04,(alpha,family,m,theta,value,theory)
                count+=1
    # Fixed redraw-time fractional cusp: independently integrate the coefficient.
    for family in ['mittag_leffler','stable','mixture']:
        alpha=0.5
        for m in [1,3]:
            for n in [5,20,80]:
                C=(math.pi**2/2)**alpha
                inv_scale=(n*C)**(1/(2*alpha))
                def integrand(y):
                    p=y/inv_scale
                    if p>=1: return 0.0
                    A=2*m if p<1e-9 else math.sin(math.pi*m*p)*math.sin(math.pi*p)/(2*math.sin(math.pi*p/2)**2)
                    ell=2*math.sin(math.pi*p/2)**2
                    return A*phi(ell,alpha,family)**n*ell**alpha
                B=quad(integrand,0,min(inv_scale,40),epsabs=1e-13,limit=120)[0]/inv_scale
                assert B>0,(family,m,n,B)
                eps=1e-6
                s0=spectral_integral(m,n,0,alpha,family)
                su=spectral_integral(m,n,eps,alpha,family)
                assert abs((s0-su)/eps**alpha/B-1)<0.015,(family,m,n,B,(s0-su)/eps**alpha)
                count+=2
    # At the strict heavy-tail boundary alpha=1/2 the phase is uniquely minimized at 1/4.
    alpha=0.5; n=1800; m=3
    s0=spectral_integral(m,n,0.0,alpha,'stable')
    vals=[]
    for th in [0,.05,.1,.15,.2,.25,.3,.35,.4,.5,.65,.8,1]:
        st=spectral_integral(m,n,th,alpha,'stable')
        vals.append(n*((1+th/n)*st/s0-1))
        count+=1
    assert min(range(len(vals)),key=lambda k: vals[k])==5
    assert abs(vals[5]+0.25)<0.005
    # Check exact survival monotonicity across the period at fixed n.
    for a,family in [(0.35,'stable'),(0.5,'mittag_leffler'),(1,'exponential')]:
        ss=[spectral_integral(2,60,th,a,family) for th in np.linspace(0,1,17)]
        assert all(x>y for x,y in zip(ss,ss[1:]))
        count+=16
    print(f'PASS: {count} finite assertions; asymptotic theorem requires the proof in RESULT.md')

if __name__=='__main__': tests()

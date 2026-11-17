"""Reproducible tests for the crossing-chord division-ratio theorem.

Run with Python 3, NumPy and SciPy: python chord_fraction_verifier.py.
These finite checks support, but do not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.special import roots_legendre

PI = math.pi


def division_fraction(gaps):
    x, y, z, w = np.asarray(gaps, dtype=float).T
    a = np.sin(PI*x)*np.sin(PI*w)
    b = np.sin(PI*y)*np.sin(PI*z)
    return a/(a+b)


def exact_cdf_by_quadrature(t, nx=160, ny=96):
    """Integrate the exact conditional crossing CDF, not a small-t approximation."""
    q=t/(1-t)
    ax, wx = roots_legendre(nx)
    ay, wy = roots_legendre(ny)
    u=(ax+1)/2; wx=wx/2
    v=(ay+1)/2; wy=wy/2
    # Resolve the logarithmic boundary layer at x=0.
    total=0.
    for branch in (0,1):
        if branch==0:
            xs=q*u; dx=q*np.ones_like(u)
        else:
            logspan=math.log(1/q)
            xs=q*np.exp(logspan*u)
            dx=logspan*xs
        x=xs[:,None]
        y=(1-x)*v[None,:]
        h=x+y
        c=q*np.sin(PI*y)/np.sin(PI*x)
        angle=np.arctan2(c*np.sin(PI*h), 1-c*np.cos(PI*h))
        wstar=angle/PI
        integrand=wstar*(1-x)*dx[:,None]
        total+=np.sum(wx[:,None]*wy[None,:]*integrand)
    return 6*total


def geometric_ratio(gaps):
    x,y,z,w=gaps
    theta=2*PI*np.array([0,x,x+y,x+y+z])
    a,c,b,d=np.exp(1j*theta)
    r=(d-c)/(b-a)
    s=(c-a)/(b-a)
    lam=-s.imag/r.imag
    return float((s+lam*r).real)


def run():
    rng=np.random.default_rng(2026)
    gaps=rng.dirichlet(np.ones(4),size=128)
    for g in gaps:
        assert abs(geometric_ratio(g)-division_fraction(g))<3e-11
    assert max(abs(division_fraction(gaps)+division_fraction(gaps[:,[1,0,3,2]])-1))<2e-14

    for t in (0.05,0.005,1e-4,1e-6):
        p=exact_cdf_by_quadrature(t)
        assert 0<p<.5
        if t>0.01:
            # Independent deterministic numerical area integration verifies the CDF.
            xx,ww=roots_legendre(100)
            vv=(xx+1)/2; ww=ww/2
            X,Y=np.meshgrid(vv,vv,indexing='ij')
            x=1-np.sqrt(X);y=np.sqrt(X)*Y
            # Reference direct formula for the conditional cutoff in w.
            q=t/(1-t)
            c=q*np.sin(PI*y)/np.sin(PI*x)
            wstar=np.arctan2(c*np.sin(PI*(x+y)),1-c*np.cos(PI*(x+y)))/PI
            p2=3*np.sum(ww[:,None]*ww[None,:]*wstar)
            assert abs(p-p2)<0.004
        print('t',format(t,'.6g'),'exact_cdf',format(p,'.12g'),
              'ratio',format(p/(t*math.log(1/t)),'.10g'))
    # Positivity and general asymptotic behavior checked at extremely small t.
    target=3/PI**2
    p=exact_cdf_by_quadrature(1e-10)
    assert abs(p/(1e-10*math.log(1e10))-target)<0.05
    print('predicted_log_coefficient',format(target,'.12g'))
    print('CROSSING_CHORD_DIVISION_CHECKS_OK')

if __name__=='__main__':
    run()

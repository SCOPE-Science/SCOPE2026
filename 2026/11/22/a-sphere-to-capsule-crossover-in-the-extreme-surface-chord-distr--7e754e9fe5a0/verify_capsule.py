"""Independent numerical quadrature checks for the capsule extreme surface-chord theorem.

Requires Python >= 3.9 and numpy.  Numerical tests support, but do not prove,
any all-parameter statement or a zero-deficit asymptotic.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def cap_cross_probability(a, r, eps, n=440, restricted=True):
    """Exact two-ordered-hemisphere pair contribution (not a local Taylor model).

    Parametrize upper/lower hemispheres by u=cos(theta),v=cos(phi) in [0,1]
    and their azimuth difference psi. Integrate the exact inequality over psi.
    The band and same-hemisphere terms are deliberately not included.
    """
    assert a >= 0 and r > 0 and 0 < eps < 2*(a+r)
    width=1.0
    if restricted and a > 0:
        k=a/(a+r)
        width=min(1.0,max(0.05,8*eps/(r*k)))
    nodes, weights=leggauss(n)
    u=1.0-width*(nodes+1.0)/2.0
    wt=width*weights/2.0
    U=u[:,None]; V=u[None,:]
    den=2*r*r*np.sqrt(np.maximum(0,1-U*U))*np.sqrt(np.maximum(0,1-V*V))
    num=r*r*(2-U*U-V*V)+(2*a+r*(U+V))**2-(2*(a+r)-eps)**2
    z=np.divide(num,den,out=np.full_like(num,-2.0),where=den>0)
    azimuth_probability=np.where(z<=-1,0.0,np.where(z>=1,1.0,1-np.arccos(np.clip(z,-1,1))/math.pi))
    # 2 ordered hemisphere choices; (2*pi*r*r / S)^2 per pair.
    factor=r*r/(2*(r+a)**2)
    return float(factor*np.sum(wt[:,None]*wt[None,:]*azimuth_probability))


def psi(lam):
    return 1-lam if lam<=0.5 else 1/(4*lam)


def check():
    tests=0
    for a in (0.2,1.,3.):
        errs=[]
        for eps in (0.03,0.015,0.0075):
            obs=cap_cross_probability(a,1,eps)
            predicted=eps*eps/(4*a*(a+1))
            relative=abs(obs/predicted-1.)
            errs.append(relative)
            assert relative < 0.016, (a,eps,relative)
            tests+=1
        assert errs[2]<errs[1]<errs[0],(a,errs)
        tests+=1

    for lam in (0.,0.2,0.5,1.,2.,4.):
        rel=[]
        for eps in (0.01,0.005):
            observed=cap_cross_probability(lam*eps,1,eps,n=550,restricted=False)
            target=eps*psi(lam)
            rel.append(abs(observed/target-1))
            assert rel[-1]<0.055,(lam,eps,rel[-1])
            tests+=1
        assert rel[1]<rel[0],(lam,rel)
        tests+=1

    for a,r,eps in ((0.8,1.1,.012),(1.4,2.0,.02)):
        x=cap_cross_probability(a,r,eps,n=500)
        y=cap_cross_probability(a/r,1,eps/r,n=500)
        assert abs(x-y)<2e-12,(x,y)
        tests+=1
        d=2*(a+r); C=1/(4*a*(a+r))
        aa=1/(2*C*d); rr=d/2-aa
        assert abs(a-aa)<1e-12 and abs(r-rr)<1e-12
        tests+=1

    # Two branches meet with identical values/slopes but unequal curvatures.
    h=0.5
    assert psi(h)==0.5 and abs((-1)-(-1/(4*h*h)))<1e-14
    assert 1/(2*h**3)==4
    tests+=1
    print('CAPSULE_SURFACE_DIAMETER_CROSSOVER_CHECKS_OK',tests)

if __name__=='__main__':
    check()

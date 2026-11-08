"""Independent finite checks of theta/Wronskian formulas for Gaussian Gabor windows.

Run: python3 CHECK.py (Python standard library only).
Numerical samples do not establish the global frame theorem; its proof is analytic.
"""
import cmath
import math


def raw_fibers(lam, x, w, cutoff=28):
    E=O=HE=HO=0j
    for k in range(-cutoff,cutoff+1):
        z=math.exp(-math.pi*lam*(x-k)**2)*cmath.exp(2j*math.pi*k*w)
        if k%2==0:
            E+=z
            HE+=(x-k)*z
        else:
            O+=z
            HO+=(x-k)*z
    return E,O,HE,HO


def constant(lam, cutoff=25):
    return sum((4*j+1)*math.exp(-math.pi*lam*(4*j+1)**2/2)
               for j in range(-cutoff,cutoff+1))


def rhs(lam,x,w):
    c=constant(lam)
    z=sum(math.exp(-2*math.pi*lam*(x-.5-j)**2)
          *cmath.exp(2j*math.pi*j*(2*w+.5)) for j in range(-28,29))
    return c*cmath.exp(2j*math.pi*w)*z


def fiber_margin(lam,c,x,w):
    E,O,HE,HO=raw_fibers(lam,x,w)
    return abs(HE-c*E)**2+abs(HO-c*O)**2


checks=0
for lam in (0.35,0.6,1.0,1.7,3.0):
    assert constant(lam)>0
    for x,w in ((.13,.07),(.37,.21),(.71,.41),(.92,.49),(.0,.0),(.0,.25)):
        E,O,HE,HO=raw_fibers(lam,x,w)
        err=abs(HE*O-HO*E-rhs(lam,x,w))
        assert err < 3e-11, (lam,x,w,err)
        checks+=1
    assert fiber_margin(lam,0j,0,0)<1e-22
    checks+=1
for c in (0.05,-.1,0.7+0.3j,-.2j):
    for lam in (.6,1.,2.):
        m=min(fiber_margin(lam,c,j/30,k/60) for j in range(31) for k in range(31))
        assert m>1e-12,(lam,c,m)
        checks+=1
print('GAUSSIAN_HERMITE_HALF_DENSITY_CHECKS_PASSED',checks)

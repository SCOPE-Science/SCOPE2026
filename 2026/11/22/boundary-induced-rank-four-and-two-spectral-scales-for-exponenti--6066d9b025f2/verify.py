"""Numerical checks of finite-interval exponential smoother commutator.
Requires Python 3 and mpmath; optional numpy for discretized eigenvalues.
These checks are finite illustrations; the proof is analytical.
"""
import math
import random
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 65

def f(a, x, L, parity):
    return mp.exp(-a*x) + parity*mp.exp(-a*(L-x))

def sigma(a,b,L,parity):
    p=parity
    # Centered formulas reduce the size of cancellation.
    ua = lambda t: 2*mp.exp(-a*L/2)*(mp.cosh(a*t) if p==1 else mp.sinh(a*t))
    vb = lambda t: 2*mp.exp(-b*L/2)*(mp.cosh(b*t) if p==1 else mp.sinh(b*t))
    # Gram determinant is a positive double integral of squared two-by-two minors.
    # Four-dimensional Gram form suffices for moderate intervals.
    A=2*mp.quad(lambda t:ua(t)**2,[0,L/2])
    B=2*mp.quad(lambda t:vb(t)**2,[0,L/2])
    C=2*mp.quad(lambda t:ua(t)*vb(t),[0,L/2])
    return mp.sqrt(max(mp.mpf('0'),A*B-C*C))/(2*(a+b))

def kernel(a,b,L,x,y):
    return (mp.exp(-b*x-a*y)-mp.exp(-a*x-b*y)
      + mp.exp(-b*(L-x)-a*(L-y))
      - mp.exp(-a*(L-x)-b*(L-y)))/(a+b)

rng=random.Random(271828)
count=0
for i in range(20):
    a=mp.mpf(str(rng.uniform(.2,2)))
    b=mp.mpf(str(rng.uniform(2.5,4.5)))
    L=mp.mpf(str(rng.uniform(.5,3)))
    x=mp.mpf(str(rng.uniform(0,float(L))))
    y=mp.mpf(str(rng.uniform(0,float(L))))
    pts=sorted({mp.mpf(0),x,y,L})
    direct=mp.mpf(0)
    for lo,hi in zip(pts[:-1],pts[1:]):
        direct+=mp.quad(lambda z:mp.exp(-a*abs(x-z)-b*abs(y-z))
                        -mp.exp(-b*abs(x-z)-a*abs(y-z)),[lo,hi])
    assert abs(direct-kernel(a,b,L,x,y)) < mp.mpf('1e-53')
    assert sigma(a,b,L,1)>sigma(a,b,L,-1)>0
    count+=2

for a,b in [(mp.mpf(1),mp.mpf(2)),(mp.mpf('0.8'),mp.mpf('2.3'))]:
    asymp_limit=(b-a)/(2*(a+b)**2*mp.sqrt(a*b))
    for L in (mp.mpf(10),mp.mpf(20),mp.mpf(50)):
        p=sigma(a,b,L,1)
        m=sigma(a,b,L,-1)
        assert p>m>0
        if L==50:
            assert abs(p/asymp_limit-1)<mp.mpf('1e-12')
            assert abs(m/asymp_limit-1)<mp.mpf('1e-12')
        count+=2

for L in [mp.mpf('.2'),mp.mpf('.1'),mp.mpf('.05')]:
    a,b=mp.mpf('.8'),mp.mpf('2.3')
    cp=(b-a)/(6*mp.sqrt(5))
    cm=a*b*(b-a)/(120*mp.sqrt(21))
    rp=sigma(a,b,L,1)/(cp*L**3)
    rm=sigma(a,b,L,-1)/(cm*L**5)
    assert mp.mpf('.65')<rp<1 and mp.mpf('.65')<rm<1
    print('L', L, 'cubic ratio', mp.nstr(rp,14), 'quintic ratio',mp.nstr(rm,14))
    count+=2

# The centered wedge-integral identities used for the sharp constants.
# The moments are exact integrals over [-L/2,L/2] after factoring L.
M2=Fraction(1,12);M4=Fraction(1,80);M6=Fraction(1,448)
assert M4-M2*M2==Fraction(1,180)
assert M2*M6-M4*M4==Fraction(1,33600)
count+=2

try:
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    a,b,L=0.7,2.1,1.5
    n=96
    z,w=leggauss(n)
    xs=(z+1)*L/2
    ws=w*L/2
    X,Y=np.meshgrid(xs,xs,indexing='ij')
    sw=np.sqrt(ws)
    Ka=np.exp(-a*np.abs(X-Y))*sw[:,None]*sw[None,:]
    Kb=np.exp(-b*np.abs(X-Y))*sw[:,None]*sw[None,:]
    C=Ka@Kb-Kb@Ka
    # Nyström product has O(n^-2) quadrature errors due diagonal cusps;
    # direct quadrature of exact finite-rank commutator is sharper.
    Cexact=np.array([[float(kernel(mp.mpf(str(a)),mp.mpf(str(b)),mp.mpf(str(L)),mp.mpf(str(x)),mp.mpf(str(y)))) for y in xs] for x in xs])*sw[:,None]*sw[None,:]
    singular=np.linalg.svd(Cexact,compute_uv=False)
    plus=float(sigma(mp.mpf(str(a)),mp.mpf(str(b)),mp.mpf(str(L)),1))
    minus=float(sigma(mp.mpf(str(a)),mp.mpf(str(b)),mp.mpf(str(L)),-1))
    assert max(abs(singular[i]-v) for i,v in enumerate([plus,plus,minus,minus])) < 3e-14
    assert singular[4] < 1e-14
    assert np.linalg.norm(C-Cexact,2)<2e-4
    count+=3
except ImportError:
    print('numpy absent: optional matrix discretization skipped')

print('PASS:',count,'analytic-identity/quadrature/asymptotic/spectrum checks')

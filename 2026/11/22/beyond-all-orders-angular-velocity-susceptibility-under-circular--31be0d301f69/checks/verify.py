"""Deterministic checks for circular-reset angular susceptibility.
Run: python checks/verify.py. Requires NumPy and SciPy.
Analytical proof is in RESULT.md; numerical checks are not a substitute.
"""
import math
import numpy as np
from scipy.special import ive
from scipy.integrate import quad
from numpy.polynomial.laguerre import laggauss

S, W = laggauss(96)

def a_age(t, R, Tx, Ty):
    """Bessel-integral exact susceptibility at fixed reset age t>0."""
    if Tx == Ty: return 0.0
    a = R * math.exp(-t)
    q = -math.expm1(-2*t)
    high, low = max(Tx, Ty), min(Tx, Ty)
    vh, vl = high*q, low*q
    # q_radial^2=a^2+2*vh*s; rescaled I_1 avoids overflow.
    z = (a*a + 2*vh*S)*(1/vl-1/vh)/4
    avg = np.dot(W, (2*vh*S/(a*a+2*vh*S))*ive(1,z))
    return math.copysign(1.0,Ty-Tx)*math.sqrt(vh/vl)*math.exp(-a*a/(2*vh))*float(avg)

def exact_chi(r, R, Tx, Ty):
    if Tx == Ty: return 0.0
    high = max(Tx,Ty)
    tstar = R/(2*math.sqrt(high*r))
    zstar = R*math.sqrt(r/high)
    val=quad(lambda x: r*tstar*math.exp(-r*tstar*x+zstar)*a_age(tstar*x,R,Tx,Ty),
             1.0e-9, 20, epsabs=1e-13, epsrel=1e-10, limit=600)[0]
    return math.exp(-zstar)*val

def asym_chi(r,R,Tx,Ty):
    hi, lo = max(Tx,Ty),min(Tx,Ty)
    return (math.copysign(1.0,Ty-Tx)*2*hi/(R*math.sqrt(hi-lo))*
            math.exp(R*R/(4*hi)) * r**(-0.5) *
            math.exp(-R*math.sqrt(r/hi)))

def contour_exact(a,z):
    if abs(z)<=a: return 0j
    return (1-a*a/abs(z)**2)*z/z.conjugate()

def contour_quad(a,z, count=32768):
    th=2*np.pi*np.arange(count)/count
    w=a*np.exp(1j*th)+z
    return np.mean(w/np.conjugate(w))

def independent_polar_age(t,R,Tx,Ty):
    a=R*math.exp(-t)
    vx=Tx*(-math.expm1(-2*t));vy=Ty*(-math.expm1(-2*t))
    def ang(q):
        return quad(lambda th: -(math.cos(2*th))*math.exp(-q*q/2*(math.cos(th)**2/vx+math.sin(th)**2/vy)),
                    0,2*math.pi,epsabs=1e-11)[0]
    return quad(lambda q:q*(1-a*a/(q*q))*ang(q)/(2*math.pi*math.sqrt(vx*vy)),
                a,12,epsabs=1e-11)[0]

checks=0
for z in [0.2+0.35j, 0.9+0.1j, 1.8+0.5j, -2.+0.3j, 0.1-3j]:
    got=contour_quad(1.,z)
    assert abs(got-contour_exact(1.,z))<1e-12,(z,got)
    checks+=1
for t in [0.2,0.5,1.]:
    v=a_age(t,1.,1.,2.)
    z=independent_polar_age(t,1.,1.,2.)
    assert abs(v-z)<2e-9,(t,v,z)
    assert v>0 and abs(v+a_age(t,1.,2.,1.))<1e-15
    assert a_age(t,1.,2.,2.)==0
    checks+=4
for r in [1,5,20,100,500]:
    val=exact_chi(r,1.,1.,2.)
    assert val>0 and abs(val+exact_chi(r,1.,2.,1.))<1e-13
    checks+=2
for r in [10000.,50000.,200000.]:
    ratio=exact_chi(r,1.,1.,2.)/asym_chi(r,1.,1.,2.)
    assert 0.93<ratio<1.02,(r,ratio)
    if r==200000.: assert ratio>0.98
    checks+=1
print('PASS',checks,'independent contour, polar, symmetry, sign and sharp-asymptotic checks')

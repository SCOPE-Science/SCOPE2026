"""Finite quadrature diagnostics for polygonal-corner Berezin power laws.
The mathematical theorem is proved analytically; numerical checks are non-certifying.
"""
import math
from scipy.integrate import quad
from scipy.special import roots_legendre
import numpy as np

x,w=roots_legendre(96)
angles=(x+1)*math.pi/2
weights=w*math.pi/2

def model_ratio(p,sigma,r,delta=0.5):
    # Wedge 0<arg w<pi/p, z=r*exp(i*pi/(2p)).
    # normalized Berezin transform divided by r^sigma.
    a=angles/p
    wa=weights/p
    def f(logt):
        t=math.exp(logt)
        power=t**p
        den=(1+power**2+2*power*np.sin(p*a))**2
        return 4*p*p/math.pi*np.sum(wa/den)*math.exp((sigma+2*p)*logt)
    return quad(f, -35, math.log(delta/r), epsabs=1e-9,epsrel=1e-9,limit=500)[0]

def F_of_s(s):
    # Mellin moment of normalized half-plane Bergman coherent-state measure at i.
    def f(logt):
        t=math.exp(logt)
        den=(1+t*t+2*t*np.sin(angles))**2
        return 4/math.pi * float(np.sum(weights/den))*math.exp((s+2)*logt)
    return quad(f,-35,35,epsabs=1e-10,epsrel=1e-10,limit=400)[0]

if __name__=='__main__':
    v=math.pi**2/4-2*math.log(2)
    print('exact logarithmic variance', v)
    for s in (-1,0,0.5,1):
        print('bisector Mellin moment',s,F_of_s(s))
    print('symmetry error',abs(F_of_s(1)-F_of_s(-1)))
    for sigma in (-2,0,2):
        # p=2, two-sided open Mellin strip (-4,4)
        val=model_ratio(2,sigma,1e-4)
        print('subcritical sigma',sigma,'normalized',val,'expected',F_of_s(sigma/2))
    for r in (1e-2,1e-3,1e-4,1e-5):
        critical=model_ratio(2,4,r)/math.log(1/r)
        supercritical=model_ratio(2,6,r)*r**2
        print('r',r,'critical coeff',critical,'limit',8,
              'supercritical coeff',supercritical,'limit',1)
    assert abs(F_of_s(-1)-F_of_s(1))<1e-7
    assert abs(F_of_s(0)-1)<1e-7
    assert abs(model_ratio(2,-2,1e-4)-F_of_s(-1))<.002
    print('PASS: 12 consistency diagnostics (quadrature, not proof)')

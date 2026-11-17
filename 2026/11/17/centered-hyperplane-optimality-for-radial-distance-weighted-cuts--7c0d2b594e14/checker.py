"""Reproducibility checks for radial distance-weighted hyperplane cuts.
Run: python checker.py (requires numpy and scipy).
Numerical quadrature supplements, and does not replace, the proofs.
"""
import math
import numpy as np
from scipy.integrate import quad

def exact_spherical_ratio(d):
    assert d >= 2
    m = d - 2
    # The centered-angle variable q=theta-pi/2 has density proportional to cos(q)^m.
    a=quad(lambda q: math.cos(q/2)*math.cos(q)**m, -math.pi/2,math.pi/2,
           epsabs=1e-12,epsrel=1e-12)[0]
    b=quad(lambda q: q*math.sin(q/2)*math.cos(q)**m, -math.pi/2,math.pi/2,
           epsabs=1e-12,epsrel=1e-12)[0]
    return .5 + b/(math.pi*a)

assert abs(exact_spherical_ratio(2)-2/math.pi)<2e-12
assert abs(exact_spherical_ratio(3)-(1-4/(3*math.pi)))<2e-12
for d in (3,4,5,7,10,20,100,300):
    assert .5 < exact_spherical_ratio(d)<.64
for d in (100,200,300):
    a=.5 + 1/(2*math.pi*d)+1/(2*math.pi*d*d)
    assert abs(exact_spherical_ratio(d)-a)<.5/d**3

# Independent cyclic-convolution evaluation of all-pairs circle cuts.
N=16384
angles=2*math.pi*np.arange(N)/N
kernel=2*np.abs(np.sin(angles/2))
Khat=np.fft.fft(kernel)
L=N*kernel.sum()
for t in (-.98,-.75,-.4,0,.24,.63,.91):
    mask=(np.cos(angles)>t).astype(float)
    in_kernel=np.fft.ifft(np.fft.fft(mask)*Khat).real
    C=2*(mask.sum()*kernel.sum()-float(mask@in_kernel))
    expected=2/math.pi*math.sqrt(1-t*t)
    assert abs(C/L-expected)<3e-4,(t,C/L,expected)
print('PASS: sphere d=2,3 exact; eight dimension quadratures; three high-d remainders; seven independent circle cut profiles')

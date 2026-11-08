"""Reproducibility checks for a two-band Fourier concentration trace law.

Run: python check.py.  Requires numpy and scipy.
Finite quadrature checks support but do not replace the analytic theorem.
"""
import math
from scipy.integrate import quad

PI = math.pi
checks = 0

def claim(condition, explanation):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(explanation)

def sinc(x):
    return 1 if x == 0 else math.sin(PI*x)/(PI*x)

def cross_freq(L,W,c):
    assert L>0 and W>0 and 2*c>W
    def kernel(h):
        return (W-abs(h))*(math.sin(PI*L*(2*c+h))/(PI*(2*c+h)))**2
    return quad(kernel,-W,0,epsabs=1e-13,epsrel=1e-12)[0] + quad(kernel,0,W,epsabs=1e-13,epsrel=1e-12)[0]

def cross_time(L,W,c):
    def kernel(t):
        return (L-t)*sinc(W*t)**2*math.cos(4*PI*c*t)
    return 2*W*W*quad(kernel,0,L,epsabs=1e-13,epsrel=1e-12,limit=500)[0]

def cross_asym(L,W,c):
    A=sinc(L*W)**2
    return W*W/(8*PI*PI*c*c)*(1-A*math.cos(4*PI*L*c))

def d_cross(L,W,c):
    def integrand(h):
        z=2*c+h
        phase=PI*L*z
        return (W-abs(h))*(2*L/PI*math.sin(2*phase)/(z*z)-4/PI**2*math.sin(phase)**2/(z**3))
    return quad(integrand,-W,0,epsabs=1e-14,epsrel=1e-12)[0]+quad(integrand,0,W,epsabs=1e-14,epsrel=1e-12)[0]

for L,W in [(0.7,0.8),(1.0,1.0),(1.0,0.75),(1.5,2.0),(2.2,0.9)]:
    for c in [2,3,5,8,12]:
        if 2*c<=W:
            continue
        a=cross_freq(L,W,c)
        b=cross_time(L,W,c)
        claim(a>0,'cross-band overlap strictly positive')
        claim(abs(a-b) < 2e-11,'frequency versus time kernel')
        h=1e-4
        numerical=(cross_freq(L,W,c+h)-cross_freq(L,W,c-h))/(2*h)
        claim(abs(numerical-d_cross(L,W,c)) < 1e-6,'derivative integral')
for L,W in [(0.7,0.8),(1,1),(1,.75),(1.5,2.0)]:
    for c in [40.,80.,160.]:
        a=cross_freq(L,W,c); b=cross_asym(L,W,c)
        claim(abs(a-b)*c**3 < 0.5,'uniform first-order asymptotic error')
for L,W in [(1,1),(1.5,2)]:
    for c in [40.25,41.25,50.25,60.25,80.25]:
        assert abs(L*W-round(L*W))<1e-10
        claim(d_cross(L,W,c)<0,'eventual monotonicity at integer product')
for L,W in [(1,.75),(.7,.8)]:
    for k in range(30,38):
        c=(k+.5)/(4*L)
        if 2*c<=W:continue
        v=d_cross(L,W,c)
        sign=1 if (k%2==0) else -1
        claim(v*sign>0,'alternating derivatives off resonance')
for k in [10000,10001,30000,30001]:
    L,W=2.2,.9
    c=(k+.5)/(4*L)
    claim(d_cross(L,W,c)*(-1)**k>0,'eventual sign changes near resonance')
print('TWO_BAND_TRACE_CHECKS_PASS', checks)

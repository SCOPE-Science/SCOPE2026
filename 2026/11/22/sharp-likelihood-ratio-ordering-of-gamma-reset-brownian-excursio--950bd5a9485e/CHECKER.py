"""Deterministic numerical checks of the Gamma reset-return likelihood-ratio theorem.

Run: python CHECKER.py  (requires SciPy and NumPy).
All comparisons here are finite-dimensional corroboration, not proofs of global order.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, kv, erfc

checks = 0

def verify(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError(label)

def g(k, z):
    if z == 0:
        if k <= 0.5:
            return float('inf')
        return gamma(k - 0.5)/(math.sqrt(math.pi) * gamma(k))
    return 2**(1.5-k) / (math.sqrt(math.pi)*gamma(k)) * z**(k-0.5) * kv(k-0.5,z)

def integral(k, z, power):
    val,err=quad(lambda t:(t-z)**power*g(k,t), z, np.inf, epsabs=5e-11, epsrel=5e-11, limit=300)
    return val

def ew(k):
    return 2*gamma(k+0.5)/(math.sqrt(math.pi)*gamma(k))

def density(k,z,v):
    return (v*integral(k,z,1)+integral(k,z,0))/(v*k+ew(k))

def tail(k,z,v):
    return (0.5*v*integral(k,z,2)+integral(k,z,1))/(v*k+ew(k))

for k in (0.6, 1.0, 1.5, 2.0, 2.5):
    verify(abs(integral(k,0,0)-1) < 3e-9, 'g normalization')
    verify(abs(integral(k,0,1)-ew(k)) < 3e-9, 'g mean')
    verify(abs(integral(k,0,2)/2-k) < 3e-9, 'brownian reward mass')

for z in (0.3,0.8,1.6,3.0):
    for v in (0.2,0.7,2.5,12.0):
        verify(abs(tail(1,z,v)-math.exp(-z)) < 4e-9, 'exponential invariance')
        exact = math.exp(-z)*(v*(z+4)+(z+3))/(4*v+3)
        verify(abs(tail(2,z,v)-exact) < 4e-9, 'Erlang-two exact tail')

for k in (0.6,1.5,2,2.5):
    vlow, vhigh=0.4,3.0
    grid=np.linspace(0.3,4.0,9)
    ratio=[]
    for z in grid:
        a,b=tail(k,z,vlow),tail(k,z,vhigh)
        # The sign applies at every positive threshold, not just the center and tails.
        verify((b>a) if k<1 else (b<a), 'stochastic-order tail')
        ratio.append(density(k,z,vhigh)/density(k,z,vlow))
    increments=np.diff(ratio)
    verify(np.all(increments>1e-8) if k<1 else np.all(increments<-1e-8), 'likelihood ratio monotonicity')

for k in (0.6,1.5,2):
    for z in (0.35,1.0,2.0):
        v=1.7
        q=tail(k,z,v)
        a=k
        b=ew(k)
        A=0.5*integral(k,z,2)
        B=integral(k,z,1)
        recovered=(B-q*b)/(q*a-A)
        verify(abs(recovered-v) < 1e-8, 'single-threshold speed inversion')

# Independently integrate the original Brownian propagator over Gamma reset times.
for k in (0.6, 1.0, 2.0):
    for x in (0.5, 1.3, 2.8):
        def gamma_clock(t):
            return t**(k-1)*math.exp(-t)/gamma(k)
        raw_return,_=quad(lambda t: gamma_clock(t)*erfc(x/(2*math.sqrt(t))),
                          0, np.inf, epsabs=2e-10, epsrel=2e-10)
        raw_diff,_=quad(lambda t: gamma_clock(t)*(
                          2*math.sqrt(t/math.pi)*math.exp(-x*x/(4*t))
                          -x*erfc(x/(2*math.sqrt(t)))),
                        0, np.inf, epsabs=2e-10, epsrel=2e-10)
        verify(abs(raw_return-integral(k,x,0)) < 2e-8, 'independent Brownian return kernel')
        verify(abs(raw_diff-integral(k,x,1)) < 2e-8, 'independent Brownian diffusion kernel')

print('PASS: %d deterministic analytical/numerical comparisons' % checks)

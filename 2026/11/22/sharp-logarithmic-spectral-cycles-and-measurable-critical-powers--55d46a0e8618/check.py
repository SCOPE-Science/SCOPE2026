"""Reproducibility checks for log-periodic radial Gaussian Fock Toeplitz symbols.
Finite numerical diagnostics complement, but do not replace, the analytic proof.
Requires Python, NumPy and SciPy. Run: python check.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln
from scipy.optimize import brentq

D = 2
BETA = 1.0
OMEGA = 1.0
ETA = 0.25
assert 0 < ETA < BETA / math.hypot(BETA, OMEGA)
Q = D / BETA

def symbol(s):
    return (1+s)**(-BETA) * (1+ETA*math.cos(OMEGA*math.log1p(s)))

def eig(k):
    a = k+D
    lo = max(0.0, a - 19*math.sqrt(a))
    hi = a + 19*math.sqrt(a) + 200
    def density_times_symbol(s):
        if s == 0.0:
            return 0.0
        return math.exp((a-1)*math.log(s)-s-gammaln(a))*symbol(s)
    return quad(density_times_symbol, lo, hi, epsabs=3e-12, epsrel=3e-12, limit=150)[0]

def H(phi):
    low=(1-ETA)**(1/BETA)
    high=(1+ETA)**(1/BETA)
    return brentq(lambda x:x**BETA-1-ETA*math.cos(phi+OMEGA*math.log(x)),low,high,xtol=1e-14)

count = 0
values = [eig(k) for k in range(361)]
assert all(values[k] > values[k+1] for k in range(360))
count+=360
for k in [20,40,80,160,320]:
    err = abs(values[k]-symbol(k))*k**(BETA+1)
    assert err < 3.0, (k,err)
    count += 1
for phase in np.linspace(0,2*math.pi,101):
    h = H(float(phase))
    assert abs(h**BETA-1-ETA*math.cos(phase+OMEGA*math.log(h))) < 1e-11
    assert (1-ETA)**(1/BETA)-1e-12 <= h <= (1+ETA)**(1/BETA)+1e-12
    count+=2
for t in [.10,.07,.05,.04,.03,.02,.015,.012]:
    assert values[-1] < t
    observed=sum((k+D-1) for k,v in enumerate(values) if v>t) # d=2, multiplicity k+1
    phi=OMEGA/BETA*math.log(1/t)
    smooth=t**(-Q)*H(phi)**D/math.factorial(D)
    scale=t**(-(D-1)/BETA)
    assert abs(observed-smooth)/scale<3.5,(t,observed,smooth,scale)
    count+=1
# The log-periodic orbit must attain both of its exact theoretical endpoints.
for val,cosphase in [(1+ETA,1),(1-ETA,-1)]:
    x = val**(1/BETA)
    phi = -OMEGA*math.log(x)+(0 if cosphase==1 else math.pi)
    assert abs(H(phi)-x) < 1e-10
    count+=1
print('FOCK_LOGPERIODIC_CHECK_OK',count)

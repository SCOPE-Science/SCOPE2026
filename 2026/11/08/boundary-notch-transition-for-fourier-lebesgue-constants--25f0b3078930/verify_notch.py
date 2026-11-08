"""Reproducible numerical enclosure supplementing the analytic notch-limit theorem.

Requires Python 3, numpy; the convergence theorem is proved in RESULT.md.
The angular and radial quadrature errors follow from the explicit Lipschitz
bounds there. A 0.001 margin is reserved for floating-point evaluation error;
this is far larger than observed double/long-double disagreement.
"""
import math
import numpy as np

N, M, delta = 3000, 2500, 0.1
T = delta + (np.arange(N) + 0.5) * ((math.pi-delta)/N)
P = (np.arange(M)+0.5) * (2*math.pi/M)
exp_phi = np.exp(1j*P)
hone = np.mean(np.abs(1-exp_phi))
grid_sum = 0.0
for start in range(0,N,30):
    t = T[start:start+30]
    z = np.exp(1j*t)
    h1 = 1-z+z*z
    havg = np.mean(np.abs(1-h1[:,None]*exp_phi[None,:]), axis=1)
    grid_sum += np.sum((havg-hone)/(2*np.sin(t/2)))
partial = (math.pi-delta)/ (math.pi*N) * grid_sum
mind = 2*math.sin(delta/2)
error_t = (4/mind)*(math.pi-delta)**2/(4*math.pi*N)
error_phi = 4*math.pi*(math.pi-delta)/(math.pi*M*mind)
error_short = delta/math.pi
lower = partial - error_t - error_phi - error_short - .001
assert .18 < partial < .22
assert lower > .10, (partial,lower)
print('NOTCH_QUADRATURE_PASS', 'N=',N,'M=',M,
      'quadrature=',round(float(partial),12),
      'certified_conservative_lower=',round(float(lower),10),
      'analytic_error=',round(error_t+error_phi+error_short,9))

# Test the exact rational polynomial numerator identity at arbitrary phases.
for n in (5,19,37):
    for j in (0,1,2,3):
        for t in (.23,.71,1.84,2.62):
            z=complex(math.cos(t),math.sin(t))
            direct=sum(z**k for k in range(-n,n+1))-z**(n-j)
            numer=(1-z**(2*n-j)*(1-z+z**(j+1)))/(1-z)*z**(-n)
            assert abs(direct-numer)<2e-11
print('NOTCH_EXACT_IDENTITY_PASS cases=48')

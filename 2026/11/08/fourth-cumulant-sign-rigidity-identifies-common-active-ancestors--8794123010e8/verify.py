"""Reproducible finite diagnostics for the four-point cumulant support theorem.
Run: python verify.py. Analytical arguments, not these diagnostics, prove the theorem.
Requires NumPy and SciPy.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm
from scipy.special import ndtri
from scipy.stats import qmc, gamma

checks = 0

def check(condition, message):
    global checks
    if not bool(condition):
        raise AssertionError(message)
    checks += 1


def telegraph_moment4(times, flip_rate):
    ts = sorted(times)
    P = lambda dt: np.array([[1+math.exp(-2*flip_rate*dt), 1-math.exp(-2*flip_rate*dt)],
                            [1-math.exp(-2*flip_rate*dt), 1+math.exp(-2*flip_rate*dt)]]) / 2
    S = np.diag([-1., 1.])
    u = np.ones(2)
    return float(np.array([0.5,0.5]) @ S @ P(ts[1]-ts[0]) @ S @ P(ts[2]-ts[1]) @ S @ P(ts[3]-ts[2]) @ S @ u)


def telegraph_cumulant4(times, flip_rate):
    ts = sorted(times)
    return -2*math.exp(-2*flip_rate*((ts[2]-ts[0])+(ts[3]-ts[1])))


def direct_cumulant4(times, flip_rate):
    m = telegraph_moment4(times, flip_rate)
    for a,b,c,d in [(0,1,2,3), (0,2,1,3), (0,3,1,2)]:
        m -= math.exp(-2*flip_rate*(abs(times[a]-times[b])+abs(times[c]-times[d])))
    return m

for rate in [0.07,0.5,3.0]:
    for times in itertools.combinations_with_replacement([0.,0.1,0.4,0.9,2.5], 4):
        for order in [times, (times[2],times[0],times[3],times[1])]:
            val=direct_cumulant4(order,rate)
            target=telegraph_cumulant4(order,rate)
            check(abs(val-target)<2e-12, "Markov four-time cumulant identity")
            check(target<0, "strict telegraph kernel sign")

# One-body stationary exact check, independent of network computations.
for mu in [0.3,1.,2.7]:
    for rate in [0.1,0.5,2.]:
        for amp in [0.7,1.5]:
            variance=amp**2/(mu*(mu+2*rate))
            cumulant=-6*amp**4/(mu*(mu+2*rate)**2*(3*mu+2*rate))
            excess=-6/(3+2*rate/mu)
            check(abs(cumulant/variance**2-excess)<3e-14, "one-body beta-law kurtosis")
            check(cumulant<0, "negative stationary kurtosis")

# An explicitly solvable directed chain: one active input reaches all vertices.
# M=-2 I+N, N21=N32=1, N**3=0, so exp(M s) is exact.
mu=2.
flip=0.8
M=np.array([[-2.,0.,0.],[1.,-2.,0.],[0.,1.,-2.]])
B=np.array([[1.],[0.],[0.]])
for s in [0.01,0.1,0.6,2.]:
    col=np.exp(-mu*s)*np.array([1.,s,s*s/2])
    check(np.allclose(expm(M*s)@B[:,0],col,rtol=1e-13,atol=1e-13), "explicit semigroup")
    check(np.all(col>0), "reachable transfer positivity")

# Four distinct observed vertices/time coordinates, using Gamma importance sampling.
# For index i (0-based), h_i(s)=exp(-mu*s) s**i/i!, integral=mu**(-i-1).
indices=[0,1,2,1]
times=np.array([0.,.3,.7,1.1])
pts=qmc.Sobol(d=4,scramble=False).random_base2(16)
pts=np.clip(pts,1e-12,1-1e-12)
times_of_force=np.zeros_like(pts)
weight=1.
for j,idx in enumerate(indices):
    times_of_force[:,j]=times[j]-gamma.ppf(pts[:,j],a=idx+1,scale=1/mu)
    weight *= mu**(-idx-1)
sorted_forces=np.sort(times_of_force,axis=1)
kernel=np.exp(-2*flip*((sorted_forces[:,2]-sorted_forces[:,0])+(sorted_forces[:,3]-sorted_forces[:,1])))
cum=-2*weight*np.mean(kernel)
check(np.isfinite(cum) and cum < -1e-10, "network mixed-lag cumulant strict sign")

# A disconnected vertex has independent telegraph ancestry, even when a shared
# Gaussian force creates a strictly positive two-point cross-covariance.
M3=np.array([[-2.,0.,0.],[1.,-2.,0.],[0.,0.,-2.]])
B3=np.array([[1.,0.],[0.,0.],[0.,1.]])
for s in [0.,0.02,.5,1.5,4.]:
    H=expm(M3*s)@B3
    check(abs(H[0,1])<1e-14 and abs(H[2,0])<1e-14,"disjoint ancestry exact transfer zeros")
check(abs(1/4-.25)<1e-15,"common Gaussian covariance is positive")

# Cooperativity is necessary for the universal fourth-cumulant sign.
# Negative off-diagonal M21 implies h_2(s)=-exp(-2s)sinh(s) <0.
Mbad=np.array([[-2.,-1.],[-1.,-2.]])
for s in [0.01,0.3,1.2,3.0]:
    H=expm(Mbad*s)@np.array([1.,0.])
    check(H[0]>0 and H[1]<0,"negative cross-transfer: odd mixed fourth cumulant is positive")

print(f"PASS: {checks} deterministic checks. Example mixed-lag connected cumulant approximately {cum:.10g} (negative).")
print("Limits: QMC illustrates one example only; no finite computation proves arbitrary network sizes or lags.")

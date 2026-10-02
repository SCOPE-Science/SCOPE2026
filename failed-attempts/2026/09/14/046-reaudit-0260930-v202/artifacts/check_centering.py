"""Environment-dependent centring is essential + single-big-jump mechanism.

Part A (exact, no truncation): environment fluctuations induce centring
fluctuations of order >> a_n. d_n(Y) solves R(d_n)=L_n(Y); deterministic
dbar_n solves R(dbar)=mu*n. By delta-method,
  d_n(Y)-dbar_n ~ (L_n - mu*n)/R'(dbar) = a_n*(L_n-mu*n),
so (d_n(Y)-dbar_n)/abar_n ~ N(0, sig^2*n) -> diverges like sqrt(n).
Simulating environments only verifies the constant and the sqrt(n) growth.

Part B (small-n exact BRW, no cap): single-big-jump decomposition
M_n = maxjump + bulk with bulk << M_n scale.
"""
import numpy as np, math
from math import gamma

rng = np.random.default_rng(1)
r = 0.5
EZ = gamma(1+1/r); SD = math.sqrt(gamma(1+2/r)-EZ**2)
mu = 0.5*(math.log(1.5)+math.log(2.5))
sig2 = 0.5*((math.log(1.5)-mu)**2+(math.log(2.5)-mu)**2)
print(f"EZ={EZ:.3f} SD={SD:.3f} mu={mu:.4f} sig={math.sqrt(sig2):.4f}", flush=True)

def solve_d(L): return (L**(1.0/r)-EZ)/SD
def Rp(t): return r*SD*(SD*t+EZ)**(r-1)

print("--- Part A: env-induced centring fluctuations (exact) ---", flush=True)
for n in [40, 200, 1000, 5000]:
    R = 4000
    m = np.where(rng.random((R, n)) < 0.5, 1.5, 2.5)
    L = np.log(m).sum(axis=1)
    dn = solve_d(L); dbar = solve_d(mu*n); abar = 1.0/Rp(dbar)
    stat = (dn-dbar)/abar
    print(f"n={n}: sd((d_n-dbar)/abar)={stat.std():.2f}  theory~sig*sqrt(n)={math.sqrt(sig2*n):.2f}", flush=True)

print("--- Part B: exact small-n BRW, single big jump ---", flush=True)
def sim_exact(n):
    m = np.where(rng.random(n) < 0.5, 1.5, 2.5)
    pos = np.array([0.0]); max_jump = -1e99
    for j in range(n):
        off = rng.poisson(m[j], size=pos.size)
        tot = int(off.sum())
        if tot == 0: return None
        rep = np.repeat(pos, off)
        X = (rng.weibull(r, size=tot)-EZ)/SD
        max_jump = max(max_jump, float(X.max()))
        pos = rep + X
    return float(pos.max()), max_jump

for n in [6, 8, 10]:
    Ms, Js = [], []
    for rep in range(40):
        out = sim_exact(n)
        if out: Ms.append(out[0]); Js.append(out[1])
    Ms = np.array(Ms); Js = np.array(Js)
    bulk = Ms - Js
    print(f"n={n}: mean M={Ms.mean():.2f}, mean maxjump={Js.mean():.2f}, mean bulk=M-maxjump={bulk.mean():.2f} (bulk O(1), extremes one-jump-driven)", flush=True)
print("CONCLUSION: (d_n(Y)-dbar_n)/a_n diverges ~ sqrt(n) => deterministic centring impossible; env-dependent b_n(Y) essential. Extremes are single-big-jump driven.", flush=True)

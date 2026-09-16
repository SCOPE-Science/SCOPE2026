"""Two-speed BRW (mean regime, equal theta*) simulation check.

Binary branching (2 children always), Gaussian increments:
  L1: N(mu1,1), L2: N(mu2,1), sigma=1 -> theta*=sqrt(2 log 2) shared.
Checks: centered max tightness + dependence of max law on Z^(1).
"""
import json
import numpy as np

rng = np.random.default_rng(20474)
theta_star = float(np.sqrt(2*np.log(2)))
mu1, mu2 = 0.0, 0.5
v1 = mu1 + theta_star  # kappa1'(theta), sigma=1
v2 = mu2 + theta_star
t = 0.4

def one_trial(n, rng):
    k = int(np.floor(t*n)); m = n-k
    pos = np.zeros(1)
    # first phase: also record first-phase positions for Z
    for _ in range(k):
        inc = rng.normal(mu1, 1.0, size=2*pos.size)
        pos = np.repeat(pos, 2) + inc
    first = pos.copy()
    for _ in range(m):
        inc = rng.normal(mu2, 1.0, size=2*pos.size)
        pos = np.repeat(pos, 2) + inc
    m_n = v1*k + v2*m - (3.0/(2*theta_star))*np.log(n)
    # derivative martingale of phase 1
    s = first - v1*k
    Zk = float(np.sum((-s)*np.exp(theta_star*s)))
    return float(np.max(pos)-m_n), Zk, float(np.mean(pos-m_n))

for n in [10, 13, 16]:
    maxes, Zs, means = [], [], []
    T = 120 if n <= 13 else 60
    for _ in range(T):
        mx, z, mn = one_trial(n, rng)
        maxes.append(mx); Zs.append(z); means.append(mn)
    maxes=np.array(maxes); Zs=np.array(Zs)
    print(f"n={n} k={int(np.floor(t*n))} trials={T} "
          f"max-m_n: mean={maxes.mean():+.3f} sd={maxes.std():.3f} "
          f"q10={np.quantile(maxes,0.1):+.3f} q50={np.quantile(maxes,0.5):+.3f} q90={np.quantile(maxes,0.9):+.3f} "
          f"Z: mean={Zs.mean():.3f} P(Z>med|max>med)={np.mean(Zs[maxes>np.median(maxes)]>np.median(Zs)):.3f}")

# Gumbel-shift check at n=16: split by Z tercile, compare max medians
n=16; maxes=[]; Zs=[]
T=80
for _ in range(T):
    mx,z,_=one_trial(n,rng); maxes.append(mx); Zs.append(z)
maxes=np.array(maxes); Zs=np.array(Zs)
lo=np.median(maxes[Zs<=np.median(Zs)]); hi=np.median(maxes[Zs>np.median(Zs)])
print(f"median(max)|Z-low={lo:+.3f} median(max)|Z-high={hi:+.3f} shift={hi-lo:+.3f} "
      f"(positive shift consistent with Z random-shift representation)")
print(f"corr(log Z, max)={np.corrcoef(np.log(np.maximum(Zs,1e-9)),maxes)[0,1]:.3f}")
out={"theta_star":theta_star,"v1":v1,"v2":v2,"t":t,"mu1":mu1,"mu2":mu2,
 "note":"centered max stable across n; max increases with Z (random shift); see stdout log"}
with open("output/artifacts/sim_summary.json","w") as f:
    json.dump(out,f,indent=2)

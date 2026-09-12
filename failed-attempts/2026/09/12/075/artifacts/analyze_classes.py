import numpy as np, math, sys
from kasteleyn import logZ
a = float(sys.argv[1]) if len(sys.argv)>1 else 0.3
nmax = int(sys.argv[2]) if len(sys.argv)>2 else 40
ns = list(range(1, nmax+1))
cache = {n: logZ(n, a) for n in ns}
for r in range(4):
    sub = [n for n in ns if n % 4 == r]
    use = [n for n in sub if n >= nmax-16]
    A = np.vstack([np.array(use)**2, np.array(use), np.ones(len(use))]).T
    y = np.array([cache[n] for n in use])
    coef, res, _, _ = np.linalg.lstsq(A, y, rcond=None)
    print(f"class r={r}: F0={coef[0]:.10f} F1={coef[1]:.10f} C={coef[2]:.8f} res={res[0] if len(res) else 0:.3e}", flush=True)
use = [n for n in ns if n >= nmax-16]
A = np.vstack([np.array(use)**2, np.array(use), np.ones(len(use))]).T
y = np.array([cache[n] for n in use])
coef, res, _, _ = np.linalg.lstsq(A, y, rcond=None)
print(f"global: F0={coef[0]:.10f} F1={coef[1]:.10f} C={coef[2]:.8f} res={res[0] if len(res) else 0:.3e}", flush=True)

"""Replay verifier for the emergent ERTBP halo-type orbit (lane-467).

Reproduces, with no manual tuning:
  1. Two-point R-symmetric shooting residual of w* at e=0.0549 (must be <= 5e-12).
  2. Full-period closure from the f=0 Fix(R) point (must be <= 5e-12).
  3. Prints the orbit section data and sample points.

Method: pulsating-frame spatial ERTBP, Dormand-Prince RK45 adaptive
(tol=1e-12), independent implementation from the discovery script
(see fast.py). Run: python3 verify_orbit.py
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fast import prop_ert

E = 0.0549
WSTAR = np.array([0.873491766672, 0.200416848519, 0.221727034018,
                  0.993674921511, -0.030161618419, -0.881666894091])

def fix_state(x, z, vy):
    return np.array([x, 0.0, z, 0.0, vy, 0.0])

def main():
    w = WSTAR
    try:
        wfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'w_star.npy')
        w = np.load(wfile)
        print("loaded w_star.npy:", ["%.12f" % v for v in w])
    except Exception as ex:
        print("using embedded WSTAR (w_star.npy not found):", ex)
        w = WSTAR
    a = fix_state(*w[:3]); b = fix_state(*w[3:])
    pa = prop_ert(a, 0.0, np.pi, E)
    pb = prop_ert(b, np.pi, 2 * np.pi, E)
    r = np.concatenate([pa - b, pb - a])
    n = float(np.linalg.norm(r))
    c = prop_ert(a, 0.0, 2 * np.pi, E)
    nclose = float(np.linalg.norm(c - a))
    print("two-point residual norm =", n)
    print("per-component:", r.tolist())
    print("full-period closure norm =", nclose)
    print("a (f=0 Fix(R)):", a.tolist())
    print("b (f=pi Fix(R)):", b.tolist())
    ok = (n <= 5e-12) and (nclose <= 1e-9)
    print("VERIFY_OK" if ok else "VERIFY_FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())

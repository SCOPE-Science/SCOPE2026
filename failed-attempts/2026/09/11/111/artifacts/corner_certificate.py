"""Rigorous variational upper bounds on first transmission exponent at 90-degree vertex.

Closed-form Rayleigh quotients (exact expressions in pi, evaluated in float):
  sigma = k on |theta|<pi/4, else 1.  W = pi*(k+3)/2, A-B = k-1.
  k<1:  trial sin -> bound A/B.   k>1:  trial cos-m -> bound B/(A-W*m^2).
Consistency check against two-mesh FD eigenvalues (non-load-bearing).
"""
import json
import numpy as np

KSTAR = (3*np.pi+4)/(4-np.pi)
print("K* =", KSTAR)
assert KSTAR > 15.6  # uses pi > 3.141: 18.6*pi > 58.4
# Theory: Q<1 condition for k>1 is exactly k < K*; denominator positivity follows.

fd = {0.2: 0.784088, 0.5: 0.893794, 2.0: 0.892829, 3.0: 0.838297,
      4.0: 0.805033, 10.0: 0.730404}  # N=600 FD values from compute_ingredients.py

rows = {}
for k in [0.2, 0.5, 2.0, 3.0, 4.0, 10.0]:
    W = np.pi*(k+3)/2
    D = k-1
    A = (W+D)/2
    B = (W-D)/2
    assert A > 0 and B > 0
    if k < 1:
        Q = A/B
        trial = "sin"
    else:
        m = (k-1)*np.sqrt(2)/W
        den = A - W*m*m
        assert den > 0
        Q = B/den
        trial = "cos-m"
    lam_up = float(np.sqrt(Q))
    assert Q < 1, (k, Q)
    assert lam_up >= fd[k] - 1e-3, (k, lam_up, fd[k])  # consistency, not proof
    rows[str(k)] = {"trial": trial, "lam_up": lam_up, "Q": float(Q),
                    "fd_N600": fd[k]}
    print(f"k={k:5}: trial={trial:6} lam1 <= {lam_up:.6f}  (FD {fd[k]:.6f})")

with open("output/artifacts/certificate_bounds.json", "w") as f:
    json.dump({"Kstar": float(KSTAR), "bounds": rows}, f, indent=1)
print("saved certificate_bounds.json")

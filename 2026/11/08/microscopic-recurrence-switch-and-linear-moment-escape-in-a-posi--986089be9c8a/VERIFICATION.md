---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproduction

Run `python3 verify.py` in the folder containing the embedded files. It uses Python 3's standard `fractions.Fraction` and no network access, dataset, or additional package.

The checker passes 6,982 exact rational assertions on five integer acceleration parameters, including stationarity over an integer range, exact supported-site masses and incoming transitions, finite-step minorization from varied initial sites, and first-moment drift identities. The code and proof use the exact prepoint transition \(X_{t+1}=X_t\pm s_r(X_t)\), with \(s_r(n)=1\) in the central three sites and \(s_r(n)=|n|+r\) outside.

Analytical validation is separate: the proof reduces the exterior to affine doubling versus opposite-sign reset, solves all stationary balance equations, proves global Doeblin contractions, sums geometric tails without truncation, and uses bounded indicator convergence to derive the moment slope. Finite code tests alone cannot certify uniqueness, infinite-support invariance or the universal moment cutoff; these rely on those mathematical arguments. No external independent audit has been performed.

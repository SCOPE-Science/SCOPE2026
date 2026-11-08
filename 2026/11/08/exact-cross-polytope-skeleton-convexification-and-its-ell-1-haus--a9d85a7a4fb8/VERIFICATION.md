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

# Verification and reproducibility

The proof in `RESULT.md` covers all integers \(n\ge2\), \(0\le k<n\) and all finite real \(\lambda\ge0\). Its critical analytic steps are the exact pointwise sparse-unit-sphere distance, the exact Minkowski-ball erosion identity, the largest-coordinate majorization lower bound with sharp equal-modulus witnesses, and the convex endpoint maximization. The threshold and the extremizer classification follow by equality analysis. No unproved computational assumption is required.

The standalone `verify.py` requires only Python 3 and its standard library. Run `python3 verify.py` after extracting the file from the research package. The actual exact-rational run returned `VERIFY_OK 980 exhaustive-grid point-distance tests; 140 profile/threshold tests`. These 1,120 tests use a deterministic random seed, enumerate signed rational sparse unit-sphere grids, and directly minimize distance to this finite grid to cross-check the analytic pointwise formula. The exact parameter tests evaluate both sharp endpoint candidates and the convexification threshold.

Finite rational-grid tests cannot establish an all-real, all-dimensional theorem. They corroborate the explicit analytic proof and are not independent mathematical auditing. Independent audit has not been performed.

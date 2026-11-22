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

# Verification notes

The analytical calculation uses the exact four eigenvalues \(0,2-\sqrt2,2,2+\sqrt2\) and exact spectral-projector entries. A derivative monotonicity argument proves the distance-two zero count, a strictly convex rescaled derivative proves the endpoint zero counts, and explicit inequalities at scaled times \(\log2\) and \(2\) prove the ordering. Both large-exponent limits are obtained by uniform convergence on compact positive rescaled intervals and bracketing of simple limiting roots.

Run `python checker.py` in a standard Python environment with NumPy and SciPy. The supplied independent matrix-exponential reconstruction passed 1574 direct numerical comparisons of entries, signs, crossing counts, and scaled roots. These are finite reproducibility checks, not exhaustive verification over all real exponents and times. Independent external mathematical review has not been performed.

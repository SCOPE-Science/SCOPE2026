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

The analytic proof establishes the exact planar \(q\)-numerical range for every antiunitary and every \(|q|\le1\). Its independent logical ingredients are a polynomial zero of the quadratic antilinear numerical form, compactness/connectedness, one-dimensional orthogonal decomposition, two elementary constrained extrema, and rotational covariance. This is a self-review; no independent verification is asserted.

Run `python3 checker.py` with Python 3 and the standard library. It checks exact Fraction identities at rational Pythagorean parameter pairs, bounds throughout a finite grid of self-overlap moduli, and numerically constructs thousands of constrained unit-vector pairs for explicit antiunitary matrices. Finite checks are supplementary diagnostics, not a proof by enumeration or a claim of exhaustive sampling.

Boundary points are obtained by compactness of the constrained pair space, not by numerical approximation. No theorem is asserted for nonisometric antilinear maps or higher-dimensional spaces.

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

# Verification and limits

The self-contained proof in `RESULT.md` checks the half-line spectral support formula, the entire complex numerical-range boundary, finite-section characteristic determinants and threshold eigenvectors, two-branch Robin scaling, the angular boundary layer, and both polynomial/exponential fixed-parameter convergence. Numerical tests do not establish infinite-dimensional results or originality.

The accompanying `checker.py` runs from the same directory using Python, NumPy and SciPy: `python checker.py`. Its successful result is `CHECKS_PASSED 261`; the exact-rational checks verify finite polynomial identities and finite cutoff equalities, while the floating-point tests check sample eigenvalues and predicted rates. No extrapolation of finite testing is used in the proof.

General Jacobi theory, more general compact or rank-one perturbations, and a separate external mathematical audit remain outside the asserted conclusions.

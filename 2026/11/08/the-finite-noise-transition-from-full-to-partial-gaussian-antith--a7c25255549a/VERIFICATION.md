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

# Reproducibility and limits

Run `python3 verify.py` in the directory containing this document and `RESULT.md`. Only the Python standard library is required. The script performs 136,111 assertions: exact-fraction tests of the optimizer against a finite correlation grid over broad integer parameter cases; exact rational cross-validation example identities; numerical stress tests of global optimality for nonexchangeable positive-semidefinite Gaussian correlation matrices; and direct simulation of the underlying randomized training/testing score for three alternative couplings.

The mathematical proof is self-contained in `RESULT.md`: it is not contingent upon Monte Carlo simulation or a finite grid. Numerical tests cannot establish uniqueness or universal quantifiers; those follow from strict convexity, Gaussian fourth moments, the eigenvalue feasibility interval and an exact rational-function monotonicity calculation. No verification is claimed beyond the stated jointly Gaussian class, fixed scalar shrinkage special case, and exact arithmetic hypotheses.

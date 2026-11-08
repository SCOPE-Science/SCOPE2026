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

# Reproducible checks

Run `python VERIFY.py` with Python 3, SymPy and NumPy. The program exactly verifies the Chebyshev identity producing the \(4/5\) threshold, the two explicit homogeneous-weight roots, and positive/negative Hessian signatures for 14 noncritical weighted branches, including full phase-space Jacobian eigenvalues and force balance. At the fold, the six-dimensional Hessian has exactly two zero directions: the expected common-phase rotation and the saddle-node direction.

These finite tests are not a proof of the continuous parameter range, the exhaustive count of sinks or global stability. The analytic argument in `RESULT.md` provides these conclusions through conserved current, the general Hessian obstruction, the exact square identity, the branch derivative and the admissible finite-step spectral bound. Independent scientific validation has not been performed.

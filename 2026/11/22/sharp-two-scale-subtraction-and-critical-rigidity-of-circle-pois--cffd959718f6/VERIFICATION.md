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

# Reproducibility and verification

The proof in `RESULT.md` is the mathematical justification for the infinite-dimensional statements. `checker.py` provides supplementary finite consistency checks and is runnable with Python 3 plus NumPy and SciPy using `python3 checker.py`.

Actual checks: 116 deterministic supplementary assertions passed. They compare principal Jacobi eigenvalues with the sharp endpoint and small-scale predictions, verify computed smaller sections lie in the stated exponential error enclosure, and check finite Gram positivity and the antipodal null direction. The Python check is not a proof of uniform validity, does not exhaust all parameters and does not establish historical priority.

The certified finite-section bound follows from the explicit row-sum estimate for the omitted band matrix. If relying on floating-point eigenvalues for an application, use directed-rounding or interval eigenvalue arithmetic to turn that analytic bound into a fully certified numerical enclosure. No external independent mathematical audit is represented.

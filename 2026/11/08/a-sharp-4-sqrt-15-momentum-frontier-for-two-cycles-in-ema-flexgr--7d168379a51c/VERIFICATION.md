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

# Verification scope and reproduction

Run `python verify.py` with Python 3, SymPy, and NumPy. A successful run prints `VERIFY_OK`, the numerical critical decay, and the symbolic two-step characteristic polynomial.

The script checks the physical periodic orbit, differentiates both sign branches, proves equality with the displayed Jacobian and characteristic polynomial by symbolic identities, confirms each exact factor used in the Schur argument, checks the critical factorization, and cross-checks several physical-coordinate Jacobians by centered finite differences. It also illustrates convergence from a zero-buffer start for two parameter values inside the stable region; this illustration is not a global convergence theorem.

The continuum statements are supported by the exact analytical factorization and the strict positivity arguments in `RESULT.md`; no finite sampling is used to certify an infinite statement. The package contains no independent external validation or certification, and it does not claim a resolved nonlinear classification at the nonhyperbolic critical decay.

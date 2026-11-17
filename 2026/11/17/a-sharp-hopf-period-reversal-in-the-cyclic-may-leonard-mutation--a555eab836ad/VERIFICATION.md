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

The exact polynomial change of coordinates and original-time Hopf reduction are derived in `RESULT.md`. `CHECK.py` is a standalone Python 3 standard-library checker: execute `python3 CHECK.py` in the package directory. It independently evaluates the three original population equations and the transformed equations, checks the Fourier coefficient algebra numerically, and tests the sharp positive-rate sign boundary. It is a finite algebra/consistency check, not an infinite-dimensional proof.

Independent adaptive-integration shooting tests (not required for the algebraic theorem) approached the predicted period derivative from both sides at two sets of strictly positive coefficients; the numerical comparisons are given in `RESULT.md`. The proof establishes the local existence and asymptotic by analytic Hopf and harmonic balance, with no claim of global cycle classification. No independent mathematical audit has been performed.

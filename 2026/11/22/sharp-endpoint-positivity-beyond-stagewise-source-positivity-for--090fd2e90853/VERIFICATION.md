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

## Exact verification
The accompanying `verify.py` (Python 3, SymPy dependency) verifies the expanded scalar endpoint polynomial, its zero-crossing parametrization, the derivative factorization and radical threshold, the first-stage bound identity, and the exact rational negative example. It also checks 500 rational input-timestep pairs in the interior, strictly below the certified boundary.

The analytic proof in `RESULT.md` establishes the universal quantifiers and the spectral lifting; finite diagnostics do not replace that argument. Only the zero-linear-part, ordinary matrix-cube, one-step input domain \(0\preceq X\preceq I\) is proved. No independent mathematical audit or external certification has been performed.

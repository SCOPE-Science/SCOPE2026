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

The accompanying `verify.py` is executable with Python 3, SymPy, NumPy and SciPy. It verifies exact identities for the linear and cubic coefficients and performs independent numerical stationary-equation and four-by-four Jacobian tests for three steepness offsets. Analytic branch existence, uniqueness within the symmetric subspace, and full-space saddle index follow from the proof in `RESULT.md` and are not inferred solely from finite numerical tests. A separate independent scientific audit has not been performed.

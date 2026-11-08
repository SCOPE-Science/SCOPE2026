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

# Verification

Running `python verify.py` verifies exact symbolic center-manifold identities and the rational examples with Python/SymPy and evaluates two illustrative positive numerical orbits with mpmath. Expected terminal marker: `VERIFY_OK`. These finite computations independently check the displayed constants but do not establish all-time global convergence. The global claim is supported by the scalar comparison argument, the fast-fiber asymptotic and the summable reciprocal recurrence given in RESULT.md.

The first asymptotic correction \(A\log n\) and the finite remainder \(K\) are separate assertions. No finite experiment can replace the absolute-summability argument for the remainder. No independent external review has been performed.

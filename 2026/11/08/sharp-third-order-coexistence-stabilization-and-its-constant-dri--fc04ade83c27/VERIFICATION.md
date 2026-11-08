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

# Verification evidence

The supplied standalone `verify.py` was run as `python verify.py`. It printed `PASS: {'nonconstant': 640, 'negative_constant': 152, 'obstructed': 168} exact-rational cases; 6 explicit nonnegative-constant obstructions`. Arithmetic is from Python's standard-library `fractions.Fraction`. The tests verify equilibrium identities, symmetric tensor reconstruction, full Jacobian rescaling, the forced row sums and the square-zero spectral certificate in the nonconstant branch.

The arbitrary-dimensional result is proved symbolically in `RESULT.md`; the finite checks do not certify infinity or independent review. The claims are local and assume unrestricted signed three-body coefficients including repeated partner indices.

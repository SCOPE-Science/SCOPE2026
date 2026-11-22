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

The analytical proof is in RESULT.md. The included `verify.py` is self-contained and uses the Python standard library. It constructs both generator products with exact rational arithmetic, and separately evaluates the propagators by the power-series definition of the matrix exponential with scaling and squaring; it does not reuse the hyperbolic closed form when computing the benchmark endpoint masses. The tested script completed with `VERIFY_OK assertions=3435`.

The exact proof applies to all positive rates, both positive and unequal stage durations, and every nonzero nonnegative initial mass vector. Its key steps are the conserved total mass, the two-dimensional Cayley–Hamilton reduction, and the explicit row-sum generator commutator. The numerical and finite rational tests are checks of implementations, not an exhaustive infinite-domain proof.

No independent scientific audit or field calibration has been performed. No general multi-stage, nonautonomous-rate-inside-stage, or spatially resolved comparison is established.

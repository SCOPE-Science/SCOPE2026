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

# Verification and scientific limits

Reproduce the supporting exact-arithmetic tests with `python3 checker.py` from the same directory as RESULT.md. The checker uses Python's standard-library `fractions.Fraction` and `math.comb` to inspect mixing-mass identities, logarithmic-coefficient algebra, rational sign certificates and finite parameter/index samples. The analytic proof, not the finite checks, establishes the all-positive-parameter and all-count claims. No independent mathematical audit has been performed; the source inspection and any remaining historical-priority risks are described in REVIEW.md and AUDIT.json.

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

The included exact-integer checker `verify_bounded_ary_parity.py` independently expands the restricted-partition product and compares all coefficient parities with those obtained from the claimed recursion. It also checks the nonzero-state transition counts and the rational generating-function coefficients on complete base-power blocks for bases three through nine, and the separately stated base-two endpoint.

Observed run: `BOUNDED_POWER_PARITY_OK 39`, with all 39 complete-block checks passing. No external dependencies or floating-point numerical approximations are required. The infinite results follow from the proof in `RESULT.md`, not from finite enumeration.

The historical-priority comparison is qualified by the possibility of an unindexed equivalent result. Independent mathematical audit has not been performed.

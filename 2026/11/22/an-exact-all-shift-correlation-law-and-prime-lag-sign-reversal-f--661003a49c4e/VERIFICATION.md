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

The complete proof is in RESULT.md. The standard-library verifier `verify.py` independently recomputes the signed partition coefficients for all positive integers through 120 using the combinatorial definition and checks thirteen shifted normalized correlations against their proven limits using all positive integers up to 120000. Its output is `ARITHMETIC_LAG_CHECK_OK 120 13 mean ...` when successful. Finite agreement is diagnostic, not an infinite proof. The prime-lag signs also follow from the exact formulas, without relying on numerical experiments.

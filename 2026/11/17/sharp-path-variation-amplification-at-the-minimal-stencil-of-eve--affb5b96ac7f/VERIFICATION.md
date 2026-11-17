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

Run `python3 verify.py` with Python's standard library. The checker constructs an exact rational inverse for each minimum-length difference penalty at orders 1 through 12 for three rational tuning values, calculates the variations of all binary one-jump input vectors, and compares to the independently derived binomial formula. It prints the signed first five values of the controlling integer `M` and the normalized high-order ratios at orders 50, 100, 200, 500, and 1000.

The analytical proof in RESULT.md, not finite numerical tests, establishes the identity for all integer orders and the limit 1+sqrt(2). The checker does not certify historical novelty or other boundary conditions.

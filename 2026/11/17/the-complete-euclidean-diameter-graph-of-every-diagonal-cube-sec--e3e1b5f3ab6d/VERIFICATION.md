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

# Verification record
The accompanying `verify.py` is standalone Python 3 using only the standard library. It enumerates all permutations of the allowed vertex coordinate multiset and computes exact squared distances with `fractions.Fraction`. It evaluates the theorem's factorial pair-count formulas on 55 cases for dimensions three through seven and section sums with denominators one, two, or three. All 55 cases passed, including even central, odd central, rational fractional, and integer boundaries. The proof does not assume any property inferred solely from these computations. The published date and full-text availability of neighboring results limit historical-priority assurance.

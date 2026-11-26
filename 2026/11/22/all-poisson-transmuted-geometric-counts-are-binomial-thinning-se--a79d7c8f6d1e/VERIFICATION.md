---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

Run `python3 verify.py` using the Python standard library. The checker tests the signed partial fractions by polynomial multiplication; computes the exact negative-transmutation obstruction; and checks the rational log-coefficient formula and positive lower bound at finite samples. These checks are not needed to infer positivity from a grid: the all-index beta-kernel estimate and the integral of nonnegative binomial-thinning probabilities in RESULT.md prove the full result.

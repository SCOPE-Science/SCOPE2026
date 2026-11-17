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

Execute `python3 verify_wheel_gini.py` using Python 3 standard library. The checker performs exact exhaustive hub-zero cut comparisons for sizes 3 to 11, checks the algebraic block expressions up to 300, confirms every dimension below the 29-rim crossover, checks the sharp 29-rim witness and values through 300, and verifies a positive bistochastic correction through size 50. All operations use exact `fractions.Fraction` arithmetic.

The cyclic-run majorization, coarea argument, complete infinite crossover and limit are proved in `RESULT.md`, not inferred from a finite check. Historical priority remains subject to full independent literature examination. Independent audit is not performed.

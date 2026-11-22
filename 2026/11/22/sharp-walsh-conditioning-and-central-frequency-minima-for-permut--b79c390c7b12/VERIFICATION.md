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

# Reproduction and limits

Run `python3 checker.py` with Python 3. The program uses only Python standard-library exact-integer arithmetic, `fractions.Fraction`, and direct permutation enumeration. It checks the complete Walsh spectrum through eight labels against an independent cycle-index coefficient expression and the rational coefficient recurrence through 100 labels. The proof's finite-dimensional enumerations and all-order induction are distinct: no claim of infinite verification follows from a finite test suite.

The normalization is probability convolution, so its maximum Walsh multiplier is exactly one. The integer multiplier list printed by the checker is scaled by the number of permutations. The independent external audit has not been performed.

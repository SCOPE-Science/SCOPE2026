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

# Reproduction and proof boundaries

Run `python3 checker.py` with Python 3 and no additional packages. It enumerates all ordered positive-integer compositions of sizes 1 through 12, tabulates all exact consecutive-word counts and mixed part-count products, then verifies the theorem using exact fractions. Its observed result is 24,558 passed assertions.

The checker is a finite consistency test, not an infinite proof. The all-integer claim is justified in `RESULT.md` by a marked-occurrence bijection, two formal power-series coefficient identities, and an exhaustive four-case sign analysis. These are symbolic mathematical arguments, not experimental extrapolations. No external or independent audit has occurred.

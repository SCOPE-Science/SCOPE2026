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

## Reproducibility

Run `python CHECK.py` using Python 3 and only the standard library. The checker independently uses the circle-doubling representation, partitions at *all* rational endpoints where observed signs change, and accumulates exact interval lengths with `fractions.Fraction`. The exact Markov-product formula is checked against every positive-probability direction word of lengths one through eleven; generating-polynomial counts and exact mean, variance and correlations are checked separately. The expected stdout is `VERIFY_OK checks=646 exact rational cylinders through length 11`.

## Limits

Enumeration to finite length cannot establish an infinite Markov property. The complete proof is the uniform-full-branch induction in RESULT.md. No external or independent validation has been carried out, and no finite-sample noisy-data performance claim is made.

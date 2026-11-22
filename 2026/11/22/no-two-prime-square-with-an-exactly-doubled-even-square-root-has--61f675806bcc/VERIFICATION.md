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

Run `python3 verify_delta.py` using Python 3. The script constructs the divisor sets by exact arithmetic and excludes three-term additive relations for a finite sample of prime powers. It also checks the special symbolic identities at each tested exponent.

## Proof limits

Finite computation cannot establish the theorem for arbitrary exponents; the proof in RESULT.md relies on the cited prime-dominance lemma, the modular separation, and descent by a factor of nine. The original maximal-difference lemma is a named external prerequisite, not a computational assertion. Independent audit has not been performed.

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
Run `python verify.py` using Python 3.10 or later with its standard library only. Expected terminal marker: `VERIFY_OK`.

## Checks actually performed
- Direct recursive border/occurrence recognition compared against the closed-form zero-gap predicate on all 40,920 weight-three binary words of lengths 3 through 32.
- 3,000 seeded longer-gap cases compared by the same independent recognizer.
- Two-one auxiliary classification checked exhaustively through length 24.
- Nonpalindromic count obtained from gap enumeration compared against coefficient extraction from the product generating function through length 700.

The computer checks are finite. The all-length theorem is justified by the separate exhaustive classification of privileged-border types and a bijection to solutions of a linear Diophantine equation. Independent audit has not been performed.

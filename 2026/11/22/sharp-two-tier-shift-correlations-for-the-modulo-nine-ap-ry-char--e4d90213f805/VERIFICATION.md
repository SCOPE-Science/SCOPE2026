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
Run `python3 artifacts/verify.py` in the package root. It uses only the Python standard library and exact rational or integer arithmetic. At package preparation it passed 20,472 assertions: 288 Apéry congruence checks for four parameter pairs at indices 0–71; an exact comparison with the classified top-tier shifts and ternary-scale invariance for all positive shifts below 6561; two finite character-correlation block checks against a proven boundary-error allowance for shifts 1–120; and 24 exact consecutive-ones identities. Checks of finitely many indices are not an infinite proof; the general theorem follows from the digit carry matrices, terminal expectation, aligned-block argument and invariant-square extremizer proof in RESULT.md. Independent validation has not been performed.

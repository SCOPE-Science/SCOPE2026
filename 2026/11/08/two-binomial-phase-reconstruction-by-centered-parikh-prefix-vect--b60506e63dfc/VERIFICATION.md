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

# Reproducible checks

Run `python verify.py` with Python 3 and no external dependencies. It prints `VERIFY_OK 35116 432228 7416` after independently counting every ordered scattered pair for each test word, comparing all phase pairs, and checking the centered-prefix prediction. The final number counts equal-deck phase pairs in the tested cases (including repetition counts), not independent mathematical results.

The verifier exhausts arbitrary periods using at least two letters over alphabets with two, three and four symbols at small sizes, and tests every run-length vector from one through four for selected three-to-five-symbol distinct-run words. The proof in `RESULT.md` supplies the universal quantifiers and the noncomputational justification. No independent proof audit has occurred, and finite enumeration is not evidence of an infinite theorem by itself.

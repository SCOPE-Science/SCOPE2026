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

From a folder containing `verify.py`, execute `python3 verify.py`. The script uses the Python standard library only and completes the exact search over 528 eligible words. It checks that exactly the two reversed gap vectors `(1,3,2,7)` and `(7,2,3,1)` have a minimum attractor of four, validates factor coverage for each selected optimum using a second direct occurrence-search implementation, verifies 117 factors for the displayed word, and proves that the six required factors have no three-position transversal by exhaustive combinations of the 18 positions.

The exhaustive parameter range is proved by the inequality in `RESULT.md`; the computation does not claim to cover any longer word. A separate mixed-integer optimization cross-check agreed for all 528 words, but its code is not required by this package. No independent scientific audit has been performed.

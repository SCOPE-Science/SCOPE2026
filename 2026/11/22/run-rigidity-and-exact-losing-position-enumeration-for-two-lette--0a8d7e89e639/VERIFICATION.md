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

# Verification evidence and limits

The precise rules of the two-ended game, regular-language classification, binomial enumerator, rational series, and sharp maximal nimber are proved in `RESULT.md` by a normal-play P/N strategy argument, stars and bars, and induction. No external theorem about this exact game is assumed.

`verification/verify_outcomes.py` evaluates legal moves from both ends and the actual mex recursively on all 262143 binary words through length 17; it separately compares the outcome to the claimed regular expression and validates the sharp maximum at each length. `verification/verify_enumerator.py` compares the closed binomial sum against coefficients of the stated rational generating function for lengths 0 through 200 and computes actual mex for alternating words through length 100. The adjacent `.txt` files contain their recorded outputs.

These are finite reproducibility checks. They do not certify a universal statement by themselves; the universal statement uses the explicit exhaustive-case proof and induction in `RESULT.md`. Literature comparisons establish only priority relative to inspected available material, not exhaustive novelty across all historical works.

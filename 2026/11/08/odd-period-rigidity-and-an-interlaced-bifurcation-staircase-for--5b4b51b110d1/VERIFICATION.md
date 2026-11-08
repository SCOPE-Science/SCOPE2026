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

# Verification and reproducibility

Run `python3 CHECK.py` with Python 3. The checker uses only `fractions.Fraction` and exact rational squared-distance comparisons. It independently iterates the three-line farthest-projection map for 4,001 rational leg ratios and checks first return times, the predicted threshold-exit index, odd line itineraries and the single perpendicular-leg transition. The current execution passed 20,009 assertions; the greatest observed least period was 101.

The proof, not the checker, establishes every real-parameter claim including the exact exceptional irrational parameters. The monotonicity and interlacing arguments are algebraic/logarithmic and must be checked independently to substantiate those infinitely many roots. This document does not certify external validation; no independent audit was performed.

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

# Verification performed

The complete analytical proof is included in `RESULT.md`; it proves interior global maximizers, at-most-one overloaded coordinate, the two-flower hyperbolic threshold, uniqueness of the higher-dimensional global switch by convexity, bounds on the switch, discontinuity, and the asymptotic optimizer. It applies for all real \(B>0\) and all integers \(n\geq2\) under the declared hypotheses.

Running `python3 checker.py` with Python 3.10 or later produced `PASS 62645 supplementary assertions`. Checks span numerical two-flower comparisons, stationary overloaded candidate detection, random feasible configurations in several dimensions, and the third-order gain at equal mean two. These numerical checks do not replace the proof or establish uniqueness alone. The displayed three-flower switching-budget approximation is not claimed as a certified enclosure. No independent external examination was performed. Two potentially relevant older complete texts were unavailable; priority remains provisional.

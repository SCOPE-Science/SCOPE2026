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

The mathematical proof in RESULT.md gives exact formulas and complete parameter-domain inequalities. To reproduce finite supplemental checks, run `python checker.py` with Python 3 and its standard library. The checker contains (i) an exact Fraction-based witness; (ii) seeded synthetic parameter-triple inverse checks; (iii) analytic derivative-sign checks. Finite tests do **not** prove the global monotonicity or the sharp minimal number of channels; both are proved symbolically in the main document.

The spot/photosphere temperatures are parameterized via exponentials of inverse temperatures; this does not assume a particular stellar temperature or telescope. This analysis establishes no accuracy bounds under measurement noise, band averaging, model misspecification or imperfect occultation geometry. A separate independent audit has not been performed.

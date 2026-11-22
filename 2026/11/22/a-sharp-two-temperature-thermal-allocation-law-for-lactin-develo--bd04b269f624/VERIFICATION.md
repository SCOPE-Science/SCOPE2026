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

# Verification of the thermal-allocation theorem

The analytical proof in `RESULT.md` checks a single contact for every \(0<a<b\), \(B>0\), and cold bound \(L<\theta\), constructs an exact concave envelope, and proves uniqueness for arbitrary Borel distributions with a prescribed mean. It establishes all endpoint, tangency, and transition cases. The cubic-contact and maximum-gain expansions use the explicitly negative third derivative at the inflection.

Run `python3 CHECK.py` with Python 3. The script requires no external libraries. On this package the checker printed:

```
PASS 85188 diagnostic assertions; contact 21.94367799281072 peak 26.931471805599454
```

Its assertions include 160 fixed-seed parameter configurations, sampled pointwise envelope dominance, sampled two-temperature schedule comparisons, contact residuals, curvature and positivity checks, cold-bound monotonicity, and the cubic onset ratio. Numerical rounding is tolerated explicitly within the script. Finite sampling provides diagnostics only, not a proof for all temperatures, parameters, or probability measures; the analytic envelope argument is the general verification.

The original 1995 published rate paper was not available in full text during this comparison. The functional form was independently matched to openly accessible `rTPC` documentation. No independent mathematical audit, experimental thermal calibration, or physiological validation is represented.

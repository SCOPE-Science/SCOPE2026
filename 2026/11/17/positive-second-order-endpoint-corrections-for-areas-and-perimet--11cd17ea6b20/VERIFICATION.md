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

The proof establishes the complete fixed-\(n\) result analytically, using the unique regular-polygon maximum, local deficit Taylor expansion, smooth radial implicit-function theorem, parity, and exact spherical moments in a zero-sum hyperplane. There is no finite exhaustive substitute for the proof.

Run `python checker.py` after installing the packages in `requirements.txt`. The checker constructs the exact circle-spacing perimeter and area deficit equations independently of the asymptotic formulas. It uses angular quadrature, solves the radial threshold by bisection, and checks the two-term probability formula at three finite thresholds each for \(n=3\) and \(n=4\). The numeric diagnostics pass, but only examine two orders and finite positive deficits.

Historical priority beyond the inspected primary texts and accessible abstracts is not independently certified. Independent audit: not performed.

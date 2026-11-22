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

## Actual checks

The standalone `checker.py` was executed with its supplied Python 3 and `mpmath` dependency. It passed: critical-parameter and critical-time bounds; convex quadratic analytic minima versus the exact two-branch formula; 65 angular cosine samples at each of 89 time samples for eight representative amplitudes; the unique first positivity root; and both late roots where applicable.

The analytic proof, not finite testing, supplies quantifiers for every real parameter and positive time. The displayed threshold decimals are approximate. No external independent audit has been performed.

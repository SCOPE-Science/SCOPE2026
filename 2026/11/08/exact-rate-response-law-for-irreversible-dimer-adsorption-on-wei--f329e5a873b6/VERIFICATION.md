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

The analytical proof in RESULT.md is the basis for the infinite family. The included `check.py` supplies an independent finite-state exact-rational test of 25 small-graph/rate instances and additional analytic-series consistency tests (52 assertions total). It passed when executed against the packaged files. The replay needs Python 3 with only the standard library.

Verified critical steps: first-edge splitting, rational recurrence, Riccati linearization, positivity of the auxiliary entire coefficients, uniqueness of the smallest-modulus zero, residue computation, strict rate response and local uniform pole isolation. Numerical finite instances do not prove the all-size claims, which rest on the written analysis. The full text of one historical primary source was inaccessible; no assertion of independent certification is made.

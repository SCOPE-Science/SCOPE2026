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

The standard-library script `verify_theta.py` enumerates all edge masks for ten three-path theta graphs, checks connectivity-based bridge counts, two-variable exact generating-polynomial coefficients, every conditional mean, rational-parameter covariances, and the terminal-curvature formula. Local execution produced `PASS: 163 exact comparisons, 8640 exhaustive edge subsets, 10 theta graphs`. The all-size root uniqueness and equilateral asymptotic are proved analytically in `RESULT.md`, not certified by finite enumeration. There was no independent mathematical audit.

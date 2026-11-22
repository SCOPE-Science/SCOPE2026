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

Reproducibility: from the extracted directory run `python3 verify.py`. The checker uses only the Python standard library, performs 72,108 analytic/quadrature/variable-slope tests, and prints a PASS line on success.

The analytic proof, not the tests, establishes all-trajectory crossing separation and the infinite-time no-return dichotomy. Tests do not certify arbitrary functions or all positive times. The constructed regulator's affine core and exponential tails are explicit in RESULT.md; positivity, monotonicity and bounded slopes follow from direct differentiation. The independent audit has not been performed.

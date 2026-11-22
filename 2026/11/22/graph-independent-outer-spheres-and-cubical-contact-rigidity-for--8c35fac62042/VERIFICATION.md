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

# Verification details

The analytic proof is contained in RESULT.md, equations (1)–(10). It uses strict Jensen equality on the hub edges, degree regularity for the rim average, exact one-variable Cauchy–Schwarz, and a separate equality classification to rule out hidden outer-sphere contacts. The converse uses Lagrange multiplier stationarity of a differentiable support objective on the interior probability simplex.

The supplied `verify.py` uses only the Python 3 standard library and should be run with `python verify.py`. It checks 32 graph configurations, including graph pairs with different rim-edge arrangements but the same order and degree, and reconstructs all 28,032 sign-pattern contacts in its test suite from the actual individual disk supporting points. It performs 8,000 other unit-normal support comparisons.

Observed output:

`REGULAR_CONE_DISCOTOPE_PASS graph_cases=32 random_support_checks=8000 explicit_contacts=28032`

These finite tests do not certify the all-dimensional theorem; that assertion rests on the explicit proof. The literature priority comparison and self-review do not constitute independent mathematical validation.

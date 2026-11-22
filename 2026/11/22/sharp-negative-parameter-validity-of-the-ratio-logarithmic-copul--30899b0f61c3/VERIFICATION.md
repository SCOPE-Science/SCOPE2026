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

The analytic proof in `RESULT.md` supplies the all-parameter result: an exact mixed-derivative factorization, monotonicity of the exponential integral, a unique root and a necessary corner obstruction.

`check.py` ran at 70 decimal digits with Python and `mpmath`; output was `PASS: 135 high-precision checks`. Its root computation gave \(0.5398149979439905133945626149911215034405\ldots\), with the defining equation assessed to within numerical precision. The checks cover selected interior coordinates and parameter values; they do not establish positivity on the full unit square or establish priority against unindexed literature.

All relevant continuous limits at zero coordinates, the independence parameter, the critical boundary, and non-admissible negative parameters are treated analytically. The numerical corner calculation is supporting evidence, not an infinite proof. Independent mathematical checking is not represented by these tests.

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

The complete analytic claim is in `RESULT.md`. To reproduce finite exact checks without external packages, invoke `python checker.py` with Python 3. The program checks stationary detailed balance with rational coefficients, strict conformity comparisons of count majorities for several unequal source weights, every monotone self-dual Boolean voting rule on \(n=1,2,3,4\) with four source-weight configurations, and 30 beta-function identities for the two-versus-one source example. It prints `exact_fraction_checks 960`, `selfdual_rule_checks 76`, and `closed_form_checks 30`. Each reported verification is local to the included script.

The program does not enumerate all free-electorate sizes, all source weights, or all voting rules for general \(n\). These infinite quantifiers rely on the exact stationary mixture, the strict likelihood-ratio ordering of the unsigned beta deviation, and the monotone Boolean coupling proved in the main text. The exact formula uses a finite positive beta integral with no numerical extrapolation. The historical originality assessment remains limited to specifically read or searched material, and independent audit is not performed.

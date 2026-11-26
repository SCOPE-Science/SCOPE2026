---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each fixed x write A_m=pi_m(x) kappa_m(x)^lambda_m>0. Component m contributes A_m y^(-lambda_m)(1+O(y^-1)) to survival and lambda_m A_m y^(-lambda_m-1)(1+O(y^-1)) to density, by the exact density formula rather than differentiation of an asymptotic equivalent. Finite positive sums leave C_* = sum over minimum-shape tiers of A_m, yielding both equivalents and hazard lambda_*/y. The same quotient by survival proves the asserted posterior limits, including ties. For a unique minimum with competitors, the error is the sum of their posterior probabilities and is asymptotic to (sum of A_m at gap Delta)/C_* times y^-Delta. This implies the printed possibly weaker rate. With a single tier, if allowed, localization is exact and Delta is not needed. Nothing here is uniform in varying x.

## originality

FAIL

The dominant tail index and dependence on minimum-shape weights and scales are already in the primary source. The remaining closed forms are immediate implications of its exact finite-mixture component laws: scale the positive sum, divide density by survival, and apply Bayes to the tier-by-survival joint probability. This is prior implication, not a claim that the source prints the posterior limit verbatim.

## value

FAIL

The distinction between unconditional tier weights and survivor weights is interpretable, but the fixed-covariate formula only makes explicit the established tail dominance by a finite coefficient sum and an elementary Bayes ratio. The rate does not even resolve more sharply than the leading competing term delivers directly. No nonroutine identification or uniform tail problem is tackled. A useful explanatory calculation is not a substantive new result here.

The dated certificate retains the supplied scientific assessment, sources and limitations.

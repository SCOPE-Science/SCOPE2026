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

For a common tilt t near zero, J(t)=E[P_{m,a} prod_i D_i^t]=m Γ(m)Γ(1+a+t)Γ(1+t)^{m-1}/Γ(m+a+mt). Differentiation is legitimate since one may bound the logarithms by slightly reduced exponents in the interior of the Dirichlet integrability domain. The covariance is -J'(0)+J(0)E[sum_i log D_i], since -m log m is constant. The derivative and E[sum_i log D_i]=m[ψ(1)-ψ(m)] give precisely the frozen bracket and its sign. At a=1 the bracket vanishes, as required by sum_i D_i=1. At a=2 it is (m-1)/(2(m+1)) and J(0)=2/(m+1). The fourth moments have numerator 24m+4m(m-1), denominator m(m+1)(m+2)(m+3), giving the stated Greenwood variance. The log variance is the second derivative of log E[prod_i D_i^t], i.e. m ψ_1(1)-m^2 ψ_1(m). These give the exact squared correlation; positivity of the covariance fixes the square-root sign. Trigamma expansion gives Var(M_m)~m(π²/6-1) and hence the stated limit. Independent `python /workspace/audit_checks_1_5.py 5` integrates at m=2 by elementary monomial-log integrals, getting 1/9, and confirms the illustrative correlations and limits. The recorded successful checker output is supplementary; its code was inspected, not executed. The independent review could not directly check the historical asymptotic citation in the full Mirakhmedov text, but the limiting formula itself is proved.

## originality

FAIL

The exact power/Moran law is a mechanical consequence of the prior Dirichlet normalizing integral (including its ordinary log derivatives), by the common tilt that defines Moran's log-product statistic. This is implication by an existing broader exact formula, not evidence that the Greenwood–Moran wording or finite rational number was itself printed. The matched entropy–Greenwood results do not give the Moran law by identifying the two statistics.

## value

FAIL

Quantifying finite null dependence between two named tests is motivated and can be useful. But under the stated standard the precise invariant is already mechanically implied: Moran is minus the common-shape Dirichlet score plus a constant, so the covariance is an ordinary derivative of the textbook power moment and the Greenwood answer is the derivative of a rational mean. The squared correlation then normalizes by standard variances; the asymptotic comparison is not a distinct surviving contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

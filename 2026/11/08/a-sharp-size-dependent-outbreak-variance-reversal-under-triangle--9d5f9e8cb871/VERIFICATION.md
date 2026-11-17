---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Conditional on Exp(1) hub infectious duration T, U=e^{-lambda T} has Beta(1/lambda,1) law. Each triangle then contributes i.i.d. count 0,1,2 with p0=U^2, p1=2(U-U^2)/(1+lambda), p2=1-p0-p1; the within-triangle secondary-transmission avoidance factor is E(exp(-lambda E))=1/(1+lambda). Conditional strong law and CLT give g_lambda(U)=1-(U+lambda U^2)/(1+lambda) and its mixed-Gaussian fluctuations, while the star limit is 1-U. Independently expanded all moments E[U^k]=1/(1+k lambda) with SymPy: the exact finite variance difference equals -lambda^2 Q_m/[2m(1+lambda)^4(1+2lambda)^2(1+3lambda)(1+4lambda)], identically; Q_1=(2lambda+3)(3lambda+1)(4lambda+1)(lambda^2-2lambda-1). For m>=1 Q_m has signs +,+,-,-,-,-, hence one positive root; positive 1/m correction to D_infinity and D_{m+1}<D_m prove strict decreasing thresholds to unique positive root of P. The asserted joint CLT is stable mixture conditional on U, not a deterministic normal law.

## originality

PASS

Fransson–Trapman 2019 full open text (PMC6534529) studies clustered configuration-model random graphs under finite second degree moments and uses branching-process major-outbreak/expected-final-size approximations. A deterministic friendship hub has triangle degree m diverging with size and a non-degenerate shared-hub random limiting fraction, so their model and theorems do not dominate the submitted exact variance crossover. McCulloch–Roberts–Laing 2019 is a line of triangles rather than a shared-hub bouquet; only abstract and indexing details accessible, leaving a genuine residual possibility of an implicit general finite motif method. Resultary semantic search returned no earlier full statement of this all-m variance threshold.

## value

PASS

This is a structurally motivated example where adding links improves expected spread but reverses finite-size risk variance at a unique explicit infection rate. The monotone m-dependent threshold and random shared-hub limit are exactly computable network epidemic risk measures that could be reused when comparing clustering interventions; not merely a fixed-size arithmetic table.

The dated certificate retains the supplied scientific assessment, sources and limitations.

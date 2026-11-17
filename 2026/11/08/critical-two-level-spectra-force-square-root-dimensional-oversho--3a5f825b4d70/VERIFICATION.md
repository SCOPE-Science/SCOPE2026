---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For each r in (0,1), F_r(alpha)=r-2r(1-r)alpha-r²(1-r)alpha²; the quartic sum of squares has derivative with coefficient signs (+,+,sign(m2),-) descending and exactly one positive zero by Descartes and endpoint signs. Under r_n=1-a/sqrt(n) and alpha=n^(1/4) beta, M_n/n converges locally uniformly to (1-a beta²)^2+D² beta⁴. A single t-eigenvalue and the O(n) trial bound keep minimizers beta bounded; the unique limit beta*=sqrt(a/(a²+D²)) gives the three ratios and actual sign-iterate error. 2aD<=a²+D² shows sharp 1/2 within stated family; norm comparison proves universal sqrt(n) order only. Independent separate two-level derivative bisection on n=4^4 through 256^4 confirmed beta→2 and spectral spike→1/2, not a proof of limits.

## originality

PASS

Best-of-knowledge PASS: the surviving final claim is distinguished by mathematical implications from the inspected prior theorems; see four comparisons and the explicit residual priority risks.

## value

PASS

A real optimization pitfall occurs when an empirically Frobenius-optimal single polynomial coefficient is unconstrained: an isolated residual makes optimal fitting sacrifice operator norm by the largest possible dimension order. The explicit globally optimized two-level asymptotic, unique minimizer and actual sign-error divergence quantify why the safeguard in the motivating algorithm is mathematically needed; no unboundedness is asserted for safeguarded PRISM.

The dated certificate retains the supplied scientific assessment, sources and limitations.

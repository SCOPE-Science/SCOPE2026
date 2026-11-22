---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Reconstructed the binomial thinning semigroup, cut decomposition of the complete-pair Gini seminorm and column-mass <=1/p estimate. The endpoint singleton produces the displayed sum. The linear rank-one-modulo-constants approximation has exact norm p(n+1)(n+2)/6 and a uniform O(n(n+1)(n-1)p^2/2) remainder. It yields gamma~n^2 p/6 for np->0 and gamma~1/p for np->infinity; endpoint Riemann sums show the log-n lower window and at 2 log n + s the exact limit e^{-s}/6. The stochastic-row overlap gives Dobrushin delta=1-(1-p)^n, hence ratio~n/6 in np->0. Independently enumerated all 62 nonconstant binary cuts at n=5,p=1/7, obtaining the same maximum and endpoint value 62921/84035. The finite check does not establish any all-n norm formula beyond stated bounds.

## originality

PASS

PASS for the model-specific sharp small-survival expansion, two logarithmic scales and exact Gini/Dobrushin asymptotic separation, not for binomial thinning, Dobrushin contraction, superlevel cuts or the general dimension-dependent comparison.

## value

PASS

The result identifies an unusually strong noncontractive seminorm amplification mechanism for a classical finite stochastic semigroup and distinguishes two parameter windows with a quantified sharp ratio to oscillation contraction. These model-specific constants and cutoff scales give a meaningful structural operator-norm comparison; it is not merely a reparametrization of classical total variation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

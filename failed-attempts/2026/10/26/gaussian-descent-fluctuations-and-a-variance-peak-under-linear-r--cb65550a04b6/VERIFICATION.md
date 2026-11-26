---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A permutation is uniquely recovered from its sequential prefix ranks; record bias factors over ranks, and descent j is exactly R_(j+1)≤R_j. Thus only adjacent covariances enter. Conditionally on the middle rank u the adjacent joint numerator is the sum of u(j−u+θ) from u=1 to j, giving the displayed joint moment; p_j telescopes as half the adjacent difference of j(j+1)/(θ+j). Substitution gives the covariance formula and, uniformly for x=j/n since λ>0, the stated profiles and integrable derivative. Blocking into intervals of length floor(n^(1/4)) separated by one site discards o(n) variance, leaves independent blocks with the same positive limiting variance, and satisfies Lindeberg. Exact centering is needed with unrestricted convergence rate. Differentiation gives the unique positive critical point and the displayed maximum. An independent rational enumeration at n=5, θ=3/2 gave mean 20/11 and variance 580/1089 and agreed site by site; this checks finite moments only. Frozen check.py was inspected and not run.

## originality

FAIL

The distinct November 2 catalogue result proves the joint record–descent CLT at θ=λn with the identical descent variance. Its proof already uses exact finite-θ moments, exact centering, uniform convergence of rational profiles, and fixed finite dependence. Reading the proof shows that replacing λ by θ_n/n in the moment estimates is immediate, uniformly for parameters in a compact positive neighborhood of λ. The weaker descent-only projection consequently gives the bound result at arbitrary convergence rate by exactly those estimates. Maximizing the common closed form is routine differentiation and not a substantive residual claim. This is a coverage judgment, not a priority claim based on the later catalogue date. The primary fixed-bias results alone would not suffice.

## value

PASS

Positive linear bias changes second-order behavior, and an explicit variance law detects the counterintuitive initial increase before descent fluctuations shrink; this is mathematically informative beyond the mean and fixed-bias CLT. The derivative calculation itself has no independent significance once the coefficient is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

At exploration starts the contracting affine recursion gives exploration variance Q=2D/[r(1−a²)]. Cycle occupancy is p_E=1/(1+rm), refractory variance a²Q; thus C(0)/Q=(1+a²rm)/(1+rm) recovers m when 0<a<1. Brownian innovations after time 0 have zero conditional covariance with X_0, so C(t) is Q/(1+rm) times the future multiplicative reset-count PGF from exploration plus a²rm times the equilibrium refractory-residual PGF. Alternating-renewal equations yield F̂_E=[s+ar(1−w)]/[s(s+r−ar w)], residual transform (1−w)/(ms). Algebraically solving the resulting Möbius map gives the stated inversion except at s=ar, where the denominator cancels and w is recovered by continuity; the same cancellation gives universal Ĉ(ar) and sign-crossing identity. Independently checked symbolic inversion and exact-rational exponential-duration cases; a=0 is correctly excluded since complete resetting loses clock law information.

## originality

PASS

PASS best-of-knowledge: Olsen–Löwen 2024 original paper on *the same exact partial-reset model* was materially read in its open full manuscript (model, time-dependent one-time propagator, stationary marginal and appendix B), and does not state stationary lag autocovariance inversion or blind s=ar crossing. Published November 2 integrated-fluctuation result identifies only Var(T), not the entire distribution W. Related Taźbierski et al. two-time reset laws concern renewal resetting without the stationary partial multiplicative-jump-plus-frozen-refractory model and calibrated inverse. A stronger general semi-Markov inverse theorem is still a residual priority risk.

## value

PASS

Exact identifiability of an arbitrary distribution W from a single stationary *second-order time statistic* is a substantive semi-Markov inverse phenomenon: one-time law forgets all but m, while all lag-covariances recover W. The universal blind frequency provides a sharp model signature and shows an isolated observation cannot identify W. All positive a,r,D and all finite-mean measures (including atoms) are covered; an exact natural inverse result with possible use in renewal-process inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.

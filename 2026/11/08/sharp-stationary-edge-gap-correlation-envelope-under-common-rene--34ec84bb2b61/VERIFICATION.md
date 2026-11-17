---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

At equilibrium the common backward recurrence age A has density P(T>a)/E[T]; conditioned on A=a, N stationary coordinates are sqrt(2Da) times independent standard Gaussians. For each fixed top rank k, kb_N times its Gaussian gap converges in first and second moments to independent Exp(1) variables; the proof uses the Gaussian-tail uniform order statistics, exact Beta(k,1) ratio and Mills bounds to control exceptional tails, not weak convergence alone. Distinct gap covariance tends to Var(sqrt A), marginal variance tends to 2E[A]-(E[sqrt A])^2. Renewal-age moment formulas give (9-8κ)/(18-8κ), κ=(E T^{3/2})²/(E T E T²). Cauchy-Schwarz forces 0<κ≤1, with equality iff T constant positive, and two-point T∈{1,R}, P(T=R)=R^{-3/2}, gives κ→0. Intermediate values follow by continuity. The theorem is only for fixed distinct edge ranks, N→∞, finite E T², stationarity. The checked source is the pinned RESULT.md plus checker.py, not merely a PASS log.

## originality

PASS

Best-of-knowledge new is the sharp two-distinct-edge-gap covariance envelope and all reset-law equality/attainability cases. The cited 2022/2025 Brownian-gas primary results furnish common-age Gaussian mixtures and individual spacing functions, but inspected discussions do not state the joint cross-gap covariance optimization. Classical extreme spacings and stationary-renewal power correlation are credited as inputs.

## value

PASS

The precise cross-gap Pearson correlation is a natural observable of global resetting-induced dependence, not merely a normalization change of a one-gap law. The sharp nonzero periodic-reset obstruction, unattainable universal upper limit and realization of every intermediate level make a useful distribution-free dependence classification for arbitrary renewal clocks.

The dated certificate retains the supplied scientific assessment, sources and limitations.

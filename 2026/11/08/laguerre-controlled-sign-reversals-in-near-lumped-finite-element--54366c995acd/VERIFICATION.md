---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The P1 Dirichlet mass and stiffness normalization gives the stated exponent and 0<λ(C_n)<4, so the mass is positive definite even at p=1. At p=0 the tridiagonal generator is Metzler, giving positivity for positive times. At p>0, rescale by z=6t/(ph²) and apply the Laguerre generating function on the spectrum of X=p C_n/6. The entry at distance d is zero in powers below d, and its dth-power coefficient is the unique shortest path, (−1)^d. Dividing the rescaled entry by (p/6)^d gives an analytic extension through p=0, uniformly on compact z sets, with leading coefficient (−1)^d L_d^(−1)(z)=−(−1)^d z L_(d−1)^(1)(z)/d. Orthogonality for weight z exp(−z) makes the d−1 positive zeros simple. The implicit-function theorem yields simple perturbed crossings and the O_n(p²) dimensionless-time error at fixed n. For d=n−1 the spectral entry has n distinct real exponential rates, since λ/(1−pλ/6) is strictly increasing. Factoring the slowest term and differentiating gives the n−1 zero bound by Rolle's theorem, counting multiplicity. The mandatory origin zero and n−2 positive roots exhaust it; the origin is simple for p>0, consistent with the signed inverse-mass derivative. For n=3 the scaled far-corner sign is that of exp((s₂−s₁)τ)+exp(−(s₃−s₂)τ)−2, with s₃−s₂>s₂−s₁ for p>0 by strict convexity of the eigenvalue map. This expression is strictly convex, initially decreases, and ultimately tends to infinity. The other entries are positive for τ>0; the p=0 endpoint instead has no positive crossing. Independent 55-digit decimal bisection on [0.2,0.3] of this expression at p=1 with rates 6λ/(6−λ), λ=2−√2,2,2+√2 gives 0.212811776921431205, confirming the reported numerical example. The uploaded checker was not run; the fixed-n proof, not finite checks, gives the exact count.

## originality

PASS

Credit qualitative failure and recovery of semidiscrete positivity and the indexed exact consistent-mass three-node endpoint p=1 as existing coverage. The supported distinct theorem concerns the general fixed-n n−2 crossing count and Laguerre root scaling in the singular near-lumped limit, together with the extension of the three-node classification to the full blend. The inspected nearby periodic, inverse-mass and threshold results do not give that theorem.

## value

PASS

It resolves a natural limitation of qualitative positivity analysis: even arbitrarily near a positivity-preserving mass choice, transmission between the endpoints of a fixed uniform mesh may alternate repeatedly before settling, with a count growing with mesh dimension in the stated fixed-n regime. The precise Laguerre scale identifies when these transient events can be seen; the all-blend three-node result is a useful benchmark. No dimension-uniform p range or eventual entrywise threshold in general dimension follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.

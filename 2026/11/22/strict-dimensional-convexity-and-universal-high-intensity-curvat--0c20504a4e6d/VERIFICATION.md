---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For λ>0 the unperturbed generator has resolvent and the rank-one eigenvalue equation is βG_d(λ)=1. Product semigroups give G_d(λ)=∫e^(−λt)q(t)^d dt; q is strictly between zero and one for t>0 by the zero-jump and one-jump probabilities. The positive root is unique, with an open initial real-x interval of existence (the zero-energy integral is lower semicontinuous by Fatou). For the tilted probability βe^(−λ(x)t)q(t)^x dt, a=−log q lies in [0,ct], so all local differentiations at a positive root are dominated by polynomial times exponential tails. The implicit derivatives are λ′=−E[a]/E[t] and λ″=Var(a+λ′t)/E[t]. Normalization makes the mean in the variance zero. Strictness follows because a″(0)=−v<0 and the tilted density is positive throughout; comparison applies to each supercritical triple. For s=λ+cd and z=1/s the resolvent is z+M₂z³+M₃z⁴+M₄z⁵+O(z⁶), with M₂=dv, M₃=dw and M₄=du+6 binom(d,2)v² by interleavings of two returns per coordinate. The inverse near z=0 exists analytically with derivative 1, gives a positive large-β root, and reversion to s gives β+M₂/β+M₃/β²+(M₄−2M₂²)/β³+O(β^−4). The second difference is 2v²/β³. Bipartite parity makes the resolvent in z odd for nearest neighbors; inversion preserves oddness, giving the improved remainder. Independent lattice-state propagation for steps ±1,±2 of rate one returned (M₁,M₂,M₃,M₄)=(0,4,6,36),(0,8,12,168),(0,12,18,396) in dimensions 1–3, testing the genuine three-loop case. The exact d=1 nearest-neighbor root sqrt(β²+4r²)−2r also reproduces the d=1 coefficient. The frozen checker and stored output were inspected, not rerun.

## originality

PASS

Prior literature covers both the rank-one eigenvalue framework and dimensional monotonicity, and already gives a leading strong-source expansion by an implicit Fourier-resolvent method. Credit here is for strict supercritical convexity of the product family, the explicit first nonzero cross-dimensional coefficient for general finite-range product kernels, and the parity refinement relative to the inspected expansion, not for monotonicity or for introducing series methods. One directly relevant nearest-neighbor paper remains an access risk, not evidence of noncoverage.

## value

PASS

A strictly diminishing marginal dimensional growth loss resolves a structural question left open by monotonicity and valid throughout the positive-root regime, not just at large β. The first nonzero curvature term exhibits cancellation of the leading drift and individual three- and four-step contributions, isolating a universal square of the two-step return rate; this gives a useful comparison even across kernels with different loop structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.

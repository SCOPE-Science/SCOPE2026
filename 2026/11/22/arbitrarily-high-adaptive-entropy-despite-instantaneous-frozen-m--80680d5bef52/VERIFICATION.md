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

The identical rows send every distribution to Bernoulli(q_m(θ)) in one step and give its unique frozen stationary distribution. Interpolation preserves [1/8,7/8] and continuity at each junction, including the parity-dependent value at b. The fixed unit-curvature loss produces the old-distribution gradient θ−x, so the update is F_m(x,θ)=(q_m(θ),x), not a one-variable update using the new distribution. On each affine piece outside the central interval both endpoint differences have the required strict sign relative to 1/2; on the central piece q_m(t)−t=1/4−t/2. Thus there is only the equilibrium (1/2,1/2). The central square is forward invariant and its second iterate scales displacements by 1/2, proving local exponential attraction. On L the second iterate g=q_m²|_L has m equal-length surjective affine branches with absolute slope m. For an independent entropy check, g^k has m^k full branches. Taking every other branch leaves intervening gaps, so inverse-branch words give an (N,δ_k)-separated set under g^k of size ceil(m^k/2)^N, with δ_k>0 independent of N. Taking k to infinity gives h(g)≥log m, while the Lipschitz bound gives h(g)≤log m. The same entropy holds on R by affine conjugacy. On the compact union K=L∪R the second iterate preserves both pieces, so h(q_m|_K)=log(m)/2. Finally F_m² acts as q_m×q_m, giving exactly log(m)/2 on the invariant K×K by the product and iterate identities. This is a lower bound for the full square, not an exact numerical claim about it.

## originality

PASS

Coupled transfer and averaged-gradient control, strong frozen mixing with finite-step oscillations, performative chaos, and full-branch entropy formulas are not new. The distinct claim is unbounded topological entropy coexisting with the specified one-step frozen mixing, fixed uniformly quadratic loss, uniform positivity, and a unique locally exponentially attracting equilibrium. The inspected results do not supply this simultaneous construction or a stronger theorem entailing it.

## value

PASS

This is a quantitative obstruction to inferring global simplicity of adaptive dynamics from stochastic relaxation and pointwise convexity alone. The controller can preserve a locally stable equilibrium and still realize arbitrarily many branches away from it, even when each plant forgets its state distribution in one transition. Exact invariant-subsystem entropy distinguishes this from a single cycle or a weak example of nonconvergence; it identifies parameter sensitivity as a resource not bounded by frozen mixing and positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.

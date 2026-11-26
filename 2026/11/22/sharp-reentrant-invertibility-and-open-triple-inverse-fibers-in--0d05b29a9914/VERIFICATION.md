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

For this exact map on the real plane, the centered, bounded sigmoid perturbation of (1−T)I gives a uniformly proper homotopy for T≠1, so degree +1 forces surjectivity and the signed count +1 for every regular target. Such fibers are compact and discrete, hence finite and odd. Differentiating gives D=diag(d₁,d₂), dᵢ=α sech²(αzᵢ)>0, and DF=(1−T)I+TMD. The determinant is strictly positive for 0<T<1 and for T>1 with q=T−1≥(17/10)Tα, even at equality because the off-diagonal contribution is +T²d₁d₂. There is then exactly one preimage by degree; local inverses give a smooth global inverse. T=1 is an invertible affine transform of the open tanh square, not an onto map of the plane. At equality along (0,R), DF tends to a rank-one matrix, so inverse derivatives are unbounded and a Lipschitz inverse is impossible. For q<(17/10)Tα, the determinant along (0,R) tends to q(q−(17/10)Tα)<0, while along (R,R) it tends to q²>0. Continuity gives critical points. Use local inversion on the negative sheet and Sard to choose a regular target there: one negative sign requires at least two positive signs by degree. Local inversion on three disjoint neighborhoods gives an open common output neighborhood; properness also makes the critical-value set closed, if one wants all targets in a smaller neighborhood to be regular. Solving the inequality gives the restoration boundary, including 20/3 at α=1/2. `python /workspace/replay_checks.py 1` independently confirms the exact rational sign bound at (0,6) and three numerical branches of signs +,−,+, not an exhaustive census at that output. The full-plane statements are analytic, not based on the numerical example.

## originality

PASS

The map, degree method, and inverse-sheet vocabulary are not new here. The supported contribution is the exact one-step global invertibility diagram, including the equality behavior and the open multiple-preimage phase, not the previously studied forward dynamics. The available same-map statements are materially different; independent confirmation of the original paper's equation-level attribution and full-text priority is limited as detailed below.

## value

PASS

Global backward reconstruction is a different structural question from forward spiking and local stability. A sharp complete parameter diagram identifies when a larger step restores unique inversion, when the inverse loses uniform regularity despite remaining smooth, and when ambiguity persists on open sets. This is useful exact geometry even without a maximum fiber count or a stability claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.

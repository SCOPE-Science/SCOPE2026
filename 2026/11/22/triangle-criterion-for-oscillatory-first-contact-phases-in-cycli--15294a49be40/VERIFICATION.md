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

The time change s=∫D_(J_t)dt gives a Brownian motion with generator ∂² in its own clock; conditional on the original chain the time-changed Brownian law does not depend on the chain. The chain in that clock jumps at rates a_i=γ/D_i, and its stationary distribution is proportional to 1/a_i, so the hitting mark is governed by the clock-changed generator, not the uniform law of J_t. Averaging its semigroup over Brownian hitting time gives H=e^(−x√L) by the Laplace transform, with the decaying branch for the two transient modes and a constant projection Π=1ρᵀ. The characteristic polynomial is z(z²−Sz+P), and the transient square root has real part u and imaginary parts ±v exactly when Δ<0. Each entry of H−Π then has a nonzero cosine coefficient at x=0, δ_ij−ρ_j, hence its sinusoidal zeros are simple and spaced π/v. For positive Δ the two modes are distinct real exponentials; at Δ=0 they give a degree-at-most-one polynomial times a decaying exponential. Nontriviality at x=0 excludes an identically zero entry in either case and gives the at-most-one-positive-zero result. Factoring Δ in the square roots of the rates gives the strict triangle inequalities, including the correct degenerate boundary. With sides 1,1,√c, the cutoff is 4; differentiating v² gives the unique maximum c=3/2 with γ/(8D), and v²∼γ(4−c)/(12D) yields the claimed divergence of spacing. Zero spacing is understood between consecutive roots; interval counts at exact root endpoints depend on endpoint convention. The frozen verifier was inspected, not executed. Its finite numerical comparisons cannot establish the infinite-sign or boundary assertions.

## originality

PASS

The general first-passage phase transform is established prior art, and the three-state generator's spectral discriminant is known in the temporal oscillation literature. The supported distinct contribution is the classification of the spatial zeros of all nine centered Brownian first-hit marks, including the real-mode and degenerate boundary cases, exact spacing, and the one-defect optimum and critical divergence for spatial frequency. The elementary triangle factorization re-expresses the known spectral discriminant; it is not a claim of a new generator-spectrum theorem. The checked primary results do not themselves state the entrywise marked spatial law or optimize its spatial oscillation frequency. This is a bounded best-of-knowledge judgment.

## value

PASS

A marked first passage can identify state preferences invisible to unmarked Brownian hitting probabilities. The exact sign boundary tells whether every centered mark reverses indefinitely or at most once, including on the repeated-mode boundary, without requiring numerical evaluation at large distance. The one-defect maximum at a nonuniform diffusivity and the diverging crossover spacing give meaningful spatial predictions beyond the known matrix transform. The magnitude is exponentially damped, so infinite mathematical reversals do not imply experimental observability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In the stated deterministic rank-one model, survival in susceptibility class xᵢ is exp(−xᵢL); integrating weighted infections with common exit rate gives the scalar pressure equation with weights uᵢ, and the attack fraction uses pᵢ. For positive uᵢ and xᵢ, F(z)/z decreases strictly from m₁ to 0 by strict concavity and boundedness, giving one positive solution exactly when κm₁>1. The rank-(k−1) truncated Vandermonde matrix has kernel spanned by bᵢ=1/∏_{ℓ≠i}(xᵢ−xℓ): Lagrange leading coefficients annihilate monomials through degree k−2 and send degree k−1 to 1. Thus the pair's weight difference is Δb, with Δ the first unmatched moment difference. The divided difference of 1−exp(−zx) has the strict sign (−1)^k for positive z by its (k−1)st derivative. Evaluating the two scalar equations at one root transfers the sign to the positive pressures, and the common strictly increasing attack-fraction map transfers it to final fractions. Equal top moments give equal weights by the full Vandermonde matrix. The proposed binary infectivity perturbation is admissible for all sufficiently small positive ε, sums to zero in the relevant marginal because ∑bᵢ=0, preserves m₁ when k≥3, and has nonzero top moment; k=2 already has an invertible system with m₀,m₁. The exact example has top-moment difference 1/24 and the stated negative factored response difference. Independent bisection of the positive roots at κ=2 reproduced both pressures and fractions to the reported digits.

## originality

PASS

The generalized convex-order and Laplace-transform sign mechanism, finite Vandermonde inversion, and scalar epidemic equation are established mathematics. In particular the all-pressure parity follows from the prior discrete sign-change criterion; it is not credited as a new stochastic-order theorem. The distinct scientific claim is the sharp finite mixed-moment information cutoff for the positive branch with both full trait marginals and the invasion threshold held fixed, witnessed for every k≥3 on any given distinct positive susceptibility support with positive frequencies. The inspected ordering and identifiability results do not give that simultaneous sharpness statement.

## value

PASS

The model-based question is whether a finite collection of leading mixed moments identifies final size when susceptibility values and both trait marginals are known. The sharpness witness shows why knowing the reproduction threshold and, even at larger k, all but the final leading mixed moment can be insufficient without changing either population trait marginal. Combined with the exact finite cutoff, this gives a useful identifiability boundary for the model, rather than a relabeling of the classical sign inequality or a comparison limited to a single transmission parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.

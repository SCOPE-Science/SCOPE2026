---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Exact intrinsic width W=2 max_edges|X_i-X_j|/R with R²~χ²_(n-1) and radial independence. In Gaussian edge variables adjacent correlations have abs value 1/2; integrating bivariate Gaussian tail yields C u^-2 exp(-2u²/3), allowing dependency Poisson error O(Δ m^(-1/3)(log m)^(-1/3)) and thus Δ=o(m^(1/3)). Uniform bounded-degree matching gives double-exponential negative and exponential positive tails for normalized maxima, enough for second-moment convergence and path variance 2π²/3 via b_m²~4 log m and radial normalization. Fixed positive leaf fractions imply each hub leaf maximum and negative minimum differ by a_m by o_L2(1); finitely many core edges vanish after subtraction, so limit max|Z_j| and moments. Polar computation yields v1=v2=1-2/π, differing CDFs (2Φ(t)-1)^k. The finite core Gaussian integral follows by conditioning on hubs. These calculations are analytic not Monte Carlo extrapolation.

## originality

PASS

The general bounded-degree Gumbel limit, star folded-normal law, and tree crosspolytope combinatorics are covered by October 25 published theorems; they are not credited. Substantive independently useful surviving claims are the improved growing-degree threshold Δ=o(m^(1/3)), rigorous moment/variance asymptotics, and the full fixed k>=2 hub law with its v2=v1 coincidence and finite-size integral.

## value

PASS

Two distinct fluctuation scales for combinatorially identical tree crosspolytopes, sharp path variance and fixed multihub distribution/variance constants address a natural metric-geometric invariant. The k=2 variance coincidence despite different laws is a meaningful exact structural comparison; the enhanced degree window supplies a nontrivial quantitative probabilistic improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.

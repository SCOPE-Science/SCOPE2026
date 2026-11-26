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

The frozen finite-difference identity agrees with Svihla Eq. (14), since ψ(k+h)−ψ(1)=H_(k+h−1). Its original citation should be Aldous–Janson, Mellin analysis of leaf height, Eq. (5.4), not Aldous–Janson–Li; the latter paper establishes the occupation limit. This attribution issue does not change the identity or claim. For an independent route through the primary sources, the measure Υ in Aldous–Janson Eq. (4.8) satisfies ∫x^r xΥ(dx)=1/H_(r+1) for r≥0. Since xΥ is finite and Hausdorff moments determine it, Berg–Durán Eq. (1.2) gives its density ∑ α_j x^ξ_j. In the Aldous–Janson occupation integral Eq. (5.3) substitute this density and integrate the nonnegative series; each term is H_(k−1) binom(k+m−1,k−1) α_j B(k−1+ξ_j,m+1). Its Gamma quotient is exactly w_(k,j) times the m-th moment of Beta(k,ξ_j), or 1 times the weight for j=0. At m=0 the weights sum to a(k,k)=1. This verifies the atom, and the interior density is positive from j=1 alone. Hausdorff uniqueness applies on [0,1], including the endpoint convention. On the interior, x^m(1−x)^r is positive and every nonzero polynomial has only finitely many zeros: integrating these and squared polynomials (also with x^m for shifted matrices) proves the strict difference, positive-definiteness and log-convexity claims. The product R_(k,m)(ξ) decreases strictly for m>0, so isolating j=1 and bounding the rest by R_(k,m)(ξ_1) gives both bounds with the stated equality conventions (the lower bound is strict also at m=0). Fixed k Gamma-ratio asymptotics give R(ξ_j)/R(ξ_1)→0 for j≥2, dominated by one under the finite positive weights. This proves the leading exponent and limit, without a joint k,n asymptotic assumption. A numerical root check gave ξ_1=1.5673537531016553325…, consistent with the record. The frozen finite rational diagnostics were inspected, not run; the all-index conclusion is analytical.

## originality

PASS

The prior literature provides an exact occupation integral and binomial sum, the reciprocal-harmonic spectral measure, and occupation asymptotics. Credit is limited to using the exact spectral inversion to make the occupation sequence itself a positive moment mixture, and to the resulting strict moment hierarchy and simultaneous finite-size bounds. The relevant primary passages were inspected; none gives that combined result.

## value

PASS

The useful change is from a signed occupation formula or asymptotic residue expansion to one positive measure controlling the entire fixed-target sequence, simultaneously available for every target k≥2. This yields strictly signed differences of arbitrary order and definite Hankel matrices, stronger than monotone convergence, and simple finite-n bounds valid even when n−k is small. The analysis credits the known limit and leading decay; it does not assert that the finite envelope coefficients are optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.

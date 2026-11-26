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

Reconstructed the Euclidean section normalization: for unit u the density of the Laplace projection at zero is the section integral of exp(−||y||₁)/2^n, giving (n−1)!/2^n times the section volume. Fourier inversion and partial fractions give c_n times the stated rational sum. On the unit sphere the integrand is dominated by (1+t²/n)^−1, so the section formula has a continuous positive extension to coordinate-wall directions; this does not require evaluating a possible zero-over-zero rational expression there. The common-denominator numerator is alternating, so division by the monic linear Vandermonde factors is exact over the integers. At a generic a_j=−a_i≠0, only terms i,j contribute a pole. Written over a_i²−a_j² their numerator has limit 2a_i^(2n−3)/∏_{k≠i,j}(a_i²−a_k²), which is nonzero. Thus no pair-sum factor cancels and the homogenized linear polynomial in z is primitive and irreducible over C. A dehomogenized factorization would homogenize and contradict this. On each open orthant, the polynomial vanishes at the radial boundary point, and its derivative in the radial scaling direction there equals the nonzero D_n of the signed point. Hence the patch is relatively open and smooth, and Zariski dense in that irreducible hypersurface. Continuity and density of open orthants in the topological boundary account for the remaining points. Any differing pair-sign products distinguish the top-degree factor sets, while simultaneous sign reversal changes the relative parity of the two nonzero homogeneous parts. This proves the exact component count and the sum of degrees. Independent dimension-four checks recover P_4=e_2e_3−e_1e_4 and the axis-limit normalization 4/3.

## originality

PASS

The strongest examined results give an upper bound for symmetric polytopes, a section-volume representation on the same family, or the exact dimension-three classification expressly outside the new claim. They do not establish denominator noncancellation, absolute irreducibility and exact mutually distinct components for n≥4. The assessment is bounded and does not certify priority.

## value

PASS

Determining whether the general degree bound is attained for the standard cross-polytope, and which irreducible equations account for its boundary, is a motivated metric-algebraic classification problem. The result settles sharpness, component multiplicity and explicit equations uniformly in dimension; this is more informative than an isolated small-dimensional check or a new expression for an already known section volume.

The dated certificate retains the supplied scientific assessment, sources and limitations.

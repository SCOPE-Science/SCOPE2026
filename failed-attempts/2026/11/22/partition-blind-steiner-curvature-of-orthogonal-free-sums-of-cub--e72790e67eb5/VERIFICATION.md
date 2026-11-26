---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The independent block radial densities are 2^(r_i) r_i u_i^(r_i−1); their simplex integral gives the claimed V. All facet normals select one signed coordinate per block, hence have norm sqrt(m) and the origin-to-plane distance 1/sqrt(m). Pyramid decomposition proves S/V. Polar product edges vary a single factor. A nonsingleton factor has 2r_i(r_i−1) edges between distinct nonopposite axes and a singleton factor one sign-reversing edge; this gives F(r_i−1) and F/2 ridges in the two cases for block i. The corresponding normal inner products after normalization are (m−1)/m and (m−2)/m. For the ridge measure, the simplex of active radii has metric with independent axis multiplicities k_i, one each except for one doubled coordinate in the nonsingleton case, or all one after removing the vanishing singleton. Eliminating the last radius makes its Gram determinant (product k_i)(sum 1/k_i), respectively 2m−1 and m−1. The remaining box coordinates give Dirichlet exponents r_i−2 for the doubled block and r_j−1 for each other active block. Multiplying by the ridge counts yields exactly the two per-block normalized measures in the proof and the tube formula has factor one-half for the exterior sectors. This covers m=1 and agrees with C2=pi for either d=2 partition. The two bracket weights are 2g(2m) and 2g(m), with g'(u)=arcsin(1/sqrt(u))/(2sqrt(u−1))−1/(2u)>0; increasing s strictly lowers the coefficient wherever different s are feasible. The inequalities on the number of singleton blocks give the stated extremizers. The illustrative facet counts are 192 and 256.

## originality

FAIL

Demonstrable earlier equivalent coverage, not a retrieval or proof failure. Resultary's 2026-11-17 enriched-chain-polytope record d1d809dcc511 explicitly identifies its body with the identical Euclidean coordinate set sum_i ||x^(i)||_infinity≤1 for arbitrary positive layer sizes, including singletons. It states the same volume, S/V and C2/V, and the same complete two-class ridge count, measures and angles. Relabel n=d, r=m, a_i=r_i and use S=2V_(d−1), C2=pi V_(d−2). Its nontrivial parameter range m≥2,d≥3 includes every possible variation relevant to the claimed fixed-d,m extremizers. Monotonicity and equality classes here are direct algebraic consequences of the two prior bracket weights and the elementary feasible singleton counts. The additional m=1 cube and d=2 polygon cases are classical boundary calculations, not a distinct original contribution.

## value

FAIL

The exact normalized curvature is a worthwhile invariant in itself, but the frozen finding does not newly supply it. With the exact same-family metric formula and full ridge census already available, the extra content is an immediate comparison of two scalar terms, a profile-count boundary, and classical low-dimensional or one-block cases. This does not constitute a separate useful mathematical advance over the known result.

The dated certificate retains the supplied scientific assessment, sources and limitations.

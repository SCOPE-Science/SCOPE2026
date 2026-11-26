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

Boben–Gévay–Pisanski Lemma 4.5 identifies this incidence configuration with the part of the fourfold/triple hyperplane construction containing one distinguished index. Removing that index leaves exactly containment of a 2-set in a 3-set. I constructed the graph by masks: sets of weights 2 and 3 joined when their XOR has weight 1. The degrees are 4(15),3(20) with 60 edges, and the exact Laplacian characteristic polynomial agrees with the claimed simple zero and all remaining eigenvalues. The exact integer cofactor determinant and Smith form give 377913600000000 and 1(24),2(2),10(2),30(2),180(4), respectively. The dual graph has first Betti number 26; for a connected special fibre with rational components this is the arithmetic genus, and all vertices have valency at least three. For a regular unit-thickness split smoothing, the component intersection matrix is −L and its multidegree quotient in the sum-zero lattice is the geometric Néron component group, as claimed conditionally.

## originality

PASS

The configuration and even its graph catalogue identification are known. The 2- and 5-primary factors are covered by the known Johnson J(6,2) result after a Schur reduction. At 3 the required Schur reduction is instead to J(6,3); the inspected general diagonal-form and k=3 Johnson theorems do not include that boundary parameter, and the Wilson rectangular result alone gives no full Smith group. The surviving statement is the complete integral group (including the additional 3-primary argument), not the geometry or disjoint claims to the two already covered primary parts.

## value

PASS

The Steiner–Plücker Levi graph and its dual are classical motivated projective configurations. The complete primary decomposition, including the 3-primary part not supplied by the checked J(6,2) corollary, is a reusable exact invariant. It also gives the precise component group for unit-thickness regular split genus-26 smoothings with this dual graph. Neither the geometric classification, the existing partial primary calculation, nor the spectrum alone gives this complete invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.

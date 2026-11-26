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

In the three ordered nonempty disjoint target blocks, a rotation fixing an interior point must preserve all blocks. Only the half-turn has enough color orbits: its three opposite pairs must be the three blocks. It fixes exactly six cube centers in two C₆-orbits. The Babson–Kozlov wedge theorem makes X simply connected with H₂(X)=0. Remove small equivariant open balls about the six centers to obtain W. Attaching the balls with simply connected boundaries does not change π₁, so W is simply connected. The free quotient W/C₆ has π₁=C₆; filling its two boundary copies of RP² with cones kills exactly the order-two subgroup by van Kampen, giving π₁(Y)=C₃ without needing the inaccessible Armstrong citation. An independent check of H₂ uses the map H₃(X)→H₃(X,W)=ℤ⁶. For any specified fixed cube with opposite pair in block i, allow one color of that pair in slots {i,i+1} and the other in {i,i+2}, modulo three. Sum all top cells allowed by these choices with orientation sign equal to the sign of the concatenated block permutation, times (−1) to the sum of the slot indices, times the product of opposite signs for each color's two choices. Each facet leaves one color unassigned and its two extensions cancel: the product-boundary deletion sign at concatenated index p in slot i is (−1)^(p−i), and permutation deletion contributes (−1)^(p+a) for color a, so the only extension-dependent sign left is that color's choice. This cycle has coefficient ±1 on the specified fixed cube and zero on the other five, because each opposite pair has only one allowed common slot. Thus the map to ℤ⁶ is onto, giving H₂(W)=0. By Hurewicz, lifting π₂ to W, and the Hopf sequence with H₂(C₆;ℤ)=0, H₂(W/C₆)=0. The relative H₂ from filling the two cones is (ℤ/2)²; both generators map to the half-turn in H₁(W/C₆), so H₂(Y)=ℤ/2. Subdivided flags are valid oriented orbit cells because strict dimensions order their vertices and stabilizers cannot invert them. An independent exact flag replay verified ∂²=0, chain ranks (351,3060,5940,3240), and nonzero Smith lists (1×350), (1×2709,3), and (1×3229,2), with residual rank-one tests establishing exact orders. These give H₀=ℤ, H₁=ℤ/3 and H₃=ℤ¹⁰, agreeing with the topological torsion check and Euler characteristic −9. Nothing occurs above degree three.

## originality

PASS

The underlying complete-graph Hom theorem, the orbit fundamental-group method, and rational rank methods are existing inputs, not novel claims. The supported distinct result is the integral classification of this first nonfree target-cycle case, especially the order-two H₂ alongside order-three H₁. The strongest inspected prior statements change the action or the complex, or only control rational data.

## value

PASS

Six is the smallest number of colors admitting a nontrivial cyclic rotation with at least three color orbits, hence the first number at which three nonempty disjoint ordered blocks can support fixed points for the full cyclic target rotation. This is a motivated boundary of the free-action examples. The exact integral invariant exposes what fails there: the two singular links kill the order-two element in π₁ but their link classes have a nonzero order-two relation in H₂, which the rational top character does not record. This supplies a useful finite test of any proposed composite-color extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.

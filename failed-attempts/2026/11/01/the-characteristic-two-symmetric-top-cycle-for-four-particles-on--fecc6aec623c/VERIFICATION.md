---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Verified for unordered configurations with a,b≥2. In the natural reduced Świątkowski model the two degree-one hub factors are the only positive-degree factors. The two top-cycle equations preserve bidegrees up to separate increments in the two disjoint edge-difference sets. Zero degree in either set gives a zero coefficient block by monomial independence, including over F₂. In weight four only bidegree (1,1) survives; repeated-index coefficients vanish and the remaining coefficients are alternating in each index pair, giving the asserted integral basis with no top boundaries. The interchange of the degree-one factors supplies the minus sign. The mod-two basis is a single unsigned orbit, whereas over other fields, or over Z, the respective pair transposition negates each prescribed basis coordinate without mixing any other coordinate into it. Frozen modular outputs were inspected as finite corroboration, not run or used as the all-parameter proof.

## originality

FAIL

No verbatim statement was located, but the full claimed refinement is a direct specialization of the published bivalent-cut theorem and the published oriented star cycles, including the symmetry rather than just the rank. Subdivide the middle edge at a canonical midpoint and cut there by ADCK Proposition 5.22. Its quotient map comes from the inclusion of the cut reduced complexes, so it commutes with leaf permutations and with exchange of the two stars. It only identifies the two central leg stabilizations. In degree two there is no term except H₁ of each star; the first H₁ of each star is at weight two, and the stabilization relation raises weight, hence does not affect weight four. For a cut star fix its central leg 0. The published oriented triod cycles α₀ᵢⱼ span the weight-two group: every αᵢⱼₖ is their alternating sum by the published chain formula; α₀ᵢⱼ are independent by the coefficient of the distinct monomial (eᵢ−e₀)(hⱼ−h₀). These are already the signed leaf-pair basis. The product is the exterior-square tensor in the finding, with the standard degree-one cross-product sign under exchange. On this signed permutation basis taking invariants is immediate: one unsigned orbit in characteristic two, and a sign-reversing stabilizer of each coordinate otherwise. This argument needs no new graph-configuration theorem or new relations. The judgment is coverage by implication, not a claim that a prior source prints this invariant dimension verbatim.

## value

FAIL

The modular symmetry question is natural, but on this family it reduces without further topology to the sign stabilizer of a pair in a known product basis. The record establishes no further obstruction, equivariant lattice beyond the initial product weight, or independent phenomenon not mechanically inherited from those products. The narrow exact finding does not meet the value criterion for a distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.

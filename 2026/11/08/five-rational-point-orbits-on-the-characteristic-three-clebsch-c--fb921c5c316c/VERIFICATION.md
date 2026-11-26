---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

On σ₁=0 the gradient entries of σ₃ are σ₂+x_i². A geometric singular point would have all squares equal, with nonzero coordinates of one magnitude and four signs equal against one opposite to meet σ₁=0 in characteristic three. The resulting σ₃ is ±a³, so no such point exists. An independent exact census (/workspace/checks/1.py) searched disjoint projective charts for points and all 7,462 rank-two RREF subspaces of the four-dimensional trace hyperplane for lines, testing each binary cubic restriction at four distinct points. It recovered 145 points and 27 rational lines, hence all geometric lines by smoothness and the 27-line theorem. Their partition into 15 coordinate-hyperplane lines and 12 others gives the representative incidence pairs (3,0),(2,0),(1,0),(0,2),(1,1). All point orbits were checked directly. Scalar multiset preservation gives S₃×C₂ for the triple zero; swaps inside two double entries with a sign exchange give (C₂×C₂)⋊C₂ ≅ D₈; the four nonzeros in the third representative comprise a cyclic scalar coset, giving C₄; in the fourth no nonidentity scalar preserves the multiset since its unique singleton is nonzero, giving C₂×C₂ by the two pair swaps; in the last only ±1 preserve the nonzero entries, giving C₂. Independent element-order counts agree. The orbit of the triple-zero point is the faithful action on unordered pairs of coordinate positions. Orbit sizes 10,15,30,30,60 exhaust the charts and each stabilizer contains an involution. This verifies the arithmetic statement over F₉ only.

## originality

PASS

Credit the known Clebsch model, S₅ action, split surface and aggregate incidence histogram. The supported distinct claim is the full rational-point orbit table with stabilizer isomorphism types and incidence per orbit; the strongest inspected comparisons do not supply that refinement or imply it from their tabulated invariants.

## value

PASS

The characteristic-three split Clebsch is a canonical surface, and point stabilizers are natural data for its specified faithful symmetry action. The table exposes why the two equal-length point orbits cannot be identified and determines the involutory isotropy of every rational point, refining known surface-level counts. The value rests on the orbit classification, not on recomputing the aggregate histogram or claiming anything for arbitrary extensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

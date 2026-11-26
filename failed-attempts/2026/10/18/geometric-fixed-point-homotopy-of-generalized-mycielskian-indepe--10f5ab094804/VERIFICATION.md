---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A fixed point has constant barycentric coordinates on each vertex orbit, so its orbit masses give the inverse to the affine barycenter map from the orbit complex. The relevant model is the independence complex of the admissible-orbit graph, not the induced complex on fixed vertices. The top clique rejects every nontrivial cycle orbit; below the top each such orbit sees all neighboring-level orbit vertices, including its own cycle one level away, because a distinct-label cross pair exists. A fixed-label orbit at the same level has a subset of that neighborhood. For nonadjacent u,v with N(u) contained in N(v), every independent face containing v can adjoin u; remove the pairs F,F∪{u} for F containing v but not u in decreasing cardinality, so each is a free-face collapse. This deletes all nonsingleton orbit vertices when f≥1. When f=0, same-level orbit vertices are twins and the same collapse leaves the apex and one vertex at each level below the top, giving P_(ℓ+1). For P_m, removing its second vertex leaves a cone and that vertex's link is Ind(P_(m−3)); the deletion cofibration yields the suspension recurrence for m≥4 with base cases point, S⁰, S⁰. For f=1 and ℓ≥2 the smaller graph has isolated vertices. For f≥2 the wedge dimensions and multiplicities are exactly Carnero Bravo's Corollary 7 after substituting f, with no depth shift in that convention. The 2019 formulation uses the shifted index ℓ+1.

## originality

FAIL

A distinct indexed result, ca85c232abce, gives the full claim and the same orbit-model vertex deletions for every subgroup and a larger depth range. Taking H=⟨σ⟩ exhausts the frozen claim, not just its sphere counts. That catalogue entry is displayed with a later date; this is demonstrable coverage in the inspected corpus, not a finding that the frozen claim lacked priority when made. The earlier character theorem and ordinary homotopy theorems do not independently prove the reduction. No distinct mathematical remainder survives the all-subgroup comparison.

## value

PASS

As a mathematical result the explicit reduction answers a natural geometric question that traces cannot settle: it identifies the actual fixed-space homotopy type and explains why cycles of different lengths give the same answer. The collapse proof is substantive, even though the stronger indexed theorem leaves no distinct claim in the frozen submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.

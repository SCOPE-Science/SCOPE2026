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

The exact intersection array gives distance shells (1,k,k,1); disjoint neighborhoods of antipodes exhaust all other vertices. Two chosen antipodal pairs, one per named color and allowed to coincide, therefore give weight four. For weight ≤4 a support of size ≤1 cannot reach the at least 2k−2 empty vertices, since 2k−2>k. At equality both supports have size two. For an adjacent support its external union has 2k−2−a₁ vertices with a₁=k−μ−1>0, and for a distance-two support it has 2k−μ<2k−2 when μ≥3. Only distance three works, giving (k+1)² optima. For the icosahedron a distance-two support would instead exhaust exactly eight external neighbors, forcing the other color onto precisely the two vertices outside that union and the original support. By vertex transitivity take the first support vertex to be the upper pole and the other to be v_i on the lower 5-cycle; the two residual vertices are v_{i−2} and v_{i+2}, which are adjacent. An adjacent second support cannot cover eight empties. This gives exactly 36 minima even at μ=2. For J(6,3), distance is 3 minus intersection size, there are nine neighbors and a unique complementary antipode, and a distance-two pair has four common neighbors (the shared element plus one from each two-element difference). Together with four common neighbors for adjacent pairs and b₂=1, this gives the stated array and 100 optima. Frozen check.py and check.cpp are replay paths for the examples; they were inspected but not executed. The family conclusion follows from the symbolic argument.

## originality

PASS

The minimum weight four follows from the published numerical lower bound and the elementary antipodal construction, so it is not credited as new. The supported distinct statement identifies both supports in every optimum for the stated Taylor array, including coincident pairs, and proves the analogous boundary classification for the icosahedron. The inspected product-domination formulation and existing equality characterizations do not yield that weight-four structure by substitution. The closest distinct local label classification is for the Petersen graph at weight five; the closest same-icosahedron antipodal catalogue entry is ordinary paired domination, not rainbow domination.

## value

PASS

A known scalar bound does not reveal whether adjacent, distance-two, and antipodal supports can all appear in optimal solutions. This theorem makes the entire optimum set explicit over a distance-regular class and gives the exact named count, including overlap of supports; the icosahedron resolves a genuine boundary where the general distance-two inequality ceases to be strict. That rigidity is useful in the equivalent product-domination problem and for comparing extremal labelings across symmetric graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.

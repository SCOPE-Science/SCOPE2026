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

The rows and columns are the closed-neighborhood indicators in the stipulated folded five-cube, and the coefficient field is GF(2). A kernel vector supported on the initially white set vanishes at each successive forced vertex by the equation at the black forcing vertex, so success implies independent columns. This also bounds success by six white vertices when the full rank is six. Greedy sequential tests are valid: a legal target is either already removed by other steps or still legal when the black set grows, and a stalled nonempty white set is a fort that cannot be eliminated by a different order. Independently, in the binary group algebra on four commuting involutions g_i put t_i=1+g_i, so t_i^2=0. Multiplication by 1+sum(g_i)+product(g_i) is multiplication by e_2(t)+e_3(t)+e_4(t), with e_j elementary squarefree sums. Its degree-2 image is one-dimensional; the degree-3 leading images of the four t_i have matrix J+I indexed by missing coordinate, invertible over GF(2); and a degree-2 monomial yields the full degree-4 monomial. Hence the rank is six. The 160 induced three-vertex paths arise from choosing a center and two out of five directions. For the center 0 and ends 1,2, only 7,11,12 are common nonneighbors outside the path; they are independent, and the resulting six-set is a fort. Permuting directions and translating proves transitivity; the stabilizer of 0 in the full graph automorphism group acts faithfully on the five directions since each other vertex is identified by its distinct pair of neighbors among those directions. Thus the full group is the affine group of order 1920. A fresh exhaustive replay, run as python3 independent_census.py in /workspace/branches/82fbe3ce-d266-406e-870f-07de7b950861 (recorded independent_census.txt), checked rank, sequential forcing and the induced degree signature for all 8008 unordered six-sets; the disjoint counts are 3976,160,3872. It also checks all 160 exceptions are forts in the single orbit with stabilizer 12. The given two white sets are both forceable; after deleting 14 from the first, insertions 2,5,8 have rank 5, and 10 has rank 6 but is in the exceptional orbit. This violates basis exchange for the family. All checks concern this graph and ordinary zero forcing. The frozen Python and C++ sources were inspected, not executed; the new enumeration verifies the main table and exchange, not a general graph theorem.

## originality

PASS

The supported distinct result is the exact comparison of ordinary forcing complements with this binary code's information sets, including the single missing fort orbit. The necessity argument is prior general theory, and no novelty credit is assigned to Z=10, the 3872 count alone, or the previously attributed ordinary reconfiguration census. The same-day skew family has a related obstruction but is not the ordinary family or this code comparison.

## value

PASS

Both rank and optimum complement size select six before the enumeration, and the code's linear recovery versus ordinary peeling is a natural comparison, not a random graph count. The exact classification isolates a single geometrically recognizable fort orbit that passes the linear test yet blocks peeling, and supplies a concrete exchange obstruction including one failed exchange that still passes rank. This remains useful even if all optimum forcing sets had already been enumerated.

The dated certificate retains the supplied scientific assessment, sources and limitations.

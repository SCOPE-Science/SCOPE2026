---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For m,n≥3 the categorical product has diameter two; GP iff no induced three-vertex path, equivalent to induced disjoint union of cliques. This yields row/column subsets, partial permutations, and three/four-corner rectangles. Combinatorial counting verifies Ψ; maximal sets are full rows, full columns, maximum partial permutations or full rectangles, giving M. Coefficient differences a3-a4 and a4-a5 determine sharp 11..17 unimodality failure. Independent true-graph shortest-path and one-vertex maximality enumeration checked all 512 subsets of K3×K3, 4096 of K3×K4 and 65536 of K4×K4; all full coefficients match. This confirms correctness, not novelty.

## originality

FAIL

DECISIVE PRIOR COVERAGE: an already documented SCOPE result at the SAME frozen commit, "Sharp reentrant unimodality windows for general-position polynomials of diagonal-deleted multipartite graphs" defines T*(r,a) on [a]×[r] with adjacency iff both coordinates differ, graph-isomorphic by definition to K_a×K_r. Its all-set coefficient formula for every a,r≥3 is exactly this submission’s Ψ (including both rectangle corrections), and it proves the exact identical unimodality window 11≤r≤17 at a=3, plus a stronger a=4 theorem. The earlier 2024 primary paper itself discusses T*(r,a). The new maximal-set polynomial does not appear in that prior SCOPE RESULT and could be a genuinely separate result, but the unchanged package incorrectly presents already-covered main findings as new. Without complete corrected mathematical files narrowing/crediting those portions and new C/O/V for the final claim, the as-submitted composite is rejected on originality. Prior overlap is implication-level, not title coincidence.

## value

PASS

The object family is natural; the complete maximal-set polynomial, purity criterion m=n=4, and unbounded cardinality gaps remain meaningful as exact invariants and do not follow from the all-set coefficient sequence alone. The already-published unimodality theorem is valuable mathematically but cannot be credited as new. Value does not cure originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.

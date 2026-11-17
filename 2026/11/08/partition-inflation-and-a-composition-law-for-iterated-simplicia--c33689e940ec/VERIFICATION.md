---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

A D_r(D_sX) vertex is exactly an unordered partition of one rs-element face U of X into r disjoint s-blocks. This gives c=(rs)!/(r!(s!)^r) equally many labels per U. Two or more labels form a simplex iff underlying rs-sets are distinct, disjoint and have union in X; this proves a natural isomorphism to uniform vertex inflation of K=D_rsX, without dimension or connectedness restrictions. Links satisfy lk_K(F)=D_rs(lk_X(U_F)). For connected K the Björner–Wachs–Welker Theorem 6.2 vertex-inflation wedge splitting directly supplies the integral formula with (c−1)^|F| copies of Σ^|F| of those links; disconnected components are handled separately, and the empty-facet link has S^{|F|−1} convention. X=Δ⁵ gives 10 vs 15 isolated vertices for (r,s)=(2,3) and (3,2), and X=Δ⁸ gives 378 vertices, 2835 edges, beta1 2458. The proof checks all face levels, not only 1-skeleton; inspected verifier independently constructs direct and partition-labelled small cases. This is a valid consequence of the earlier splitting, which is credited, not newly proved.

## originality

PASS

Best-of-knowledge PASS with specifically described primary-source, broader-implication and alias comparisons; unindexed equivalents and two inaccessible highly relevant full texts remain real residual risks, not falsely declared excluded.

## value

PASS

The behavior of two iterations of a naturally introduced simplicial operation is a genuine categorical/topological structural question: the composition law determines precisely how parameters multiply, explains the many labels and is provably order-sensitive even for a 6-vertex simplex; a classical splitting then yields a link-by-link integral homotopy recursion. This is meaningful independent of the previously known splitting itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.

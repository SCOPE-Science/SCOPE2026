---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

At the assigned frozen 10-file tree, all 15 Petersen edges are defined as GP(5,2), and each face is exactly an edge mask excluding all k-edge matchings for k=2..5. An independent Python reconstruction enumerated all 75/145/90/6 forbidden matchings, 56/1073/8558/27449 augmented faces and 24/530/4271/13720 toggle pairs, then oriented and topologically sorted every 105/3990/47085/194040 Hasse incidence with no cycles. It independently recovered the exact critical CW cell dimensions and signed integer Morse matrices. For k=3 the lone 4-to-3 column is primitive; for k=4 the 8x5 6-to-5 matrix has rank four and a determinant +1 maximal minor, with 7-to-6 primitive column spanning its kernel; for k=5 the 10-to-9 column is primitive. The CW models have one vertex and no lower positive cells. Standard Morse CW, Hurewicz, and homological Whitehead give the claimed integral wedge homotopy types, not just mod-two Betti groups. For k=2 six critical 1-cells are loops; for k>=6 no matching fits ten vertices and the full simplex is contractible. Distinct positive homology degrees at consecutive k and final contractibility prove the four unit-length persistence bars. Source tree hash was reconstructed as an actual Git tree from all ten returned blob identities and agrees exactly with assignment.

## originality

PASS

The claim is a complete four-stage integral Petersen nonmatching filtration. Its k=3 constituent is explicitly PRIOR and is strengthened by the 2026-10-18 published S_5 character theorem; no novelty is claimed for that constituent. The same-model 2026-11-08 published mirror is the assigned claim, not an independent earlier result. Focused published-result and primary literature searches did not locate the two nontrivial k=4/k=5 integral homotopy classifications or the complete threshold persistence. Foundational complete/bipartite graph theorems, arbitrary-graph Leray upper bounds, newer bipartite edge-addition theory, and differently-defined matching/independence complexes do not imply those exact claims. Best-of-knowledge PASS for the nontrivial surviving complete classification, with explicit residual priority risks rather than claiming universal absence.

## value

PASS

The Petersen graph is the smallest canonical vertex-transitive nonbipartite cubic graph, and the matching-number bounded edge-subset filtration is natural and complete rather than an arbitrary selected threshold. The k=4 integral Morse attaching matrix and primitive lattice calculation and the k=5 high-dimensional wedge resolve nontrivial topology not provided by the prior known k=3 stage or general Leray bounds. The full sequence 6 S^1, 9 S^3, 4 S^5, 5 S^9 and exact integral persistence is a self-contained benchmark for graph-complex topology and future equivariant comparisons. No downstream theorem, arbitrary graph family, or general cubic classification is claimed; narrow complete finite exact results are valuable when the object/invariant are natural and not fully tabulated already.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The forward subsets satisfying the degree condition are matchings, and either reversed arc can be added without a cycle. With both additions, a cycle is possible exactly when both cross edges are chosen, since consecutive forward arcs are impossible and the two reversed arcs have disjoint endpoints. If cross-completeness fails, the full simplicial join with the edge on the reversed arcs is a cone. Otherwise let C be the join of that edge with the forward matchings avoiding the cross pair, and K the residual matching complex. The full multipath complex is C union (∂Δ³ * K), where Δ³ has the four special arcs as vertices. Their intersection is the join of the edge on the reversed arcs, the boundary of the edge on the cross arcs, and K, hence is contractible. The intersection inclusions are simplicial cofibrations, so the inclusion ∂Δ³ * K into the union gives the claimed equivalence. This also gives S² directly when K consists only of the empty face. Threefold integral homology shift and Jonsson's exact chessboard group yield the stated K7,7 corollary. The frozen checker and verification prose were inspected without executing the checker; mod-two runs cannot substantiate integral torsion.

## originality

FAIL

The distinct same-day Resultary record 5cee81ae2fdc explicitly covers the entire final finding at the same generality, including the empty residual graph convention and the identical integral torsion example. This is demonstrated statement-level duplication, not an inference about relative priority from the date or about authorship. No distinct new theorem or substantive new method remains in the assigned statement.

## value

PASS

As a mathematical statement, the dichotomy classifies the full homotopy type of a natural family after a minimal cyclic modification. It transfers suspended residual matching-complex topology, including integral torsion missed by field checks, and cleanly distinguishes a cone from a directed-cycle case. This substantive content is already present in the matched record; its intrinsic value does not establish originality here.

The dated certificate retains the supplied scientific assessment, sources and limitations.

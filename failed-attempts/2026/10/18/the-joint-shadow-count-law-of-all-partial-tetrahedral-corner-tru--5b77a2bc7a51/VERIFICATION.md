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

Barycentric coordinates put the cut at vertex i at lambda_i=1-t_i and all old facets at lambda_i=0. The depth hypothesis prevents two cut facets from meeting and leaves every old edge with positive length. For a generic direction U, the relative interior of the edge normal cone meets U-perp precisely when its two facet normals have opposite scalar-product signs; such an exposed edge projects to one full polygon edge. A cut facet has the negative of its opposite old facet's normal. Thus there are four old silhouette edges and one additional edge per cut for a 2:2 sign split; for a 1:3 split with outlier i there are three old edges and two additional edges per cut except at i. The outlier event is the tangent cone at i and its antipode up to boundaries, because the other three inequalities are exactly the incident-facet cone inequalities and positive facet-area equilibrium forces the fourth sign. Its mass is Omega_i/(2 pi). All masses are positive: the cones have interiors and v0+v1-v2-v3 has barycentric direction derivatives (1,1,-1,-1), giving an open balanced chamber. The empty and singleton mask coordinates distinguish the five outcomes. Complementation and labeled angle recovery follow by substitution. The finite checker was inspected, not used as a proof or executed.

## originality

FAIL

The complete stated law is mechanically covered by an independently indexed pointwise transfer formula and the classical per-vertex projection probability, not merely by a regular-tetrahedron table or by the formerly known unlabeled sum. Resultary 2ea0e48a588e, equations (1)–(2) and proof section 4, determines each mask's count for every generic direction and arbitrary shape, under a depth hypothesis containing the frozen one. Feldman–Klain p. 1 equation (1) supplies the probability of disappearance of each individually specified vertex, not just the sum in their Theorem 1. For the unique sign outlier i, the direction traverses exactly the tangent cone at i or its antipode: this is the disappearing vertex event in that equation. Thus the exact same five-atom joint law, labeled recovery, and complement law follow. The overlapping catalogue record is distinct and listed on a later date; this is a finding of demonstrable coverage in the inspected sources, not a claim that the later record historically preceded the frozen one or that this finding was copied.

## value

FAIL

All-mask coupling and labeled solid-angle inference are natural and useful as mathematical observations. But after the checked pointwise transfer law, reading off the five vectors and their weights from the existing per-vertex probabilities is immediate. The frozen additional claims (marginals and singleton recovery) introduce no further geometric mechanism or nontrivial exact invariant beyond this relabeling; no separate substantive increment survives at the claimed scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.

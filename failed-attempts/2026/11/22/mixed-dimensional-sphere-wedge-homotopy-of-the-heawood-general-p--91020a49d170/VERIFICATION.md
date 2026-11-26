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

In the Fano incidence graph same-part distances are 2 and cross-part distances are 1 (incident) or 3 (nonincident). A mixed triple is forbidden exactly when one of its cross pairs is incident: its distance multiset is then (1,1,2) or (1,2,3), while both cross distances equal to 3 give no equality. Same-part triples are allowed. I reconstructed all faces with this direct criterion, then independently reproduced the specified matching and oriented incidence check. There were 210 forbidden triples, 478 nonempty faces, 225 pairs, and complete acyclic elimination of 478 nodes and 1610 arcs. The critical faces were exactly the listed vertex, 21 edges, and six tetrahedra. With no two-cells in the resulting CW model the 3-cells attach to a graph, hence all attaching maps from S² are null. This proves the integral wedge and associated homology; no modular inference is needed.

## originality

FAIL

The complete claimed wedge is a routine corollary of the exact, earlier Heawood independence-complex wedge in Resultary dbd95019d1e2, not merely a coincidence of rank six. With the distances verified above, any set of size at least three containing an incident point–line pair contains a forbidden triple: take any third vertex. Conversely, all independent sets have no forbidden triple. Every pair is in GP. Thus GP(H) equals Ind(H) with exactly the 21 graph edges added as maximal one-simplices. The known Ind(H) wedge of six S³ is connected, and attaching any such interval between its existing vertices adds precisely one S¹ up to homotopy. This gives the full displayed wedge, including torsion-freeness, from the existing exact result.

## value

FAIL

The graph is a natural benchmark, but the precise frozen invariant is mechanically recoverable from the known same-graph independence wedge: a diameter-three incidence check isolates the 21 graph edges, and each adds a circle by the standard interval attachment. The new certificate reproduces the same critical tetrahedra and adds those edges; it does not establish a distinct substantive invariant, a uniform family classification, or a meaningful independent remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.

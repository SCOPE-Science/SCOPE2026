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

Truncating each of 30 icosahedral edges into two oriented endpoint vertices yields 60 vertices and a cubic 90-edge graph. Independently enumerated cliques of its graph square (distance<=2) and obtained face vector (60,270,340,120,12), Euler characteristic 22. Retrieved actual certificate.json at blob d7e6158a... and independently replayed ALL 120 ordered elementary collapses: in each step smaller simplex was present with the single strict coface exactly the asserted larger simplex; verified 2D residual f-vector (60,270,232). For simple connectivity, every new distance-two edge can be replaced by two original edges inside a 2-simplex; the icosahedral truncation has 12 pentagon and 20 hexagon facial disks, with each pentagonal loop contained in a 4-simplex and each hexagonal loop filled by four specified triangles. These loops normally generate pi1 of the original embedded graph on S2. Thus pi1=0. Euler=22 and 2D collapse imply free H2 rank 21; Hurewicz and the simply connected homological Whitehead theorem upgrade this to wedge^21 S2.

## originality

PASS

Best-of-knowledge comparison of precise scientific statements supports originality of the new refinement; all described known premises are credited. The stated unexamined-primary and unindexed-coverage risks remain real.

## value

PASS

Determines the integral homotopy type of a distinguished 60-vertex fullerene graph metric at the first nontrivial scale, using a complete short simplicial-collapse certificate and a facial simple-connectivity proof. The exact 21-sphere invariant is a reusable and naturally motivated benchmark for graph Rips topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.

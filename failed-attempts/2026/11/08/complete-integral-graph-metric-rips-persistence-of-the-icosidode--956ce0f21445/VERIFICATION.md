---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Reconstructed GP(10,2) dodecahedron edges, 30-vertex line graph and BFS graph metric. Independent pair counts by distances (1,...,5)=(60,120,120,120,15); precisely fifteen disjoint maximal-distance pairs imply S14 at radius four. Independently enumerated K2 and K3 cliques with full f-vectors (30,180,380,330,102) and (30,300,1340,3150,4374,3800,2100,720,140,12). Inspected package verify.py exact matching/cocycle checks: it pairs noncritical faces and tests all 3-simplex cocycle equations on common 56-triangle surface. An earlier complete primary proof establishes integer evaluations +1 and -1 on the common oriented surface cycle, hence the inclusion is primitive and ±1 in H2. The current random-seed search is a finite witness discovery, not a proof by timeout or of a wider family.

## originality

FAIL

October 25, 2026 primary record already determines the complete graph-metric integral persistence of the same icosidodecahedral graph, including the crucial H2 survival across radius three and stronger inclusion equivalence.

## value

FAIL

An exact integral persistent class on a natural Archimedean graph is intrinsically valuable, but the identical complete barcode and the stronger K2→K3 homotopy equivalence were proved on October 25, leaving no unknown new invariant in this final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.

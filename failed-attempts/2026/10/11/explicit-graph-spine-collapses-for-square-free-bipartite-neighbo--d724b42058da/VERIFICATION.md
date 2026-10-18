---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The square-free graph condition guarantees two distinct neighborhood simplices share at most one vertex. For each center and root, pairing every non-root face of size >=2 with its rooted coface in decreasing cardinality is a valid elementary collapse because no different center contains that face. The residual star edges are unique, connected by alternating graph walks, and have count e-|B| on A, thus cycle rank e-|V|+1; similarly on B. The statement holds for leaves, trees and isolated K2 (connected no isolates). The proof is mathematically valid and not dependent on the reported 1501 small enumerations.

## originality

FAIL

Exact prior SCOPE/Resultary record “Explicit graph spines for neighborhood complexes of square-free bipartite graphs” was imported at 13:16:35 UTC on 2026-10-11, before this record at 13:16:43 UTC. It states the same root-chosen elementary collapse on BOTH bipartition sides for ALL connected square-free bipartite graphs, with the same star-edge construction; furthermore it identifies the spine as an explicit forest contraction. This submitted result is already a literal mathematical consequence, not a separately novel theorem. The still earlier high-girth collapse supplies the identical local mechanism for the minimum-degree>=2 subclass.

## value

FAIL

The precise theorem is already provided by the earlier, slightly stronger graph-minor/spine record, and its extra cycle-rank calculation is an immediate Euler count. A duplicate standalone theorem does not fill an independent mathematical gap, even though correct and reproducible.

The dated certificate retains the supplied scientific assessment, sources and limitations.

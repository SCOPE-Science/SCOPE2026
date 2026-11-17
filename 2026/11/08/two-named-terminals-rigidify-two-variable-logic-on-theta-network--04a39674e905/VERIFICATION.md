---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

With two terminal constants, unary distance-at-most-r predicates are built by alternating only x,y and reusing bound variable names. For shortest terminal distance a>=2, a strict distance difference <a implies both distances follow the direct path; the midpoint predicate (floor(L/2),ceil(L/2)) then picks exactly one vertex on each path of length L. Existence of one or two witnesses recovers each length multiplicity because there are exactly three paths. Equal multisets give isomorphism. Without named terminals each vertex has both a distinct neighbor and a distinct nonneighbor, enabling an indefinite two-pebble partial-isomorphism response and a common FO2 theory. Partition counting yields floor((N²-6N+12)/12), and the named FO1 lower bound uses Θ(4,4,4),Θ(5,5,5). Independently checked 960 midpoint multiplicities by BFS.

## originality

PASS

Primary logical-complexity and theta metric-dimension literature supplies the language, pebble characterization, and distance-related ingredients; inspected theorems do not state the pair of named FO2 rigidity and unnamed FO2 total collapse. Best-of-knowledge novelty is the midpoint witness extraction and exact theory census in this natural family.

## value

PASS

This is an exact expressive-power boundary on a natural minimal series-parallel network: two distinguished terminals restore complete isomorphism identification whereas without constants the whole infinite family collapses to one counting-free FO2 theory. It includes an exact partition-valued theory census and a sharp FO1-versus-FO2 distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.

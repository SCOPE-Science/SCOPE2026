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

Exact Frucht 12-vertex 18-edge cubic graph with diameter four from VERIFY.py. Adams-Shukla-Singh neighborhood-facet lemma for vertex-centered closed balls in the graph geometric realization gives at odd r=3 unions N1[u]∪N1[v] over each edge, and at even r=4 N2[v] over each vertex, constant until next integer. Independently generated all 423 and 2084 nonempty faces, with facets 17 and 10; the source/independent reverse-vertex acyclic matching yields 209 pairs and critical cells (one 0, two 2, two 3) at r3, 1040 pairs and (one 0, two 3, one 4) at r4. Independently projected exact integer Morse boundaries for each unmatched higher cell, all zero, and inspected source Hasse-DAG acyclicity algorithm and alternative mod-two rank checks. As π2(∨2 S²)=Z² and π3(∨2 S³)=Z², zero attaching degrees suffice for the respective integral wedge homotopy types, not only homology.

## originality

PASS

No earlier classification of these two consecutive Frucht graph Čech nerves was identified. The full primary Adams-Shukla-Singh source provides the shared combinatorial nerve lemma and calculations for HYPERCUBE graphs, not Frucht; similarly named prior Frucht independence/Rips/three-cut calculations use different face rules. Best-of-knowledge PASS, subject to unindexed equal-case studies.

## value

PASS

The Frucht graph is the canonical small cubic asymmetric graph; its intrinsic closed-ball Čech nerves at adjacent natural thresholds exhibit distinct nontrivial mixed-dimensional sphere-wedge transitions, determined integrally, not merely finite Betti tables. These precise homotopy types are natural benchmark invariants for geometric graph nerves and cannot be read from generic cubic-girth results.

The dated certificate retains the supplied scientific assessment, sources and limitations.

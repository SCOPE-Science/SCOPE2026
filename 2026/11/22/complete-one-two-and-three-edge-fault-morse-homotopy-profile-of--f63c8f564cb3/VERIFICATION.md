---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Up to three removed edges the deleted graph is a forest. In each displayed shape the bipartition fixes the placement up to shore permutations and an optional shore swap; orbit sizes in table order are 1,9,18,18,6,36,36,6, totaling 130. The admitted incidence matchings are rooted forests: along any undirected cycle, outdegree ≤1 and using each edge once force a directed cycle. Independently enumerated rooted forests and checked the frozen pivot orders by a fresh reconstruction and DFS of the directed face poset. Every orbit has one critical 0-cell, no critical 1- or 2-cells, and the stated critical 3- and 4-cell counts. As an independent route to the degree calculation, exact rational ranks of the original signed simplicial boundaries give Betti numbers in dimensions 3 and 4 equal to the critical counts (python /workspace/reproductions/morse.py). Thus the Morse cellular ∂4 is zero over Q and hence over Z. Each 4-cell attaches to a wedge of 3-spheres, where Hurewicz identifies π3 with integral H3. The zero degree vectors therefore imply nullhomotopic attaching maps; this is stronger than a field Betti check. This proves the full table and sharp first contractibility threshold, with no extension beyond the eight orbits.

## originality

PASS

Pass for the distinct complete edge-fault profile and first-contractible-fault threshold, not for every row as an individually novel homotopy calculation. The intact type is prior as stated. The three-disjoint row is also covered by cycle literature (the residual graph is C6), and the contractible row itself follows by applying the known leaf-collapse mechanism twice. Neither implication supplies the full profile or excludes all smaller contractible faults. No matching prior for that complete threshold/table was established.

## value

PASS

The complete small-biclique classification gives a natural sharp threshold for contractibility and distinguishes faults of equal cardinality by exact integral homotopy. The comparison, including cases with both 3- and 4-spheres, is not determined by generic connectivity or Euler characteristic, and is useful independently of the prior isolated rows. It makes no claim for larger bicliques or more faults.

The dated certificate retains the supplied scientific assessment, sources and limitations.

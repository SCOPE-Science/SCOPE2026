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

Independent replay (python /workspace/branches/replay_durer.py) scanned every six-edge subset covering all 12 vertices, giving precisely ten perfect matchings. Exactly the matchings avoiding each fault survive. Their simplex cover has simplex intersections whenever nonempty; the nerve theorem applies. Independently built the nerve as the union of simplices on matching indices sharing each graph edge, then read the frozen certificate as data and verified every one of 2,632 unique codimension-one proper coface deletions with respect to the whole current nerve, over all 988 faults. Each nonempty residue is connected and at most one-dimensional, so contracting a spanning tree gives the actual circle-wedge homotopy type with rank E-V+1, not just homology. Direct Euler computations on the original complexes agree. The reproduced (void, point, one, two, three circles) rows are (0,1,0,0,0), (0,6,6,6,0), (0,78,63,12,0), (20,662,132,0,2); one-edge types checked individually and the only rank-three faults are (0,2,4) and (1,3,5). This checks the supplied witnesses rather than independently rediscovering them.

## originality

PASS

The supported distinct result is the exact nonzero-fault homotopy atlas, not intact contractibility. Searches and statement comparisons found no distinct same-object fault atlas or theorem giving those ranks. Same-graph results for arbitrary matchings, independent sets, and cut complexes compare different objects.

## value

PASS

Three deletions are a natural cutoff in this cubic graph: a vertex star is already fatal. The atlas distinguishes the three edge classes after a single fault and shows that rank two disappears at three faults, while exactly the two alternating rim faults create rank three. The combination of this topological sensitivity with the 20 void cases gives a useful exact benchmark for extendible-matchings topology, beyond an intact complex or a mere perfect-matching count. No persistence-map consequence is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

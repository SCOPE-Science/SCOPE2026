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

For an interior witness on a unit edge, the distance from a vertex center is the minimum of the two distances via its endpoints. At distance at most 3/2 from the witness, at least one of the endpoint distances is at most one, since those distances are integral. Thus the edge midpoint also witnesses the face. A witness at a vertex is covered by an incident midpoint witness. This gives the closed-neighborhood union facets and verifies that the nerve built with the recomputed metric is an actual subcomplex. The incidence multiplier sends the differences 0,1,3 in a 3-cycle, and translations give all 21 incidence edges. An independently written bit-mask reconstruction exhausts both face sets and tests topological sorting of the oriented Hasse incidences. Intact: 847 faces, 399 pairs, one critical vertex and 48 triangles, 3010 incidences. Faulted: 714 faces, 338 pairs, one critical vertex and 37 triangles, 2498 incidences. Relative: 133 faces, 61 pairs and exactly 11 critical triangles, acyclic also on the full intact poset leaving the faulted subcomplex untouched. Replay evidence: heawood_independent_check.py at /workspace/branches/0b485231-2e8a-489a-85ea-b40bceed8a3d; the frozen verifier was read, not executed. Absolute discrete Morse theory gives wedges of two-spheres; relative acyclic matching gives attachments under the base. The 11 attaching circles are null in the simply connected faulted nerve, so the under-base splitting and primitive integral map follow, not just mod-two ranks or a difference of Betti numbers.

## originality

PASS

The intact scale-three 48-sphere wedge is established earlier and receives no novelty credit. The one-edge recomputed-metric nerve and the under-base inclusion are not supplied by the inspected exact baseline, analogous fault results, or the general facet formula.

## value

PASS

The canonical cubic Fano incidence graph and its already-known scale-three sphere wedge motivate testing a single incidence fault at exactly that stage. The result describes the integral comparison map and the under-base homotopy, not merely a face or Betti count. This exact robustness test is useful for the given nerve without implying an all-scale, all-fault, or equivariant theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

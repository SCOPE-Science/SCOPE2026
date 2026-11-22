---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The fully bidirected wheel with four rim vertices has 16 ordered arcs. An arc subset is a multipath precisely if indegree/outdegree<=1 and there are no directed cycles. Independent exhaustive 2^16 mask traversal found 260 nonempty faces with f=(16,76,120,48), complete face Hasse graph with 704 covers, exactly 116 deterministic Morse pairs, acyclicity of all 260 nodes after reversing matched covers, and unmatched cells one 0-cell, 19 two-cells and 8 three-cells. Independent signed integer Morse reduction gives the full 19x8 differential identically zero; Hurewicz for the wedge of S2 makes all 3-cell attachments nullhomotopic, proving integral wedge ^19 S2 and ^8 S3. Independently built rational 120x48 third-boundary matrix of rank 40 and signed D4 arc action; the H3 character on 5 class types is (8,0,0,0,0), hence regular, and reduced Lefschetz formula yields H2=(19,3,-1,1,1), decomposing 3A1+2A2+3B1+3B2+4E. These are exhaustive exact finite checks of this graph, not extrapolated family claims.

## originality

PASS

Published earlier wheel mod-two census already gives this same W5 Betti numbers 19 and 8, and **those ranks alone are not new**. It explicitly does not determine integral homotopy type, torsion, or dihedral action. The present exact acyclic integer Morse differential establishes a mixed wedge (not implied solely by F2 Betti ranks) and complete new D4 rational characters. Caputi–Collari–Smith 2026 Theorem 2.10 addresses pure bidirected polygons, no hub; other fan and alternate-spoke wheel computations do not imply this fully bidirected W5 group action. Best-of-knowledge PASS for surviving integral homotopy plus representation.

## value

PASS

A small fully bidirected wheel is a natural first cyclic hub extension of known polygon multipath complexes, where torsion and attaching maps cannot be decided from mod-two Betti counts. Exact integral mixed-dimensional homotopy together with automorphism-character resolution is a meaningful complete finite classification and useful benchmark for higher wheel families.

The dated certificate retains the supplied scientific assessment, sources and limitations.

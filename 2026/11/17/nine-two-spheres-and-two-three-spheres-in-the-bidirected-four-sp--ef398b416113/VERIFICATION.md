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

Reconstructed the exact definition: 14 directed-arc vertices from seven fully bidirected fan edges; a face is an arc set with indegrees/outdegrees <=1 and no directed cycles, including 2-cycles. Independent direct enumeration returned 160 nonempty faces, f=(14,56,70,20). Regenerated the specified 14-index staged matching: 74 pairs, 402 directed Hasse incidences, complete acyclic topological sort, critical cells (one vertex,nine triangles,two tetrahedra). Exact integral reduction gives zero 9x2 Morse boundary, so three-cell attaching maps vanish in pi_2 of the nine-S2 wedge and the integral homotopy wedge follows. Independent rational rank-18 top boundary/trace on its 2D kernel gave rho trace H3=0, reduced H2=1, so rational eigenspace multiplicities H2=(5,4), H3=(1,1). No integral equivariant splitting is asserted.

## originality

PASS

Best-of-knowledge: full Caputi–Collari–Smith text classifies bidirected path and cycle multipath complexes, not the hub-added fan, and its source/sink T-operations do not apply to this fully bidirected graph. Nearby published five-vertex wheel and four-vertex complete bidirected complexes concern different graphs/homotopy groups. An unindexed same-fan census remains possible.

## value

PASS

The first exact mixed-dimensional integral homotopy calculation and reflection representation on a nontrivial triangular bidirected fan is a natural small boundary class between path/cycle and wheel families; the nine S2, two S3, and character are nontrivial, independent data not mechanically implied by those examples. Exact finite classification is appropriate to this explicitly natural object.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. For even n>=6, each index reflection has exactly two special coordinate orbits whose individual free supports are permitted faces; other reflection orbits are nonadjacent pairs forced to endpoint signs. Because the two special supports are mutually nonadjacent, their parameters vary only on a square boundary; different reflection mirrors can meet only at sign vertices since a nonidentity rotation fixes no positive-dimensional permitted face. Therefore the full mirrored boundary is exactly the labelled reflection-symmetric sign-word graph modulo D_n. Independently generated complete bitmask mirror graphs yielded (mirror vertices,boundary components) n=6:(52,2), 8:(160,4), 10:(424,10), 12:(1036,20); the n=10 component signature is (0,56),(5,40),(9,40),(17,40),(27,40),(51,40),(85,32),(119,40),(165,56),(347,40). Independent face-poset orbit triangulation gives cubical orbit ranks (78,272,136), barycentric f-vector (486,1584,1024), 96 incidence-one edges, Euler -74, and contradictory orientation propagation around an interior dual cycle. A connected nonorientable surface with b=10, chi=-74 has h=2-b-chi=66 crosscaps. Computations exhaust n=10 only; the all-even assertion rests on geometric fixed-locus argument.

## originality

PASS

PASS qualified. The 2026-11-01 published all-width dihedral-quotient homotopy theorem already proves chi/rank and explicitly gives the n=10 boundary count 10 in its VERIFICATION discussion; the number 10 ALONE is NOT original. That prior theorem expressly does not determine even-width boundary counts in its theorem or orientability. The new all-even reflection-word graph as an exact boundary model plus an explicit nonorientability obstruction and complete n=10 homeomorphism type remain mathematically distinct and are not consequences of homotopy wedge rank or knowing b=10 alone.

## value

PASS

PASS. A natural equivariant topological quotient of a classical moment-angle surface has a homeomorphism problem not decided by homotopy rank. A uniform exact mirror graph for all even widths and the precise nonorientable homeomorphism type for the first decagonal case provide reusable structural/computational classification beyond a known Euler characteristic. The boundary count alone would be old, but is not the entire finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
